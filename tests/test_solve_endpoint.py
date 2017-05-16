# -*- coding: utf-8 -*-

import pytest
import json

headers = {'Content-Type': 'application/json'}


@pytest.fixture
def app():
    from app import app
    return app


def test_ping_endpoint(client):
    data = {"array": [[None] * 9] * 9}
    res = client.post('/api/v1/solve',
                      headers=headers,
                      data=json.dumps(data))

    assert res.json == {'status': 'OK'}
