‎import os
‎from telegram import Update
‎from telegram.ext import Application, CommandHandler, ContextTypes
‎
‎TOKEN = os.getenv("8762907720:AAHBjaUN6svqHL7OEk8Hx-IxxrOfnlu8tdA")
‎
‎async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
‎    await update.message.reply_text("🤖 PulseTread Bot is Live!")
‎
‎def main():
‎    app = Application.builder().token(TOKEN).build()
‎    app.add_handler(CommandHandler("start", start))
‎    app.run_polling()
‎
‎if __name__ == "__main__":
‎    main()
