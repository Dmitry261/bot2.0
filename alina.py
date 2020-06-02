import telebot
import datetime as dt
import random

bot = telebot.TeleBot('895467971:AAHUMyfrv_gFzg8A09SAC1sIk7LxBuHZud0')

mood = ['отлично','хорошо','нормально','сойдет']
work = ['лежу','учусь','развиваюсь','развлекаюсь']
dish = ['картошка','курица','рыба','мясо']


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start, я новый бот Дмитрия Хадзугова. Пока что я могу ответить на маленькое количество сообщений.Вот примеры сообщений, на которые я точно отвечу. Как дела? Что делаешь? Я тебя люблю. Сколько время? Что приготовить?')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'как дела?':
        z = random.choice(mood)
        bot.send_message(message.chat.id, z)
    elif message.text.lower() == 'что делаешь?':
        m = random.choice(work)
        bot.send_message(message.chat.id, m)
    elif message.text.lower() == 'что приготовить?':
        l = random.choice(dish)
        bot.send_message(message.chat.id, l)
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAALl8F7WjppyoXbnlKKXqsCbe-ntfpv7AALrAwACfvLFDNJ65npPDkGSGgQ')
    elif message.text.lower() == 'сколько время?':
        bot.send_message(message.chat.id, dt.datetime.now())
    else:
        bot.send_message(message.chat.id, 'Жалко')



bot.polling()


