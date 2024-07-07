project-root/
│
├── backend/
│   ├── alembic/
│   │   ├── versions/
│   │   ├── env.py
│   │   └── script.py.mako
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   └── database.py
│   ├── alembic.ini
│   ├── requirements.txt
│   └── .env
│
└── frontend/
    ├── public/
    │   └── index.html
    ├── src/
    │   ├── assets/
    │   ├── components/
    │   │   ├── FeedbackForm.vue
    │   ├── App.vue
    │   ├── main.js
    ├── package.json
    ├── package-lock.json
    └── vue.config.js

1. Setup Backend
   
a. Buat virtual environment dan install dependencies
cd project-root/backend
python -m venv venv
source venv/bin/activate  # Untuk macOS/Linux
# atau
venv\Scripts\activate  # Untuk Windows
pip install 'fastapi[all]' sqlalchemy asyncpg alembic 'pydantic<2'


b. Buat file requirements.txt
fastapi[all]
sqlalchemy
asyncpg
alembic
pydantic<2


c. Buat file .env
DATABASE_URL=postgresql+asyncpg://postgres:admin@localhost/postgres




