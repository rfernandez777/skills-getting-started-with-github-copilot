import copy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module


@pytest.fixture
def client():
    with TestClient(app_module.app) as test_client:
        yield test_client


@pytest.fixture(autouse=True)
def reset_activities():
    original_state = copy.deepcopy(app_module.activities)
    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(original_state))
    yield
    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(original_state))
