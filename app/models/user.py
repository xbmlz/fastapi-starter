from email.policy import default
from sqlalchemy import Boolean, Column, Integer, String
from app.db.session import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    hashed_password = Column(String)
    email = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
