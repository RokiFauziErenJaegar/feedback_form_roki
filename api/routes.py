# feedback_form/api/routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database.connection import get_session
from schemas.feedback import FeedbackCreate
from crud.feedback import create_feedback

router = APIRouter()

@router.post("/feedback/", response_model=FeedbackCreate)
async def create_feedback_endpoint(feedback: FeedbackCreate, session: AsyncSession = Depends(get_session)):
    return await create_feedback(session, feedback.score)
