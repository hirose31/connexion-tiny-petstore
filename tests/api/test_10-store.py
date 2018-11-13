# -*- coding: utf-8 -*-

import re

from utils import set_of


class TestStore:
    def test_fetch_all(self, testapp):
        res = testapp.get('/v2/stores')
        data = res.json

        assert len(data) == 3
        assert set_of('name', data) == {'Pets Unlimited', 'The Pet Mansion', 'Nothing One'}

    def test_create(self, testapp):
        res = testapp.post_json('/v2/stores', {
            'name': 'foo',
            'address': 'Toshima',
        })
        data = res.json

        assert res.status_int == 201
        assert isinstance(data, dict)
        assert data['name'] == 'foo'

        # error
        # missing required param
        res = testapp.post_json('/v2/stores', {
            'address': 'Toshima',
        },
            expect_errors=True,
        )

        assert res.status_int == 400

        # invalid character
        res = testapp.post_json('/v2/stores', {
            'name': '!foo',
            'address': 'Toshima',
        },
            expect_errors=True,
        )

        assert res.status_int == 400

        # same name
        res = testapp.post_json('/v2/stores', {
            'name': 'foo',
            'address': 'Shimane',
        },
            expect_errors=True,
        )
        data = res.json

        assert res.status_int == 400
        assert data['detail'] == 'store foo already exists'

    def test_fetch(self, testapp):
        res = testapp.get('/v2/stores/%d' % 1)
        data = res.json

        assert res.status_int == 200
        assert isinstance(data, dict)
        assert data['name'] == 'Pets Unlimited'

        # error
        # not found
        res = testapp.get('/v2/stores/%d' % 99,
                          expect_errors=True,
                          )
        data = res.json

        assert res.status_int == 404

    def test_update(self, testapp):
        new_name = 'foo'
        res = testapp.patch_json('/v2/stores/1', {
            'name': new_name,
        })
        data = res.json

        assert res.status_int == 200
        assert isinstance(data, dict)

        res = testapp.get('/v2/stores/1')
        data = res.json
        assert data['name'] == 'foo'

        # error
        # invalid character
        res = testapp.patch_json('/v2/stores/1', {
            'name': '!foo',
        },
            expect_errors=True,
        )
        data = res.json

        assert res.status_int == 400

        # not found
        res = testapp.patch_json('/v2/stores/31', {
            'name': 'bar',
        },
            expect_errors=True,
        )

        assert res.status_int == 404

    def test_delete(self, testapp):
        # create to delete
        res = testapp.post_json('/v2/stores', {
            'name': 'foo',
            'address': 'Toshima',
        })
        data = res.json

        assert res.status_int == 201
        store_id = data['id']

        # delete
        res = testapp.delete('/v2/stores/%d' % store_id)

        assert res.status_int == 204
        assert res.text == ''

        # check
        res = testapp.get('/v2/stores/%d' % store_id,
                          expect_errors=True,
                          )

        assert res.status_int == 404

        # delete again
        res = testapp.delete('/v2/stores/%d' % store_id)

        assert res.status_int == 204
        assert res.text == ''

        # error
        # cannot delete a store which have pets
        res = testapp.delete('/v2/stores/%d' % 1,
                             expect_errors=True,
                             )
        data = res.json

        assert res.status_int == 400
        assert re.search(r'^store .+ has pets$', data['detail'])

    def test_search(self, testapp):
        res = testapp.post_json('/v2/search/stores', {
            'address': 'Shibuya',
        })
        data = res.json

        assert len(data) == 1
        assert set_of('name', data) == {'Pets Unlimited'}

        res = testapp.post_json('/v2/search/stores', {
            'address': 'Saitama',
        })
        data = res.json

        assert len(data) == 0

        res = testapp.post_json('/v2/search/stores', {
            'address': {'like': '%i%'},
        })
        data = res.json

        assert len(data) == 3

        res = testapp.post_json('/v2/search/stores', {
            'address': {'like': '%a'},
        })
        data = res.json

        assert len(data) == 2
        assert set_of('name', data) == {'Pets Unlimited', 'The Pet Mansion'}

        res = testapp.post_json('/v2/search/stores', {
            'name': {'like': '%Mansion%'},
            'address': {'like': '%a'},
        })
        data = res.json

        assert len(data) == 1
        assert set_of('name', data) == {'The Pet Mansion'}

        # error
        res = testapp.post_json('/v2/search/stores', {
            'blah': 'blah',
        },
            expect_errors=True,
        )

        assert res.status_int == 400
