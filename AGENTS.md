# AGENTS.md — guide for coding agents

## Layout

- `backend/` — FastAPI app (`main.py`), one in-memory Python list as the store. **No database**: tasks vanish on restart.
- `frontend/` — React SPA (`src/App.jsx`), Vite dev server proxies `/tasks` to the backend.

## Setup & run

```bash
pip install -r backend/requirements.txt        # fastapi, uvicorn, pydantic
(cd backend && uvicorn main:app --port 8000)   # API on :8000
(cd frontend && npm install && npm run dev)    # UI on :5173
```

## Conventions

- CRUD endpoints live in `backend/main.py`; stats (total/done/pending) are derived there too.
- No tests, linter, or CI configured — verify manually by hitting `GET /tasks` after changes.
- Keep diffs minimal; this is a small demo app, don't add infrastructure it doesn't need.
