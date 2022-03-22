from os import makedirs
import time
import multiprocessing
from requests import get
from bs4 import BeautifulSoup


def downloadIMage(pokemon):
  img_data = get(pokemon["url"]).content
  with open(f'pokemons/{pokemon["name"]}.png', 'wb') as handler:
    handler.write(img_data)


def getUrlsImages():
  page = get('https://pokemondb.net/pokedex/shiny')

  beautiful_soup = BeautifulSoup(page.content, 'html.parser')
  pokemons = beautiful_soup.find_all('span', attrs={'class':'img-fixed shinydex-sprite shinydex-sprite-normal'})

  dados = []
  for pokemon in pokemons:
    dados.append({
      "name": pokemon.get("data-alt"), 
      "url": pokemon.get("data-src")
      })

    if(len(dados) > 10):
      break

  return dados


def main():
  pokemons = getUrlsImages()
  makedirs('pokemons',exist_ok=True)

  # -> Pool
  start = time.time()
  pool = multiprocessing.Pool()
  pool.map(downloadIMage, pokemons)
  end = time.time()

  print(f"-> COM POOL")
  print(f"Finalizado em {end - start:.2f} Segundos!\n")

  # -> Sem Pool
  s = time.time()
  for pokemon in pokemons:
      downloadIMage(pokemon)
  e = time.time()

  print(f"-> Sem POOL")
  print(f"Finalizado em {e - s:.2f} Segundos!\n")


main()