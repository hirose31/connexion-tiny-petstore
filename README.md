# Connexion Example / Tiny Pet Store

## Overview

This example application implement a very basic "Pet Store" REST service using the [Connexion](https://github.com/zalando/connexion).

Connexion is a framework that automagically handles HTTP requests based on [OpenAPI Specification](https://www.openapis.org/) of your API described in YAML format. 

This example application uses the following modules and has features.

- OpenAPI 3.0
- [Connexion](https://github.com/zalando/connexion) >= 2.0.0
- [SQLAlchemy](https://www.sqlalchemy.org/) ORM, [SQLAlchemy-Utils](https://github.com/kvesteri/sqlalchemy-utils), [Flask-Alchemy](http://github.com/mitsuhiko/flask-sqlalchemy), [sqlathanor](https://sqlathanor.readthedocs.io/en/latest)
    - one-to-many relationship (store and pets)
    - automatically encode ORM objects to JSON using sqlathanor
- json_querybuilder
    - search resources by simple query language in JSON
- [pytest](https://docs.pytest.org/en/latest/), [WebTest](https://docs.pylonsproject.org/projects/webtest/en/latest/)


## Requirements
Python 3.5.2+

## Files

- controllers/
    - controller functions mapped using `operationId` in `openapi.yaml`
    - simply call model methods
- models/
    - staticmethods implement business logic using ORMs
- orm/
    - just a SQLAlchemy ORM

## Usage

To run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
make spec  # if you modified tiny-petstore.yaml
python3 app.py
  or
./bin/start-server
```

and open your browser to here:

```
http://localhost:9090/v3/ui/
```

Your OpenAPI definition lives here:

```
http://localhost:9090/v3/openapi.json
```

To launch the integration tests, use tox:
```
pip3 install -r requirements.txt -r test-requirements.txt
python3 setup.py test
  or
PYTHONPATH=. pytest
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t tiny_petstore .

# starting up a container
docker run -p 9090:9090 tiny_petstore
```

## Contribution

We welcome your ideas, issues and pull requests!

