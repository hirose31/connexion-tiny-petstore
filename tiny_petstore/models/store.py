# coding: utf-8

import logging
from werkzeug.exceptions import BadRequest
from json_querybuilder import querybuilder

import tiny_petstore.orm as orm
from tiny_petstore.extensions import db
from tiny_petstore import util

logger = logging.getLogger(__name__)


class Store():
    @staticmethod
    def create_from_dict(create_order: dict=None):
        logger.debug('create_order: %s', create_order)

        resource = create_order
        store = orm.Store.new_from_dict(resource)

        me = Store.fetch_by_name(name=store.name)
        if me is not None:
            raise BadRequest('store %s already exists' % store.name)

        db.session.add(store)
        db.session.commit()

        return store

    @staticmethod
    def fetch(id: str=None):
        return orm.Store.query.filter_by(id=id).one_or_none()

    @staticmethod
    def fetch_by_name(name: str=None):
        return orm.Store.query.filter_by(name=name).one_or_none()

    @staticmethod
    def query(query_order: dict=None):
        if query_order is None:
            return orm.Store.query.all()
        else:
            try:
                query = orm.Store.query.join(orm.Pet, isouter=True)

                return querybuilder(query, query_order).all()
            except (KeyError, ValueError, AttributeError) as ex:
                raise BadRequest(str(ex))

    @staticmethod
    def update(id: str=None, update_order: dict=None) -> dict:
        store = Store.fetch(id=id)
        if store is None:
            return None

        for k, v in update_order.items():
            setattr(store, k, v)

        db.session.add(store)
        db.session.commit()

        return store

    @staticmethod
    def delete(id: str=None) -> None:
        store = Store.fetch(id=id)
        if store is None:
            return

        if store.pets != []:
            raise BadRequest('store %s has pets' % store.name)

        db.session.delete(store)
        db.session.commit()

        return
