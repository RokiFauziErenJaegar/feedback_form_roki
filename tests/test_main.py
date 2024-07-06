# feedback_form/tests/test_main.py
import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from main import app
from database.connection import Base, get_session

DATABASE_URL = "postgresql+asyncpg://postgres:admin@localhost/test_db"

engine = create_async_engine(DATABASE_URL, echo=True)
TestingSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

async def override_get_session():
    async with TestingSessionLocal() as session:
        yield session

app.dependency_overrides[get_session] = override_get_session

@pytest.fixture(scope="module")
async def test_client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

@pytest.fixture(scope="module", autouse=True)
async def setup_and_teardown_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

async def test_create_feedback(test_client):
    response = await test_client.post("/feedback/", json={"score": 5})
    assert response.status_code == 200
    assert response.json()["score"] == 5
