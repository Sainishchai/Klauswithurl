import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '28394784'))
API_HASH = environ.get('API_HASH', '9544a3ad7d8660acbae0dcf553c808e5')
BOT_TOKEN = environ.get('BOT_TOKEN', '5877942822:AAHNf46r8fFlnlmzbjdjfihuSIYK4UMdOmk')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
PICS = (environ.get('PICS', 'https://telegra.ph/file/825eb0b9b48f4332e5271.jpg https://telegra.ph/file/b958949b16be1f0dd01a6.jpg https://telegra.ph/file/fe666659e64576db72b06.jpg https://telegra.ph/file/7d204c124a17df7e223fc.jpg https://telegra.ph/file/54ac56480944b69813426.png https://telegra.ph/file/5de1e88e4e322c81fe26f.jpg https://telegra.ph/file/8450338748ac577a7cdc5.jpg https://telegra.ph/file/e242c4a1af8f9b0a55164.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1966376217').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001834151925, -1001843351268').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '1966376217').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = environ.get('AUTH_CHANNEL', -1001687768591)
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://klaus:sai@cluster0.w1hv2ov.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001876764500'))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '-1001152304736').split()]
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', '𝓢𝓪𝓲')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', 'True')), False)
IMDB = is_enabled((environ.get('IMDB', 'True')), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', 'True')), False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "📂 <em>File Name</em>: <code>𝓚𝓵𝓪𝓾𝓼™|{file_name}</code> \n\n🖇 <em>File Size</em>: <code>{file_size}</code> </i>Join</i> [⚡️𝓢𝓪𝓲 𝓜𝓸𝓿𝓲𝓮𝓼](https://t.me/sai_movies_update)  \n\n🖥 <i>Requests</i> - ||@sai_movies27||")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", "📂 <em>File Name</em>: <code>𝓚𝓵𝓪𝓾𝓼™|{file_name}</code> \n\n🖇 <em>File Size</em>: <code>{file_size}</code> </i>Join</i> [⚡️𝓢𝓪𝓲 𝓜𝓸𝓿𝓲𝓮𝓼](https://t.me/sai_movies_update)  \n\n🖥 <i>Requests</i> - ||@sai_movies27||")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "🏷 𝖳𝗂𝗍𝗅𝖾: <a href={url}>{title}</a> \n🔮 𝖸𝖾𝖺𝗋: {year} \n⭐️ 𝖱𝖺𝗍𝗂𝗇𝗀𝗌: {rating}/ 10 \n🎭 𝖦𝖾𝗇𝖾𝗋𝗌: {genres} \n\n🎊 𝖯𝗈𝗐𝖾𝗋𝖾𝖽 𝖡𝗒 [𝓚𝓵𝓪𝓾𝓼™](https://t.me/sai_movies_update)")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "True")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

## EXTRA FEATURES ##

      # URL Shortener #

SHORTLINK_URL = environ.get('SHORTLINK_URL', 'shorturllink.in')
SHORTLINK_API = environ.get('SHORTLINK_API', 'b9936c4bb0e1902d055496919ce071291ec01626')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', True))
