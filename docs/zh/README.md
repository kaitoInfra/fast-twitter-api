# Twitter API 客户端

一个简单易用的Twitter数据获取API客户端,提供多语言SDK支持。

## 功能特性

### 用户数据
- 获取用户信息 `/twitter/user/info`
- 获取用户关注者列表 `/twitter/user/followers` 
- 获取用户关注列表 `/twitter/user/followings`
- 获取用户提及 `/twitter/user/mentions`

### 推文数据
- 获取用户推文 `/twitter/user/last_tweets`
- 获取推文回复 `/twitter/tweet/replies`
- 获取推文引用 `/twitter/tweet/quotes`
- 获取推文转发者 `/twitter/tweet/retweeters`
- 高级推文搜索 `/twitter/tweet/advanced_search`

### 列表数据
- 获取列表推文 `/twitter/list/tweets`

## 快速开始

### Python
```python
from twitter_api_client import TwitterAPIClient

client = TwitterAPIClient('your_api_key')

# 获取用户信息
user = client.get_user_info('elonmusk')
print(user)

# 搜索推文
tweets = client.search_tweets('python programming')
for tweet in tweets['tweets']:
    print(tweet['text'])
```

更多示例代码请查看:
- [Python](../../examples/python/)
- [JavaScript](../../examples/javascript/)
- [Java](../../examples/java/)
- [Go](../../examples/go/)
- [CURL](../../examples/curl/)

## 文档

文档支持以下语言:
- [English](../en/)
- [中文](../zh/)
- [日本語](../ja/)
- [Español](../es/)
- [한국어](../ko/)
- [Français](../fr/)
- [Deutsch](../de/)
- [Italiano](../it/)
- [Português](../pt/)
- [Русский](../ru/)

## 开源协议

本项目采用 MIT 协议开源 - 详见 [LICENSE](../../LICENSE) 文件 