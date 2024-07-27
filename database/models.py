import enum
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, mapped_column, Mapped
from .base import Base

class Status(enum.Enum):
    PENDING = "pending"
    DECLINED = "declined"
    CONFIRMED = "confirmed"

class User(Base):
    __tablename__ = 'users'
    firstname: Mapped[str] = mapped_column(String, nullable=False)
    lastname: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    posts: Mapped[list['Post']] = relationship('Post', back_populates="created_by")
    sent_requests: Mapped[list["Friendship"]] = relationship(
        "Friendship",
        foreign_keys='Friendship.sender_id',
        back_populates="sender"
    )
    received_requests: Mapped[list["Friendship"]] = relationship(
        "Friendship",
        foreign_keys='Friendship.receiver_id',
        back_populates="receiver"
    )

    @property
    def fullname(self):
        return f'{self.firstname} {self.lastname}'

    @property
    def pending_requests(self):
        return [friendship for friendship in self.received_requests if friendship.status == Status.PENDING]

    @property
    def friends(self):
        return [friendship for friendship in self.sent_requests + self.received_requests if friendship.status == Status.CONFIRMED]

class Friendship(Base):
    __tablename__ = 'friendships'
    sender_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    receiver_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    status: Mapped[Status] = mapped_column(Enum(Status), nullable=False, default=Status.PENDING)
    chat_id: Mapped[int] = mapped_column(Integer, ForeignKey('chats.id'), unique=True)
    chat: Mapped['Chat'] = relationship('Chat', back_populates='friendship', uselist=False)
    sender: Mapped["User"] = relationship('User', foreign_keys=[sender_id], back_populates="sent_requests")
    receiver: Mapped["User"] = relationship('User', foreign_keys=[receiver_id], back_populates="received_requests")

class Post(Base):
    __tablename__ = 'posts'
    content: Mapped[str] = mapped_column(String, nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    created_by: Mapped[User] = relationship('User', back_populates='posts')

class Chat(Base):
    __tablename__ = 'chats'
    friendship: Mapped['Friendship'] = relationship('Friendship', back_populates='chat', uselist=False)
    history: Mapped[list['Message']] = relationship('Message', back_populates='chat')

class Message(Base):
    __tablename__ = 'messages'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    content: Mapped[str] = mapped_column(String, nullable=False)
    chat_id: Mapped[int] = mapped_column(Integer, ForeignKey('chats.id'))
    chat: Mapped[Chat] = relationship('Chat', back_populates='history')
    sender_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    sender: Mapped[User] = relationship('User')
   