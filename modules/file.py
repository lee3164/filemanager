from . import Base
from sqlalchemy import Table, Column, String, Integer, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class File(Base):
    __tablename__ = 'file'

    id = Column(Integer, primary_key=True)
    fname = Column(String)
    fparent = Column(String)
    # filepath = Column(String)
    frealpath = Column(String)
    ftype = Column(String)
    fmode = Column(Integer)
    fcomment = Column(String)
    fatime = Column(DateTime, default=datetime.now())
    fmtime = Column(DateTime, default=datetime.now())

    uid = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='file')

    def to_json(self):
        pass

_group_map_user_table = Table('group_map_user_table', Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('uid', Integer, ForeignKey('user.id')),
    Column('gid', Integer, ForeignKey('group.id'))
)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    uname = Column(String)
    usex = Column(Enum('M', 'F'))
    uemail = Column(String)
    ucomment = Column(String)
    upassword = Column(String)

    file = relationship('File', back_populates='user')
    group = relationship('Group', back_populates='user', secondary=_group_map_user_table)
    def to_json(self):
        pass

class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    gname = Column(String)
    gcomment = Column(String)

    user = relationship('User', back_populates='group', secondary=_group_map_user_table)
    def to_json(self):
        pass

