from Adarsh.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
import time
import shutil, psutil
from utils_bot import *
from Adarsh import StartTime


START_TEXT = """ Your Telegram DC Is : `{}`  """


@StreamBot.on_message(filters.regex("😎Mᴀɪɴᴛᴀɪɴᴇʀs"))
async def maintainers(b,m):
    try:
       await b.send_message(chat_id=m.chat.id,text="HELLO",quote=True)
    except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="I am Made By [Archie Bots ](https://t.me/Archie_Bots)",
                    
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("Owner💻", url=f"https://t.me/Archie_Bots")
                            ]
                        ]
                    ),
                    
                    disable_web_page_preview=True)
            
         
@StreamBot.on_message(filters.regex("Sᴜʙsᴄʀɪʙᴇ ❤️"))
async def follow_user(b,m):
    try:
       await b.send_message(chat_id=m.chat.id,text="HELLO",quote=True)
    except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<B>HERE'S THE SUBSCRIBE LINK</B>",
                    
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("Subscribe ❤️", url=f"https://t.me/Archie_Bots")
                            ]
                        ]
                    ),
                    
                    disable_web_page_preview=True)
        

@StreamBot.on_message(filters.regex("DC"))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.dc_id)
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        quote=True
    )
    
    
@StreamBot.on_message(filters.regex("📡 Pɪɴɢ"))
async def ping(b, m):
    start_t = time.time()
    ag = await m.reply_text("....")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await ag.edit(f"Pɪɴɢ!\n{time_taken_s:.3f} ms")
    
    
    
    
@StreamBot.on_message(filters.private & filters.regex("📊 Sᴛᴀᴛᴜs"))
async def stats(bot, update):
  currentTime = readable_time((time.time() - StartTime))
  total, used, free = shutil.disk_usage('.')
  total = get_readable_file_size(total)
  used = get_readable_file_size(used)
  free = get_readable_file_size(free)
  sent = get_readable_file_size(psutil.net_io_counters().bytes_sent)
  recv = get_readable_file_size(psutil.net_io_counters().bytes_recv)
  cpuUsage = psutil.cpu_percent(interval=0.5)
  memory = psutil.virtual_memory().percent
  disk = psutil.disk_usage('/').percent
  botstats = f'<b>Bot Uptime:</b> {currentTime}\n' \
            f'<b>Total disk space:</b> {total}\n' \
            f'<b>Used:</b> {used}  ' \
            f'<b>Free:</b> {free}\n\n' \
            f'📊Data Usage📊\n<b>Upload:</b> {sent}\n' \
            f'<b>Down:</b> {recv}\n\n' \
            f'<b>CPU:</b> {cpuUsage}% ' \
            f'<b>RAM:</b> {memory}% ' \
            f'<b>Disk:</b> {disk}%'
  await update.reply_text(botstats)
