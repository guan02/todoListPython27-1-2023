from flask import Flask, request, make_response
from flask_cors import CORS  # cors

from faker import Faker
import json

app = Flask(__name__)
CORS(app)  # cors
books = []


@app.route('/')
def index():
  return 'Hello from Flask!'


#genera lista
@app.route('/books', methods=["GET"])
def book_list():
  #  books = []
  if (len(books) <= 0):
    faker = Faker()

    for i in range(5):
      #aggiunge elemento
      books.append({
        "id": i,
        "titolo": faker.name(),
        "description": faker.text()
      })
    return books
  else:
    return books

#ritorna libro specifico
@app.route('/books/<int:id>', methods=["GET"])
def book(id):
  #books = book_list()
  return [id, books[id]]

#aggiunge 
@app.route('/books', methods=["POST"])
def book_create():
  body = request.json

  books.append(body)
  return books

#elimina in base id 
@app.route('/books/<int:id>', methods=["DELETE"])
def book_deleteToID(id):
  #books = book_list()
  if id >= 0 and id < len(books):
    del books[id]
    return make_response({ "message": "Libro eliminato con successo" }, 200)

  return make_response({ "message": "L'id passato non esiste" }, 404)
    
#eliminare tramite titolo
@app.route('/books/<string:nome>', methods=["DELETE"])
def book_deleteToName(nome):
  #books = book_list()  
  for i in range(len(books)):
    if (books[i]["titolo"] == nome ):
      del books[i]
  
      return [
        books,
      ]
    else:
      return books


app.run(host='0.0.0.0', port=81)
