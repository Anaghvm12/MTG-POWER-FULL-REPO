"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter

# -- Constants -- #
ALIVE = "വെറുതെ Alive അടിച്ചു വെറുപ്പിക്കാതട ഞൻ ഇവട ജീവനോടെ ഒക്കെ തന്നെ ണ്ട് MANH ചത്തൊന്നും പോയിട്ടില്ല🥲\n\n ⍟𝐌𝐲 𝐜𝐫𝐞𝐚𝐭𝐨𝐫: @MagnusTG\n\n⍟𝐌𝐲 𝐬𝐮𝐩𝐩𝐨𝐫𝐭: @cinemahubmoviesS\n\n⍟𝐌𝐲 𝐮𝐩𝐝𝐚𝐭𝐞𝐬: @NewOTTmoviesAll\n\n⍟𝐌𝐲 𝐬𝐮𝐩𝐩𝐨𝐫𝐭𝐞𝐫: @MagnusTG"
HELP = "InlineKeyboardButton('ᴀᴅᴍɪɴ', callback_data='admin'),
        InlineKeyboardButton('ᴄᴏɴɴᴇᴄᴛ', callback_data='coct'),
        InlineKeyboardButton('ғɪʟᴛᴇʀ', callback_data='auto_manual')
        ],[
        InlineKeyboardButton('ɢᴛʀᴀɴs', callback_data='gtrans'),
        InlineKeyboardButton('ɪɴғᴏ', callback_data='info'),
        InlineKeyboardButton('ᴘᴀsᴛᴇ', callback_data='paste')
        ],[
        InlineKeyboardButton('ᴘᴜʀɢᴇ', callback_data='purge'),
        InlineKeyboardButton('ʀᴇsᴛʀɪᴄᴛ', callback_data='restric'),
        InlineKeyboardButton('sᴇᴀʀᴄʜ', callback_data='search')
       ],[
       InlineKeyboardButton('ᴛɢʀᴀᴘʜ', callback_data='tgraph'),
       InlineKeyboardButton('ᴡʜᴏɪs', callback_data='whois'),
       InlineKeyboardButton('ғᴜɴ', callback_data='fun')
       ],[
       InlineKeyboardButton('ᴀʟɪᴠᴇ', callback_data='alive'),
       InlineKeyboardButton('sᴏɴɢ', callback_data='song'),
       InlineKeyboardButton('ᴊsᴏɴ', callback_data='json')
       ],[
       InlineKeyboardButton('ᴘɪɴ', callback_data='pin'),
       InlineKeyboardButton('ᴄᴏʀᴏɴᴀ', callback_data='corona'),
       InlineKeyboardButton('sᴛɪᴄᴋᴇʀ', callback_data='stickerid')
       ],[
       InlineKeyboardButton('ᴛᴛꜱ', callback_data='ttss'),          
       InlineKeyboardButton('yᴛ-ᴛʜᴜᴍʙ', callback_data='ytthumb'),            
       InlineKeyboardButton('ᴜʀʟ-sʜᴏʀᴛ', callback_data='urlshort')
       ],[
       InlineKeyboardButton('ʀᴇᴩᴏʀᴛ', callback_data='report'),
       InlineKeyboardButton("ᴠɪᴅᴇᴏ", callback_data='video'),
       InlineKeyboardButton("ɢɪᴛʜᴜʙ", callback_data='github')
       ],[
       InlineKeyboardButton('ᴋɪᴄᴋ', callback_data='zombies'),
       InlineKeyboardButton('ᴍᴜᴛᴇ', callback_data='restric'),
       InlineKeyboardButton('ᴀᴜᴅɪᴏ-ʙᴏᴏᴋ', callback_data='abook')
       ],[
       InlineKeyboardButton('sᴏᴜʀᴄᴇ', callback_data='source'),
       InlineKeyboardButton('ꜰɪʟᴇ-ꜱᴛᴏʀᴇ', callback_data='newdata'),
       InlineKeyboardButton("ɪᴍᴀɢᴇ", callback_data='image')
       ],[
       InlineKeyboardButton('⬅️ ʙᴀᴄᴋ', callback_data='start'),
       InlineKeyboardButton('sᴛᴀᴛᴜs 🔰', callback_data='stats'),
       InlineKeyboardButton('ᴄʟᴏsᴇ ⛔', callback_data='close_data')"
REPO = "നമ്മൾ നമ്മൾ പോലുമറിയാതെ അധോലോകം ആയി മാറിക്കഴിഞ്ഞിരിക്കുന്നു ഷാജിയേട്ടാ..."
# -- Constants End -- #


@Client.on_message(filters.command("alive", COMMAND_HAND_LER) & f_onw_fliter)
async def check_alive(_, message):
    await message.reply_text(ALIVE)


@Client.on_message(filters.command("help", COMMAND_HAND_LER) & f_onw_fliter)
async def help_me(_, message):
    await message.reply_text(HELP)


@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")


@Client.on_message(filters.command("repo", COMMAND_HAND_LER) & f_onw_fliter)
async def repo(_, message):
    await message.reply_text(REPO)
