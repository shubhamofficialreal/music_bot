import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", "5889054634:AAFM0W-A9IKxzQJNcYgalDObMzKAG4ZReY0")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://its_star_boi:7234049299@cluster0.8twjh9e.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001621682412"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "𝐒𝐇𝐈𝐙𝐔𝐊𝐀 𓆩🇽𓆪 𝐑𝐎𝐁𝐎𝐓")

OWNER_ID = list(map(int, getenv("OWNER_ID", "5463205082").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/its-star-boi/music_bot")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/star_X_network")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/Best_FriendsFor_Ever")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "f093cabe31c54c9a954269f68a0083d3")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "74d48e8223e843c086bc53b84e5a4a4c")

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes


STRING1 = getenv("STRING_SESSION", "BQAOD9oUKusjDXDoKvtqxp76rkFmQKhihVq5SHv77crPSrRixAiAjqGkwhiPM0_EfairejSnWrqMgBBT72DkjzOQCsXPLOml1xDsIOTQF_mD1pD9-aCqo6IL18B7B1Eg5pMd6HhBjE0Up5yDXgE1ntISQuhEb_dYW_UAaGcOIArmXPtMeUu4xVlUpSeKhqFcr_jm-KLCSGzxrGpYaXHtAQ7Z42kwohZ2d0gVO2ljO2YaFA5bkI0qADBtB8jbIWF6qhMxl0JrRzcWrnR4yHJZidyYHL9JS5UtY0r5ioqlULq5r9SpURm1S2hAy_ae46bpH5KnfQ6oy_rZJSWgToxIlrZbAAAAAWTkphYA")
STRING2 = getenv("STRING_SESSION2", "BQCG7kL9HvdyxdyVy7YpO2F28KiDRcavJ0qxmk_qEYG9gItwNVkVxMEyH_i5Dr_0Hy-5c1xA5NgScfqKayuJfB3T8eUNVjOUf1tV9y4wCsFYgiiRdsDj8X0fQce9bHcWxLXjvayLbkREejJ56Lo6VfjYDAKkihrw-1CsEqEQeoGGNTaM7ZUF3J9c7BTHFpk_Eh2Qm5eJEsUhyICZ74QWf4o1aYzOk2kj3nifwUbOjI7Z9T_OTlw21D_oW92BZDLqiZqAfA14zVPEDdy_6Sod5ZDVmHboKv9XKQ12kCsJQuo71ULTlnQvRweSA1ZKujDTa9CC-3f6Xy8mgS8HIOlj8ZZ3aNPuSQA")
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "https://te.legra.ph/file/56d1760224589ee370186.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://telegra.ph/file/1e1d6269dbc443b0e5bd0.jpg",
)

PLAYLIST_IMG_URL = "https://telegra.ph/file/2f6c4b784ee0977777e93.jpg"

GLOBAL_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"

STATS_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"

TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"

TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"

STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"

SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"

YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://telegra.ph/file/56d1760224589ee370186.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://te.legra.ph/file/56d1760224589ee370186.jpg"
