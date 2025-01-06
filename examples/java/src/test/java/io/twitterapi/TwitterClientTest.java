package io.twitterapi;

import io.twitterapi.config.TwitterConfig;
import io.twitterapi.exception.TwitterException;
import io.twitterapi.model.User;
import okhttp3.mockwebserver.MockResponse;
import okhttp3.mockwebserver.MockWebServer;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.time.Duration;

import static org.junit.jupiter.api.Assertions.*;

class TwitterClientTest {
    private MockWebServer mockWebServer;
    private TwitterClient client;

    @BeforeEach
    void setUp() throws IOException {
        mockWebServer = new MockWebServer();
        mockWebServer.start();

        TwitterConfig config = TwitterConfig.builder()
            .baseUrl(mockWebServer.url("/").toString())
            .connectTimeout(Duration.ofSeconds(1))
            .build();

        client = new TwitterClient("test-api-key", config);
    }

    @AfterEach
    void tearDown() throws IOException {
        mockWebServer.shutdown();
    }

    @Test
    void getUserInfo_Success() throws TwitterException {
        // Arrange
        String responseJson = """
            {
                "data": {
                    "id": "12345",
                    "userName": "testuser",
                    "name": "Test User",
                    "followers": 1000,
                    "following": 500,
                    "statusesCount": 1234,
                    "createdAt": "2020-01-01",
                    "isBlueVerified": true,
                    "canDm": true,
                    "profilePicture": "https://example.com/pic.jpg"
                }
            }
            """;

        mockWebServer.enqueue(new MockResponse()
            .setResponseCode(200)
            .setBody(responseJson)
            .addHeader("Content-Type", "application/json"));

        // Act
        User user = client.getUserInfo("testuser");

        // Assert
        assertNotNull(user);
        assertEquals("testuser", user.getUsername());
        assertEquals(1000, user.getFollowersCount());
        assertEquals(500, user.getFollowingCount());
    }

    @Test
    void getUserInfo_Error() {
        // Arrange
        mockWebServer.enqueue(new MockResponse()
            .setResponseCode(404)
            .setBody("{\"error\":\"User not found\"}"));

        // Act & Assert
        assertThrows(TwitterException.class, () -> 
            client.getUserInfo("nonexistent"));
    }
} 