# Cliente API do Twitter

Um cliente API simples e fácil de usar para recuperar dados do Twitter, com suporte SDK em várias linguagens.

## Funcionalidades

### Dados do Usuário
- Obter informações do usuário `/twitter/user/info`
- Obter lista de seguidores `/twitter/user/followers`
- Obter lista de seguindo `/twitter/user/followings`
- Obter menções `/twitter/user/mentions`

### Dados dos Tweets
- Obter tweets do usuário `/twitter/user/last_tweets`
- Obter respostas `/twitter/tweet/replies`
- Obter citações `/twitter/tweet/quotes`
- Obter retweeters `/twitter/tweet/retweeters`
- Pesquisa avançada `/twitter/tweet/advanced_search`

### Dados das Listas
- Obter tweets da lista `/twitter/list/tweets`

## Início Rápido

### Python
```python
from twitter_api_client import TwitterAPIClient

client = TwitterAPIClient('your_api_key')

# Obter informações do usuário
user = client.get_user_info('elonmusk')
print(user)

# Pesquisar tweets
tweets = client.search_tweets('python programming')
for tweet in tweets['tweets']:
    print(tweet['text'])
```

Para mais exemplos de código, consulte:
- [Python](../../examples/python/)
- [JavaScript](../../examples/javascript/)
- [Java](../../examples/java/)
- [Go](../../examples/go/)
- [CURL](../../examples/curl/)

## Documentação

A documentação está disponível em vários idiomas:
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

## Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE](../../LICENSE) para detalhes 