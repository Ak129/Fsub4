#CodeXBotz #mrismanaziz

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
coming Soon....
"""

    close = [
        [InlineKeyboardButton("Tutup", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("Bantuan", callback_data="help"),
            InlineKeyboardButton("Tutup", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("Tentang", callback_data="about"),
            InlineKeyboardButton("Tutup", callback_data="close")
        ],
    ]

    ABOUT = """
<b>@{} is a bot to save posts or files that can be accessed through a special link.</b>

  🤖 <b>Bot Re-Brand Available: <a href='https://t.me/Abhishekooo'>Contact me</a></b>
  🌹 <b>Channels: <a>@OpMods4u @ApkThugs @AiplexMods</a></b>
"""
