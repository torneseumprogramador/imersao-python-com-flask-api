# Código feito na imersão de python api com flask 
## Feito na comunidade do torne-se um programador
- https://www.torneseumprogramador.com.br/aulas/logica_programacao_python

## Dependências:
- mysql

## Configuração:
```shell
# arquivo env_vars.sh
export HOST="localhost"
export USER="root"
export PASS="root"
export DATABASE="imersao_python_flask"
```

## Para startar a aplicação API digite: 
```shell
sh mysql_migration.sh # rodar migrações do mysql
sh bundle.sh dev # instalar dependências (dev|prod)
sh start.sh # startar a aplicação
```


## Configure o seu host da maquina local com este mapeamento: 
```shell
sudo vim /etc/hosts # MacOs e Linux
notepad C:\Windows\System32\drivers\etc\hosts # Windows
```

```code
127.0.0.1 localhost api.imersao.com.br
```

## Para startar a aplicação FRONT digite: 
```shell
open front-end/index.html # MacOS
start front-end/index.html # windows
xdg-open front-end/index.html # linux
```

## Exemplos em testes feitos com curl via sh
```shell
sh testes/curl/get.sh
sh testes/curl/post.sh
sh testes/curl/put.sh
sh testes/curl/delete.sh
```


## Testes com unittest
### todas as vezes que eu criar um teste novo somente importar no arquivo test.sh como no exemplo abaixo:
```python
import unittest

from testes.unittests.dominio.entidades.aluno_test import TestAluno

unittest.main()
```

## Como executar testes com unittest
```shell
sh test.sh
```

## deploy
### para entrar no servidor executar o comando abaixo
```shell
IP_MAQUINA=<SEU IP> CHAVE_PEM=<SUA CHAVE PRIVADA RSA> sh conectar_no_servidor.sh
```