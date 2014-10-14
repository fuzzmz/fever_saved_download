from sqlalchemy.dialects.mysql.base import LONGTEXT, TINYINT
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy import *
import ConfigParser


def make_connection():
    # TODO ask for configuration file location
    config = ConfigParser.ConfigParser()
    config.read(".\\config.ini")
    username = config.get('connection_info', 'user')
    password = config.get('connection_info', 'password')
    hostname = config.get('connection_info', 'host')
    port = config.get('connection_info', 'port')
    database = config.get('connection_info', 'db')
    connection = 'mysql://%s:%s@%s:%s/%s' % (username, password, hostname, port, database)
    return connection
def main():
    engine = create_engine(make_connection(), echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    Base = declarative_base()

    class FeverItems(Base):
        __tablename__ = 'fever_items'

        id = Column(INTEGER, primary_key=True)

    records = session.query(FeverItems.description).filter_by(is_saved=1)
    saved_items = session.query(FeverItems.id).filter_by(is_saved=1).all()
    contents = []
    for record in records:
        contents.append(record)
    for item in saved_items:
        session.query(FeverItems).filter_by(id=int(item)).update({"is_saved": 0})
    return contents

    # TODO mark posts as unsaved as you go through them

if __name__ == "__main__":
    main()
