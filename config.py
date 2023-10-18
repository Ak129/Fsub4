# Codexbotz # @mrismanaziz

import logging
import os
from distutils.util import strtobool
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6461358025:AAGU5DQRiN17RgT_WpXj4YExeem3ej6AuMw")

API_ID = int(os.environ.get("API_ID", "26562289"))
API_HASH = os.environ.get("API_HASH", "d7426fd6f91cff563d62d318a7e5aab1")

CHANNEL_DB = int(os.environ.get("CHANNEL_DB", "-1001818902142"))
DATABASE_URL = os.environ.get("DATABASE_URL", "postgres://agmmlzsy:YcJlBiH6otmbc9LXCbS2jzLOUY58MCfD@trumpet.db.elephantsql.com/agmmlzsy")

RESTRICT = strtobool(os.environ.get("RESTRICT", "True"))

FORCE_SUB_1 = int(os.environ.get("FORCE_SUB_1", "-1001864926969"))
FORCE_SUB_2 = int(os.environ.get("FORCE_SUB_2", "-1001605233670"))
FORCE_SUB_3 = int(os.environ.get("FORCE_SUB_3", "0"))
FORCE_SUB_4 = int(os.environ.get("FORCE_SUB_4", "0"))

WORKERS = int(os.environ.get("WORKERS", "4"))

START_MESSAGE = os.environ.get(
    "START_MESSAGE",
    "<b>👋 Hello {mention}!</b>"
    "\n\n"
    "<b>I can save private files on a specific Channel and other users can access them from a special link</b>.",
)
FORCE_MESSAGE = os.environ.get(
    "FORCE_MESSAGE",
    "<b>👋 Hello {mention}!</b>"
    "\n\n"
    "<b>🚨You Must Join All The Channel First, to Get Your Mods/Pin/Files.</b>"
    "\n\n"
    "⚠️<b>After joining come back to this bot & click on
    ✅Done/Get Link button to get your mod/pin/files.</b>",
)

try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "5454532062").split())]
except ValueError:
    raise Exception("Your Admin list does not contain a valid Telegram User ID.")
    
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)
DISABLE_BUTTON = strtobool(os.environ.get("DISABLE_BUTTON", "False"))


LOGS_FILE = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOGS_FILE, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
