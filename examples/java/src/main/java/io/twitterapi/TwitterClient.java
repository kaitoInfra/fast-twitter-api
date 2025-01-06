package io.twitterapi;

import com.fasterxml.jackson.databind.ObjectMapper;
import io.twitterapi.exception.TwitterException;
import io.twitterapi.model.Tweet;
import io.twitterapi.model.User;
import lombok.extern.slf4j.Slf4j;
import okhttp3.*;
import java.io.IOException;
import java.util.Map;
import java.util.concurrent.TimeUnit;
import java.util.HashMap;

@Slf4j
public class TwitterClient {
    private final OkHttpClient httpClient;
    private final ObjectMapper objectMapper;
    private final String apiKey;
    private final String baseUrl;

    public TwitterClient(String apiKey) {
        this(apiKey, TwitterConfig.builder().build());
    }

    public TwitterClient(String apiKey, TwitterConfig config) {
        this.apiKey = apiKey;
        this.baseUrl = config.getBaseUrl();
        this.objectMapper = new ObjectMapper();
        
        this.httpClient = new OkHttpClient.Builder()
            .connectTimeout(config.getConnectTimeout().toMillis(), TimeUnit.MILLISECONDS)
            .readTimeout(config.getReadTimeout().toMillis(), TimeUnit.MILLISECONDS)
            .writeTimeout(config.getWriteTimeout().toMillis(), TimeUnit.MILLISECONDS)
            .build();
    }

    public User getUserInfo(String username) throws TwitterException {
        Map<String, Object> response = executeRequest("/twitter/user/info", 
            Map.of("userName", username));
        return objectMapper.convertValue(response.get("data"), User.class);
    }

    public Map<String, Object> getUserTweets(String username, boolean includeReplies, String cursor) 
            throws TwitterException {
        return executeRequest("/twitter/user/last_tweets", Map.of(
            "userName", username,
            "includeReplies", includeReplies,
            "cursor", cursor
        ));
    }

    public Map<String, Object> searchTweets(String query, String cursor) throws TwitterException {
        return executeRequest("/twitter/tweet/advanced_search", Map.of(
            "query", query,
            "cursor", cursor
        ));
    }

    public Map<String, Object> getUserFollowers(String username, String cursor) throws TwitterException {
        return executeRequest("/twitter/user/followers", Map.of(
            "userName", username,
            "cursor", cursor
        ));
    }

    public Map<String, Object> getUserFollowing(String username, String cursor) throws TwitterException {
        return executeRequest("/twitter/user/followings", Map.of(
            "userName", username,
            "cursor", cursor
        ));
    }

    public Map<String, Object> getUserMentions(
            String username,
            Long sinceTime,
            Long untilTime,
            String cursor) throws TwitterException {
        Map<String, Object> params = new HashMap<>();
        params.put("userName", username);
        params.put("cursor", cursor);
        if (sinceTime != null) {
            params.put("sinceTime", sinceTime);
        }
        if (untilTime != null) {
            params.put("untilTime", untilTime);
        }
        return executeRequest("/twitter/user/mentions", params);
    }

    public Map<String, Object> getTweetReplies(
            String tweetId,
            Long sinceTime,
            Long untilTime,
            String cursor) throws TwitterException {
        Map<String, Object> params = new HashMap<>();
        params.put("tweetId", tweetId);
        params.put("cursor", cursor);
        if (sinceTime != null) {
            params.put("sinceTime", sinceTime);
        }
        if (untilTime != null) {
            params.put("untilTime", untilTime);
        }
        return executeRequest("/twitter/tweet/replies", params);
    }

    public Map<String, Object> getTweetQuotes(
            String tweetId,
            boolean includeReplies,
            String cursor) throws TwitterException {
        return executeRequest("/twitter/tweet/quotes", Map.of(
            "tweetId", tweetId,
            "includeReplies", includeReplies,
            "cursor", cursor
        ));
    }

    private Map<String, Object> executeRequest(String endpoint, Map<String, Object> params) 
            throws TwitterException {
        HttpUrl.Builder urlBuilder = HttpUrl.parse(baseUrl + endpoint).newBuilder();
        params.forEach((key, value) -> {
            if (value != null) {
                urlBuilder.addQueryParameter(key, String.valueOf(value));
            }
        });

        Request request = new Request.Builder()
            .url(urlBuilder.build())
            .addHeader("X-API-Key", apiKey)
            .build();

        try (Response response = httpClient.newCall(request).execute()) {
            if (!response.isSuccessful()) {
                throw new TwitterException("API request failed: " + response.code());
            }

            String responseBody = response.body().string();
            return objectMapper.readValue(responseBody, Map.class);
        } catch (IOException e) {
            throw new TwitterException("Failed to execute request", e);
        }
    }
} 