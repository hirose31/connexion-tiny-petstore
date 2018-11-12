# -*- coding: utf-8 -*-

from json_querybuilder import querybuilder
from models import model
from sqlalchemy import Column, Integer, String, Sequence


class Basic(model):
    __tablename__ = 'basics'
    id = Column(Integer, Sequence('basic_id_seq'), primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return "<Basic(id='{0:s}', name='{1:s}', age='{2:d}')>".format(
            str(self.id),
            self.name,
            self.age,
        )


def test_init(session):
    session.add_all([
        Basic(name='foo', age=10),
        Basic(name='bar', age=20),
        Basic(name='baz', age=30),
    ])
    session.commit()


class TestBasic:
    def test_equal(self, session):
        filter = {
            'name': {'==': 'foo'},
        }
        res = querybuilder(session.query(Basic), filter).all()
        assert len(res) == 1

        filter = {
            'name': {'!=': 'foo'},
        }
        res = querybuilder(session.query(Basic), filter).all()
        assert len(res) == 2

        filter = {
            'name': 'foo',
        }
        res = querybuilder(session.query(Basic), filter).all()
        assert len(res) == 1

        filter = {
            'name': 'foo',
            'age': 20,
        }
        res = querybuilder(session.query(Basic), filter).all()
        assert len(res) == 0

        filter = {
            'name': 'foo',
            'age': 10.0,
        }
        res = querybuilder(session.query(Basic), filter).all()
        assert len(res) == 1

    def test_in(self, session):
        filter = {
            'name': {'IN': ['foo', 'hoge']}
        }
        res = querybuilder(session.query(Basic), filter).all()
        assert len(res) == 1

        filter = {
            'name': {'!in': ['foo', 'hoge']}
        }
        res = querybuilder(session.query(Basic), filter).all()
        assert len(res) == 2

        filter = {
            'name': {'in': 'foo'}
        }
        res = querybuilder(session.query(Basic), filter).all()
        assert len(res) == 1

    def test_arithmetic(self, session):
        filter = {
            'age': {'==': 20}
        }
        res = querybuilder(session.query(Basic), filter).all()
        assert len(res) == 1
        assert res[0].name == 'bar'

        filter = {
            'age': {'>': 20}
        }
        res = querybuilder(session.query(Basic), filter).all()
        assert len(res) == 1

        filter = {
            'age': {'>=': 20}
        }
        res = querybuilder(session.query(Basic), filter).all()
        assert len(res) == 2

        filter = {
            'age': {'<': 20}
        }
        res = querybuilder(session.query(Basic), filter).all()
        assert len(res) == 1

        filter = {
            'age': {'<=': 20}
        }
        res = querybuilder(session.query(Basic), filter).all()
        assert len(res) == 2

    def test_like(self, session):
        filter = {
            'name': {'like': 'b%'}
        }
        res = querybuilder(session.query(Basic), filter).all()
        assert len(res) == 2

        filter = {
            'name': {'!like': 'b%'}
        }
        res = querybuilder(session.query(Basic), filter).all()
        assert len(res) == 1

    def test_boolean_op(self, session):
        filter = {
            'name': ['OR', {'==': 'bar'}, {'like': 'baz%'}],
        }
        res = querybuilder(session.query(Basic), filter).all()
        assert len(res) == 2

        filter = {
            'name': ['and', {'==': 'bar'}, {'like': 'ba%'}],
        }
        res = querybuilder(session.query(Basic), filter).all()
        assert len(res) == 1
