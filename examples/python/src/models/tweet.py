"""
Tweet data model classes.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional, Dict

@dataclass
class TweetEntities:
    """Tweet entities like hashtags, urls, and mentions."""
    hashtags: List[Dict[str, str]]
    urls: List[Dict[str, str]]
    user_mentions: List[Dict[str, str]]

@dataclass
class Tweet:
    """Represents a Tweet object."""
    id: str
    text: str
    author: 'User'  # Forward reference
    created_at: str
    like_count: int
    retweet_count: int
    reply_count: int
    quote_count: int
    view_count: Optional[int]
    lang: Optional[str]
    source: str
    entities: Optional[TweetEntities]
    quoted_tweet: Optional['Tweet']
    retweeted_tweet: Optional['Tweet']
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Tweet':
        """Create Tweet instance from dictionary."""
        return cls(
            id=data['id'],
            text=data['text'],
            author=User.from_dict(data['author']),
            created_at=data['createdAt'],
            like_count=data['likeCount'],
            retweet_count=data['retweetCount'],
            reply_count=data['replyCount'],
            quote_count=data['quoteCount'],
            view_count=data.get('viewCount'),
            lang=data.get('lang'),
            source=data['source'],
            entities=TweetEntities(**data['entities']) if data.get('entities') else None,
            quoted_tweet=cls.from_dict(data['quoted_tweet']) if data.get('quoted_tweet') else None,
            retweeted_tweet=cls.from_dict(data['retweeted_tweet']) if data.get('retweeted_tweet') else None
        ) 