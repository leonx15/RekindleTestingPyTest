from pytest_metadata.plugin import metadata_key
from utils import utils_main

# Add other information fields to HTML report in environment place.
def pytest_configure(config):
    config.stash[metadata_key]["HOST"] = utils_main.load_config()["host_env"]
    config.stash[metadata_key]["Database HOST"] = utils_main.load_config()["db_host"]
