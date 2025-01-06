package io.twitterapi.examples;

import io.twitterapi.TwitterClient;
import io.twitterapi.config.TwitterConfig;
import io.twitterapi.model.Tweet;
import io.twitterapi.model.User;
import io.twitterapi.util.TwitterUtils;

import java.time.Instant;
import java.time.temporal.ChronoUnit;
import java.util.Map;

public class CompleteExample {
    public static void main(String[] args) {
        String apiKey = System.getenv("TWITTER_API_KEY");
        if (apiKey == null || apiKey.isEmpty()) {
            throw new IllegalArgumentException("Please set TWITTER_API_KEY environment variable");
        }

        // Initialize client with custom configuration
        TwitterConfig config = TwitterConfig.builder()
            .maxRetries(5)
            .retryInterval(Duration.ofSeconds(2))
            .build();
            
        TwitterClient client = new TwitterClient(apiKey);

        try {
            // Example 1: Get user information
            String username = "elonmusk";
            System.out.printf("%n=== Getting info for user: %s ===%n", username);
            
            User user = client.getUserInfo(username);
            System.out.printf("Name: %s%n", user.getName());
            System.out.printf("Followers: %,d%n", user.getFollowersCount());
            System.out.printf("Following: %,d%n", user.getFollowingCount());

            // Example 2: Get user's recent tweets
            System.out.println("\n=== Recent tweets ===");
            Map<String, Object> tweets = client.getUserTweets(username, false, "");
            @SuppressWarnings("unchecked")
            List<Map<String, Object>> tweetList = (List<Map<String, Object>>) tweets.get("tweets");
            
            tweetList.stream()
                .limit(3)
                .forEach(tweet -> {
                    System.out.printf("- %s...%n", 
                        ((String) tweet.get("text")).substring(0, Math.min(100, 
                            ((String) tweet.get("text")).length())));
                    System.out.printf("  Likes: %,d, Retweets: %,d%n", 
                        tweet.get("likeCount"), tweet.get("retweetCount"));
                });

            // Example 3: Advanced search
            System.out.println("\n=== Advanced Search Example ===");
            String query = TwitterUtils.buildAdvancedQuery(
                "artificial intelligence",
                "elonmusk",
                "2024-01-01",
                null,
                "en"
            );
            
            Map<String, Object> searchResults = client.searchTweets(query, "");
            System.out.printf("Search results for: %s%n", query);
            
            @SuppressWarnings("unchecked")
            List<Map<String, Object>> resultList = (List<Map<String, Object>>) searchResults.get("tweets");
            
            resultList.stream()
                .limit(3)
                .forEach(tweet -> {
                    System.out.printf("- %s...%n", 
                        ((String) tweet.get("text")).substring(0, Math.min(100, 
                            ((String) tweet.get("text")).length())));
                    System.out.printf("  Posted at: %s%n", tweet.get("createdAt"));
                });

        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
            e.printStackTrace();
        }
    }
} 