import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message when the /start command is issued."""
    user_first_name = update.effective_user.first_name if update.effective_user else "there"
    await update.message.reply_text(
        f"Hello, {user_first_name}! I am Raw Data Bot. Use /help to see available commands."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a help message when the /help command is issued."""
    help_text = (
        "*Available commands:*
"        "/start - Start interaction with the bot
"        "/help - Show this help message"
    )
    await update.message.reply_markdown_v2(help_text)

async def main() -> None:
    token = os.getenv("BOT_TOKEN")
    if not token:
        logger.error("BOT_TOKEN environment variable not set")
        raise RuntimeError("BOT_TOKEN environment variable not set")

    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    logger.info("Bot started. Listening for updates...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
