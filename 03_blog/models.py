from sqlalchemy import Table, Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

association_table = Table('association', Base.metadata,
    Column('left_id', Integer, ForeignKey('posts.id')),
    Column('right_id', Integer, ForeignKey('tags.id'))
)

def setup_db(db_name):
    engine = create_engine(f'sqlite:///{db_name}.db')
    Base.metadata.create_all(engine)
    return engine
    
def create_session(engine):
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    return session

def drop_db(engine):
    Base.metadata.drop_all(bind=engine)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    posts = relationship("Post")
    

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    author = Column(Integer, ForeignKey('users.id'))
    title = Column(String)
    text = Column(String)
    tags = relationship("Tag",
        secondary=association_table,
        back_populates="posts")


class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    posts = relationship("Post",
        secondary=association_table,
        back_populates="tags")

