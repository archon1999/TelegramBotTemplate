from telebot import TeleBot, types

from backend.templates import Messages, Smiles, Keys
from backend.models import BotUser

import utils
from call_types import CallTypes


def start_command_handler(bot: TeleBot, message):
    chat_id = message.chat.id
    for text in Messages.START_COMMAND.getall():
        bot.send_message(chat_id, text)
