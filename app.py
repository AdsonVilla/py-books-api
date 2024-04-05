from flask import Flask, jsonify, request

app = Flask(__name__)


books = [
    {
        'id': 1,
        'title': 'Bom dia, Verônica',
        'author': 'Raphael Montes',
    },
    {
        'id': 2,
        'title': 'Dias perfeitos',
        'author': 'Raphael Montes',
    },
    {
        'id': 3,
        'title': 'Harry Potter',
        'author': 'J. K. Rolling',
    },
]   

# consultar todos
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# consultar id
@app.route('/books/<int:id>', methods=['GET'])
def get_book_by_id(id):
    for book in books:
        if book.get('id') == id:
            return jsonify(book)

# editar
@app.route('/books/<int:id>', methods=['PUT'])
def edit_book_by_id(id):
    edited_book = request.get_json()
    for indice,book in enumerate(books):
        if book.get('id') == id:
            books[indice].update(edited_book)
            return jsonify(books[indice])
        

# criar
@app.route('/books', methods=['POST'])
def create_book():
    new_book = request.get_json()
    books.append(new_book)
    
    return jsonify(books)
# excluir
app.run(port=5000, host='localhost', debug=True)