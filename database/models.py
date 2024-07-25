from datetime import date
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import mapped_column,Mapped,relationship
from .base import Base


class User(Base):
    __tablename__='users'
    firstname:Mapped[str]=mapped_column(String, nullable=False)
    lastname:Mapped[str]=mapped_column(String, nullable=False)
    email:Mapped[str]=mapped_column(String, nullable=False)
    password:Mapped[str]=mapped_column(String, nullable=False)
    
    @property
    def fullname (self):
        return f'{self.firstname} {self.lastname}'

class Post(Base):
    __tablename__='posts'
    content:Mapped[str]=mapped_column(String, nullable=False)
    user_id:Mapped[int]=mapped_column(Integer, ForeignKey('users.id'))
    user:Mapped[User]= relationship('User',back_populates='users')
    

class Chat(Base):
    __tablename__ = 'chats'
    friendship_id: Mapped[int] = mapped_column(ForeignKey('friendships.id'))
    friendship: Mapped['Friendship'] = relationship('Friendship', back_populates='friendships')
    history_id: Mapped[int] = mapped_column(ForeignKey('histories.id'))
    history: Mapped['History'] = relationship('History', back_populates='hostories')

    
class Friendship(Base):
    __tablename__='friendships'
    friend_1:Mapped[User]=mapped_column(Integer, ForeignKey('users.id'))
    friend_2:Mapped[User]=mapped_column(Integer, ForeignKey('users.id'))
    chat_id: Mapped[Integer]=mapped_column(Integer, ForeignKey('chats.id'))
    chat:Mapped[Chat]=relationship('Chat',back_populates='chats')
    
class History(Base):
    __tablename__='histories'
    id:Mapped[int]= mapped_column(Integer, primary_key=True)
    chat_id: Mapped[Integer]=mapped_column(Integer, ForeignKey('chats.id'))
    chat:Mapped[Chat]=relationship('Chat',back_populates='chats')
