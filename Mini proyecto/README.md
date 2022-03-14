# SW API GraphQL

## Requirements
* [Python](https://www.python.org/) (realizado en python 3.8)
* [Django](https://github.com/django/django)
* [Django Filter](https://github.com/carltongibson/django-filter)
* [Django model utils](https://github.com/jazzband/django-model-utils)
* [Graphene](https://github.com/graphql-python/graphene-django)
* [.EVN](https://github.com/theskumar/python-dotenv)

## Setup

Clone the project
```
git clone https://github.com/Jcmantillam/prueba_tecnica_LQN
cd 'Mini proyecto'
```

Using virtualenv:

```
python -m venv env
.\env\Scripts\activat
```
Install the dependencies:
```
pip install -r requirements.txt
```

Run migrations and load fixtures
```
python manage.py migrate
python manage.py load_fixtures
```

### Running the server
```
python manage.py runserver
```
If you want to check it out, access the graphi explorer here: `127.0.0.1:8000/explore`.

The service should be available in the URL: `127.0.0.1:8000/graphql`.

### Runing the tests
```
python manage.py test
```
## Collections
You can see some examples for how to work with the project [here](https://go.postman.co/workspace/LQN~f2f87426-0503-4c6e-8978-02bd1b658314/collection/7532490-9aeec079-2472-4760-b7d5-a654f781d832?action=share&creator=7532490)
