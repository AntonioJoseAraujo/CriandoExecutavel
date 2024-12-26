# Criando Executável

Este projeto é um exemplo de como criar um executável a partir de um script Python. O executável gerado permite acessar um site específico. 

## 📋 Descrição
Este repositório contém um projeto Python que cria um executável para acessar um site específico. O script app.py automatiza a navegação no site, e o PyInstaller é utilizado para transformar o script em um executável.

## 🚀 Como Usar

1. Clone este repositório:
    ```sh
    git clone https://github.com/AntonioJoseAraujo/CRIANODEXECUTAVEL.git
    ```

2. Navegue até a pasta do projeto:
    ```sh
    cd CRIANODEXECUTAVEL
    ```

3. Ative seu ambiente virtual (opcional, mas recomendado):
    ```sh
    python -m venv venv
    source venv/bin/activate   # No Windows: venv\Scripts\activate
    ```

4. Instale as dependências necessárias:
    ```sh
    pip install -r requirements.txt
    ```

5. Gere o executável utilizando o PyInstaller:
    ```sh
    pyinstaller --onefile --windowed --icon=circulo.ico app.py
    ```

6. O executável será gerado na pasta build/exe.win-amd64-3.11
   

## 📂 Estrutura do Projeto

A estrutura do projeto é a seguinte:

```plaintext
CRIANODEXECUTAVEL/
├── build/
│   └── exe.win-amd64-3.11/
├── musicas/
├── app.py
├── circulo.ico
├── dados.txt
└── setup.py
```

## 🛠 Tecnologias Usadas
- Python
- Selenium
- cx_Freeze
- Módulos padrão do Python(sys, os)no

  
### 📫 Como me encontrar

- [LinkedIn](https://www.linkedin.com/in/antonio-jose-de-araujo/)
- [E-mail](dev.antonioaraujo@gmail.com)
