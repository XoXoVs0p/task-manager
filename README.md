# Task Manager

A full-stack task manager web app built with **FastAPI** (Python) and **React**.

## Features

- Create, complete, and delete tasks
- Add optional descriptions
- Real-time stats (total, done, pending)
- Beautiful gradient UI with smooth animations

## Quick Start

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

API runs at `http://localhost:8000`

### Frontend

```bash
cd frontend
npm install
npm run dev
```

UI runs at `http://localhost:5173`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/tasks` | List all tasks |
| GET | `/tasks/{id}` | Get a task |
| POST | `/tasks` | Create a task |
| PUT | `/tasks/{id}` | Update a task |
| DELETE | `/tasks/{id}` | Delete a task |
| DELETE | `/tasks` | Delete all tasks |

## License

MIT
