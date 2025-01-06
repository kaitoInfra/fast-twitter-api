package io.twitterapi.model;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Data;
import java.util.List;
import java.util.Map;

@Data
public class TweetEntities {
    private List<HashtagEntity> hashtags;
    private List<UrlEntity> urls;
    
    @JsonProperty("user_mentions")
    private List<UserMentionEntity> userMentions;

    @Data
    public static class HashtagEntity {
        private String text;
        private List<Integer> indices;
    }

    @Data
    public static class UrlEntity {
        private String url;
        
        @JsonProperty("expanded_url")
        private String expandedUrl;
        
        @JsonProperty("display_url")
        private String displayUrl;
        
        private List<Integer> indices;
    }

    @Data
    public static class UserMentionEntity {
        private String id;
        
        @JsonProperty("screen_name")
        private String screenName;
        
        private String name;
        private List<Integer> indices;
    }
} 