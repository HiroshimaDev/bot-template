from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Boolean,
    Text,
    Float,
    Date,
    BigInteger
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(BigInteger, primary_key=True)
    username = Column(String(64))
    security_permission_id = Column(Integer, ForeignKey('security_permissions.id'))
    security_permission = relationship('SecurityPermission', back_populates='users')

    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class SecurityPermission(Base):
    __tablename__ = 'security_permissions'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    users = relationship('User', back_populates='security_permission')

    can_use_bot = Column(Boolean, default=True)
    can_use_admin_panel = Column(Boolean, default=False)
    

    created_at = Column(DateTime)
    updated_at = Column(DateTime)
