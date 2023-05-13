from flask import Flask, jsonify, request

app = Flask(__name__)

clients = []

@app.route("/clients", methods=["GET"])
def get_clients():
    return jsonify(clients)

@app.route("/clients", methods=["POST"])
def create_client():
    new_client = request.get_json()
    clients.append(new_client)
    return jsonify(new_client), 201

@app.route("/clients/<int:client_id>", methods=["GET"])
def get_client(client_id):
    for client in clients:
        if client["id"] == client_id:
            return jsonify(client)
    return jsonify({"error": "Client not found"}), 404

@app.route("/clients/<int:client_id>", methods=["PUT"])
def update_client(client_id):
    for client in clients:
        if client["id"] == client_id:
            updated_client = request.get_json()
            client.update(updated_client)
            return jsonify(client)
    return jsonify({"error": "Client not found"}), 404

@app.route("/clients/<int:client_id>", methods=["DELETE"])
def delete_client(client_id):
    for client in clients:
        if client["id"] == client_id:
            clients.remove(client)
            return jsonify({"message": "Client deleted"})
    return jsonify({"error": "Client not found"}), 404

if __name__ == "__main__":
    app.run()
