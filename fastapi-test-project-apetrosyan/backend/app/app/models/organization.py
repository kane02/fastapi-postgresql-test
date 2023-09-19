from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class Organization(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=False)
    description = Column(String, index=False)
