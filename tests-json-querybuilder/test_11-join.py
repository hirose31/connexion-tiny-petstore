# -*- coding: utf-8 -*-

from json_querybuilder import querybuilder
from models import model
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import relationship


class User(model):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String)

    addresses = relationship('Address',
                             backref='user',
                             lazy='joined',
                             innerjoin=True,
                             )

    def __repr__(self):
        return "<User(id='{0:s}', name='{1:s}', addresses='{2:s}')>".format(
            str(self.id),
            self.name,
            str(self.addresses),
        )


class Address(model):
    __tablename__ = 'addresses'
    id = Column(Integer, Sequence('address_id_seq'), primary_key=True)
    email = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return "<Address(email='%s', user='%s')>" % (
            self.email,
            self.user.name,
        )


class Score(model):
    __tablename__ = 'scores'
    id = Column(Integer, Sequence('score_id_seq'), primary_key=True)
    score = Column(Integer, default='0', server_default='0')
    user_id = Column(Integer)

    def __repr__(self):
        return "<Score(user_id='%s', score='%d')>" % (
            self.user_id,
            self.score,
        )


def test_init(session):
    foo = User(name='foo')
    foo.addresses.append(Address(email='foo@example.com'))
    foo.addresses.append(Address(email='foo@example.org'))

    bar = User(name='bar')

    session.add_all([
        foo,
        bar,
    ])
    session.commit()

    session.add_all([
        Score(score=31, user_id=foo.id),
        Score(score=99, user_id=99),
    ])
    session.commit()


class TestJoin:
    def test_fk(self, session):
        filter = {
            'addresses.email': {'==': 'foo@example.com'},
        }
        res = querybuilder(session.query(User), filter).all()
        assert len(res) == 1

    def test_no_relationship(self, session):
        filter = {
            'scores.score': {'==': 31},
        }
        res = querybuilder(session.query(User, Score).join(
            Score, User.id == Score.user_id), filter).all()
        assert len(res) == 1

        filter = {
            'scores.score': {'>=': 50},
        }
        res = querybuilder(session.query(User, Score).join(
            Score, User.id == Score.user_id), filter).all()
        assert len(res) == 0
