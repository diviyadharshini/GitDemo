import pytest


@pytest.fixture(scope="class")
def setup():
    print("I am first-to perform pre")
    yield
    print("I will be after main because of yield-to perform post")

@pytest.fixture()
def dataload():
    print("user profile")
    return["diviya","dharshini","diviyadharshini123@gmail.com"]

@pytest.fixture(params=[("chrome","AA","BB"),("Firefox","CC"),("IE","DD")])
def crossbrowser(request):
    return request.param