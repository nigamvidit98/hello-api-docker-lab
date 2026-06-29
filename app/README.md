# app

Run the FastAPI app locally with uvicorn:

```bash
pip install -r app/requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Endpoints:
- GET / -> { "message": "Hello from FastAPI" }
- GET /health -> { "status": "healthy" }
- GET /version -> { "status": "healthy" }
- GET /hostname -> { "hostname": "..." }
- GET /echo -> { "message": "Hello" }
