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
@{} adalah Bot untuk menyimpan postingan atau file yang dapat diakses melalui link khusus.

  Framework: <a href='https://docs.pyrogram.org'>Pyrogram</a>
  Re-Code From: <a href='https://github.com/mrismanaziz/File-Sharing-Man'>File-Sharing-Man</a>
"""
