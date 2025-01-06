"""
Custom exceptions for Twitter API client.
"""

class TwitterAPIError(Exception):
    """Base exception for Twitter API errors."""
    
    def __init__(self, message: str, status_code: int = None):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

class TwitterAuthError(TwitterAPIError):
    """Raised when authentication fails."""
    pass

class TwitterRateLimitError(TwitterAPIError):
    """Raised when rate limit is exceeded."""
    pass

class TwitterNotFoundError(TwitterAPIError):
    """Raised when resource is not found."""
    pass

class TwitterValidationError(TwitterAPIError):
    """Raised when request validation fails."""
    pass 