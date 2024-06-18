# Sudoku

![Result](/assets/images/result.png)

- [Sudoku](#sudoku)
  - [Development Environment Setup](#development-environment-setup)
  - [Operation Check Procedure](#operation-check-procedure)
    - [How to Start the Server](#how-to-start-the-server)
    - [POST with cURL](#post-with-curl)
  - [Appendix](#appendix)
    - [Hierarchical Structure](#hierarchical-structure)
    - [Open Swagger UI](#open-swagger-ui)


## Development Environment Setup
The following command will install Python 3.12.3 and the libraries listed.

```sh
rye sync
```

- Rye
- Python: 3.12.3
  - pulp: 2.8.0
  - uvicorn: 0.30.0
  - pydantic: 2.7.1
  - pydantic-settings: 2.2.1
  - google-cloud-logging: 3.10.0
  - fastapi: 0.111.0
  - opentelemetry-api: 1.24.0
  - opentelemetry-sdk: 1.24.0
  - opentelemetry-exporter-gcp-trace: 1.6.0
  - opentelemetry-propagator-gcp: 1.6.0
  - opentelemetry-instrumentation-fastapi: 0.45b0
  - psutil: 5.9.8
  - gunicorn: 22.0.0


## Operation Check Procedure

### How to Start the Server
The server can be started by executing the following command.

```sh
rye run uvicorn app.main:app --host 0.0.0.0
```


### POST with cURL
```sh
curl -X 'GET' \
  'http://localhost:8000/api/v1/solve?prob=%5B%5B8%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%5D%2C%5B0%2C0%2C3%2C6%2C0%2C0%2C0%2C0%2C0%5D%2C%5B0%2C7%2C0%2C0%2C9%2C0%2C2%2C0%2C0%5D%2C%5B0%2C5%2C0%2C0%2C0%2C7%2C0%2C0%2C0%5D%2C%5B0%2C0%2C0%2C0%2C4%2C5%2C7%2C0%2C0%5D%2C%5B0%2C0%2C0%2C1%2C0%2C0%2C0%2C3%2C0%5D%2C%5B0%2C0%2C1%2C0%2C0%2C0%2C0%2C6%2C8%5D%2C%5B0%2C0%2C8%2C5%2C0%2C0%2C0%2C1%2C0%5D%2C%5B0%2C9%2C0%2C0%2C0%2C0%2C4%2C0%2C0%5D%5D' \
  -H 'accept: application/json'
```


## Appendix

### Hierarchical Structure
```
.
├── app
│   ├── api
│   │   ├── errors
│   │   │   ├── http_error.py
│   │   │   ├── __init__.py
│   │   │   └── validation_error.py
│   │   └── routes
│   │       ├── api.py
│   │       ├── healthz.py
│   │       ├── __init__.py
│   │       └── solve.py
│   ├── core
│   │   ├── config.py
│   │   ├── __init__.py
│   │   └── settings
│   │       ├── app.py
│   │       └── __init__.py
│   ├── __init__.py
│   ├── main.py
│   ├── model
│   │   ├── board.py
│   │   ├── __init__.py
│   │   ├── schema
│   │   │   ├── board.py
│   │   │   ├── __init__.py
│   │   │   └── response.py
│   │   └── solver.py
│   └── service
│       ├── __init__.py
│       └── solve.py
├── Dockerfile
├── entrypoint.sh
├── LICENSE
├── openapi.json
├── pyproject.toml
├── README.md
├── requirements-dev.lock
├── requirements.lock
├── ruff.toml
└── tests
    └── test_solve.py
```


### Open Swagger UI
Access the following URL to develop using the Swagger UI.

```sh
http://localhost:8000/docs
```

![Swagger](/assets/images/swagger.png)
