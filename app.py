import os
import json
import uuid
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)
app.secret_key = "reading_tracker_secret_123"
BOOKS_FILE = "books.json"

def get_books():
    if not os.path.exists(BOOKS_FILE) or os.stat(BOOKS_FILE).st_size == 0:
        with open(BOOKS_FILE, 'w') as f:
            json.dump([], f)
        return []
    with open(BOOKS_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_books(books):
    with open(BOOKS_FILE, 'w') as f:
        json.dump(books, f, indent=4)

@app.route('/')
def index():
    books = get_books()
    stats = {'total': len(books), 'finished': len([b for b in books if b.get('status') == 'finished'])}
    return render_template('index.html', books=books, stats=stats)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        books = get_books()
        books.append({
            "id": str(uuid.uuid4()),
            "title": request.form.get('title'),
            "author": request.form.get('author'),
            "status": request.form.get('status'),
            "rating": request.form.get('rating', 0),
            "review": request.form.get('review', "")
        })
        save_books(books)
        return redirect(url_for('index'))
    return render_template('add_book.html')

@app.route('/edit/<book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    books = get_books()
    book = next((b for b in books if b['id'] == book_id), None)
    if request.method == 'POST' and book:
        book.update({"title": request.form.get('title'), "author": request.form.get('author'), "status": request.form.get('status')})
        save_books(books)
        return redirect(url_for('index'))
    return render_template('edit_book.html', book=book)

@app.route('/delete/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    books = [b for b in get_books() if b['id'] != book_id]
    save_books(books)
    return jsonify({"success": True})

if __name__ == '__main__':
    app.run(debug=True)