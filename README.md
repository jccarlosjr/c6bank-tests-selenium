# 🏦 C6Bank Test Automation

Functional test automation for Banco C6's web system, using **Python**, **Selenium WebDriver**, and **Pytest**.

---

## 🚀 Technologies Used

- Python 3.10+
- Selenium WebDriver
- Pytest
- Pytest-HTML (for generating reports)
- Page Object Model (POM)
- ChromeDriver

---

## 🗂️ Project Structure

```
c6bank-tests-selenium/
│
├── tests/              # Test cases
├── pages/              # Page Objects
├── drivers/            # WebDriver setup and exec
├── utils/              # Utility functions
├── reports/            # HTML reports
├── config/             # Configuration
├── requirements.txt    # Dependencies
└── README.md
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/c6bank-tests-selenium.git
cd c6bank-tests-selenium
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate          # Windows
source venv/bin/activate       # Linux/macOS
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🧪 Running the Tests

### Run all tests:

```bash
pytest
```

### Run tests with HTML report:

```bash
pytest tests/ --html=reports/report.html
```

---

## 📸 Reports

After running with `--html`, open:

```
reports/report.html
```

---

## 🧰 Prerequisites

- Google Chrome installed
- Compatible `chromedriver.exe` version (set in drivers/webdrivers)

---

## ✨ Contributions

Contributions are welcome! Feel free to open issues or pull requests.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

> Project created for study purposes and demonstration of modern QA practices with web automation.

---

---

# 🏦 Automação de Testes do C6Bank

Automação de testes funcionais do sistema web do Banco C6, utilizando **Python**, **Selenium WebDriver** e **Pytest**.

---

## 🚀 Tecnologias Utilizadas

- Python 3.10+
- Selenium WebDriver
- Pytest
- Pytest-HTML (para geração de relatórios)
- Page Object Model (POM)
- ChromeDriver

---

## 🗂️ Estrutura do Projeto

```
c6bank-tests-selenium/
│
├── tests/              # Casos de teste
├── pages/              # Page Objects
├── drivers/            # Setup do WebDriver
├── utils/              # Funções auxiliares
├── reports/            # Relatórios HTML
├── config/             # Configurações do sistema
├── requirements.txt    # Dependências
└── README.md
```

---

## ⚙️ Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/c6bank-tests-selenium.git
cd c6bank-tests-selenium
```

2. Crie e ative o ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate          # Windows
source venv/bin/activate       # Linux/macOS
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## 🧪 Executando os Testes

### Todos os testes:

```bash
pytest
```

### Teste com relatório HTML:

```bash
pytest tests/ --html=reports/report.html
```

---

## 📸 Relatórios

Após a execução com `--html`, abra o arquivo:

```
reports/report.html
```

---

## 🧰 Pré-requisitos

- Google Chrome instalado
- `chromedriver.exe` compatível com sua versão do navegador (localizado na pasta drivers/webdrivers)

---

## ✨ Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

> Projeto desenvolvido para fins de estudo e demonstração de práticas modernas de QA com automação web.
