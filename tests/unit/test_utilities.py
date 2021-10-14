'''
   unit tests for utilities methods
'''
import pytest
from src.utilities import get_logger, change_log_location, file_encrypt, file_decrypt, Config

code_path = "C:\\Users\\RAMA\\Desktop\\python\\playground\\anymind_project"

class TestUtilities:

    def test_get_logger(self):
        try:
            logger, _ = get_logger()
            assert True
        except:
            assert False

    def test_change_log_location(self):
        try:
            logger, _ = get_logger()
            new_file = f"{code_path}\\tests\\unit\\test_data\\sample_file.log"
            change_log_location(logger, new_file)
            assert True
        except:
            assert False

    def test_file_encrypt(self):
        test_file = f"{code_path}\\tests\\unit\\test_data\\test_enc_file.enc"
        test_key = "anymindgroup.com"

        with open(test_file, 'w') as f:
            f.write("some test key")

        try:
            file_encrypt(test_file, test_key)
            assert True
        except:
            assert False

    def test_file_encrypt_exception(self):
        test_file = f"{code_path}\\tests\\unit\\test_data\\file_not_exists.enc"
        test_key = "anymindgroup.com"

        try:
            file_encrypt(test_file, test_key)
            assert False
        except:
            assert True

    def test_file_decrypt(self):
        test_file = f"{code_path}\\tests\\unit\\test_data\\test_enc_file.enc"
        test_key = "anymindgroup.com"

        with open(test_file, 'w') as f:
            f.write("secret_key")

        file_encrypt(test_file, test_key)
        assert "secret_key" == file_decrypt(test_file, test_key)

    def test_config(self):
        cfg = Config()

        assert cfg.twitter_search_api == "https://api.twitter.com/2/tweets/search/recent"
        assert cfg.bearer_token_enc_file == f"{code_path}\\secret_keys\\bearer_token.enc"
        assert cfg.app_key == "anymindgroup.com"
        assert cfg.app_key_enc_file == f"{code_path}\\secret_keys\\app_key.enc"
