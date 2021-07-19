from telegram.ext import Updater, MessageHandler,Filters
from Adafruit_IO import Client

aio = Client('adeebsheriff', 'aio_pGHz18TwT4XW2N3qleIxIOscChBV')

def demo1(bot,update):
  chat_id = bot.message.chat_id
  path = 'https://cdn3.vectorstock.com/i/1000x1000/87/22/i-am-fine-lettering-typography-calligraphy-overlay-vector-15208722.jpg'
  bot.message.reply_text('I am fine')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
def demo2(bot,update):
  chat_id = bot.message.chat_id
  path = 'https://static.scientificamerican.com/sciam/cache/file/2B38DE31-C1D3-4339-8808D61972976EE4.jpg'
  bot.message.reply_text('LIGHT is turned ON')
  aio.send('bedroom-light', 1)
  data1 = aio.receive('bedroom-light')
  print(f'Received value: {data1.value}')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
def demo3(bot,update):
  chat_id = bot.message.chat_id
  path = 'https://image.shutterstock.com/image-photo/light-bulb-turned-off-over-260nw-320485652.jpg'
  bot.message.reply_text('LIGHT is turned OFF')
  aio.send('bedroom-light', 0)
  data1 = aio.receive('bedroom-light')
  print(f'Received value: {data1.value}')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
def demo4(bot,update):
  chat_id = bot.message.chat_id
  path = 'https://cdn.frontdoorhome.com/ahs/blog/prod/static/cs/ahs/image/running-fan.jpg'
  bot.message.reply_text('FAN is turned ON')
  aio.send('bedroom-fan', 1)
  data2 = aio.receive('bedroom-fan')
  print(f'Received value: {data2.value}')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
def demo5(bot,update):
  chat_id = bot.message.chat_id
  path = 'https://www.destinationlighting.com/fliptheswitch/wp-content/uploads/sites/2/2018/05/zudio-casablanca.jpg'
  bot.message.reply_text('FAN is turned OFF')
  aio.send('bedroom-fan', 0)
  data2 = aio.receive('bedroom-fan')
  print(f'Received value: {data2.value}')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
def main(bot,update):
  a = bot.message.text.lower()
  print(a)

  if a == "how are you?":
    demo1(bot,update)
  elif a =="light on" or a=="turn on light":
    demo2(bot,update)
  elif a =="light off" or a=="turn off light":
    demo3(bot,update)
  elif a =="switch on the fan" or a=="turn on fan":
    demo4(bot,update)
  elif a =="switch of the fan" or a=="turn off fan":
    demo5(bot,update)
  else:
    bot.message.reply_text('Invalid Text')
BOT_TOKEN = '1902516606:AAEsExBqBph2OyXxMBNGShsIOX2zmZrtdKU'
u = Updater(BOT_TOKEN,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()
