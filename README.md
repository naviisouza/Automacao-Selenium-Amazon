# 🛒 Automação Amazon com Selenium

Este projeto realiza a automação de busca de livros na Amazon Brasil, adicionando os itens ao carrinho e exibindo a página final com os produtos selecionados.

## 🧱 Padrão de Projeto Utilizado: Page Object Model (POM)

O Page Object Model (POM) é um padrão de projeto utilizado em automação de testes que organiza o código em camadas separadas:

- **Page Layer**: contém os elementos da página e os métodos que interagem com ela.
- **Test Layer**: executa os cenários de teste utilizando os métodos definidos na camada de página.

Essa separação melhora a legibilidade, facilita a manutenção e permite reutilizar os métodos em diferentes testes.

### Estrutura do projeto:

```
automacao/
├── pages/
│   └── amazon_page.py       # Elementos e ações da página da Amazon
├── tests/
│   └── run_amazon_search.py # Script principal de execução
├── logs/
│   └── automacao.log        # Arquivo de log gerado automaticamente
├── README.md                # Documentação do projeto
└── requirements.txt         # Dependências do projeto
```

## ⚙️ Como instalar o projeto

1. Instale o Python (recomendado: versão 3.10 ou superior)

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## ▶️ Como executar a automação

1. Navegue até a pasta raiz do projeto:

```bash
cd ...\automacao
```

2. Execute o script principal:

```bash
py tests/run_amazon_search.py
```

## 📋 Como verificar os logs

Após a execução, um arquivo de log será gerado automaticamente em:

```
logs/automacao.log
```

Esse arquivo registra cada etapa da automação, incluindo buscas, cliques e adições ao carrinho.

## ✅ O que a automação faz

- Busca o livro “Dom Casmurro” e adiciona ao carrinho  
- Busca o livro “O Pequeno Príncipe” e adiciona ao carrinho  
- Abre a página do carrinho para visualizar os itens

---

Projeto desenvolvido com Selenium com Python e estruturado com boas práticas de automação.
