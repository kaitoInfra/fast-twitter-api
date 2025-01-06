package io.twitterapi.retry;

import io.twitterapi.exception.TwitterException;
import lombok.extern.slf4j.Slf4j;

import java.time.Duration;
import java.util.function.Supplier;

@Slf4j
public class RetryStrategy {
    private final int maxRetries;
    private final Duration retryInterval;

    public RetryStrategy(int maxRetries, Duration retryInterval) {
        this.maxRetries = maxRetries;
        this.retryInterval = retryInterval;
    }

    public <T> T execute(Supplier<T> operation) throws TwitterException {
        TwitterException lastException = null;
        
        for (int attempt = 0; attempt <= maxRetries; attempt++) {
            try {
                return operation.get();
            } catch (TwitterException e) {
                lastException = e;
                
                if (attempt < maxRetries && shouldRetry(e)) {
                    log.warn("Request failed (attempt {}), retrying in {} ms: {}", 
                        attempt + 1, retryInterval.toMillis(), e.getMessage());
                    sleep();
                    continue;
                }
                break;
            }
        }
        
        throw lastException;
    }

    private boolean shouldRetry(TwitterException e) {
        // Retry on rate limits and server errors
        return e.getStatusCode() == 429 || (e.getStatusCode() >= 500 && e.getStatusCode() < 600);
    }

    private void sleep() {
        try {
            Thread.sleep(retryInterval.toMillis());
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            throw new TwitterException("Retry interrupted", e);
        }
    }
} 