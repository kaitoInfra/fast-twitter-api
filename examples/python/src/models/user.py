"""
User data model classes.
"""

from dataclasses import dataclass
from typing import List, Optional, Dict

@dataclass
class User:
    """Represents a Twitter user."""
    id: str
    username: str
    name: str
    description: Optional[str]
    followers_count: int
    following_count: int
    tweet_count: int
    listed_count: int
    created_at: str
    verified: bool
    protected: bool
    location: Optional[str]
    url: Optional[str]
    profile_image_url: str
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'User':
        """Create User instance from dictionary."""
        return cls(
            id=data['id'],
            username=data['userName'],
            name=data['name'],
            description=data.get('description'),
            followers_count=data['followers'],
            following_count=data['following'],
            tweet_count=data['statusesCount'],
            listed_count=0,  # Not provided in API
            created_at=data['createdAt'],
            verified=data['isBlueVerified'],
            protected=not data['canDm'],
            location=data.get('location'),
            url=data.get('url'),
            profile_image_url=data['profilePicture']
        ) 