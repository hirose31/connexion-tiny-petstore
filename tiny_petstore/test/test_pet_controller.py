# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from tiny_petstore.models.pet import Pet  # noqa: E501
from tiny_petstore.models.pet_create_param import PetCreateParam  # noqa: E501
from tiny_petstore.models.pet_param import PetParam  # noqa: E501
from tiny_petstore.test import BaseTestCase


class TestPetController(BaseTestCase):
    """PetController integration test stubs"""

    def test_create_pet(self):
        """Test case for create_pet

        Add a new pet to the store
        """
        create_order = PetCreateParam()
        response = self.client.open(
            '/v2/pets',
            method='POST',
            data=json.dumps(create_order),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_pet(self):
        """Test case for delete_pet

        Deletes a pet
        """
        response = self.client.open(
            '/v2/pets/{id}'.format(id=789),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_fetch_all_pets(self):
        """Test case for fetch_all_pets

        Returns pets
        """
        response = self.client.open(
            '/v2/pets',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_fetch_pet(self):
        """Test case for fetch_pet

        Find pet by ID
        """
        response = self.client.open(
            '/v2/pets/{id}'.format(id=789),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_pets(self):
        """Test case for search_pets

        Returns pets matched search conditions
        """
        search_order = None
        response = self.client.open(
            '/v2/search/pets',
            method='POST',
            data=json.dumps(search_order),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_pet(self):
        """Test case for update_pet

        Updates a pet
        """
        update_order = PetParam()
        response = self.client.open(
            '/v2/pets/{id}'.format(id=789),
            method='PATCH',
            data=json.dumps(update_order),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
