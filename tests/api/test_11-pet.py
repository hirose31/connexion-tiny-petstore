# -*- coding: utf-8 -*-

import re

from utils import set_of


class TestPet:
    def test_fetch_all(self, testapp):
        res = testapp.get('/v2/pets')
        data = res.json

        assert len(data) == 3
        assert set_of('name', data) == {'tama', 'mike', 'chibi'}

    def test_create(self, testapp):
        res = testapp.post_json('/v2/pets', {
            'name': 'azuki',
            'store.name': 'Pets Unlimited',
            'status': 'available',
        })
        data = res.json

        assert res.status_int == 201
        assert isinstance(data, dict)
        assert data['name'] == 'azuki'
        assert data['status'] == 'available'

        # status default is pending
        res = testapp.post_json('/v2/pets', {
            'name': 'kotetsu',
            'store.name': 'Pets Unlimited',
        })
        data = res.json

        assert res.status_int == 201
        assert isinstance(data, dict)
        assert data['name'] == 'kotetsu'
        assert data['status'] == 'pending'

        # error
        # missing required param
        res = testapp.post_json('/v2/pets', {
            'name': 'cheshire',
        },
            expect_errors=True,
        )

        assert res.status_int == 400

        # invalid character
        res = testapp.post_json('/v2/pets', {
            'name': '!cheshire',
            'store.name': 'Pets Unlimited',
        },
            expect_errors=True,
        )

        assert res.status_int == 400

        # same name
        res = testapp.post_json('/v2/pets', {
            'name': 'azuki',
            'store.name': 'Pets Unlimited',
        },
            expect_errors=True,
        )
        data = res.json

        assert res.status_int == 400
        assert data['detail'] == 'pet azuki already exists'

    def test_fetch(self, testapp):
        res = testapp.get('/v2/pets/%d' % 1)
        data = res.json

        assert res.status_int == 200
        assert isinstance(data, dict)
        assert data['name'] == 'tama'

        # error
        # not found
        res = testapp.get('/v2/pets/%d' % 99,
                          expect_errors=True,
                          )
        data = res.json

        assert res.status_int == 404

    def test_update(self, testapp):
        new_name = 'azuki'
        res = testapp.patch_json('/v2/pets/1', {
            'name': new_name,
            'store.name': 'The Pet Mansion',
        })
        data = res.json

        assert res.status_int == 200
        assert isinstance(data, dict)

        res = testapp.get('/v2/pets/1')
        data = res.json
        assert data['name'] == 'azuki'
        assert data['store']['name'] == 'The Pet Mansion'

        # error
        # invalid character
        res = testapp.patch_json('/v2/pets/1', {
            'name': '!cheshire',
        },
            expect_errors=True,
        )
        data = res.json

        assert res.status_int == 400

        # not found
        res = testapp.patch_json('/v2/pets/31', {
            'name': 'cheshire',
        },
            expect_errors=True,
        )

        assert res.status_int == 404

        # store not found
        res = testapp.patch_json('/v2/pets/1', {
            'store.name': 'oops',
        },
            expect_errors=True,
        )
        data = res.json

        assert res.status_int == 400
        assert data['detail'] == 'store oops does not exist'

        # unknown status
        res = testapp.patch_json('/v2/pets/1', {
            'status': 'oops',
        },
            expect_errors=True,
        )
        data = res.json

        assert res.status_int == 400
        assert re.search(r'is not one of', data['detail'])

    def test_delete(self, testapp):
        # create to delete
        res = testapp.post_json('/v2/pets', {
            'name': 'cheshire',
            'store.name': 'Pets Unlimited',
        })
        data = res.json

        assert res.status_int == 201
        pet_id = data['id']

        # delete
        res = testapp.delete('/v2/pets/%d' % pet_id)

        assert res.status_int == 204
        assert res.text == ''

        # check
        res = testapp.get('/v2/pets/%d' % pet_id,
                          expect_errors=True,
                          )

        assert res.status_int == 404

        # delete again
        res = testapp.delete('/v2/pets/%d' % pet_id)

        assert res.status_int == 204
        assert res.text == ''
