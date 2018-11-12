# -*- coding: utf-8 -*-

import logging
from sqlathanor import AttributeConfiguration

from tiny_petstore.extensions import db

logger = logging.getLogger(__name__)


class Pet(db.Model):
    __tablename__ = 'pet'

    __serialization__ = [
        AttributeConfiguration(name='store',
                               supports_dict=True,
                               ),
    ]

    id = db.Column(db.Integer,
                   db.Sequence('pet_id_seq'),
                   primary_key=True,
                   supports_dict=True,
                   )

    name = db.Column(db.String,
                     index=True,
                     unique=True,
                     nullable=False,
                     supports_dict=True,
                     )

    store_id = db.Column(db.Integer,
                         db.ForeignKey('store.id'),
                         nullable=False,
                         supports_dict=False,
                         )

    status = db.Column(db.String,
                       default='pending',
                       server_default='pending',
                       supports_dict=True,
                       )

    def __repr__(self):
        return "<Pet(id='{0:d}' name='{1:s}' status='{2:s}' store='{3:s}')>".format(
            self.id,
            self.name,
            self.status,
            self.store.name,
        )
