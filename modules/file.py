from . import Base
from sqlalchemy import Table, Column, String, Integer, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class File(Base):
    __tablename__ = 'file'

    id = Column(Integer, primary_key=True, nullable=False)
    fname = Column(String, nullable=False)
    fparent = Column(String, nullable=False)
    # filepath = Column(String)
    ftype = Column(Enum('r', 'd', 'l'), nullable=False)
    fmode = Column(String(9), nullable=False)
    fcomment = Column(String, default='', nullable=False)
    fatime = Column(DateTime, default=datetime.now(), nullable=False)
    fmtime = Column(DateTime, default=datetime.now(), nullable=False)
    flink = Column(String, nullable=False)

    uid = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User', back_populates='file')

    gid = Column(Integer, ForeignKey('group.id'), nullable=False)
    group = relationship('Group', back_populates='file')

    def to_json(self):
        ret = {
            'fid': self.id,
            'file_name': self.fname,
            'file_parent': self.fparent,
            'file_type': self.ftype,
            'file_mode': self.fmode,
            'file_comment': self.fcomment,
            'file_atime': str(self.fatime)[:19],
            'file_mtime': str(self.fmtime)[:19],
            'file_link': self.flink,
            'user': self.user.uname,
            'group': self.group.gname
        }

        return ret

class FileMD5(Base):
    """
    CREATE TABLE file_md5 (
        id INTEGER NOT NULL,
        fname VARCHAR NOT NULL,
        md5 VARCHAR(32) NOT NULL,
        PRIMARY KEY (id)
    )
    """
    __tablename__ = 'file_md5'

    id = Column(Integer, primary_key=True)
    fname = Column(String, nullable=False)
    md5 = Column(String(32), nullable=False)


_group_map_user_table = Table('group_map_user_table', Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('uid', Integer, ForeignKey('user.id')),
    Column('gid', Integer, ForeignKey('group.id'))
)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    uname = Column(String, nullable=False)
    usex = Column(Enum('m', 'f'), nullable=False)
    uemail = Column(String, nullable=False)
    ucomment = Column(String, default='', nullable=False)
    upassword = Column(String, nullable=False)

    file = relationship('File', back_populates='user')
    group = relationship('Group', back_populates='user',
                         secondary=_group_map_user_table)

    def to_json(self):
        groups = [ g.gname for g in self.group ]
        ret = {
            'user_name': self.uname,
            'user_sex': self.usex,
            'user_email': self.uemail,
            'user_comment': self.ucomment,
            'groups': groups
        }
        return ret

class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    gname = Column(String, nullable=False)
    gcomment = Column(String, default='', nullable=False)

    file = relationship('File', back_populates='group')
    user = relationship('User', back_populates='group', secondary=_group_map_user_table)

    def to_json(self):
        pass

