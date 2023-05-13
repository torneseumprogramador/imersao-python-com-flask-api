CREATE DATABASE IF NOT EXISTS imersao_python_flask;

use imersao_python_flask;

CREATE TABLE IF NOT EXISTS imersao_python_flask.clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_cliente VARCHAR(150),
    matricula VARCHAR(20)
);
