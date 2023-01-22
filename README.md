# FastApi101

- [] MKDIR
- [] PyENV
- [] Configurando Poetry
- [] Estrutura de Pastas
- [] Instalar dependências
- [] 



## MKDIR

```bash

# cria uma pasta para o projeto
$ mkdir FastApi101

# mudar o terminal para acessar a pasta criada
$ cd FastApi101

FastApi101$ _

```

## PyENV

### Instalação

https://github.com/pyenv/pyenv

### Comandos para configurar o interpretador Python

```bash

# Exibe versoes
$ pyenv versions

Saída:
  3.10.9 (set by C:\path\pyenv\version\)
* 3.8.10
  3.9.13

# configura uma versão especifica para uso
$ pyenv global 3.10.9

```

## Configurando Poetry

```bash

$ poetry init

Saída (Deve responder as perguntas): 
This command will guide you through creating your pyproject.toml config.

Package name [fastapi101]:
Version [0.1.0]:  
Description []:  
Author [Dalmo Felipe <dalmo.felipe@gmail.com>, n to skip]:  
License []:  
Compatible Python versions [^3.10]:  

Would you like to define your main dependencies interactively? (yes/no) [yes] no
Would you like to define your development dependencies interactively? (yes/no) [yes] no

Generated file

```

Após responder as perguntas acima, o arquivo `pyproject.toml` será criado na raiz da pasta do projeto. Depois desses passos, ative o ambiente virtual do poetry

```bash

$ poetry shell

Saída:
(fastapi101-py3.10)$ _

```

