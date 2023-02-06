# InspiroQuotes

An API using Inspiro AI quote generator.

## Installation

```Python
pip install InspiroQuotes
```

## Example

```Python
from InspiroQuotes import Quote

Q = Quote()

from pyrogram import filters, Client


pbot = Client("PyroBot", api_id="API_ID", api_hash="API_HASH", bot_token="TOKEN")


@pbot.on_message(filters.command("quote"))
async def sauce(_, message):

    quote_url = await Q.quote()
    return await message.reply_photo(photo=quote_url)

```
