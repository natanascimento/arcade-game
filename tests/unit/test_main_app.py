from app import main


def test_version_on_main_app():
    assert main() == "0.1.0"
