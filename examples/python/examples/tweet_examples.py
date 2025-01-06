"""
Examples demonstrating tweet-related API functionality.
"""

import os
from datetime import datetime, timedelta
from src.client import TwitterAPIClient

def main():
    # Initialize client
    api_key = os.getenv("TWITTER_API_KEY")
    if not api_key:
        raise ValueError("Please set TWITTER_API_KEY environment variable")
        
    client = TwitterAPIClient(api_key)
    
    # Example 1: Get tweet replies
    print("\n=== Getting Tweet Replies ===")
    tweet_id = "1234567890"  # Replace with actual tweet ID
    replies = client.get_tweet_replies(tweet_id)
    for reply in replies['replies']:
        print(f"Reply from {reply['author']['userName']}: {reply['text']}")
        print(f"Time: {reply['createdAt']}")
        print("---")
    
    # Example 2: Get replies with time filters
    print("\n=== Getting Recent Replies ===")
    # Get replies from last 24 hours
    since_time = int((datetime.now() - timedelta(days=1)).timestamp())
    recent_replies = client.get_tweet_replies(
        tweet_id,
        since_time=since_time
    )
    for reply in recent_replies['replies']:
        print(f"Recent reply: {reply['text']}")
        print("---")
    
    # Example 3: Get tweet quotes
    print("\n=== Getting Tweet Quotes ===")
    quotes = client.get_tweet_quotes(tweet_id)
    for quote in quotes['tweets']:
        print(f"Quote from {quote['author']['userName']}")
        print(f"Original tweet: {quote['quoted_tweet']['text']}")
        print(f"Quote text: {quote['text']}")
        print("---")
    
    # Example 4: Get quotes with pagination
    print("\n=== Quotes with Pagination ===")
    cursor = ""
    page = 1
    while True:
        result = client.get_tweet_quotes(tweet_id, cursor=cursor)
        print(f"\nPage {page}:")
        for quote in result['tweets']:
            print(f"- {quote['text'][:100]}...")
            
        if not result['has_next_page']:
            break
            
        cursor = result['next_cursor']
        page += 1
        if page > 3:  # Limit to 3 pages for example
            break

if __name__ == "__main__":
    main() 