from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import as_declarative
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from datetime import date

from sqlalchemy import  Integer
from sqlalchemy.orm import mapped_column,Mapped
@as_declarative()
class Base:
    id:Mapped[int]= mapped_column(Integer, primary_key=True)
    __name__: str
    created_at:Mapped[date]=mapped_column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    updated_at:Mapped[date]=mapped_column(TIMESTAMP(timezone=True)),
    #to generate tablename from classname
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()