# feedback_form/crud/feedback.py
from sqlalchemy.ext.asyncio import AsyncSession
from models.feedback import Feedback

async def create_feedback(session: AsyncSession, score: int):
    feedback = Feedback(score=score)
    session.add(feedback)
    await session.commit()
    await session.refresh(feedback)
    return feedback
