from flask import jsonify


def inicial_index():
    return jsonify({
        'mensagem': 'Bem vindo a imersão de Python com Flask API',
        'endpoints': [
            { 
                "GET": "/alunos",
                "POST": {
                    "rota": "/alunos",
                    "body": {
                        "id": 0,
                        "nome": "",
                        "matricula": "",
                    }
                }
            }
        ]
    })
