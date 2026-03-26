# Appium Mobile Banking Framework

Framework inicial de automação mobile com Appium + Python + Pytest, focado em cenários de QA para um app bancário simulado.

## Objetivo
Demonstrar automação mobile com foco em qualidade, cobrindo cenários de negócio como:
- login
- saldo
- transferência
- histórico
- logout

## Stack
- Python
- Appium
- Pytest
- Android Emulator
- UiAutomator2

## Estrutura
- `pages/`: Page Objects
- `tests/`: testes smoke e regression
- `utils/`: driver, waits e screenshots
- `config/`: capabilities e configurações
- `data/`: massa de dados simples

## Como executar
```bash
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install -r requirements.txt
pytest
```

## Relatório HTML
```bash
pytest --html=report.html --self-contained-html
```

## Observação
Os locators atuais são placeholders iniciais e devem ser ajustados para o app/tela real usada no projeto.
