"""
Examples demonstrating tweet search functionality.
"""

import os
from src.client import TwitterAPIClient

def main():
    # Initialize client
    api_key = os.getenv("TWITTER_API_KEY")
    if not api_key:
        raise ValueError("Please set TWITTER_API_KEY environment variable")
        
    client = TwitterAPIClient(api_key)
    
    # Example 1: Basic search
    print("\n=== Basic Search ===")
    results = client.search_tweets("python programming")
    for tweet in results['tweets']:
        print(f"Tweet: {tweet['text']}")
        print(f"Author: {tweet['author']['userName']}")
        print("---")
    
    # Example 2: Advanced search with filters
    print("\n=== Advanced Search ===")
    query = '"machine learning" lang:en from:elonmusk since:2023-01-01'
    results = client.search_tweets(query)
    for tweet in results['tweets']:
        print(f"Tweet: {tweet['text']}")
        print(f"Created at: {tweet['createdAt']}")
        print("---")
    
    # Example 3: Search with pagination
    print("\n=== Search with Pagination ===")
    cursor = ""
    page = 1
    while True:
        results = client.search_tweets("artificial intelligence", cursor=cursor)
        print(f"\nPage {page}:")
        for tweet in results['tweets']:
            print(f"- {tweet['text'][:100]}...")
            
        if not results['has_next_page']:
            break
            
        cursor = results['next_cursor']
        page += 1
        if page > 3:  # Limit to 3 pages for example
            break

if __name__ == "__main__":
    main() 