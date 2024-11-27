import re
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

API_ID = int(environ.get("API_ID", "25061703"))
API_HASH = environ.get("API_HASH", "744a017a9c53f3ab489ea0bfa0ffce3f")
BOT_TOKEN = environ.get("BOT_TOKEN", "7711608312:AAGnkhxkCOe96KKvzJZJBzUqBDPKyJkxv2E")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002410351186"))
ADMINS = int(environ.get("ADMINS", "6899946963"))
DB_URI = environ.get("DB_URI", "mongodb+srv://nimovie09:cx52vvB7cVmZ6zNM@cluster0.cbk2f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "chatgptvjbot")
OPENAI_API = environ.get("OPENAI_API", "")
AI = is_enabled((environ.get("AI","True")), False)
