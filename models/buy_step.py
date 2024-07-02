from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship

from models.database import BaseModel


class Buy_step(BaseModel):
    __tablename__ = 'buy_step'

    buy_step_id = Column(Integer, primary_key=True)
    buy_id = Column(Integer, ForeignKey('buy.buy_id'))
    step_id = Column(Integer, ForeignKey('step.step_id'))
    date_step_beg = Column(Date)
    date_step_end = Column(Date)

    buy = relationship('buy', back_populates='buy_step')
    step = relationship('step', back_populates='buy_step')
