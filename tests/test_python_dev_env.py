"""Test Hello world."""


from python_dev_env import __version__
from python_dev_env.hello_world import hello_world


def test_version():
    """test_version."""
    assert __version__ == '0.1.0'

# @pytest.fixture
# def world():
#     return "world"


def test_hello_world():
    """test_hello_world."""
    result = hello_world("world")
    assert result == "hello world"
