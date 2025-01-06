"""
Helper functions for Twitter API client.
"""

from datetime import datetime
from typing import Optional, List
import re
import time

def format_timestamp(timestamp: int) -> str:
    """Convert Unix timestamp to formatted date string.
    
    Args:
        timestamp: Unix timestamp in seconds
        
    Returns:
        Formatted date string
    """
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def parse_tweet_time(time_str: str) -> Optional[int]:
    """Parse Twitter time string to Unix timestamp.
    
    Args:
        time_str: Twitter time string format
        
    Returns:
        Unix timestamp in seconds or None if parsing fails
    """
    try:
        dt = datetime.strptime(time_str, '%a %b %d %H:%M:%S +0000 %Y')
        return int(dt.timestamp())
    except ValueError:
        return None

def build_advanced_query(
    keywords: str,
    username: Optional[str] = None,
    since: Optional[str] = None,
    until: Optional[str] = None,
    lang: Optional[str] = None
) -> str:
    """Build advanced search query string.
    
    Args:
        keywords: Search keywords
        username: Filter by username
        since: Start date (YYYY-MM-DD)
        until: End date (YYYY-MM-DD)
        lang: Language code
        
    Returns:
        Formatted query string
    """
    query_parts = [keywords]
    
    if username:
        query_parts.append(f"from:{username}")
    if since:
        query_parts.append(f"since:{since}")
    if until:
        query_parts.append(f"until:{until}")
    if lang:
        query_parts.append(f"lang:{lang}")
        
    return " ".join(query_parts) 

def extract_tweet_id_from_url(url: str) -> Optional[str]:
    """Extract tweet ID from a Twitter URL.
    
    Args:
        url: Twitter status URL
        
    Returns:
        Tweet ID if found, None otherwise
    """
    pattern = r'twitter\.com/\w+/status/(\d+)'
    match = re.search(pattern, url)
    return match.group(1) if match else None

def chunk_list(lst: List, chunk_size: int) -> List[List]:
    """Split a list into chunks of specified size.
    
    Args:
        lst: List to split
        chunk_size: Size of each chunk
        
    Returns:
        List of chunks
    """
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

def rate_limit_handler(func):
    """Decorator to handle rate limiting.
    
    Args:
        func: Function to decorate
        
    Returns:
        Wrapped function with rate limit handling
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except TwitterRateLimitError as e:
            print(f"Rate limit exceeded. Waiting 60 seconds...")
            time.sleep(60)
            return func(*args, **kwargs)
    return wrapper 