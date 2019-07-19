import os

import pytest


@pytest.fixture
def fixture_directory():
    """
    This exists as a fixture so that it gets passed around more easily to
    pytest functions, without needing to do funky import stuff in the test
    suite because it's not technically installed.

    No, I am not going to rely on people being in the right directory to have
    tests be a valid Python package. So this somewhat ugly but elegant hack
    will have to do.

    With <3
    """
    return os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "fixtures"
