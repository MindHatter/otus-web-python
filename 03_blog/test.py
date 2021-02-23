from models import setup_db, create_session, drop_db, User, Post, Tag
from sqlalchemy.orm import sessionmaker


def test_create_user():
    engine = setup_db("test")
    session = create_session(engine)

    user = User()
    user.name = "Alex"
    session.add(user)
    session.commit()
    users = session.query(User).all()
    assert len(users) == 1

    drop_db(engine)
