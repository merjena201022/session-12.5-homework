Bug 1: The Typo
Where: app.py

What: Code said book_tittle, but HTML said book_title.

How: Terminal showed KeyError.

Fix: Changed book_tittle to book_title.

 Bug 2: The Bracket
Where: index.html

What: Missing a } at the end of {{ book.title }.

How: Browser showed "Internal Server Error."

Fix: Added the missing }.

 Bug 3: The ID Name
Where: script.js

What: JavaScript used ID book-list, but HTML used list-books.

How: Console showed "Cannot read properties of null."

Fix: Changed the ID in script.js to match the HTML.

 Bug 4: The Method
Where: index.html (Form tag)

What: The <form> was missing method="POST".

How: Network Tab showed a GET request instead of POST.

Fix: Added method="POST" to the <form> tag.

🐛 Bug 5: The Folder
Where: Files/Folders

What: style.css was in the main folder, not the static folder.

How: Network Tab showed a 404 Not Found error.

Fix: Moved style.css into the static folder.

🐛 Bug 6: The Permission
Where: app.py (Route)

What: The @app.route was missing methods=['POST'].

How: Network Tab showed a 405 Method Not Allowed error.

Fix: Added methods=['GET', 'POST'] to the route.