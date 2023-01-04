import requests
from bs4 import BeautifulSoup

def extract():
    web = 'https://www.sportytrader.es/cuotas/baloncesto/usa/nba-306/'
    resultado = requests.get(web)
    soup = BeautifulSoup(resultado.content, 'html.parser')
    return soup

def transform(soup):

    apuestas = soup.find_all('span', {'class':'px-1 h-booklogosm font-bold bg-primary-yellow text-white leading-8 rounded-r-md w-14 md:w-18 flex justify-center items-center text-base'})

    equipos = soup.find_all('span',{'class':'font-medium w-full lg:w-1/2 text-center dark:text-white'})

    lista_apuestas = []
    lista_equipos = []

    for apuesta in apuestas:
        lista_apuestas.append(apuesta.text)

    lista_apuestas = [lista_apuestas[i:i+2] for i in range(0, len(lista_apuestas), 2)]

    for equipo in equipos:
        eq = equipo.find('a').text
        eq = eq[1:-1]
        eq = eq.split(' - ')
        lista_equipos.append(eq)

    return lista_apuestas, lista_equipos

def load(lista_apuestas, lista_equipos):
    dic = {}
    lista = []

    for i in range(len(lista_equipos)):
        dic = {lista_equipos[i][0]:float(lista_apuestas[i][0]), lista_equipos[i][1]:float(lista_apuestas[i][1])}
        lista.append(dic)


    for i in range(len(lista)):
        partidos = list(lista[i].keys())
        if lista[i][partidos[0]] < lista[i][partidos[1]]:
            print(f'En el partido entre {partidos[0]} y {partidos[1]}, el pronóstico es que gane {partidos[0]} con una cuota de {lista[i][partidos[0]]}.')
        else:
            print(f'En el partido entre {partidos[0]} y {partidos[1]}, el pronóstico es que gane {partidos[1]} con una cuota de {lista[i][partidos[1]]}.')


if __name__ == '__main__':

    soup = extract()
    lista_apuestas, lista_equipos = transform(soup)
    load(lista_apuestas, lista_equipos)