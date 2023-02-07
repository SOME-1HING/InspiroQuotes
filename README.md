# InspiroQuotes

An API using Inspiro AI quote generator.

## Installation

```Python
pip install InspiroQuotes
```

## Example

- For General Purpose

```Python
from InspiroQuotes import Quote

Q = Quote()

img_link1 = Q.quote()
img_link2 = Q.img_quote()
text_quote = Q.text_quote()

print(img_link1)
print(img_link2)
print(text_quote)

```

- For Telegram

```Python
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

```
