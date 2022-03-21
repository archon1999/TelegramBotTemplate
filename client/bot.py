from telebot import TeleBot

import config
import commands
import handlers
from call_types import CallTypes

from backend.models import BotUser


message_handlers = {
    '/start': commands.start_command_handler,
}

key_handlers = {

}

state_handlers = {

}

bot = TeleBot(
    token=config.TOKEN,
    num_threads=3,
    parse_mode='HTML',
)


def create_user(message) -> BotUser:
    return BotUser.objects.create(
        chat_id=message.chat.id,
        first_name=message.chat.first_name,
        last_name=message.chat.last_name,
        username_name=message.chat.username,
    )


@bot.message_handler
def message_handler(message):
    chat_id = message.chat.id
    if not BotUser.objects.filter(chat_id=chat_id).exists():
        create_user(message)

    user = BotUser.objects.get(chat_id=chat_id)
    if user.bot_state:
        state_handlers[user.bot_state](bot, message)

    for text, handler in message_handlers.items():
        if message.text == text:
            handler(bot, message)
            break

    for key, handler in key_handlers.items():
        if message.text in key.getall():
            handler(bot, message)
            break


callback_query_handlers = {
    CallTypes.Language: handlers.language_call_query_handler,
}


@bot.callback_query_handler(func=lambda call: True)
def callback_query_handler(call):
    call_type = CallTypes.parse_data(call.data)
    for CallType, handler in callback_query_handlers.items():
        if CallType == call_type.__class__:
            handler(bot, call)
            break


if __name__ == "__main__":
    # bot.polling()
    bot.infinity_polling()
