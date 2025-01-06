"""
Complete example demonstrating various Twitter API features.
"""

import os
import time
from datetime import datetime, timedelta
from src.client import TwitterAPIClient
from src.utils.helpers import build_advanced_query, format_timestamp

def main():
    # Initialize client
    api_key = os.getenv("TWITTER_API_KEY")
    if not api_key:
        raise ValueError("Please set TWITTER_API_KEY environment variable")
        
    client = TwitterAPIClient(api_key)
    
    # Example 1: Get user information and recent tweets
    username = "elonmusk"
    print(f"\n=== Getting info for user: {username} ===")
    
    user_info = client.get_user_info(username)
    print(f"Name: {user_info['data']['name']}")
    print(f"Followers: {user_info['data']['followers']:,}")
    print(f"Following: {user_info['data']['following']:,}")
    
    # Get recent tweets
    tweets = client.get_user_tweets(username, include_replies=False)
    print("\nRecent tweets:")
    for tweet in tweets['tweets'][:3]:  # Show first 3 tweets
        print(f"- {tweet['text'][:100]}...")
        print(f"  Likes: {tweet['likeCount']:,}, Retweets: {tweet['retweetCount']:,}")
    
    # Example 2: Advanced search
    print("\n=== Advanced Search Example ===")
    query = build_advanced_query(
        keywords="artificial intelligence",
        username="elonmusk",
        since="2024-01-01",
        lang="en"
    )
    results = client.search_tweets(query)
    print(f"\nSearch results for: {query}")
    for tweet in results['tweets'][:3]:
        print(f"- {tweet['text'][:100]}...")
        print(f"  Posted at: {tweet['createdAt']}")
    
    # Example 3: Get tweet engagement
    print("\n=== Tweet Engagement Example ===")
    tweet_id = results['tweets'][0]['id']  # Use first tweet from search
    
    # Get replies
    replies = client.get_tweet_replies(tweet_id)
    print(f"\nReplies to tweet {tweet_id}:")
    for reply in replies['replies'][:3]:
        print(f"- {reply['text'][:100]}...")
    
    # Get quotes
    quotes = client.get_tweet_quotes(tweet_id)
    print(f"\nQuotes of tweet {tweet_id}:")
    for quote in quotes['tweets'][:3]:
        print(f"- {quote['text'][:100]}...")
    
    # Example 4: Get user mentions
    print(f"\n=== Recent mentions of {username} ===")
    since_time = int((datetime.now() - timedelta(days=7)).timestamp())
    mentions = client.get_user_mentions(username, since_time=since_time)
    for mention in mentions['tweets'][:3]:
        print(f"- {mention['text'][:100]}...")
        print(f"  By: {mention['author']['userName']}")

if __name__ == "__main__":
    main() 