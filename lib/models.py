#!/usr/bin/env python3

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base   # ✅ modern import

Base = declarative_base()

class Dog(Base):
    __tablename__ = 'dogs'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    breed = Column(String())
