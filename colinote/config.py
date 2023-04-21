import configparser
import os

config = configparser.ConfigParser()
config_file = os.path.join(os.path.expanduser("~"), ".colinoterc")

if os.path.exists(config_file):
    config.read(config_file)

if not config.has_section("DEFAULT"):
    config["DEFAULT"] = {}

if not config.has_option("DEFAULT", "data_file"):
    config["DEFAULT"]["data_file"] = "notes.json"

with open(config_file, "w") as f:
    config.write(f)

data_file = config["DEFAULT"]["data_file"]
