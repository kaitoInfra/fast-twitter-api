"""
Examples demonstrating user-related API functionality.
"""

import os
from src.client import TwitterAPIClient

def main():
    # Initialize client with API key from environment
    api_key = os.getenv("TWITTER_API_KEY")
    if not api_key:
        raise ValueError("Please set TWITTER_API_KEY environment variable")
        
    client = TwitterAPIClient(api_key)
    
    # Example 1: Get user information
    print("\n=== Getting User Information ===")
    user_info = client.get_user_info("elonmusk")
    print(f"Name: {user_info['data']['name']}")
    print(f"Followers: {user_info['data']['followers']}")
    print(f"Following: {user_info['data']['following']}")
    
    # Example 2: Get user's recent tweets
    print("\n=== Getting User's Recent Tweets ===")
    tweets = client.get_user_tweets("elonmusk", include_replies=False)
    for tweet in tweets['tweets']:
        print(f"Tweet: {tweet['text']}")
        print(f"Likes: {tweet['likeCount']}")
        print("---")
        
    # Example 3: Pagination example
    print("\n=== Pagination Example ===")
    cursor = ""
    page = 1
    while True:
        result = client.get_user_tweets("elonmusk", cursor=cursor)
        print(f"\nPage {page}:")
        for tweet in result['tweets']:
            print(f"- {tweet['text'][:100]}...")
            
        if not result['has_next_page']:
            break
            
        cursor = result['next_cursor']
        page += 1
        if page > 3:  # Limit to 3 pages for example
            break

if __name__ == "__main__":
    main() 