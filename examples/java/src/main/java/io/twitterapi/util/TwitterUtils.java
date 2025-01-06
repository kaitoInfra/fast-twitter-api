package io.twitterapi.util;

import java.time.Instant;
import java.time.ZoneId;
import java.time.format.DateTimeFormatter;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.Optional;

public class TwitterUtils {
    private static final Pattern TWEET_URL_PATTERN = 
        Pattern.compile("twitter\\.com/\\w+/status/(\\d+)");
    
    private static final DateTimeFormatter TWITTER_DATE_FORMATTER = 
        DateTimeFormatter.ofPattern("EEE MMM dd HH:mm:ss Z yyyy")
            .withZone(ZoneId.of("UTC"));

    /**
     * Extract tweet ID from a Twitter URL.
     *
     * @param url Twitter status URL
     * @return Optional containing tweet ID if found
     */
    public static Optional<String> extractTweetId(String url) {
        if (url == null || url.isEmpty()) {
            return Optional.empty();
        }

        Matcher matcher = TWEET_URL_PATTERN.matcher(url);
        return matcher.find() ? Optional.of(matcher.group(1)) : Optional.empty();
    }

    /**
     * Build advanced search query.
     *
     * @param keywords Search keywords
     * @param username Filter by username (optional)
     * @param since Start date YYYY-MM-DD (optional)
     * @param until End date YYYY-MM-DD (optional)
     * @param lang Language code (optional)
     * @return Formatted query string
     */
    public static String buildAdvancedQuery(
            String keywords,
            String username,
            String since,
            String until,
            String lang) {
        StringBuilder query = new StringBuilder(keywords);

        if (username != null && !username.isEmpty()) {
            query.append(" from:").append(username);
        }
        if (since != null && !since.isEmpty()) {
            query.append(" since:").append(since);
        }
        if (until != null && !until.isEmpty()) {
            query.append(" until:").append(until);
        }
        if (lang != null && !lang.isEmpty()) {
            query.append(" lang:").append(lang);
        }

        return query.toString();
    }

    /**
     * Parse Twitter date string to Instant.
     *
     * @param dateStr Twitter date string
     * @return Optional containing parsed Instant
     */
    public static Optional<Instant> parseTwitterDate(String dateStr) {
        try {
            return Optional.of(Instant.from(TWITTER_DATE_FORMATTER.parse(dateStr)));
        } catch (Exception e) {
            return Optional.empty();
        }
    }
} 