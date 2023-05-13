CREATE DATABASE IF NOT EXISTS imersao_python_flask;

-- Não é necessário usar o comando 'use' no PostgreSQL

CREATE TABLE IF NOT EXISTS imersao_python_flask.alunos (
    id SERIAL PRIMARY KEY,
    nome_aluno VARCHAR(150),
    matricula VARCHAR(20)
);
