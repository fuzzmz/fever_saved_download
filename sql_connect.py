import os
from sqlalchemy.dialects.mysql.base import LONGTEXT, TINYINT
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy import *
import ConfigParser
import sys


def make_connection(config_location):
    config = ConfigParser.ConfigParser()
    config.read(config_location)
    username = config.get('connection_info', 'user')
    password = config.get('connection_info', 'password')
    hostname = config.get('connection_info', 'host')
    port = config.get('connection_info', 'port')
    database = config.get('connection_info', 'db')
    connection = 'mysql://%s:%s@%s:%s/%s' % (username, password, hostname, port, database)
    return connection
def main(keep_saved, config_location):
    if not config_location:
        config_location = os.path.dirname(os.path.abspath(__file__)) + "\\config.ini"
    try:
        open(config_location)
    except IOError:
        print "Problem opening config.ini at " + config_location
    engine = create_engine(make_connection(config_location), echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    Base = declarative_base()

    class FeverItems(Base):
        __tablename__ = 'fever_items'

        id = Column(INTEGER, primary_key=True)
        description = Column(LONGTEXT)
        is_saved = Column(TINYINT)

    records = session.query(FeverItems.description).filter_by(is_saved=1)
    contents = []
    for record in records:
        contents.append(record)
    if not keep_saved:
    session.query(FeverItems).filter_by(is_saved=1).update({"is_saved": 0})
    session.commit()
    return contents


if __name__ == "__main__":
    main(bool(sys.argv[1]), str(sys.argv[2]))
