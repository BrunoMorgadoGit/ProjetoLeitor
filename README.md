# ProjetoLeitor

Instruções rápidas para instalar dependências e ativar um ambiente virtual (`venv`).

## Requisitos

- Python 3.8+ instalado ou superior
- `git` (opcional)

## Criar e ativar `venv`

### Verifique se você possui permissões suficientes para criar ambientes virtuais.

Windows (PowerShell):

```Powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

### Depois, crie e ative o ambiente virtual no seu diretório do projeto:

Windows (cmd):

```cmd
python -m venv .venv
.\.venv\Scripts\activate
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Após ativar, atualize o pip e tools básicos:

```bash
python -m pip install --upgrade pip setuptools wheel
```

## Instalar dependências

Se já houver um `requirements.txt` gerado (ex.: `pip freeze > requirements.txt`):

```bash
pip install -r requirements.txt
```

Para novas bibliotecas no projeto, execute este comando para atualizar o arquivo requirements.txt:
    
```Powershell
pip freeze > requirements.txt
```

Se preferir instalar as dependências mínimas usadas no projeto:

```bash
pip install flask easyocr opencv-python-headless numpy pillow scikit-image torch torchvision
```

## Executar a aplicação

Com o `venv` ativado, execute:

```bash
python projetoleitor/projetox.py
```

A aplicação iniciará em `http://127.0.0.1:5000` por padrão.
