# -*- coding: utf-8 -*-

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import model


@pytest.fixture(scope='module', autouse=True)
def session():
    engine = create_engine('sqlite://',
                           echo=True,
                           )

    model.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    yield session

    session.close()
    model.metadata.drop_all(engine)
