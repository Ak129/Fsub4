#CodeXBotz #mrismanaziz

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
Coming Soon....
"""

    close = [
        [InlineKeyboardButton("🔒 Close", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("🔥Trending App", callback_data="help"),
            InlineKeyboardButton("🔒 Close", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("😊 About Me", callback_data="about"),
            InlineKeyboardButton("🔒 Close", callback_data="close")
        ],
    ]

    ABOUT = """
"<b>○ Creator : <a href='https://t.me/Abhishekooo'>This Person</a>\n○ Language : <code>Python3</code>\n○ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a></b"""
    
