#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Uso: $0 <ambiente>"
  echo "Exemplo: $0 dev"
  exit 1
fi

ambiente=$1

if [ "$ambiente" = "dev" ]; then
  python3 -m pip install -r bundle/bundle-dev.txt
elif [ "$ambiente" = "prod" ]; then
  python3 -m pip install -r bundle/bundle-prod.txt
else
  echo "Ambiente inválido. Use 'dev' ou 'prod'."
  exit 1
fi
