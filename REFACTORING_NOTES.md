
Modularization of Data Handling: I extracted the JSON reading and writing logic into two standalone functions: load_data() and save_data().
Why: In the previous version, the file opening code was repeated in every route. Now, if I want to change the file name or switch to a database, I only have to change it in one place.
Input Validation: I moved the task validation into a dedicated step before saving.
Why: This prevents "corrupt" or empty tasks from being saved to the JSON file, ensuring the app doesn't crash when rendering the dashboard.
Clean Naming Convention: I renamed vague variables like d, list, or x to descriptive names like all_tasks, new_task, and task_id.
Why: This makes the code "self-documenting," meaning another developer can understand what the code does just by reading the names.
The hardest part was implementing the AJAX Delete functionality. It required perfectly synchronizing three different languages:
Python (Flask): To create a DELETE route that returns JSON instead of a full webpage.
JavaScript: To send the request behind the scenes using the fetch() API.
HTML/CSS: To ensure the specific task card disappeared from the screen smoothly without the whole page flickering or reloading.
The code is significantly more maintainable.
Reduced Redundancy: By using helper functions, the total lines of code in the main routes were reduced by about 30%.
Separation of Concerns: The design (CSS) is now separated from the structure (HTML), and the logic (Python) is separated from the storage (JSON).
Scalability: The app is now "Database Ready." Because the data handling is isolated, Homework 3 (migrating to SQL) will be much easier.
I implemented an Asynchronous Delete feature.
How it works: When a user clicks "Delete," the browser sends a background request to the /delete/<id> route.
The Benefit: The user stays on the same page, and the task card fades away instantly. This creates a "Minimalist" and high-end user experience common in modern apps like Notion or Trello.
AI served as a Senior Architect during this process by:
Optimizing Logic: It suggested using uuid for unique IDs instead of simple numbers, which prevents ID conflicts.
Debugging Design: It helped resolve CSS pathing issues by suggesting internal styles as a fallback when the external stylesheet failed to load.