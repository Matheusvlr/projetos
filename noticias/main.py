# importar requests
import requests

# importar o tradutor
from googletrans import Translator

# iniciar o tradutor
translator = Translator()

api_key = '699cdb695fb84d91b7ac949aa1e2752e'

pesquisa = 'Google'

# definição de função para a coleta de notícias
def dados():
    noticias_url = f'https://newsapi.org/v2/everything?q={pesquisa}&apiKey={api_key}'

    # fazer uma solicitação
    response = requests.get(noticias_url)

    # convesão dos dados da resposta em JSON
    json_data = response.json()

    # Mostrar os 5 primeiros artigos 
    artigos = json_data['articles'][:5]


    titulos = []
    descricoes = []
    urls = []
    imagens = []

    for artigo in artigos:
        # titulo
        titulos.append(translator.translate(artigo['title'], dest='pt_BR').text)

         # descricoes
        descricoes.append(translator.translate(artigo['description'], dest='pt_BR').text)

         # urls
        urls.append(artigo['url'])

         # imagens
        imagens.append(artigo['urlToImage'])

    # retornar o título
    return [titulos]


# chamar a função
print(dados())

