# Twitter API Java Client

A Java client library for the Twitter API.

## Requirements

- Java 11 or higher
- Maven 3.6 or higher

## Installation

Add this dependency to your project's POM:

```xml
<dependency>
    <groupId>io.twitterapi</groupId>
    <artifactId>twitter-api-client</artifactId>
    <version>1.0.0</version>
</dependency>
```

## Quick Start

```java
import io.twitterapi.TwitterClient;
import io.twitterapi.model.User;

public class QuickStart {
    public static void main(String[] args) {
        // Initialize client
        TwitterClient client = new TwitterClient("your-api-key");

        try {
            // Get user information
            User user = client.getUserInfo("elonmusk");
            System.out.println("Name: " + user.getName());
            System.out.println("Followers: " + user.getFollowersCount());

            // Search tweets
            Map<String, Object> results = client.searchTweets("java programming", "");
            // Process results...
            
        } catch (TwitterException e) {
            e.printStackTrace();
        }
    }
}
```

## Configuration

You can customize the client behavior using TwitterConfig:

```java
TwitterConfig config = TwitterConfig.builder()
    .connectTimeout(Duration.ofSeconds(30))
    .maxRetries(3)
    .retryInterval(Duration.ofSeconds(1))
    .build();

TwitterClient client = new TwitterClient("your-api-key", config);
```

## Features

- User information retrieval
- Tweet search
- Pagination support
- Rate limiting handling
- Customizable configuration
- Exception handling

## Examples

See the `examples` directory for more detailed examples.

## Documentation

For detailed API documentation, please visit [https://twitterapi.io/docs](https://twitterapi.io/docs)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 