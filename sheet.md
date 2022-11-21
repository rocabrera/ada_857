## Comandos de python

```
python -m venv <nome da sua env>
```

## Docker

Se você estiver no ***folder*** que contém o arquivo Dockerfile:
```
docker image build -t <nome_imagem> .
```

Executa o container com o último comando da imagem: 
```
docker container run <nome_imagem>
```

Executa o container com o último comando da imagem alterado: 

```
docker container run -it <nome_imagem> <comando>
```

Exemplo para entrar dentro do container (caso a imagem base tenha o comando bash):

```
docker container run -it <nome_imagem> bash
```

## GIT

Commandos básicos:

- ```git clone <url do repo>``` : bla bla
- ```git add <caminho para o arquivo a ser adicionado>``` : bla bla
- ```git status```: Esse comando para entender o que está acontecendo.
- ```git commit -m "mensagem obrigatória"```: bla bla

Commandos Avançados:

- ```git switch -c <nome_branch>```: cria uma branch 
- ```git checkout -b <nome_branch>```: cria uma branch 

Depois ... entender: 

- git restore 

Git para equipes:

- git branch: <branch>
- git merge:
- ...

## Tests

Instalando libs de tests:
```
pip install pytest
```
Executando os tests (a flag -s serve para printar no terminal):
```
pytest -s tests
```
No computador do professor:
```
python -m pytest -s tests
```