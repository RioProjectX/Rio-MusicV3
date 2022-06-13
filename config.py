from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "4110592"))
API_HASH = getenv("API_HASH", "aa7c849566922168031b95212860ede0")
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_NAME = getenv("BOT_NAME","R")
BOT_USERNAME = getenv("BOT_USERNAME", "Rio Music")
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "DevilsHeavenMF")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "500"))
START_IMG = getenv("START_IMG", "https://telegra.ph/file/660176f499df4e28ebc58.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/660176f499df4e28ebc58.jpg")
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
