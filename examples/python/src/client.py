"""
Twitter API Client Implementation
A clean and elegant client for accessing Twitter API endpoints.
"""

import requests
from typing import Dict, List, Optional, Union
from datetime import datetime

class TwitterAPIClient:
    """Twitter API client for accessing various Twitter endpoints."""
    
    def __init__(self, api_key: str, base_url: str = "https://api.twitterapi.io"):
        """Initialize the Twitter API client.
        
        Args:
            api_key: Your Twitter API key
            base_url: Base URL for API endpoints
        """
        self.api_key = api_key
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "X-API-Key": api_key,
            "Content-Type": "application/json"
        })

    def _make_request(
        self, 
        endpoint: str, 
        params: Optional[Dict] = None
    ) -> Dict:
        """Make a request to the API.
        
        Args:
            endpoint: API endpoint to call
            params: Query parameters
            
        Returns:
            API response as dictionary
            
        Raises:
            requests.exceptions.RequestException: If the request fails
        """
        url = f"{self.base_url}{endpoint}"
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_user_info(self, username: str) -> Dict:
        """Get information about a Twitter user.
        
        Args:
            username: Twitter username/screen name
            
        Returns:
            User information including profile details
        """
        return self._make_request("/twitter/user/info", {"userName": username})

    def get_user_tweets(
        self,
        username: str,
        include_replies: bool = False,
        cursor: str = ""
    ) -> Dict:
        """Get tweets from a specific user.
        
        Args:
            username: Twitter username
            include_replies: Whether to include replies
            cursor: Pagination cursor
            
        Returns:
            List of tweets and pagination info
        """
        params = {
            "userName": username,
            "includeReplies": include_replies,
            "cursor": cursor
        }
        return self._make_request("/twitter/user/last_tweets", params)

    def search_tweets(
        self,
        query: str,
        cursor: str = ""
    ) -> Dict:
        """Search for tweets using advanced query.
        
        Args:
            query: Search query string
            cursor: Pagination cursor
            
        Returns:
            Search results and pagination info
        """
        params = {
            "query": query,
            "cursor": cursor
        }
        return self._make_request("/twitter/tweet/advanced_search", params)

    def get_tweet_replies(
        self,
        tweet_id: str,
        since_time: Optional[int] = None,
        until_time: Optional[int] = None,
        cursor: str = ""
    ) -> Dict:
        """Get replies to a specific tweet.
        
        Args:
            tweet_id: ID of the tweet
            since_time: Filter replies after this timestamp
            until_time: Filter replies before this timestamp
            cursor: Pagination cursor
            
        Returns:
            List of reply tweets and pagination info
        """
        params = {
            "tweetId": tweet_id,
            "cursor": cursor
        }
        if since_time:
            params["sinceTime"] = since_time
        if until_time:
            params["untilTime"] = until_time
            
        return self._make_request("/twitter/tweet/replies", params)

    def get_tweet_quotes(
        self,
        tweet_id: str,
        include_replies: bool = True,
        cursor: str = ""
    ) -> Dict:
        """Get quotes of a specific tweet.
        
        Args:
            tweet_id: ID of the tweet
            include_replies: Whether to include replies
            cursor: Pagination cursor
            
        Returns:
            List of quote tweets and pagination info
        """
        params = {
            "tweetId": tweet_id,
            "includeReplies": include_replies,
            "cursor": cursor
        }
        return self._make_request("/twitter/tweet/quotes", params)

    def get_user_followers(
        self,
        username: str,
        cursor: str = ""
    ) -> Dict:
        """Get user's followers.
        
        Args:
            username: Twitter username
            cursor: Pagination cursor
            
        Returns:
            List of followers and pagination info
        """
        params = {
            "userName": username,
            "cursor": cursor
        }
        return self._make_request("/twitter/user/followers", params)

    def get_user_following(
        self,
        username: str,
        cursor: str = ""
    ) -> Dict:
        """Get users that a user is following.
        
        Args:
            username: Twitter username
            cursor: Pagination cursor
            
        Returns:
            List of following users and pagination info
        """
        params = {
            "userName": username,
            "cursor": cursor
        }
        return self._make_request("/twitter/user/followings", params)

    def get_user_mentions(
        self,
        username: str,
        since_time: Optional[int] = None,
        until_time: Optional[int] = None,
        cursor: str = ""
    ) -> Dict:
        """Get mentions of a user.
        
        Args:
            username: Twitter username
            since_time: Filter mentions after this timestamp
            until_time: Filter mentions before this timestamp
            cursor: Pagination cursor
            
        Returns:
            List of mentions and pagination info
        """
        params = {
            "userName": username,
            "cursor": cursor
        }
        if since_time:
            params["sinceTime"] = since_time
        if until_time:
            params["untilTime"] = until_time
            
        return self._make_request("/twitter/user/mentions", params) 