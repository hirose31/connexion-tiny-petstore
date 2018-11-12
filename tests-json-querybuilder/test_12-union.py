# -*- coding: utf-8 -*-

from json_querybuilder import querybuilder
from models import model
from sqlalchemy import Column, Integer, String, Sequence


class Basic(model):
    __tablename__ = 'basics2'
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
        Basic(name='qux', age=40),
    ])
    session.commit()


class TestUnion:
    def test_union(self, session):
        filters = [
            {
                'name': {'like': 'ba%'},
            },
            {
                'name': {'in': ['foo', 'baz']},
            },
        ]

        res = querybuilder(session.query(Basic), filters).all()
        assert len(res) == 3
        assert set([r.name for r in res]) == {'foo', 'bar', 'baz'}
