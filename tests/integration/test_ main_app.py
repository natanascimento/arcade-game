import pytest
from app import main


@pytest.mark.skip()
def test_version_on_main_app():
    assert main() == "0.1.0"
