# MoodTrac Backend

Django REST API for the MoodTrac mood tracking application.

## Setup Instructions

### 1. Create a Virtual Environment
```bash
cd backend
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Migrations
```bash
python manage.py migrate
```

### 4. Create a Superuser
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin account.

### 5. Run the Server
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/api/`

## API Endpoints

- `GET /api/moods/` - List all your moods
- `POST /api/moods/` - Create a new mood entry
- `GET /api/moods/{id}/` - Get a specific mood
- `PUT /api/moods/{id}/` - Update a mood
- `DELETE /api/moods/{id}/` - Delete a mood
- `GET /api/moods/today/` - Get today's moods
- `GET /api/stats/` - Get mood statistics

## Authentication

The API uses session authentication. You need to be logged in to access the endpoints.

## Example: Create a Mood Entry

```bash
curl -X POST http://localhost:8000/api/moods/ \
  -H "Content-Type: application/json" \
  -d '{
    "mood": "happy",
    "intensity": 8,
    "notes": "Had a great day today!"
  }'
```