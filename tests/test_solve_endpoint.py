# -*- coding: utf-8 -*-

import pytest
import json

headers = {'Content-Type': 'application/json'}


@pytest.fixture
def app():
    from app import app
    return app


def test_ping_endpoint(client):
    data = {
        "array": [
            [2, None, 7, None, None, 5, None, 6, None],
            [None, None, None, 6, None, None, None, 1, 2],
            [None, None, 6, None, 1, None, None, None, None],
            [7, None, None, None, None, 2, None, None, None],
            [4, 8, None, None, None, None, None, 9, 1],
            [None, None, None, 8, None, None, None, None, 5],
            [None, None, None, None, 3, None, 8, None, None],
            [8, 7, None, None, None, 9, None, None, None],
            [None, 9, None, 5, None, None, 3, None, 4]
        ]
    }
    res = client.post('/api/v1/solve',
                      headers=headers,
                      data=json.dumps(data))

    expected = {
        "solution": [
            [2, 1, 7, 9, 8, 5, 4, 6, 3],
            [3, 5, 8, 6, 4, 7, 9, 1, 2],
            [9, 4, 6, 2, 1, 3, 5, 8, 7],
            [7, 3, 9, 1, 5, 2, 6, 4, 8],
            [4, 8, 5, 3, 7, 6, 2, 9, 1],
            [6, 2, 1, 8, 9, 4, 7, 3, 5],
            [5, 6, 4, 7, 3, 1, 8, 2, 9],
            [8, 7, 3, 4, 2, 9, 1, 5, 6],
            [1, 9, 2, 5, 6, 8, 3, 7, 4]],
        "status": "OK"}

    assert res.json == expected
