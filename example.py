from InspiroQuotes import Quote
from pyrogram import filters, Client
from pyrogram.types import Message

Q = Quote()
pbot = Client("PyroBot", api_id="API_ID", api_hash="API_HASH", bot_token="TOKEN")


@pbot.on_message(filters.command("quote"))
async def sauce(_, message: Message):
    quote_url = await Q.quote()
    return await message.reply_photo(photo=quote_url)


@pbot.on_message(filters.command("tquote"))
async def sauce(_, message: Message):
    text_quote = await Q.text_quote()
    return await message.reply_text(text_quote)
