import requests
from bs4 import BeautifulSoup


class BuscadorResultados:
    URL_BUSCA = "https://loterias.caixa.gov.br/Paginas/Lotofacil.aspx"
    HEADERS = {
        "User-agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
            " Chrome/89.0.4389.90 Safari/537.36"
        )
    }

    def obtem_pagina_lotofacil(self):
        response = requests.get(self.URL_BUSCA, headers=self.HEADERS)
        # soup = BeautifulSoup(response.text, 'html5lib')
        soup = BeautifulSoup(response.text, 'html.parser')
        elementos_li = soup.select('.simple-container.lista-dezenas.lotofacil li.dezena')
        # import pdb; pdb.set_trace()
        for elemento in elementos_li:
            print(elemento.text)


        # resposta_str = '\n'.join([str(tag) for tag in resposta])

        # for dezena_element in dezenas_elements:
        # #     print(dezena_element)
        # with open('li_s_lotofacil.html', 'w', encoding='utf-8') as arquivo:
        #     arquivo.write(resposta_str)
        # print("aquivo salvo com sucesso!")
