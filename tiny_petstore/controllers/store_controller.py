import connexion
import six

from tiny_petstore.models.store import Store  # noqa: E501
from tiny_petstore.models.store_create_param import StoreCreateParam  # noqa: E501
from tiny_petstore.models.store_param import StoreParam  # noqa: E501
from tiny_petstore import util


def create_store(create_order):  # noqa: E501
    """Add a new store to the store

     # noqa: E501

    :param create_order: Store object that needs to be added to the store
    :type create_order: dict | bytes

    :rtype: Store
    """
    if connexion.request.is_json:
        create_order = StoreCreateParam.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_store(id):  # noqa: E501
    """Deletes a store

     # noqa: E501

    :param id: Store id to delete
    :type id: int

    :rtype: None
    """
    return 'do some magic!'


def fetch_all_stores():  # noqa: E501
    """Returns stores

    Returns all stores.  # noqa: E501


    :rtype: List[Store]
    """
    return 'do some magic!'


def fetch_store(id):  # noqa: E501
    """Find store by ID

    Returns a single store # noqa: E501

    :param id: ID of store to return
    :type id: int

    :rtype: Store
    """
    return 'do some magic!'


def search_stores(search_order=None):  # noqa: E501
    """Returns stores matched search conditions

    Returns stores which matched by search conditions.  # noqa: E501

    :param search_order: 
    :type search_order: 

    :rtype: List[Store]
    """
    return 'do some magic!'


def update_store(id, update_order):  # noqa: E501
    """Updates a store

     # noqa: E501

    :param id: ID of store that needs to be updated
    :type id: int
    :param update_order: 
    :type update_order: dict | bytes

    :rtype: Store
    """
    if connexion.request.is_json:
        update_order = StoreParam.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
