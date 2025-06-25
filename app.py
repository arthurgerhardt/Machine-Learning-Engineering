from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

items = []

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items), 200

@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    items.append(data)
    return jsonify({"message": "Item criado com sucesso!", "item": data}), 201

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    if 0 <= item_id < len(items):
        data = request.get_json()
        items[item_id] = data
        return jsonify({"message": "Item atualizado com sucesso!", "item": data}), 200
    return jsonify({"error": "Item não encontrado"}), 404

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if 0 <= item_id < len(items):
        deleted_item = items.pop(item_id)
        return jsonify({"message": "Item deletado com sucesso!", "item": deleted_item}), 200
    return jsonify({"error": "Item não encontrado"}), 404

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Recurso não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)