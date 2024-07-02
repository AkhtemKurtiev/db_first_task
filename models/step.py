from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship

from models.database import BaseModel


class Step(BaseModel):
    __tablename__ = 'step'

    step_id = Column(Integer, primary_key=True)
    name_step = Column(Text)

    buy_steps = relationship('buy_step', back_populates='step')
