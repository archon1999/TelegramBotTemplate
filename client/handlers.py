from telebot import TeleBot

from call_types import CallTypes


def language_callback_query_handler(bot: TeleBot, call):
    call_type = CallTypes.parse_data(call.data)
    lang = call_type.lang
