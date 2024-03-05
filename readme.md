# Interview task by Chartr

How to run

1. Clone the repository:

    ```bash
    git clone https://github.com/shraysalvi/chartr-task.git
    ```
2. Installation
   
   ```
   pip install -r requirements.txt
   ```

3. Run the project
   
   ```
   python manage.py runserver
   ```

4. Go to the swagger UI at `127.0.0.1:8000/swagger/` or api endpoint `127.0.0.1:8000/notes/`.

## Project Description: Simple Note Taking API

### Objective:

Build a RESTful API for a simple note-taking application using Django and Django REST Framework. This application will allow for creating, fetching, querying, and updating notes without user management. No UI needs to be developed. If you can attach a Swagger UI to test these APIs, even better.

### Core Features:
- Create Note: Allow API consumers to create a new note with a title and body.
- Fetch Note by ID: Enable fetching of a note using its primary key.
- Query Notes by Title Substring: Implement functionality to query notes based on a substring present in the note's title, returning all matching notes.
- Update Note: Provide the ability to update the title and body of an existing note identified by its primary key.
- 
### Models:

- Note
    - title: CharField, a brief title for the note.
    - body: TextField, the main content of the note.
    - created_at: DateTimeField, the date and time the note was created.
    - updated_at: DateTimeField, the date and time the note was last updated.
Feel free to add more fields/models if you want.

### Endpoints:
- POST /notes/: Create a new note.
- GET /notes/<pk>/: Fetch a note by its primary key.
- GET /notes/?title=<substring>: Query notes by title substring.
- PUT /notes/<pk>/: Update an existing note.

Feel free to add more endpoints if you want.
