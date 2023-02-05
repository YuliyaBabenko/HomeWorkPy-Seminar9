from bot_commands import *
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

app = ApplicationBuilder().token("5972795135:AAGG4gLu7GBnOF2xSAeiqm6mvYpx4LkNwS4").build()

app.add_handler(CommandHandler('hi', hi_command))
app.add_handler(CommandHandler('time', time_command))
app.add_handler(CommandHandler('help', help_command))
app.add_handler(CommandHandler('sum', sum_command))


print('server start')
app.run_polling()
