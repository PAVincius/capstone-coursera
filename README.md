# AI Command Center - Capstone Project

Este repositório contém a implementação do projeto Capstone, focado em criar uma solução de Machine Learning robusta, modular e pronta para produção. O projeto segue as melhores práticas de Engenharia de Software e MLOps.

## 📂 Estrutura do Repositório

```plaintext
capstone-coursera/
├── data/               # Dados brutos e processados
├── models/             # Modelos serializados (.joblib)
├── logs/               # Logs de aplicação e testes
├── src/                # Código fonte principal
│   ├── app.py          # API Flask com endpoint de predição
│   ├── ingestion.py    # Pipeline de ingestão de dados
│   ├── logger.py       # Configuração de logging customizada
│   └── model.py        # Lógica de treinamento e inferência
├── tests/              # Testes unitários e de integração
├── notebooks/          # Notebooks para EDA e experimentação
├── Dockerfile          # Definição do container da aplicação
├── requirements.txt    # Dependências do projeto
└── run-tests.sh        # Script utilitário para execução de testes
```

## 🚀 Como Executar

### Pré-requisitos
- Python 3.9+
- Docker (opcional)

### Instalação Local

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

2. Execute a API:
   ```bash
   python src/app.py
   ```
   A API estará disponível em `http://localhost:5000`.

### Execução via Docker

1. Construa a imagem:
   ```bash
   docker build -t capstone-api .
   ```

2. Execute o container:
   ```bash
   docker run -p 5000:5000 capstone-api
   ```

## 🧪 Testes

O projeto conta com uma suíte de testes automatizados para garantir a qualidade do código.

Para rodar os testes:
```bash
./run-tests.sh
# ou
pytest tests/
```

Os logs de teste são isolados em `logs/test/` para não interferir na monitoria de produção.

## 📊 Funcionalidades

- **Ingestão de Dados**: Suporte a CSV e JSON via `src/ingestion.py`.
- **API de Predição**: Endpoint `/predict` capaz de lidar com requisições globais e específicas por país.
- **Monitoramento**: Decoradores de performance para medir tempo de resposta e drift.
- **Logging**: Sistema de logs estruturado e isolado por ambiente.
