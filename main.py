from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app= Flask(__name__)
api= Api(app)

#Defining Data
book= [
    {
        'id': 1,
        'title': 'The Great Gatsby',
        'author': 'F. Scott Fitzgerald',
        'year_published': 1925
    },
    {
        'id': 2,
        'title': 'To Kill a Mockingbird',
        'author': 'Harper Lee',
        'year_published': 1960
    }
]

# Define Api Endpoint
class BookList(Resource):
    def get(self):
        return jsonify({'books': book})
    
    def post(self):
        data= request.get_json()
        new_book= {
            'id':len(book)+ 1,
            'title': data["title"],
            'author': data["author"],
            'year_published': data["year_published"]
        }
        book.append(new_book)
        return jsonify({'book': new_book}), 201

class Book(Resource):
    def get(self, book_id):
        book= next((bok for bok in book if bok["id"] == book_id), None)
        if book:
            return jsonify({'book': book})
        else:
            return jsonify({'error': 'Book Not Found'}), 404
    
    def put(self, book_id):
        data= request.get_json()
        book= next((bok for bok in book if bok["id"] == book_id), None)
        if book:
            book.update(data)
            return jsonify({'book': book})
        else:
            return jsonify({'error': 'Book Not Found'}), 404
    
    def delete(self, book_id):
        global books
        books= [book for book in books if book['id'] != book_id]
        return '', 404
    
# Add endpoint Api
api.add_resource(BookList, '/books')
api.add_resource(Book, '/books/<int:book_id>')

if __name__ == '__main__':
    app.run(debug= Truen)