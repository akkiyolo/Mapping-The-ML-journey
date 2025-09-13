## put and delete -Http verbs
### working with api's --json

from flask import Flask, jsonify, request

app = Flask(__name__)

## Initial data in my to do list
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"}
]

@app.route('/')
def home():
    return "Welcome to my sample to do list"

## get : retrieve all the items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

## get: retrieve a specific item by id
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "item not found"}), 404
    return jsonify(item)

## post create a new task
@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error": "Invalid request - name is required"}), 400
    new_item = {
        "id": items[-1]["id"] + 1 if items else 1,
        "name": request.json['name'],
        "description": request.json.get('description', '')  # Use get() with default value
    }
    items.append(new_item)
    return jsonify(new_item), 201

## put: update an existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    
    if not request.json:
        return jsonify({"error": "Invalid request - JSON data required"}), 400
    
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)

# DELETE : delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    original_length = len(items)
    items = [item for item in items if item["id"] != item_id]
    
    if len(items) == original_length:
        return jsonify({"error": "Item not found"}), 404
    
    return jsonify({"result": "Item deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)