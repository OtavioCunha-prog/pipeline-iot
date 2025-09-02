# Pipeline IoT com Big Data e IA

##  Descrição do Projeto
Este projeto implementa um pipeline completo utilizando **IoT, Big Data e Inteligência Artificial**, 
com foco no processamento e visualização de dados em tempo real.

###  Tecnologias Utilizadas
- Python 3.x
- PostgreSQL (via Docker)
- Streamlit (dashboard)
- Pandas
- SQL

##  Como Executar

### 1. Clonar o repositório
```bash
git clone https://github.com/OtavioCunha-prog/pipeline-iot.git
cd pipeline-iot
```

### 2. Subir o banco de dados PostgreSQL
```bash
docker-compose up -d
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Ingerir dados no banco
```bash
python src/ingest_data.py
```

### 5. Rodar o dashboard
```bash
streamlit run src/dashboard.py
```

##  Views SQL
As views utilizadas estão disponíveis em `/sql/views.sql`.

##  Dados
O dataset utilizado pode ser baixado no Kaggle:
[Air Quality Dataset](https://www.kaggle.com/datasets/volpatto/air-quality)

Após o download, salve o arquivo CSV na pasta `/data`.

##  Capturas de Tela
As capturas do dashboard devem ser adicionadas na pasta `/docs/prints_dashboard`.

##  Comandos Git utilizados
```bash
git init
git add .
git commit -m "Primeira versão do projeto"
git branch -M main
git remote add origin <url-do-repositorio>
git push -u origin main
```

---
 Autor: Otávio Alvernaz C. Filho  
 Professor: Felipe Bonatto
