import random
from pyrogram import Client, filters, enums
from pyrogram.errors import *
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from config import *
import asyncio
from Script import text
from .db import tb
from .fsub import get_fsub

@Client.on_message(filters.command("start"))
async def start_cmd(client, message):
    if await tb.get_user(message.from_user.id) is None:
        await tb.add_user(message.from_user.id, message.from_user.first_name)
        bot = await client.get_me()
        await client.send_message(
            LOG_CHANNEL,
            text.LOG.format(
                message.from_user.id,
                getattr(message.from_user, "dc_id", "N/A"),
                message.from_user.first_name or "N/A",
                f"@{message.from_user.username}" if message.from_user.username else "N/A",
                bot.username
            )
        )
    if IS_FSUB and not await get_fsub(client, message): return
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=text.START.format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton('⇆ 𝖠𝖽𝖽 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉 ⇆', url=f"https://telegram.me/CMG_AutoApproverBot?startgroup=true&admin=invite_users")],
            [InlineKeyboardButton('ℹ️ 𝖠𝖻𝗈𝗎𝗍', callback_data='about'),
             InlineKeyboardButton('📚 𝖧𝖾𝗅𝗉', callback_data='help')],
            [InlineKeyboardButton('⇆ 𝖠𝖽𝖽 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 ⇆', url=f"https://telegram.me/CMG_AutoApproverBot?startchannel=true&admin=invite_users")]
            ])
        )

@Client.on_message(filters.command("help") & filters.private)
async def help_cmd(client, message):
    reply = await message.reply(
        text=("<b>❓ 𝘏𝘢𝘷𝘪𝘯𝘨 𝘛𝘳𝘰𝘶𝘣𝘭𝘦?\n\n𝘐𝘧 𝘺𝘰𝘶'𝘳𝘦 𝘧𝘢𝘤𝘪𝘯𝘨 𝘢𝘯𝘺 𝘱𝘳𝘰𝘣𝘭𝘦𝘮 𝘸𝘩𝘪𝘭𝘦 𝘶𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘣𝘰𝘵 𝘰𝘳 𝘪𝘵𝘴 𝘤𝘰𝘮𝘮𝘢𝘯𝘥𝘴, 𝘱𝘭𝘦𝘢𝘴𝘦 𝘮𝘦𝘴𝘴𝘢𝘨𝘦 𝘵𝘩𝘦 𝘢𝘥𝘮𝘪𝘯..</b>"
        ),
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("⚜️ 𝘊𝘰𝘯𝘵𝘢𝘤𝘵 𝘈𝘥𝘮𝘪𝘯 ⚜️", url="https://telegram.me/CMG_4dmin")]
        ])
    )
    await asyncio.sleep(300)
    await reply.delete()
    try:
        await message.delete()
    except:
        pass

@Client.on_message(filters.command('accept') & filters.private)
async def accept(client, message):
    show = await message.reply("**Please Wait.....**")
    user_data = await tb.get_session(message.from_user.id)
    if user_data is None:
        return await show.edit("**To accept join requests, please /login first.**")
    try:
        acc = Client("joinrequest", session_string=user_data, api_id=API_ID, api_hash=API_HASH)
        await acc.connect()
    except:
        return await show.edit("**Your login session has expired. Use /logout first, then /login again.**")
    await show.edit("**Forward a message from your Channel or Group (with forward tag).\n\nMake sure your logged-in account is an admin there with full rights.**")
    fwd_msg = await client.listen(message.chat.id)
    if fwd_msg.forward_from_chat and fwd_msg.forward_from_chat.type not in [enums.ChatType.PRIVATE, enums.ChatType.BOT]:
        chat_id = fwd_msg.forward_from_chat.id
        try:
            info = await acc.get_chat(chat_id)
        except:
            return await show.edit("**Error: Ensure your account is admin in this Channel/Group with required rights.**")
    else:
        return await message.reply("**Message not forwarded from a valid Channel/Group.**")
    await fwd_msg.delete()
    msg = await show.edit("**Accepting all join requests... Please wait.**")
    try:
        while True:
            await acc.approve_all_chat_join_requests(chat_id)
            await asyncio.sleep(1)
            join_requests = [req async for req in acc.get_chat_join_requests(chat_id)]
            if not join_requests:
                break
        await msg.edit("**✅ Successfully accepted all join requests.**")
    except Exception as e:
        await msg.edit(f"**An error occurred:** `{str(e)}`")

@Client.on_chat_join_request()
async def approve_new(client, m):
    if not NEW_REQ_MODE:
        return
    try:
        await client.approve_chat_join_request(m.chat.id, m.from_user.id)
        try:
            await client.send_message(
                m.from_user.id,
                f"𝘏𝘪𝘪 {m.from_user.mention} 👋,\n\𝘯𝘠𝘰𝘶𝘳 𝘙𝘦𝘲𝘶𝘦𝘴𝘵 𝘵𝘰 𝘑𝘰𝘪𝘯 {m.chat.title} 𝘏𝘢𝘴 𝘉𝘦𝘦𝘯 𝘈𝘤𝘤𝘦𝘱𝘵𝘦𝘥.\𝘯\𝘯𝘊𝘭𝘪𝘤𝘬 /Start 𝘵𝘰 𝘜𝘴𝘦 𝘔𝘦 𝘪𝘯 𝘠𝘰𝘶𝘳 𝘊𝘩𝘢𝘯𝘯𝘦𝘭 𝘰𝘳 𝘎𝘳𝘰𝘶𝘱."
            )
        except:
            pass
    except Exception as e:
        print(str(e))
        pass
