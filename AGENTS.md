# AGENTS.md — guide for coding agents

## Layout

- `backend/` — FastAPI app (`main.py`), one in-memory Python list as the store. **No database**: tasks vanish on restart.
- `frontend/` — React SPA (`src/App.jsx`); it calls the API directly at `http://localhost:8000` (a `/tasks` proxy exists in `vite.config.js` but `App.jsx` doesn't use it).

## Setup & run

Run these in **two terminals** — uvicorn stays in the foreground:

```bash
pip install -r backend/requirements.txt        # fastapi, uvicorn, pydantic
(cd backend && uvicorn main:app --port 8000)   # API on :8000
(cd frontend && npm install && npm run dev)    # UI on :5173
```

## Conventions

- CRUD endpoints live in `backend/main.py`; stats (total/done/pending) are computed client-side in `App.jsx`.
- No tests, linter, or CI configured — verify manually with a quick CRUD smoke (list, create, complete, delete) after changes.
- Keep diffs minimal; this is a small demo app, don't add infrastructure it doesn't need.
