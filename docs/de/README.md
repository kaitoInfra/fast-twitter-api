# Twitter API Client

Ein einfach zu verwendender Twitter-Daten-API-Client mit SDK-Unterstützung in mehreren Programmiersprachen.

## Funktionen

### Benutzerdaten
- Benutzerinformationen abrufen `/twitter/user/info`
- Followerliste abrufen `/twitter/user/followers`
- Following-Liste abrufen `/twitter/user/followings`
- Erwähnungen abrufen `/twitter/user/mentions`

### Tweet-Daten
- Benutzer-Tweets abrufen `/twitter/user/last_tweets`
- Antworten abrufen `/twitter/tweet/replies`
- Zitate abrufen `/twitter/tweet/quotes`
- Retweeter abrufen `/twitter/tweet/retweeters`
- Erweiterte Suche `/twitter/tweet/advanced_search`

### Listen-Daten
- Listen-Tweets abrufen `/twitter/list/tweets`

## Schnellstart

### Python
```python
from twitter_api_client import TwitterAPIClient

client = TwitterAPIClient('your_api_key')

# Benutzerinformationen abrufen
user = client.get_user_info('elonmusk')
print(user)

# Tweets suchen
tweets = client.search_tweets('python programming')
for tweet in tweets['tweets']:
    print(tweet['text'])
```

Weitere Codebeispiele finden Sie hier:
- [Python](../../examples/python/)
- [JavaScript](../../examples/javascript/)
- [Java](../../examples/java/)
- [Go](../../examples/go/)
- [CURL](../../examples/curl/)

## Dokumentation

Die Dokumentation ist in mehreren Sprachen verfügbar:
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

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz - siehe die [LICENSE](../../LICENSE) Datei für Details 