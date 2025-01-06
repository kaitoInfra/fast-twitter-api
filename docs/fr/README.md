# Client API Twitter

Un client API simple et facile à utiliser pour récupérer des données Twitter, avec support SDK dans plusieurs langages.

## Fonctionnalités

### Données Utilisateur
- Obtenir les informations utilisateur `/twitter/user/info`
- Obtenir la liste des abonnés `/twitter/user/followers`
- Obtenir la liste des abonnements `/twitter/user/followings`
- Obtenir les mentions `/twitter/user/mentions`

### Données des Tweets
- Obtenir les tweets de l'utilisateur `/twitter/user/last_tweets`
- Obtenir les réponses `/twitter/tweet/replies`
- Obtenir les citations `/twitter/tweet/quotes`
- Obtenir les retweeteurs `/twitter/tweet/retweeters`
- Recherche avancée `/twitter/tweet/advanced_search`

### Données des Listes
- Obtenir les tweets d'une liste `/twitter/list/tweets`

## Démarrage Rapide

### Python
```python
from twitter_api_client import TwitterAPIClient

client = TwitterAPIClient('your_api_key')

# Obtenir les informations utilisateur
user = client.get_user_info('elonmusk')
print(user)

# Rechercher des tweets
tweets = client.search_tweets('python programming')
for tweet in tweets['tweets']:
    print(tweet['text'])
```

Pour plus d'exemples de code, consultez:
- [Python](../../examples/python/)
- [JavaScript](../../examples/javascript/)
- [Java](../../examples/java/)
- [Go](../../examples/go/)
- [CURL](../../examples/curl/)

## Documentation

La documentation est disponible dans plusieurs langues:
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

## Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](../../LICENSE) pour plus de détails 