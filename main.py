from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import asyncio

TOKEN = "PASTE_YOUR_TOKEN_HERE"  # Replace this

products = [
    {"name": "Alien Hoodie", "price": "$49", "desc": "🔥 Limited edition alien drip"},
    {"name": "Nebula Mug", "price": "$19", "desc": "☕ Space fuel container"},
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(p["name"], callback_data=str(i))] for i, p in enumerate(products)
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome to Arenabazzar 👽🔥\nCheck out our products:", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    p = products[int(query.data)]
    await query.edit_message_text(text=f"{p['name']} - {p['price']}\n{p['desc']}")

async def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
