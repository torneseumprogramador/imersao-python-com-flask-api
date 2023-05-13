#!/bin/bash

# Verifica se a variável CHAVE_PEM está definida
if [ -z "$CHAVE_PEM" ]; then
    read -p "Digite a CHAVE_PEM: " CHAVE_PEM
fi

chmod 400 $CHAVE_PEM

# Verifica se a variável IP_MAQUINA está definida
if [ -z "$IP_MAQUINA" ]; then
    read -p "Digite o IP_MAQUINA: " IP_MAQUINA
fi

# Conecta via SSH usando a chave PEM e o endereço IP da máquina
ssh -i "$CHAVE_PEM" ubuntu@"$IP_MAQUINA" -o ServerAliveInterval=60
