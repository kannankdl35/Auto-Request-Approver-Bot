import os
from typing import List

API_ID = os.environ.get("API_ID", "8721997")
API_HASH = os.environ.get("API_HASH", "47dbeccf2ade0e096f08dce7617f4f3b")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8215877176:AAGxDk2r09IDBRBdBWixDQwTmjPNuwLliMM")
ADMIN = int(os.environ.get("ADMIN", "1994878828"))
PICS = (os.environ.get("PICS", "https://envs.sh/Fkx.jpg")).split()

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1003027578148"))
NEW_REQ_MODE = os.environ.get("NEW_REQ_MODE", "True").lower() == "true"  # Set "True" For accept new requests

DB_URI = os.environ.get("DB_URI", "mongodb+srv://deepakkadakkal30:RSE9t6lq0aBie3RK@cluster0.6quqrqj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "Cluster0")

IS_FSUB = os.environ.get("IS_FSUB", "False").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "-1001797005272").split())) # Add Multiple channel ids
