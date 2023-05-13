from flask import jsonify


def inicial_index():
    return jsonify({
        'mensagem': 'Bem vindo a imersão de Python com Flask API',
        'endpoints': [
            { 
                "alunos": {
                    "GET": "/alunos",
                    "POST": {
                        "rota": "/alunos",
                        "body": {
                            "id": 0,
                            "nome": "",
                            "matricula": "",
                        }
                    },
                    "PUT": {
                        "rota": "/alunos/{id}",
                        "body": {
                            "nome": "",
                            "matricula": "",
                        }
                    },
                    "DELETE": "/alunos/{id}"
                }
            }
        ]
    })
