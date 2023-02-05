from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import *

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(f'Hello, my dear {update.effective_user.first_name}! I\'ve been waiting fo you!')

async def help_command(update: Update, context: CallbackContext):
    log(update, context)
    await update.message.reply_text(f'/hi\n/time\n/help')


async def time_command(update: Update, context: CallbackContext):
    log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')


async def count_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    await update.message.reply_text(f'Your result is {eval(msg.split(" ")[1])}')
