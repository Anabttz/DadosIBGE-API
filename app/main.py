from fastapi import FastAPI
from scraper import obter_estados, obter_municipios_por_estado

app = FastAPI(
    title="API IBGE - Dados do Brasil",
    description="API REST que consome dados reais do IBGE (estados e municípios).",
    version="1.0.0"
)

@app.get("/")
def raiz():
    return {"mensagem": "Bem-vindo à API IBGE! 🚀 Acesse /estados ou /municipios/{sigla}"}

@app.get("/estados")
def listar_estados():
    return obter_estados()

@app.get("/municipios/{sigla_estado}")
def listar_municipios(sigla_estado: str):
    return obter_municipios_por_estado(sigla_estado.upper())
