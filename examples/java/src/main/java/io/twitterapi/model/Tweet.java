package io.twitterapi.model;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Data;
import java.time.Instant;
import java.util.List;

@Data
public class Tweet {
    private String id;
    private String text;
    private User author;
    
    @JsonProperty("createdAt")
    private String createdAt;
    
    @JsonProperty("likeCount")
    private int likeCount;
    
    @JsonProperty("retweetCount")
    private int retweetCount;
    
    @JsonProperty("replyCount")
    private int replyCount;
    
    @JsonProperty("quoteCount")
    private int quoteCount;
    
    @JsonProperty("viewCount")
    private Integer viewCount;
    
    private String lang;
    private String source;
    private TweetEntities entities;
    
    @JsonProperty("quoted_tweet")
    private Tweet quotedTweet;
    
    @JsonProperty("retweeted_tweet")
    private Tweet retweetedTweet;
} 