import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 21782992
API_HASH = "5c8a12b9dd70d182e11d9ead5d357dab"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7290157519:AAEpxiPRdd_e662Hi63tsHjfbofkJQRVlvs"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://combinado:combinado@cluster0.2a7qm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOGGER_ID = -1002246269016

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = 672466909

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/AnonymousX1025/AnonXMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FallenAssociation")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DevilsHeavenMF")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = "AQFMYdAAlhdmdT54AAteIiqpPpf1sEm9WGj_95conNnzQswFl8exaDC2YRcwectMiKBTXNVIQT18blP7BvFwY9oDjr_4KiDFjYeZP1whpkbpqChZ6F_k42B_5RTzDgBSgbXRCKJGhHo5jM_v4Dg6w5iCvKmZVYVHQzqNh07V1wf1sNpyDyCcF857SVFxK5tNolji6E0Phk3HGAP1nb3b7YFbma4MjCsqaUZ1HCicEW2LmafJD1LXDFbvPvcM-D_HglHBHfc_qNDlIL4mVayiic-JXfR6qVfXAGc3fTGGifufx_MRQIh3mOf-0Z5dTocPh36rCga4q93FeGH0xEP-5lEe-zYTRQAAAAAoFQfdAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://te.legra.ph/file/3843e2f17e49395e4adab.png"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/adc241f65e920429b824f.png"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/fe4373a26d55df8ed04e5.png"
STATS_IMG_URL = "https://te.legra.ph/file/5291ecdc07dd635bc1a81.png"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/fe4373a26d55df8ed04e5.png"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/fe4373a26d55df8ed04e5.png"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
