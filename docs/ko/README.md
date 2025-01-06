# Twitter API 클라이언트

간단하고 사용하기 쉬운 Twitter 데이터 검색 API 클라이언트로, 다양한 언어의 SDK를 지원합니다.

## 기능

### 사용자 데이터
- 사용자 정보 조회 `/twitter/user/info`
- 팔로워 목록 조회 `/twitter/user/followers`
- 팔로잉 목록 조회 `/twitter/user/followings`
- 멘션 조회 `/twitter/user/mentions`

### 트윗 데이터
- 사용자 트윗 조회 `/twitter/user/last_tweets`
- 답글 조회 `/twitter/tweet/replies`
- 인용 조회 `/twitter/tweet/quotes`
- 리트윗한 사용자 조회 `/twitter/tweet/retweeters`
- 고급 검색 `/twitter/tweet/advanced_search`

### 리스트 데이터
- 리스트 트윗 조회 `/twitter/list/tweets`

## 빠른 시작

### Python
```python
from twitter_api_client import TwitterAPIClient

client = TwitterAPIClient('your_api_key')

# 사용자 정보 조회
user = client.get_user_info('elonmusk')
print(user)

# 트윗 검색
tweets = client.search_tweets('python programming')
for tweet in tweets['tweets']:
    print(tweet['text'])
```

더 많은 코드 예제:
- [Python](../../examples/python/)
- [JavaScript](../../examples/javascript/)
- [Java](../../examples/java/)
- [Go](../../examples/go/)
- [CURL](../../examples/curl/)

## 문서

다음 언어로 문서를 제공합니다:
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

## 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다 - 자세한 내용은 [LICENSE](../../LICENSE) 파일을 참조하세요 