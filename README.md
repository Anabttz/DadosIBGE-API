
# DadosIBGE-API

Este projeto é uma API desenvolvida com **FastAPI**, **Docker** e **web scraping**, criada para disponibilizar informações atualizadas sobre estados e municípios brasileiros.  
A aplicação realiza a coleta de dados diretamente do site do IBGE e os fornece através de endpoints estruturados e de fácil acesso.

---

## Sobre o Projeto

O **DadosIBGE-API** foi desenvolvido com foco em praticar e aplicar conceitos de desenvolvimento backend, APIs REST e containerização com Docker.  
O projeto demonstra como construir uma API utilizando FastAPI, capaz de integrar-se com fontes de dados externas por meio de scraping automatizado.

---

## Funcionalidades

- Listagem de todos os estados do Brasil.  
- Consulta de municípios por sigla do estado.  
- Retorno dos dados em formato JSON.  
- Estrutura simples, escalável e containerizada.

---

## Tecnologias Utilizadas

- **Python 3.11**
- **FastAPI**
- **Requests**
- **BeautifulSoup4** (para scraping)
- **Docker e Docker Compose**
- **Uvicorn**

---

## Como Executar o Projeto

### 1. Clonar o repositório
```
git clone https://github.com/Anabttz/DadosIBGE-API.git
cd DadosIBGE-API
```

### 2. Subir os containers com Docker

Copiar código
```
docker-compose up --build
```

### 3. Acessar a API
Após a inicialização, acesse no navegador ou no terminal:

http://localhost:8001

### 4.Documentação automática

Acesse a documentação interativa gerada pelo FastAPI:

http://localhost:8001/docs


## Estrutura do Projeto
```
DadosIBGE-API/
│
├── app/  
│   ├── main.py              # Arquivo principal da aplicação FastAPI  
│   ├── scraping.py          # Módulo responsável pela coleta dos dados do   IBGE
│   ├── requirements.txt     # Dependências do projeto  
│
├── Dockerfile               # Configuração da imagem Docker  
├── docker-compose.yml       # Configuração dos containers  
```

---




