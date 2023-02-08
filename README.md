<!-- markdownlint-disable MD024 -->

# InspiroQuotes

An API using Inspiro AI quote generator.

## Installation / Upgrade

### Windows

```shell
py -m pip install --upgrade InspiroQuotes
```

### MacOS/Unix

```shell
python3 -m pip install --upgrade InspiroQuotes
```

### Dependency

Add `InspiroQuotes` in `requirements.txt`.

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

# Changelog

All notable changes to the `InspiroQuotes` project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)

## [Unreleased]

### Added

- `changelog.md` in `root directory`.

### Changed

- `img_link2 = Q.quote()` to `img_link2 = Q.img_quote()` in `README.md`.
  
### Fixed

- Function name of both `sauce` in `/example.py` to `img_quote` and `text_quote` respectively.

## [1.0.2] - 2022-02-08

### Added

- Function `img_quote` in `/InspiroQuotes/__main__.py`.
- Function `text_quote` in `/InspiroQuotes/__main__.py`.
- More simple `print` statement in `test.py`.
- New function in `/example.py` that works for command `/tquote` and sends text quotes.

### Changed

- `__version__` from `1.0.1` to `1.0.2` in `/InspiroQuotes/__init__.py`.
- `/example.py`
- `README.md` and added more information.

## [1.0.1] - 2022-02-07

### Added

- `__init__.py` in `/InspiroQuotes/`.
- `test` in `root directory`.
- `__init__.py` in `/test/`.
- `test.py` in `/test/`.
- Simple `print` statement in `test.py`.
- `example.py` in `root directory`.
- `README.md` in `root directory`.
- `setup.py` in `root directory`.

### Changed

- `__version__` from `1.0.0` to `1.0.1` in `/InspiroQuotes/__init__.py`.

## [1.0.0] - 2022-02-06

### Added

- Class `Quote` in `__main__.py`.
- Function `quote` in Class `Quote`.
- Package `requests` dependency in `requirements.txt`.

## Commitment

- [Unreleased](https://github.com/SOME-1HING/InspiroQuotes/compare/v1.0.2...HEAD)
- [1.0.2](https://github.com/SOME-1HING/InspiroQuotes/compare/v1.0.1...v1.0.2)
- [1.0.1](https://github.com/SOME-1HING/InspiroQuotes/tree/v1.0.1)
