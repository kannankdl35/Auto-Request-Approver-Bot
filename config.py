import os
from typing import List

API_ID = os.environ.get("API_ID", "8721997")
API_HASH = os.environ.get("API_HASH", "47dbeccf2ade0e096f08dce7617f4f3b")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8215877176:AAGxDk2r09IDBRBdBWixDQwTmjPNuwLliMM")
ADMIN = int(os.environ.get("ADMIN", "1994878828 2002710801"))
PICS = (os.environ.get("PICS", "https://envs.sh/Fkx.jpg")).split()

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
NEW_REQ_MODE = os.environ.get("NEW_REQ_MODE", "False").lower() == "true"  # Set "True" For accept new requests

DB_URI = os.environ.get("DB_URI", "")
DB_NAME = os.environ.get("DB_NAME", "")

IS_FSUB = os.environ.get("IS_FSUB", "False").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "-100******** -100*********").split())) # Add Multiple channel ids
