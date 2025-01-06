# Cliente de API de Twitter

Un cliente de API simple y fácil de usar para obtener datos de Twitter, con soporte SDK en varios lenguajes.

## Características

### Datos de Usuario
- Obtener información del usuario `/twitter/user/info`
- Obtener lista de seguidores `/twitter/user/followers`
- Obtener lista de seguidos `/twitter/user/followings`
- Obtener menciones `/twitter/user/mentions`

### Datos de Tweets
- Obtener tweets del usuario `/twitter/user/last_tweets`
- Obtener respuestas `/twitter/tweet/replies`
- Obtener citas `/twitter/tweet/quotes`
- Obtener retuiteadores `/twitter/tweet/retweeters`
- Búsqueda avanzada `/twitter/tweet/advanced_search`

### Datos de Listas
- Obtener tweets de lista `/twitter/list/tweets`

## Inicio Rápido

### Python
```python
from twitter_api_client import TwitterAPIClient

client = TwitterAPIClient('your_api_key')

# Obtener información del usuario
user = client.get_user_info('elonmusk')
print(user)

# Buscar tweets
tweets = client.search_tweets('python programming')
for tweet in tweets['tweets']:
    print(tweet['text'])
```

Para más ejemplos de código, consulte:
- [Python](../../examples/python/)
- [JavaScript](../../examples/javascript/)
- [Java](../../examples/java/)
- [Go](../../examples/go/)
- [CURL](../../examples/curl/)

## Documentación

La documentación está disponible en varios idiomas:
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

## Licencia

Este proyecto está bajo la Licencia MIT - vea el archivo [LICENSE](../../LICENSE) para más detalles 