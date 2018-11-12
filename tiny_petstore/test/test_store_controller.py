# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from tiny_petstore.models.store import Store  # noqa: E501
from tiny_petstore.models.store_create_param import StoreCreateParam  # noqa: E501
from tiny_petstore.models.store_param import StoreParam  # noqa: E501
from tiny_petstore.test import BaseTestCase


class TestStoreController(BaseTestCase):
    """StoreController integration test stubs"""

    def test_create_store(self):
        """Test case for create_store

        Add a new store to the store
        """
        create_order = StoreCreateParam()
        response = self.client.open(
            '/v2/stores',
            method='POST',
            data=json.dumps(create_order),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_store(self):
        """Test case for delete_store

        Deletes a store
        """
        response = self.client.open(
            '/v2/stores/{id}'.format(id=789),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_fetch_all_stores(self):
        """Test case for fetch_all_stores

        Returns stores
        """
        response = self.client.open(
            '/v2/stores',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_fetch_store(self):
        """Test case for fetch_store

        Find store by ID
        """
        response = self.client.open(
            '/v2/stores/{id}'.format(id=789),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_stores(self):
        """Test case for search_stores

        Returns stores matched search conditions
        """
        search_order = None
        response = self.client.open(
            '/v2/search/stores',
            method='POST',
            data=json.dumps(search_order),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_store(self):
        """Test case for update_store

        Updates a store
        """
        update_order = StoreParam()
        response = self.client.open(
            '/v2/stores/{id}'.format(id=789),
            method='PATCH',
            data=json.dumps(update_order),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
