import telebot
from bot_logic import gen_pass, gen_emodji, timers, flip_coin, jokes  # Импортируем функции из bot_logic


# Замени 'TOKEN' на токен твоего бота
bot = telebot.TeleBot("token")

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Какую команду вы выберете? /hello, /bye, /pass, /emodji, /jokes, /coin, /timers")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['pass'])
def send_password(message):
    password = gen_pass(10)  # Устанавливаем длину пароля, например, 10 символов
    bot.reply_to(message, f"Вот твой сгенерированный пароль: {password}")

@bot.message_handler(commands=['emodji'])
def send_emodji(message):
    emodji = gen_emodji()
    bot.reply_to(message, f"Вот эмоджи': {emodji}")

@bot.message_handler(commands=['coin'])
def send_coin(message):
    coin = flip_coin()
    bot.reply_to(message, f"Монетка выпала так: {coin}")

@bot.message_handler(commands=['jokes'])
def send_jokes(message):
    joke = jokes()
    bot.reply_to(message, f"Шутка: {joke}")   

@bot.message_handler(commands=['timers'])
def send_timers(message):
    timer = timers()
    bot.reply_to(message, f"Время: {timer}")  

# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)

@bot.message_handler(commands=["ping"])
def on_ping(message):
    bot.reply_to(message, "Понг!")

@bot.message_handler(commands=["poll"])
def create_poll(message):
    bot.send_message(message.chat.id, "Мнение")
    answer_options = ["да", "нет", "ДА", "-"]

    bot.send_poll(
        chat_id=message.chat.id,
        question="Вам нравится кодланд?",
        options=answer_options,
        type="quiz",
        correct_option_id=2,
        is_anonymous=False,
    )

@bot.poll_answer_handler()
def handle_poll(poll):
    # This handler can be used to log User answers and to send next poll
    pass

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

# Запускаем бота
bot.polling()
