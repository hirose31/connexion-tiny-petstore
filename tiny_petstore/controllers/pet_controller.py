import connexion
import six

from tiny_petstore.models.pet import Pet  # noqa: E501
from tiny_petstore.models.pet_create_param import PetCreateParam  # noqa: E501
from tiny_petstore.models.pet_param import PetParam  # noqa: E501
from tiny_petstore import util


def create_pet(create_order):  # noqa: E501
    """Add a new pet to the store

     # noqa: E501

    :param create_order: Pet object that needs to be added to the store
    :type create_order: dict | bytes

    :rtype: Pet
    """
    if connexion.request.is_json:
        create_order = PetCreateParam.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_pet(id):  # noqa: E501
    """Deletes a pet

     # noqa: E501

    :param id: Pet id to delete
    :type id: int

    :rtype: None
    """
    return 'do some magic!'


def fetch_all_pets():  # noqa: E501
    """Returns pets

    Returns all pets.  # noqa: E501


    :rtype: List[Pet]
    """
    return 'do some magic!'


def fetch_pet(id):  # noqa: E501
    """Find pet by ID

    Returns a single pet # noqa: E501

    :param id: ID of pet to return
    :type id: int

    :rtype: Pet
    """
    return 'do some magic!'


def search_pets(search_order=None):  # noqa: E501
    """Returns pets matched search conditions

    Returns pets which matched by search conditions.  # noqa: E501

    :param search_order: 
    :type search_order: 

    :rtype: List[Pet]
    """
    return 'do some magic!'


def update_pet(id, update_order):  # noqa: E501
    """Updates a pet

     # noqa: E501

    :param id: ID of pet that needs to be updated
    :type id: int
    :param update_order: 
    :type update_order: dict | bytes

    :rtype: Pet
    """
    if connexion.request.is_json:
        update_order = PetParam.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
