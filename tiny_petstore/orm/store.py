# -*- coding: utf-8 -*-

import logging

from tiny_petstore.extensions import db

logger = logging.getLogger(__name__)


class Store(db.Model):
    __tablename__ = 'store'

    id = db.Column(db.Integer,
                   db.Sequence('store_id_seq'),
                   primary_key=True,
                   supports_dict=True,
                   )

    name = db.Column(db.String,
                     index=True,
                     unique=True,
                     nullable=False,
                     supports_dict=True,
                     )

    address = db.Column(db.String,
                        nullable=False,
                        supports_dict=True,
                        )

    pets = db.relationship('Pet',
                           backref='store',
                           supports_dict=True,
                           )

    def __repr__(self):
        return "<Store(id='{0:d}' name='{1:s}' address='{2:s}' pets='{3:s}')>".format(
            self.id,
            self.name,
            self.address,
            ','.join([p.name for p in sorted(self.pets, key=lambda p: p.name)])
        )
