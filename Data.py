#CodeXBotz #mrismanaziz

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
coming Soon....
"""

    close = [
        [InlineKeyboardButton("🔒 Close", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("◀️ Back", callback_data="help"),
            InlineKeyboardButton("🔒 Close", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("😊 About me", callback_data="about"),
            InlineKeyboardButton("🔒 Close", callback_data="close")
        ],
    ]

    ABOUT = """
<b>@{} is a bot to save posts or files that can be accessed through a special link.</b>

  🤖 <b>Bot Re-Brand Available: <a href='https://t.me/Abhishekooo'>Contact me</a></b>
"""
    
