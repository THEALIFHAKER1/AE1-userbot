# Copyright (C) 2021 AE1 ENTERTAINMENT.

""" AE1-USERBOT starting point """

from importlib import import_module
import os

from telethon.errors.rpcerrorlist import PhoneNumberInvalidError

from ae1-userbot import LOGS, bot
from ae1-userbot.modules import ALL_MODULES

INVALID_PH = '\nERROR: The phone no. entered is incorrect' \
             '\n  Tip: Use country code (eg +60) along with num.' \
             '\n       Recheck your phone number'

try:
    bot.start()
except PhoneNumberInvalidError:
    print(INVALID_PH)
    exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

LOGS.info("AE1-USERBOT is alive now go fuck yourself."
          " Should you need assistance, head to https://t.me/THEALIFHAKER1_REDIRECT")
LOGS.info("Your bot version is v1.0.")

SEM_TEST = os.environ.get("SEMAPHORE", None)
if SEM_TEST:
    bot.disconnect()
else:
    bot.run_until_disconnected()
