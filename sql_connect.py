from sqlalchemy.dialects.mysql.base import LONGTEXT
from sqlalchemy.dialects.mysql.base import TINYINT
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy import *


def main():
    engine = create_engine('mysql://URL', echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    Base = declarative_base()
    class fever_items(Base):
        __tablename__ = 'fever_items'

        id = Column(INTEGER, primary_key=True)
        feed_id = Column(INTEGER)
        uid = Column(VARCHAR(255))
        title = Column(VARCHAR(255))
        author = Column(VARCHAR(255))
        description = Column(LONGTEXT)
        link = Column(VARCHAR(255))
        url_checksum = Column(INTEGER)
        read_on_time = Column(INTEGER)
        is_saved = Column(TINYINT)
        created_on_time = Column(INTEGER)
        added_on_time = Column(INTEGER)

    records = session.query(fever_items.description).filter_by(is_saved=1)
    contents = []
    for record in records:
        contents.append(record)
    return contents


if __name__ == "__main__":
    main()
