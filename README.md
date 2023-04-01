# Levr takehome assessment - Task App

## Before you begin

_Please read this entire document before you begin_

This assessment contains a functional bare-bones django application where the following already exists:

- The app `tasks` contains a model, viewset, serializer and url configured for `TodoList`
- A migration has been created for `tasks` app
- `taskapp/settings.py` has been configured with `rest_framework` and `tasks`
- `requirements.txt` contains django rest framework
- Once you run `python manage.py migrate`, you should be able to run `python manage.py runserver` and visit the api at `http://127.0.0.1:8000/api/`

The following endpoints already function:
1. View existing Todo Lists at `GET /api/todo_lists`; responds with `[{"id": int, "created_at": datetime, "title": str}, ... {}]`
2. Create a new Todo List with `POST /api/todo_list -d {"title": "SomeTitle"}`


## Instructions

The goal of this application is to create a minimalistic but functional REST API for a todo app. 

### Primary objectives

1. The app should be able to do at least the following:
- Create, update and delete (CRUD) todo-lists
- Create, update and delete todo-items, which are associated with todo-lists
  - When requesting `GET /api/todo_lists`, please change the returned payload to include nested attributes for todo-items.
  - e.g. `[{"id": int, "title": str, ..., todo_items: [{"text": str, ...},]}, ...]`
- Allow todo-lists to be tagged with zero or more tags.
- Check and un-check todo-items

2. Please create a text file named `instructions.md` that includes all steps required to get your app running and any extra context.
  - If you run out of time, you may also use this file to document what you would do in a production app.

**Notes**:
- No frontend templates are required - this app will purely be assessed as a REST API.


### Secondary objectives

If you have time, please also do one or more of the following, whichever you find easy and/or important:
- Associate todo-lists with users, such that only permitted users may operate on their own todo-lists.
- Create unit tests and run them with `python manage.py test`
- Configure the admin console
- Dockerize your app
- Implement a dockerized local postgres DB
  - In this case, please include management commands to create mock data and document steps in your `instructions.md`
    - https://docs.djangoproject.com/en/4.1/howto/custom-management-commands/



## Details

1. Please use python3.
2. We aim to keep this simple, so try to keep the time required to under three hours. Partial solutions are okay, provided you can talk us through the paths you went down, and where you would go next.
3. Feel free to comment on anything that is out of scope of this challenge, but would be relevant in the real world.
4. We like virtual environments; if you use any third party packages please include them in the `requirements.txt` file, (but please don't include your virtual environment in the zipped up solution).
5. We will run `python manage.py runserver` and `python manage.py test` on your solution; try to make sure both of those calls run.
6. Once complete, zip up your assessment and email it back to us!
7. Go do something fun afterwards; you've earned it!

