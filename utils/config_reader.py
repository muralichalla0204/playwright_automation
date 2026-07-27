import configparser

config = configparser.ConfigParser()
config.read("config.ini")


def get_browser():
    return config.get("settings", "browser")


def get_headless():
    return config.getboolean("settings", "headless")


def get_url():
    return config.get("settings", "url")

def get_api_base_url():
    return config.get("settings", "api_base_url")


def get_api_key():
    return config.get("settings", "api_key")