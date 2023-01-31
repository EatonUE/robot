from telegram.ext import Updater, CommandHandler


USAGE = '/find <name> - find your EG account!'


def start(update, context):
  update.message.reply_text(USAGE)


def find(update, context):
  update.message.reply_text(f'服务器维护!')


def main():
  updater = Updater("5803318544:AAHPGk6sdocRXTmhk7oQQtO1uWJL4hx3u7o", use_context=True)
  dp = updater.dispatcher 

  # on different commands - answer in Telegram 
  dp.add_handler(CommandHandler("start", start)) 
  dp.add_handler(CommandHandler("find", find)) 

  # Start the Bot 
  updater.start_polling() 
  updater.idle() 


if __name__ == '__main__': 
  main()
