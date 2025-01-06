package io.twitterapi.config;

import lombok.Builder;
import lombok.Data;
import java.time.Duration;

@Data
@Builder
public class TwitterConfig {
    @Builder.Default
    private String baseUrl = "https://api.twitterapi.io";
    
    @Builder.Default
    private Duration connectTimeout = Duration.ofSeconds(30);
    
    @Builder.Default
    private Duration readTimeout = Duration.ofSeconds(30);
    
    @Builder.Default
    private Duration writeTimeout = Duration.ofSeconds(30);
    
    @Builder.Default
    private int maxRetries = 3;
    
    @Builder.Default
    private Duration retryInterval = Duration.ofSeconds(1);
} 