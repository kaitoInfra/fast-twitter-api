package io.twitterapi.model;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Data;

@Data
public class User {
    private String id;
    
    @JsonProperty("userName")
    private String username;
    
    private String name;
    private String description;
    
    @JsonProperty("followers")
    private int followersCount;
    
    @JsonProperty("following")
    private int followingCount;
    
    @JsonProperty("statusesCount")
    private int tweetCount;
    
    @JsonProperty("createdAt")
    private String createdAt;
    
    @JsonProperty("isBlueVerified")
    private boolean verified;
    
    @JsonProperty("canDm")
    private boolean canDm;
    
    private String location;
    private String url;
    
    @JsonProperty("profilePicture")
    private String profileImageUrl;
} 