# -*- coding: utf-8 -*-

from json_querybuilder import querybuilder
from models import model
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, Table
from sqlalchemy.orm import relationship, aliased

person_relation = Table('person_relation',
                        model.metadata,
                        Column('parent', ForeignKey('person.name'), primary_key=True),
                        Column('child', ForeignKey('person.name'), primary_key=True),
                        )


class Person(model):
    __tablename__ = 'person'

    name = Column(String,
                  primary_key=True,
                  )

    parent = relationship("Person",
                          secondary=person_relation,
                          primaryjoin="Person.name==person_relation.c.parent",
                          secondaryjoin="Person.name==person_relation.c.child",
                          backref="child",
                          lazy="joined",
                          join_depth=1,
                          )

    def __repr__(self):
        parent = ','.join([s.name for s in self.parent])
        child = ','.join([s.name for s in self.child])
        return "<Person(name='{0:s}' parent='{1:s}' child='{2:s}'>".format(self.name, parent, child)


def test_init(session):
    mother = Person(name='mother')
    me = Person(name='me')
    daughter = Person(name='daughter')
    son = Person(name='son')
    stranger = Person(name='stranger')

    me.parent = [mother]
    me.child = [daughter, son]

    session.add_all([
        mother,
        me,
        daughter,
        son,
        stranger,
    ])
    session.commit()


def base_query(session):
    parent_p = aliased(Person, name='parent')
    child_p = aliased(Person, name='child')

    return session.query(Person).\
        outerjoin(parent_p, Person.parent).\
        outerjoin(child_p, Person.child)


class TestJoin:
    def test_relation(self, session):
        filter = {
            # no filter
        }
        res = querybuilder(base_query(session), filter).all()
        assert len(res) == 5

    def test_filter(self, session):
        filter = {
            'parent.name': 'me',
        }
        res = querybuilder(base_query(session), filter).all()
        assert len(res) == 2
        assert set([r.name for r in res]) == {'daughter', 'son'}

        filter = {
            'child.name': 'me',
        }
        res = querybuilder(base_query(session), filter).all()
        assert len(res) == 1
        assert set([r.name for r in res]) == {'mother'}
