#(©)t.me/CodeFlix_Bots




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7322378265:AAGl3pyOZ4vzESzcYEysdnQe5i24FvOfE4A")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "24177479"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "6a21ab3ea9fc9052f023980646630c01")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002212096027"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "PROVIDER")

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7208538115"))

#Port
PORT = os.environ.get("PORT", "1022")

#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://sunitverma080:95xPiJttR9BoLplO@cluster0.oc927.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "cluster0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002222206723"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002222581548"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "100"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>Hello {first}</b>\n\nmuth marna band kr de dusro ko sex krte dekh muth marne maja aata kya?? cuck ho? eww bhai imagine tumhara brain itna fucked up ho chuka hai ki tum dusro ko sex krte dekh maja ata sad bhai ye sab band kr do @brainsaga if you want bot like this </a></b>")
try:
    ADMINS=[7208538115]
    for x in (os.environ.get("ADMINS", "7208538115").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "👋 Hello {first}!\nTo access these files you have to join our channel first.\nPlease subscribe to our channels through the buttons below and then tap on try again to get your files.\nThank You ❤️")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>By @Mrbeast087</a>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = " aee lavdya ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ admin!!"

ADMINS.append(OWNER_ID)
ADMINS.append(7208538115)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
