import os




class Config((object)):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("5036308958:AAF7taC4V4Qdj78OUhmlXFdfi7jRRXxlOnw", "")
    # The Telegram API things
    APP_ID = int(os.environ.get("1424314", 12345))
    API_HASH = os.environ.get("d1c1c9262bbae8f5eeb80ba47c9f3dff")
    # Get these values from my.telegram.org
    # Banned Unwanted Members..
    BANNED_USERS = {int(x) for x in os.environ.get("BANNED_USERS", "").split()}
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # The download location for auth users.

    # Telegram maximum file upload size
    MAX_FILE_SIZE = 2097152000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 2097152000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("128", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = None  # os.environ.get("DEF_THUMB_NAIL_VID_S", "")
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # watermark file
    DEF_WATER_MARK_FILE = ""
    # your telegram id
    OWNER_ID = int(os.environ.get("1079261681", ""))
    # database session name, example: xurluploader
    SESSION_NAME = os.environ.get("SESSION_NAME", "")
    # database uri (mongodb)
    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    PROCESS_TEXT = """
    Process: {}
    """
    LOGGED_AS_USER = """
    Successfully Logged Into Mega.nz User Account
    """
    LOGIN_ERROR_TEXT = """
    Can't Get Mega Email and Password Login as an Anonymouse User
    """

    ERROR_TEXT = """ 
    Log: {}
    Save the Log file and Send it to @TMWAD for Help :)
    """ 
