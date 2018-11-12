import logging
from connexion import NoContent
from flask import abort

from tiny_petstore.models.store import Store

logger = logging.getLogger(__name__)


def create_store(create_order=None):
    """Add a new store to the store

     # noqa: E501

    :param create_order: Store object that needs to be added to the store
    :type create_order: dict | bytes

    :rtype: Store
    """
    item = Store.create_from_dict(create_order)
    return item, 201


def delete_store(id):  # noqa: E501
    """Deletes a store

     # noqa: E501

    :param id: Store id to delete
    :type id: int

    :rtype: None
    """
    Store.delete(id=id)
    return NoContent, 204


def fetch_all_stores():  # noqa: E501
    """Returns stores

    Returns all stores.  # noqa: E501


    :rtype: List[Store]
    """
    items = Store.query(query_order=None)
    return items


def fetch_store(id):  # noqa: E501
    """Find store by ID

    Returns a single store # noqa: E501

    :param id: ID of store to return
    :type id: int

    :rtype: Store
    """
    item = Store.fetch(id=id)
    if item is None:
        abort(404, 'store not found for id: %d' % id)
    else:
        return item


def search_stores(search_order=None):  # noqa: E501
    """Returns stores matched search conditions

    Returns stores which matched by search conditions.  # noqa: E501

    :param search_order: 
    :type search_order: 

    :rtype: List[Store]
    """
    items = Store.query(query_order=search_order)
    return items


def update_store(id, update_order):  # noqa: E501
    """Updates a store

     # noqa: E501

    :param id: ID of store that needs to be updated
    :type id: int
    :param update_order: 
    :type update_order: dict | bytes

    :rtype: Store
    """
    item = Store.update(id=id, update_order=update_order)
    if item is None:
        abort(404, 'store not found for id: %d' % id)
    else:
        return item
