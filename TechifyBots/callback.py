from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from Script import text
from config import ADMIN

@Client.on_callback_query()
async def callback_query_handler(client, query: CallbackQuery):
    if query.data == "start":
        await query.message.edit_caption(
            caption=text.START.format(query.from_user.mention),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('⇆ 𝖠𝖽𝖽 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉 ⇆', url=f"https://telegram.me/QuickAcceptBot?startgroup=true&admin=invite_users")],
                [InlineKeyboardButton('ℹ️ 𝖠𝖻𝗈𝗎𝗍', callback_data='about'),
                 InlineKeyboardButton('📚 𝖧𝖾𝗅𝗉', callback_data='help')],
                [InlineKeyboardButton('⇆ 𝖠𝖽𝖽 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 ⇆', url=f"https://telegram.me/QuickAcceptBot?startchannel=true&admin=invite_users")]
            ])
        )

    elif query.data == "help":
        await query.message.edit_caption(
            caption=text.HELP.format(query.from_user.mention),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('📢 𝘊𝘩𝘢𝘯𝘯𝘦𝘭', url='https://telegram.me/cinemagram_links'),
                 InlineKeyboardButton('💬 𝘚𝘶𝘱𝘱𝘰𝘳𝘵', url='https://telegram.me/CMG_4dmin')],
                [InlineKeyboardButton('↩️ 𝘉𝘢𝘤𝘬', callback_data="start"),
                 InlineKeyboardButton('❌ 𝘊𝘭𝘰𝘴𝘦', callback_data="close")]
            ])
        )

    elif query.data == "about":
        await query.message.edit_caption(
            caption=text.ABOUT,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('👨‍💻 𝘋𝘦𝘷𝘦𝘭𝘰𝘱𝘦𝘳 👨‍💻', url='https://telegram.me/CMG_4dmin')],
                [InlineKeyboardButton("↩️ 𝘉𝘢𝘤𝘬", callback_data="start"),
                 InlineKeyboardButton("❌ 𝘊𝘭𝘰𝘴𝘦", callback_data="close")]
            ])
        )

    elif query.data == "close":
        await query.message.delete()
