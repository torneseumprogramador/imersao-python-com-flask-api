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

## comandos executados no no servidor em aula
```shell
1  apt install nginx
2  git clone https://github.com/torneseumprogramador/imersao-python-com-fask-api.git
3  exit
4  ls
5  cd imersao-python-com-fask-api/
6  python3 -version
7  python3 --version
8  pip
9  apt install python3-pip
10  apt uopdate
11  apt update
12  apt install python3-pip
13  apt install mysql-server
14  mysql
15  ls
16  sh bundle prod
17  sh bundle.sh prod
18  ls
19  sh mysql_migration.sh 
20  ls
21  cat infraestrutura/db/mysql/migrations/executados.txt 
22  ls
23  cat infraestrutura/db/mysql/migrations/executados.txt 
24  mysql -uroot -p'root'
25  ls
26  sh start.sh 
27  vim /etc/nginx/sites-available/default 
28  systemctl restart nginx
29  sh start.sh 
30  mysql 
31  vim /etc/mysql/my.cnf
32  vim /usr/local/mysql/my.cnf
33  vim /etc/mysql/mysql.cnf 
34  vim /etc/mysql/my.cnf
35  vim /etc/mysql/conf.d/mysql.cnf 
36  vim /etc/mysql/mysql.conf.d/mysql.cnf 
37  vim /etc/mysql/mysql.conf.d/mysqld.cnf 
38  systemctl restart mysql
39  ip address
40  mysql -uroot -p'root' -h 172.31.53.230
41  vim env_vars.sh 
42  sh start.sh 
43  vim env_vars.sh 
44  mysql -uroot -p'root' -h 172.31.53.230
45  unset HOST
46  vim env_vars.sh 
47  sh start.sh 
48  vim infraestrutura/db/mysql/db.py 
49  sh start.sh 
50  vim infraestrutura/db/mysql/db.py 
51  cat env_vars.sh 
52  vim ~/.bashrc 
53  source ~/.bashrc 
54  sh start.sh 
55  sh start.sh &
56  exit
57  lsof -i:5000 # descobrir o pid da aplicação rodando
58  kill -9 9807 # derrubar a aplciação com o pip capturado
59  vim /etc/nginx/sites-available/default 
60  cat /etc/nginx/sites-available/default 
61  pwd
62  cd imersao-python-com-fask-api/
63  cd front-end/
64  ls
65  pwd
66  vim /etc/nginx/sites-available/default 
67  systemctl restar nginx
68  systemctl restart nginx
69  vim index.html 
70  cd ../
71  sh start.sh &
72  ls /root/imersao-python-com-fask-api/front-end
73  ls -l /root/imersao-python-com-fask-api/front-end
74  sudo chown www-data:www-data /root/imersao-python-com-fask-api/front-end/index.html
75  sudo chown www-data:www-data /root/imersao-python-com-fask-api/front-end/index.html 
76  ls -l /root/imersao-python-com-fask-api/front-end
77  ls
78  vim /var/www/html/index.html
79  vim /etc/nginx/sites-available/default 
80  systemctl restar nginx
81  systemctl restart nginx
82  history
```

### .bashrc
```shell
vim ~/.bashrc
```
```vim
export HOST="172.31.53.230"
export USER="root"
export PASS="root"
export DATABASE="imersao_python_flask"

# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
[ -z "$PS1" ] && return

# don't put duplicate lines in the history. See bash(1) for more options
# ... or force ignoredups and ignorespace
HISTCONTROL=ignoredups:ignorespace

# append to the history file, don't overwrite it
shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "$debian_chroot" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
    xterm-color) color_prompt=yes;;
esac

# uncomment for a colored prompt, if the terminal has the capability; turned
# off by default to not distract the user: the focus in a terminal window
# should be on the output of commands, not on the prompt
#force_color_prompt=yes

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
        # We have color support; assume it's compliant with Ecma-48
        # (ISO/IEC-6429). (Lack of such support is extremely rare, and such
        # a case would tend to support setf rather than setaf.)
        color_prompt=yes
    else
        color_prompt=
    fi
fi

if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt force_color_prompt

# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    ;;
*)
    ;;
esac

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
#if [ -f /etc/bash_completion ] && ! shopt -oq posix; then
#    . /etc/bash_completion
#fi
```


### comandos mysql
```mysql
CREATE USER 'root'@'%' IDENTIFIED BY 'root';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```

### config mysql
```shell
vim /etc/mysql/mysql.conf.d/mysqld.cnf
````
```vim
#
# The MySQL database server configuration file.
#
# One can use all long options that the program supports.
# Run program with --help to get a list of available options and with
# --print-defaults to see which it would actually understand and use.
#
# For explanations see
# http://dev.mysql.com/doc/mysql/en/server-system-variables.html

# Here is entries for some specific programs
# The following values assume you have at least 32M ram

[mysqld]
#
# * Basic Settings
#
user            = mysql
# pid-file      = /var/run/mysqld/mysqld.pid
# socket        = /var/run/mysqld/mysqld.sock
# port          = 3306
# datadir       = /var/lib/mysql


# If MySQL is running as a replication slave, this should be
# changed. Ref https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_tmpdir
# tmpdir                = /tmp
#
# Instead of skip-networking the default is now to listen only on
# localhost which is more compatible and is not less secure.
bind-address            = 0.0.0.0
mysqlx-bind-address     = 0.0.0.0
#
# * Fine Tuning
#
key_buffer_size         = 16M
# max_allowed_packet    = 64M
# thread_stack          = 256K

# thread_cache_size       = -1

# This replaces the startup script and checks MyISAM tables if needed
# the first time they are touched
myisam-recover-options  = BACKUP

# max_connections        = 151

# table_open_cache       = 4000

#
# * Logging and Replication
#
# Both location gets rotated by the cronjob.
#
# Log all queries
# Be aware that this log type is a performance killer.
# general_log_file        = /var/log/mysql/query.log
# general_log             = 1
#
# Error log - should be very few entries.
#
log_error = /var/log/mysql/error.log
#
# Here you can see queries with especially long duration
# slow_query_log                = 1
# slow_query_log_file   = /var/log/mysql/mysql-slow.log
# long_query_time = 2
# log-queries-not-using-indexes
#
# The following can be used as easy to replay backup logs or for replication.
# note: if you are setting up a replication slave, see README.Debian about
#       other settings you may need to change.
# server-id             = 1
# log_bin                       = /var/log/mysql/mysql-bin.log
# binlog_expire_logs_seconds    = 2592000
max_binlog_size   = 100M
# binlog_do_db          = include_database_name
# binlog_ignore_db      = include_database_name
```

## Nginx
```vim
server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;

        server_name api.imersao.com.br;

        location / {
                proxy_pass http://localhost:5000;
        }
}

server {
        listen 80;
        listen [::]:80;

        root /var/www/html;
        index index.html;

        server_name imersao.com.br;

        location / {
                try_files $uri $uri/ =404;
        }
}

```