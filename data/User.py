# coding=utf-8

"""
@company:广东浩迪创新科技有限公司
@version: ??
@author: AA-ldc
@file: User.py
@time: 2017/3/21 15:12
@function：
"""
from sqlalchemy import Column, String, Float, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Student(Base):
    __tablename__ = 'Student'
    FIRST_NAME = Column(String(20), primary_key=True)
    LAST_NAME = Column(String(20))
    AGE = Column(Integer())
    SEX = Column(String(1))
    INCOME = Column(Float(precision=0.3))
