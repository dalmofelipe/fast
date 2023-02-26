## FastApi101

### Preparar Ambiente

Clonar projeto

```bash
> git clone https://github.com/dalmofelipe/FastApi101.git
```

Iniciar shell poetry

```bash
> cd FastApi101
> poetry shell
```

Instalar dependências do `pyproject.toml`

```bash
> poetry install
```

### Executando o Projeto

Criar arquivo `.env` na raiz do projeto. Configure `ENVIRONMENT=DEV`, o sqlite irá gerar o arquivo de dados `database.sqlite` no diretorio `fast/infra/`. Para modificar o local desse arquivo , edite no `.env` a variável `DB_DEV=sqlite:///novo/caminho/do/arquivo/database.sqlite`.

Para iniciar o servidor, usar o comando runserver da CLI

```bash
> fast runserver --port=3333
```

O server ficará escultando na porta 3333, no host http://localhost:3333.

Por padrão o app esculta a porta 8000, `--port=3333` é opcional.

Acesse a ajuda com os comandos:

```bash
> fast --help
> fast runserver --help
```

### ToDo

- [x] Criptografar senha com bcrypt, antes de persistir no banco
- [x] Extrair Routes dos Controllers do modulo WEB
- [x] Extrair Routes do modulo API
- [x] Logar no sistema, exibindo uma tela de boa vindas apos logon
- [ ] Proteger página index de usuários não logados com session ou bearer token
- [ ] Session? dar um jeito de salvar dados do usuário logado no navegador
- [ ] Retornar um Token JWT? api? garantindo autenticação do usuário
- [x] Variáveis de ambiente
- [x] Conexão com MySQL ou Postgres
- [ ] Refatorar código de registro de usuário, de modo que fique indempedente das interfaces api, cli e web
- [x] Configurar o formatador de código blue
- [ ] Controlar Error 404 com página pessonalizada


### Links

- [PyENV - https://github.com/pyenv/pyenv](https://github.com/pyenv/pyenv)
- [Poetry - https://python-poetry.org/docs/](https://python-poetry.org/docs/)
- [FastAPI - https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)
- [SQLModel - https://sqlmodel.tiangolo.com/](https://sqlmodel.tiangolo.com/)

