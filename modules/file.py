from . import Base
from sqlalchemy import Column, String, Integer, Enum, DateTime
from datetime import datetime

class Files(Base):
    __tablename__ = 'files'

    id = Column(Integer, primary_key=True)
    filename = Column(String)
    fileparent = Column(String)
    filepath = Column(String)
    filetype = Column(String)
    atime = Column(DateTime, default=datetime.now())
    mtime = Column(DateTime, default=datetime.now())

    def to_json(self):
        ret = {
            'filename': self.filename,
            'fileparent': self.fileparent,
            'filepath': self.filepath,
            'filetype': self.filetype,
            'atime': str(self.atime),
            'mtime': str(self.mtime)
        }
        return ret
