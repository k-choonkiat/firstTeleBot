# - *- coding: utf- 8 - *-

from telegram.ext import MessageHandler,Updater, CommandHandler,Filters, InlineQueryHandler
import requests
import re
#filter out non-command messages eg. random pieces of text 


#used for logging errors and error handling
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


def start(bot, update):
  update.message.reply_text("I'm a bot, Nice to meet you!")

def hi(bot, update):
    update.message.reply_text("I am a bot, please talk to me")


def convert_uppercase(bot, update):
  update.message.reply_text(update.message.text.upper())

#creating a function to an image
def get_url():
    # we can use https://random.dog/woof.json to get the json data and from there the url  
    contents = requests.get('https://random.dog/woof.json').json()
    # we can then use the url and then save it in a var
    url = contents['url']
    return url

def bop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def main():
  # Create Updater object and attach dispatcher to it
  updater = Updater('789556609:AAFsHzvLf-EY7iZZZt3FYFV-3x7avTBqCn8')
  # name for dispatcher
  dispatcher = updater.dispatcher
  print("Bot started")

  # Add command handler to dispatcher
  start_handler = CommandHandler('start',start)
  dispatcher.add_handler(start_handler)
  
  #handles hi
  hi_handler = CommandHandler('hi',hi)
  dispatcher.add_handler(hi_handler)

  #sends photo when doggo is asked for
  dispatcher.add_handler(CommandHandler('bop',bop))
  
  #message handler class is used to handle all non-command messages
  upper_case = MessageHandler(Filters.text, convert_uppercase)
  #here we just change message to upper_case
  dispatcher.add_handler(upper_case)



  # Start the bot
  updater.start_polling()

  # Run the bot until you press Ctrl-C
  updater.idle()

if __name__ == '__main__':
  main()
