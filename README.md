# Django-TDD-Docker

## Objectives
1. Develop a RESTful API with Python, and Django REST Framework.
2. Practice Test-Driven Development and DevOps knowledge that I have learned from my Software Engineering course in my 3rd year of my university.
3. Use pytest to test Django app.
4. Practice my Docker knowledge by containerize Django and Postgres inside a Docker container and use Docker compose.
5. Run unit and integration tests inside a Docker container.
6. Implement an API with Django REST Framework Views and Serializers.
7. Learn GitLab CI/CD for continuous integration and deployment.

## API Route
API url : https://stark-shore-47287.herokuapp.com
| Endpoint | HTTP Method | CRUD Method | Result |
| ----------- | ----------- | ---------| -------|
| /api/movies | GET | READ | Get all movies |
| /api/movies/:id | GET | READ | Get a single movie |
| /api/movies | POST | CREATE | Add a movie |
| /api/movies/:id | PUT | UPDATE | Update a movie |
| /api/movies/:id | DELETE | DELETE | Delete a movie |
| /ping | GET | READ | Check API status |

## Run on your machine
Build the images:
```
$ docker-compose build
```
Run the containers:
```
$ docker-compose up -d
```
Create migrations:
```
$ docker-compose exec movies python manage.py makemigrations
```
Apply migrations:
```
$ docker-compose exec movies python manage.py migrate
```
Run the tests:
```
$ docker-compose exec movies pytest -p no:warnings
```
Bring down the containers:
```
$ docker-compose down
```

## TO-DO
1. Add filtering, sorting, pagination and field limiting
2. Add React Front-end
