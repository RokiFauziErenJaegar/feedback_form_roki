# feedback_form/schemas/feedback.py
from pydantic import BaseModel

class FeedbackCreate(BaseModel):
    rating: int

    class Config:
        orm_mode = True
