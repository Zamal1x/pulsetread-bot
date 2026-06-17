‎from telegram import Update
‎from telegram.ext import Application, CommandHandler, ContextTypes
‎
‎TOKEN = "8762907720:AAG_BkZvBdL7SLt2OpgWufWtubrqNnulGUg"
‎
‎async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
‎    await update.message.reply_text(
‎        "🤖 Welcome to PulseTread AI\n\n📊 Bot is Online!"
‎    )
‎
‎app = Application.builder().token(TOKEN).build()
‎
‎app.add_handler(CommandHandler("start", start))
‎
‎app.run_polling()
