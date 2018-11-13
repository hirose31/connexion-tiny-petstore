import logging
import connexion
from connexion import NoContent
from flask import abort

from tiny_petstore.models.pet import Pet

logger = logging.getLogger(__name__)


def create_pet():  # noqa: E501
    """Add a new pet to the pet

     # noqa: E501

    :param create_order: Pet object that needs to be added to the pet
    :type create_order: dict | bytes

    :rtype: Pet
    """
    create_order = connexion.request.get_json()
    item = Pet.create_from_dict(create_order)
    return item, 201


def delete_pet(id):  # noqa: E501
    """Deletes a pet

     # noqa: E501

    :param id: Pet id to delete
    :type id: int

    :rtype: None
    """
    Pet.delete(id=id)
    return NoContent, 204


def fetch_all_pets():  # noqa: E501
    """Returns pets

    Returns all pets.  # noqa: E501


    :rtype: List[Pet]
    """
    items = Pet.query(query_order=None)
    return items


def fetch_pet(id):  # noqa: E501
    """Find pet by ID

    Returns a single pet # noqa: E501

    :param id: ID of pet to return
    :type id: int

    :rtype: Pet
    """
    item = Pet.fetch(id=id)
    if item is None:
        abort(404, 'pet not found for id: %d' % id)
    else:
        return item


def search_pets():  # noqa: E501
    """Returns pets matched search conditions

    Returns pets which matched by search conditions.  # noqa: E501

    :param search_order: 
    :type search_order: 

    :rtype: List[Pet]
    """
    search_order = connexion.request.get_json()
    items = Pet.query(query_order=search_order)
    return items


def update_pet(id):  # noqa: E501
    """Updates a pet

     # noqa: E501

    :param id: ID of pet that needs to be updated
    :type id: int
    :param update_order: 
    :type update_order: dict | bytes

    :rtype: Pet
    """
    update_order = connexion.request.get_json()
    item = Pet.update(id=id, update_order=update_order)
    if item is None:
        abort(404, 'pet not found for id: %d' % id)
    else:
        return item
