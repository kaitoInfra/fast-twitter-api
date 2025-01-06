# Twitter API Client

A simple and easy-to-use Twitter data retrieval API client with multi-language SDK support.
Backed by [TwitterAPIDotIO](https://twitterapi.io)
## Features

### User Data
- Get user information `/twitter/user/info`
- Get user followers `/twitter/user/followers` 
- Get user followings `/twitter/user/followings`
- Get user mentions `/twitter/user/mentions`

### Tweet Data
- Get user tweets `/twitter/user/last_tweets`
- Get tweet replies `/twitter/tweet/replies`
- Get tweet quotes `/twitter/tweet/quotes`
- Get tweet retweeters `/twitter/tweet/retweeters`
- Advanced tweet search `/twitter/tweet/advanced_search`

### List Data
- Get list tweets `/twitter/list/tweets`

## Quick Start

### Python
```python
from twitter_api_client import TwitterAPIClient

client = TwitterAPIClient('your_api_key')

# Get user information
user = client.get_user_info('elonmusk')
print(user)

# Search tweets
tweets = client.search_tweets('python programming')
for tweet in tweets['tweets']:
    print(tweet['text'])
```

For more code examples, check:
- [Python](examples/python/)
- [JavaScript](examples/javascript/)
- [Java](examples/java/)
- [Go](examples/go/)
- [CURL](examples/curl/)

## Documentation

Documentation is available in multiple languages:
- [English](docs/en/)
- [中文](docs/zh/)
- [日本語](docs/ja/)
- [Español](docs/es/)
- [한국어](docs/ko/)
- [Français](docs/fr/)
- [Deutsch](docs/de/)
- [Italiano](docs/it/)
- [Português](docs/pt/)
- [Русский](docs/ru/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.