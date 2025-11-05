
import requests

BASE_URL = "http://localhost:8001"  # Endereço da API


def listar_estados():
    url = f"{BASE_URL}/estados"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        estados = resposta.json()
        print("🗺️  Lista de estados:")
        for estado in estados:
            print(f"- {estado['sigla']} | {estado['nome']}")
    else:
        print("Erro ao obter estados:", resposta.text)

def listar_municipios(sigla):
    url = f"{BASE_URL}/municipios/{sigla.upper()}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        municipios = resposta.json()
        print(f"\n🏙️  Municípios do estado {sigla.upper()}:")
        for cidade in municipios[:10]:  # mostra apenas os 10 primeiros
            print(f"- {cidade['nome']}")
    else:
        print("Erro ao obter municípios:", resposta.text)

if __name__ == "__main__":
    listar_estados()
    listar_municipios("SP")  # É possível trocar SP por RJ, MG, BA...
