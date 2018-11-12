# coding: utf-8

import logging
from werkzeug.exceptions import BadRequest
from json_querybuilder import querybuilder

import tiny_petstore.orm as orm
from tiny_petstore.extensions import db
from tiny_petstore.models.store import Store

logger = logging.getLogger(__name__)


class Pet():
    @staticmethod
    def create_from_dict(create_order: dict=None):
        logger.debug('create_order: %s', create_order)

        resource = create_order
        store_name = resource.pop('store.name', None)
        pet = orm.Pet.new_from_dict(resource)

        me = Pet.fetch_by_name(name=pet.name)
        if me is not None:
            raise BadRequest('pet %s already exists' % pet.name)

        if store_name is not None:
            store = Store.fetch_by_name(name=store_name)
            if store is None:
                raise BadRequest('store %s does not exist' % store_name)
            pet.store = store

        db.session.add(pet)
        db.session.commit()

        return pet

    @staticmethod
    def fetch(id: str=None):
        return orm.Pet.query.filter_by(id=id).one_or_none()

    @staticmethod
    def fetch_by_name(name: str=None):
        return orm.Pet.query.filter_by(name=name).one_or_none()

    @staticmethod
    def query(query_order: dict=None):
        if query_order is None:
            return orm.Pet.query.all()
        else:
            try:
                query = orm.Pet.query

                return querybuilder(query, query_order).all()
            except (KeyError, ValueError, AttributeError) as ex:
                raise BadRequest(str(ex))

    @staticmethod
    def update(id: str=None, update_order: dict=None) -> dict:
        pet = Pet.fetch(id=id)
        if pet is None:
            return None

        store_name = update_order.pop('store.name', None)

        if store_name is not None:
            store = Store.fetch_by_name(name=store_name)
            if store is None:
                raise BadRequest('store %s does not exist' % store_name)
            pet.store = store

        for k, v in update_order.items():
            setattr(pet, k, v)

        db.session.add(pet)
        db.session.commit()

        return pet

    @staticmethod
    def delete(id: str=None) -> None:
        pet = Pet.fetch(id=id)
        if pet is None:
            return

        db.session.delete(pet)
        db.session.commit()

        return
