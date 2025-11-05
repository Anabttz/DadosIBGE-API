
import requests

def obter_estados():
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
    resposta = requests.get(url)
    return resposta.json()

def obter_municipios_por_estado(sigla):
    url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{sigla}/municipios"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        return resposta.json()
    return {"erro": f"Estado '{sigla}' não encontrado."}
