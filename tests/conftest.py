# -*- coding: utf-8 -*-
"""Defines fixtures available to all tests."""

import pytest
import webtest as wt

from tiny_petstore.app import create_app
from tiny_petstore.extensions import db as _db
from tiny_petstore.configs import TestConfig
import tiny_petstore.orm as orm


@pytest.yield_fixture(scope='function')
def app():
    """An application for the tests."""
    _app = create_app(TestConfig)

    ctx = _app.app.test_request_context()
    ctx.push()

    yield _app.app

    ctx.pop()


@pytest.fixture(scope='function')
def testapp(app):
    """A Webtest app."""
    return wt.TestApp(app)


@pytest.fixture(scope='function', autouse=True)
def db(app):
    """A database for the tests."""
    _db.app = app
    with app.app_context():
        _db.create_all()

    setup_initial_data(_db)

    yield _db

    # Explicitly close DB connection
    _db.session.close()
    _db.drop_all()


def setup_initial_data(db):
    s1 = orm.Store(name='Pets Unlimited', address='Shibuya')
    s2 = orm.Store(name='The Pet Mansion', address='Nerima')
    s3 = orm.Store(name='Nothing One', address='Minato')

    tama = orm.Pet(name='tama', status='avaiable')
    mike = orm.Pet(name='mike', status='pending')
    chibi = orm.Pet(name='chibi', status='sold')

    s1.pets = [tama, mike]
    s2.pets = [chibi]

    db.session.add_all([s1, s2, s3])
    db.session.commit()
