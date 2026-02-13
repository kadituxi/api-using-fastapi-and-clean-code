import datetime

from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime

from db.db import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True, index=True)
    password = Column(Text)
    is_verified = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))
    updated_at = Column(DateTime, onupdate=datetime.datetime.now(datetime.timezone.utc))

    def __repr__(self):
        return f"<User>: {self.name}"
