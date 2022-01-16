# Django-TDD-Docker

[Test-Driven Development with Django, Django REST Framework, and Docker](https://testdriven.io/courses/tdd-django/)

# What tools and technologies are used in this repository
## Core
1. Python
2. Django
3. Docker
4. Postgres
5. Django REST Framework
6. Gunicorn
7. WhiteNoise
8. Swagger/OpenAPI

## Testing and Linting
1. pytest
2. Coverage.py
3. Flake8
4. Black
5. isort
6. HTTPie

## Python Version Control
1. pyenv
2. pipenv

## Services
1. GitLab
2. Heroku

## TBD
- git branch strategy

## How to Run
### Test
```shell
$ makefile test
```

### Server

Build the image:
```shell
$ docker-compose build
```

Once the build is done, fire up the container in detached mode:
```shell
$ docker-compose up -d
```

Bring down the development containers
```shell
$ docker-compose down -v
```

## Pycharm IDE setting
- `app` directory mark as Sources root

---
## Reference
- [Test-Driven Development with Django, Django REST Framework, and Docker](https://testdriven.io/courses/tdd-django/)
- [How to write a good readme file](https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/)
- [commit convention](https://www.conventionalcommits.org/en/v1.0.0/)
