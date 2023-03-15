try:
    from logging import getLogger
    from os import environ
    LOGGER = getLogger(__name__)
    from os import getenv
    import sys
    import os
    from dotenv import load_dotenv
    from base64 import b64decode as who
    from distutils.util import strtobool as sb
    load_dotenv("config.env", override=True)
except:
    print("not installed pykillerx")


API_ID = int(getenv("API_ID", "")) 
API_HASH = getenv("API_HASH", "")
OWNER_ID = int(getenv("OWNER_ID", ""))
BOT_TOKEN = getenv("BOT_TOKEN", "")

ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PACK_NAME = getenv("PACK_NAME", "kang pack")

GCAST_BLACKLIST = {int(x) for x in getenv("GCAST_BLACKLIST", "").split()}

PREFIXES = getenv("PREFIXES") # this command . or +
DB_URL = getenv("DATABASE_URL")
RMBG_API = getenv("RMBG_API")
OPENAI_API = getenv("OPENAI_API")
DEEPAI_API = getenv("DEEPAI_API")
API_KEY_GOOGLE = getenv("API_KEY_GOOGLE")
SEARCH_ENGINE_ID = getenv("SEARCH_ENGINE_ID")
SAVE_CONTENT = int(getenv("SAVE_CONTENT", -1001624259885))
MAX_MESSAGE_LENGTH = 4096

BOT_VER = "0.3.20@build"
BRANCH = getenv("BRANCH", "dev")
 
STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", None)
STRING_SESSION3 = getenv("STRING_SESSION3", None)
