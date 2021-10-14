'''
    Helper methods for running FLASK APP
'''
import logging
import sys
import os
import json

from base64 import b64decode, b64encode
from configparser import ConfigParser
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import unpad, pad
from logging.handlers import RotatingFileHandler

# WINDOWS path , we can change to any code location
code_path = "C:\\Users\\RAMA\\Desktop\\python\\playground\\anymind_project"

# config file path
cfg_file = f"{code_path}\\cfg\\twitter_rest_api.cfg"

# A pretty default logging format
default_format = "%(asctime)s|%(levelname)s|%(name)s|%(funcName)s|%(message)s"


def get_logger(log_file="out.log",
               log_level=logging.INFO,
               console_level=logging.INFO,
               log_format=default_format,
               log_name=None):
    """
    Create a new root logger and sets its formatting and handlers.

    Parameters:
    log_file (str): full path to file logger will write to
    log_level (int): file logging level. defaults to logging.INFO
    console_level (int): console logging level. defaults to logging.INFO
    log_format (str): log message format. defaults to "%(asctime)s|%(levelname)-5s|%(name)s|%(funcName)s|%(message)s"

    Returns: New root logger

    """
    # Set up new root logger
    new_logger = logging.getLogger(log_name)
    new_logger.setLevel(log_level)

    # Set the time format
    log_format = logging.Formatter(log_format, "%Y-%m-%d %H:%M:%S")

    # Set up file handler
    file_handler = RotatingFileHandler(log_file, maxBytes=1000 * 1000)
    file_handler.setLevel(log_level)
    file_handler.setFormatter(log_format)
    new_logger.addHandler(file_handler)

    # Set up stream handler
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(console_level)
    stream_handler.setFormatter(log_format)
    new_logger.addHandler(stream_handler)

    return new_logger, file_handler


def change_log_location(logger, new_file):
    """
    Take an existing logger and updates the log file path.

    Parameters:
    logger (logging.Logger): logger whose log file location you want to change
    new_file (str): full path to new log file you want to use

    """
    # Create new file handler for new log file
    new_file_handler = RotatingFileHandler(new_file, maxBytes=1000 * 1000)

    # Keep formatter and logging level from old handler
    new_file_handler.setFormatter(logger.handlers[0].formatter)
    new_file_handler.setLevel(logger.getEffectiveLevel())

    # Set the logger's handlers
    logger.handlers = [new_file_handler, logger.handlers[1]]


def file_encrypt(pass_file: str, key: str):
    """
    This method encrypts the data file passed.
    Parameters:
        pass_file: File consists of secret data that needs to be encrypted
        key: password with which data is encrypted
    initialization_vector: initialization vector,this value is also used as encrypting/decrypting parameter
        this value gets stored along with decrypted value in .enc file.
    """
    try:
        if not os.path.isfile(pass_file):
            raise OSError(f"File {pass_file} not found!")
        with open(pass_file, "rb") as data:
            plain_text = data.read()
        key = bytes(key.encode('utf-8'))
        cipher = AES.new(key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(plain_text, AES.block_size))
        initialization_vector = b64encode(cipher.iv).decode('utf-8')
        cipher_data = b64encode(ct_bytes).decode('utf-8')
        encrypted_file = os.path.splitext(pass_file)[0]
        with open(encrypted_file + ".enc", "w") as file_out:
            encrypted_data = {'iv': initialization_vector, 'ciphertext': cipher_data}
            json.dump(encrypted_data, file_out)
        return "File " + pass_file + " is encrypted successfully"
    except Exception as exc:
        raise exc


def file_decrypt(pass_file: str, key: str):
    """
    This method decrypts the data file passed.
    Parameters:
        pass_file: File consists of encrypted data that needs to be decrypted.
        key: password with which data is encrypted
    iv: initialization vector, this value is already stored along with encrypted data in .enc file.
    returns:
        The decrypted data.
    """
    try:
        if not os.path.isfile(pass_file):
            raise OSError(f"File {pass_file} not found!")
        with open(pass_file, "r") as file_descriptor:
            b64 = json.loads(file_descriptor.read())
        key = bytes(key.encode('utf-8'))
        initialization_vector = b64decode(b64['iv'])
        cipher_data = b64decode(b64['ciphertext'])
        cipher = AES.new(key, AES.MODE_CBC, iv=initialization_vector)
        return unpad(cipher.decrypt(cipher_data), AES.block_size).decode("utf-8").strip("\n")
    except Exception as exc:
        raise exc


class Config:
    def __init__(self):
        '''
        Read config file and set app configuration values
        '''

        self.twitter_search_api = None
        self.twitter_by_id_api = None
        self.twitter_by_username_api = None
        self.bearer_token_enc_file = None
        self.app_key = None
        self.logfile_location = None
        self.app_key_enc_file = None

        config = ConfigParser()
        config.read(cfg_file)

        # Get all config details
        config_data = dict(config.items('twitter_rest_api'))
        for key, value in config_data.items():
            if hasattr(self, key):
                setattr(self, key, value)

        self.bearer_token_enc_file = f"{code_path}\\secret_keys\\{self.bearer_token_enc_file}"
        self.bearer_token = file_decrypt(self.bearer_token_enc_file, self.app_key)

        self.app_key_enc_file = f"{code_path}\\secret_keys\\{self.app_key_enc_file}"
        self.app_key = file_decrypt(self.app_key_enc_file, self.app_key)
