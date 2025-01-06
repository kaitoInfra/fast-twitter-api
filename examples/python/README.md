# Twitter API Python Examples

This directory contains Python examples for using the Twitter API client.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set your API key:
```bash
export TWITTER_API_KEY='your_api_key'
```

## Examples

### User Examples
- Get user information
- Get user tweets
- Pagination examples

```bash
python examples/user_examples.py
```

### Search Examples
- Basic tweet search
- Advanced search with filters
- Search pagination

```bash
python examples/search_examples.py
```

### Tweet Examples
- Get tweet replies
- Get tweet quotes
- Time-based filtering
- Pagination examples

```bash
python examples/tweet_examples.py
```

## Project Structure

```
.
├── README.md           # This file
├── requirements.txt    # Project dependencies
├── src/               # Source code
│   ├── client.py      # API client implementation
│   └── utils/         # Utility functions
└── examples/          # Example scripts
```

## Documentation

For detailed API documentation, please visit [https://twitterapi.io/docs](https://twitterapi.io/docs) 