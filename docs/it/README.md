# Client API Twitter

Un client API semplice e facile da usare per recuperare i dati di Twitter, con supporto SDK in diversi linguaggi.

## Funzionalità

### Dati Utente
- Ottenere informazioni utente `/twitter/user/info`
- Ottenere lista follower `/twitter/user/followers`
- Ottenere lista following `/twitter/user/followings`
- Ottenere menzioni `/twitter/user/mentions`

### Dati Tweet
- Ottenere tweet utente `/twitter/user/last_tweets`
- Ottenere risposte `/twitter/tweet/replies`
- Ottenere citazioni `/twitter/tweet/quotes`
- Ottenere retweeter `/twitter/tweet/retweeters`
- Ricerca avanzata `/twitter/tweet/advanced_search`

### Dati Liste
- Ottenere tweet della lista `/twitter/list/tweets`

## Avvio Rapido

### Python
```python
from twitter_api_client import TwitterAPIClient

client = TwitterAPIClient('your_api_key')

# Ottenere informazioni utente
user = client.get_user_info('elonmusk')
print(user)

# Cercare tweet
tweets = client.search_tweets('python programming')
for tweet in tweets['tweets']:
    print(tweet['text'])
```

Per altri esempi di codice, consulta:
- [Python](../../examples/python/)
- [JavaScript](../../examples/javascript/)
- [Java](../../examples/java/)
- [Go](../../examples/go/)
- [CURL](../../examples/curl/)

## Documentazione

La documentazione è disponibile in diverse lingue:
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

## Licenza

Questo progetto è sotto licenza MIT - vedere il file [LICENSE](../../LICENSE) per i dettagli 