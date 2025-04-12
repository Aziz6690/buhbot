import telebot
import os
import openai

# Получаем токены
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Настройка OpenAI
openai.api_key = OPENAI_API_KEY

# Инициализация Telegram бота
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Ты бухгалтер из Казахстана. Помогаешь считать налоги, расходы, объясняешь термины простыми словами."},
                {"role": "user", "content": message.text}
            ],
            temperature=0.3
        )
        reply = response.choices[0].message["content"]
        bot.send_message(message.chat.id, reply)

    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка: {e}")

bot.polling()
