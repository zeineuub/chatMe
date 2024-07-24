from datetime import date
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import mapped_column,Mapped,relationship
from .database import Base
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from typing import List,Optional

class User(Base):
    __tablename__='users'
    id:Mapped[int]= mapped_column(Integer, primary_key=True)
    firstname:Mapped[str]=mapped_column(String, nullable=False)
    lastname:Mapped[str]=mapped_column(String, nullable=False)
    email:Mapped[str]=mapped_column(String, nullable=False)
    password:Mapped[str]=mapped_column(String, nullable=False)
    created_at:Mapped[date]=mapped_column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    @property
    def fullname (self):
        return f'{self.firstname} {self.lastname}'

class Post(Base):
    __tablename__='posts'
    id:Mapped[int]= mapped_column(Integer, primary_key=True)
    content:Mapped[str]=mapped_column(String, nullable=False)
    user_id:Mapped[int]=mapped_column(Integer, ForeignKey('users.id'))
    user:Mapped[User]= relationship('User',back_populates='users')
    created_at:Mapped[date]=mapped_column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    

class Chat(Base):
    __tablename__ = 'chats'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    friendship_id: Mapped[int] = mapped_column(ForeignKey('friendships.id'))
    friendship: Mapped['Friendship'] = relationship('Friendship', back_populates='friendships')
    history_id: Mapped[int] = mapped_column(ForeignKey('histories.id'))
    history: Mapped['History'] = relationship('History', back_populates='hostories')
    created_at: Mapped[date] = mapped_column(TIMESTAMP(timezone=True)),

    
class Friendship(Base):
    __tablename__='friendships'
    id:Mapped[int]= mapped_column(Integer, primary_key=True)
    friend_1:Mapped[User]=mapped_column(Integer, ForeignKey('users.id'))
    friend_2:Mapped[User]=mapped_column(Integer, ForeignKey('users.id'))
    chat_id: Mapped[Integer]=mapped_column(Integer, ForeignKey('chats.id'))
    chat:Mapped[Chat]=relationship('Chat',back_populates='chats')
    created_at:Mapped[date]=mapped_column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    
class History(Base):
    __tablename__='histories'
    id:Mapped[int]= mapped_column(Integer, primary_key=True)
    chat_id: Mapped[Integer]=mapped_column(Integer, ForeignKey('chats.id'))
    chat:Mapped[Chat]=relationship('Chat',back_populates='chats')
    created_at:Mapped[date]=mapped_column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
