'''
   unit tests for flask app creation
'''
import pytest
from src.app import create_flask_app


class TestApplication:
    def test_create_flask_app(self):
        try:
            create_flask_app()
            assert True
        except:
            assert False
