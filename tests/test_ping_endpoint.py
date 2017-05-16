# -*- coding: utf-8 -*-

import pytest


@pytest.fixture
def app():
    from app import app
    return app


def test_ping_endpoint(client):
    res = client.get('/api/v1/ping')

    assert res.json == {'ping': 'pong'}
