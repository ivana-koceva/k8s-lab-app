# Application

Flask app with three endpoints. Runs under Gunicorn with 2 workers, on port 8080.


## Endpoints

| Endpoint | Response |
|----------|----------|
| `GET /` | `{"status": "ok", "version": "0.1.0"}` |
| `GET /health` | `{"healthy": true}` |
| `GET /metrics` | Prometheus metrics |

## Running locally

```bash
pip install -r requirements.txt
flask --app src/app run --port 8080
```

```bash
# tests
pytest tests/ -v
```

```bash
# with Docker
docker build -t flask-demo .
docker run -p 8080:8080 flask-demo
```

The app will be at `http://localhost:8080`.

## Dependencies

Pinned in `requirements.txt`. To update, install what you need and run `pip freeze > requirements.txt`.
