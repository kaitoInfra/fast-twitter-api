# Клиент Twitter API

Простой и удобный API-клиент для получения данных Twitter с поддержкой SDK на нескольких языках программирования.

## Возможности

### Данные пользователя
- Получить информацию о пользователе `/twitter/user/info`
- Получить список подписчиков `/twitter/user/followers`
- Получить список подписок `/twitter/user/followings`
- Получить упоминания `/twitter/user/mentions`

### Данные твитов
- Получить твиты пользователя `/twitter/user/last_tweets`
- Получить ответы `/twitter/tweet/replies`
- Получить цитаты `/twitter/tweet/quotes`
- Получить ретвитнувших `/twitter/tweet/retweeters`
- Расширенный поиск `/twitter/tweet/advanced_search`

### Данные списков
- Получить твиты из списка `/twitter/list/tweets`

## Быстрый старт

### Python
```python
from twitter_api_client import TwitterAPIClient

client = TwitterAPIClient('your_api_key')

# Получить информацию о пользователе
user = client.get_user_info('elonmusk')
print(user)

# Поиск твитов
tweets = client.search_tweets('python programming')
for tweet in tweets['tweets']:
    print(tweet['text'])
```

Другие примеры кода:
- [Python](../../examples/python/)
- [JavaScript](../../examples/javascript/)
- [Java](../../examples/java/)
- [Go](../../examples/go/)
- [CURL](../../examples/curl/)

## Документация

Документация доступна на нескольких языках:
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

## Лицензия

Этот проект распространяется под лицензией MIT - подробности см. в файле [LICENSE](../../LICENSE) 