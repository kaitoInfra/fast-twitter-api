# Twitter API クライアント

シンプルで使いやすいTwitterデータ取得APIクライアント。複数言語のSDKをサポートしています。

## 機能

### ユーザーデータ
- ユーザー情報の取得 `/twitter/user/info`
- フォロワーリストの取得 `/twitter/user/followers` 
- フォローリストの取得 `/twitter/user/followings`
- メンションの取得 `/twitter/user/mentions`

### ツイートデータ
- ユーザーツイートの取得 `/twitter/user/last_tweets`
- リプライの取得 `/twitter/tweet/replies`
- 引用の取得 `/twitter/tweet/quotes`
- リツイートユーザーの取得 `/twitter/tweet/retweeters`
- 高度な検索 `/twitter/tweet/advanced_search`

### リストデータ
- リストツイートの取得 `/twitter/list/tweets`

## クイックスタート

### Python
```python
from twitter_api_client import TwitterAPIClient

client = TwitterAPIClient('your_api_key')

# ユーザー情報の取得
user = client.get_user_info('elonmusk')
print(user)

# ツイートの検索
tweets = client.search_tweets('python programming')
for tweet in tweets['tweets']:
    print(tweet['text'])
```

その他のコード例はこちら:
- [Python](../../examples/python/)
- [JavaScript](../../examples/javascript/)
- [Java](../../examples/java/)
- [Go](../../examples/go/)
- [CURL](../../examples/curl/)

## ドキュメント

ドキュメントは以下の言語で利用可能です:
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

## ライセンス

このプロジェクトはMITライセンスの下で公開されています - 詳細は[LICENSE](../../LICENSE)ファイルをご覧ください 