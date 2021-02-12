import logging
import asyncio
from telethon import TelegramClient, events, Button
from decouple import config
from telethon.tl.functions.users import GetFullUserRequest

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.INFO)

# start the bot
print("Starting...")
try:
    apiid = config("APP_ID", cast=int)
    apihash = config("API_HASH")
    bottoken = config("BOT_TOKEN")
    frm = config("FROM_CHANNEL", cast=int)
    tochnl = config("TO_CHANNEL", cast=int)
    tochnl2 =config("TO_CHANNEL2",cast=int)
    datgbot = TelegramClient('bot', apiid, apihash).start(bot_token=bottoken)
except:
    print("Environment vars are missing! Kindly recheck.")
    print("Bot is quiting...")
    exit()


@datgbot.on(events.NewMessage(pattern="/start"))
async def _(event):
    ok = await datgbot(GetFullUserRequest(event.sender_id))
    await event.reply(f"𝙷𝚎 𝚑𝚎`{ok.user.first_name}`!\n\n𝙸 𝚊𝚖 𝚊 𝙲𝚑𝚊𝚗𝚗𝚕𝚎 𝙿𝚘𝚜𝚝𝚎𝚛 𝚋𝚘𝚝. \n 𝙿𝚛𝚎𝚜𝚜 /help 𝚝𝚘 𝚐𝚎𝚝 𝚒𝚗𝚏𝚘 \nI can be used in only two channels (one user) at a time..\n[🤘](https://telegra.ph/file/1eca514b5e6202b1d92b3.jpg)", 
    buttons = [[Button.url("🤝Main Group🛰️", url="t.me/danuma01"), Button.url("📝Bot News🛸", url="https://t.me/Dbotai")],[Button.url("✈️Developer✈️", url="https://lasiya.ml"),Button.url("🤙 Contact Dev 🛶", url="https://t.me/Danuma_admin_bot")]],link_preview=True)


@datgbot.on(events.NewMessage(pattern="/help"))
async def helpp(event):
    await event.reply("**Help**\n\nThis bot will send all new posts in one channel to the other channel (without forwarded tag).\nIt can be used only in two channels at a time, \n\nAdd me to both the channels and make me an admin in both, and all new messages would be autoposted on the linked channel!\n\nLiked the bot? Drop a ♥Danuma projectject")

@datgbot.on(events.NewMessage(incoming=True, chats=frm)) 
async def _(event): 
    if not event.is_private:
        try:
            await event.client.send_message(tochnl,tochnl2,event.message)
        except:
            print("TO_CHANNEL ID is wrong or I can't send messages there (make me admin).")


print("Bot has started.")
print("Visit @Danuma01")
datgbot.run_until_disconnected()
