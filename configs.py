# @ZonaKimochi Copyright
import os


class Config(object):
	API_ID = int(os.environ.get("API_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
	LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})
🕷️ **Owner Bot:** @Cinemaindo_Admin
👥 **Group:** (https://t.me/Diskusi_Cinemaindo)
📢 **Channel:** (https://t.me/CinemaIndoXXI)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Owner:** @Cinemaindo_admin
Bot ini dibuat khusus untuk menyimpan file dan mengubah nya menjadi link, jika ingin menyewa bot seperti ini hubungi owner.
[Donate Now](https://Trakteer.id/CinemaindoXXI/Tip)
"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\n.
Bot ini khusus untuk Download/Streaming Film Subtitle Indonesia, Official Bot of @CinemaindoXXI Nonton Film Subtitle Indonesia.
"""
