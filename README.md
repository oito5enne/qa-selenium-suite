# Suíte de Testes Automatizados — Selenium + Pytest

Automação de testes end-to-end de um fluxo de e-commerce, usando **Page Object Model**, **esperas explícitas** e **relatório HTML**. Alvo: [saucedemo.com](https://www.saucedemo.com), aplicação pública criada para prática de automação.

## O que este projeto demonstra

- **Page Object Model (POM)** — separação entre lógica de teste e detalhes da interface, o padrão usado em projetos de QA reais.
- **Esperas explícitas** — zero `sleep` fixo; os testes esperam o elemento certo, ficando estáveis.
- **Testes parametrizados** — um único teste cobre vários cenários de login inválido.
- **Marcadores** (`smoke` / `regression`) — permite rodar só o essencial ou a suíte completa.
- **Modo headless** — pronto para rodar em CI.
- **Relatório HTML** gerado automaticamente a cada execução.

## Cobertura

| Arquivo | Cenários |
|---|---|
| `test_login.py` | Login válido + 4 cenários negativos (usuário bloqueado, senha errada, campos vazios) |
| `test_inventory.py` | Listagem de produtos e adição ao carrinho |
| `test_checkout.py` | Fluxo completo de compra (login → carrinho → checkout → confirmação) |

## Como rodar

```bash
# 1. Crie um ambiente virtual
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Rode a suíte (abre o navegador)
pytest

# Só os testes de fumaça
pytest -m smoke

# Sem abrir janela (CI)
HEADLESS=1 pytest
```

Ao final, abra `report.html` para ver o relatório.

## Estrutura

```
qa-selenium-suite/
├── conftest.py          # fixture do WebDriver (setup/teardown)
├── pytest.ini           # configuração e marcadores
├── pages/               # Page Objects
│   ├── base_page.py     # interações comuns + esperas
│   ├── login_page.py
│   ├── inventory_page.py
│   └── checkout_page.py
└── tests/               # casos de teste
    ├── test_login.py
    ├── test_inventory.py
    └── test_checkout.py
```

## Stack

Python · Selenium · Pytest · webdriver-manager · pytest-html
