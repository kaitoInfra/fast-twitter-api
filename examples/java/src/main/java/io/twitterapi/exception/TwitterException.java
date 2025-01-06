package io.twitterapi.exception;

import lombok.Getter;

@Getter
public class TwitterException extends Exception {
    private final int statusCode;
    private final String errorCode;

    public TwitterException(String message) {
        this(message, null, 0, null);
    }

    public TwitterException(String message, Throwable cause) {
        this(message, cause, 0, null);
    }

    public TwitterException(String message, int statusCode) {
        this(message, null, statusCode, null);
    }

    public TwitterException(String message, Throwable cause, int statusCode, String errorCode) {
        super(message, cause);
        this.statusCode = statusCode;
        this.errorCode = errorCode;
    }
} 