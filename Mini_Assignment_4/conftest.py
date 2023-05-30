import pytest


@pytest.fixture(scope="function")
def fixture(request):
    print("Started TestCase " + request.module.__name__ + ".")
    yield
    print("Completed TestCase " + request.module.__name__ + ".")
