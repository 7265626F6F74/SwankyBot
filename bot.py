#!/usr/bin/python
__author__ = 'scarletfloppy'
# Imports
from telegram.ext import Updater, CommandHandler
from random import randint
import telegram, json, os.path, sys

# Variables
botfile = "/root/.ssh/token.json"
conf = "/root/bot/config.json"
tophats=[]
fedoras=[]
derps=[]

if os.path.isfile(botfile) == True: # Load in the swankybot.json config file from the container/host or exit if it doesn't exist
    with open(botfile) as file:
        botarr = json.load(file)
else:
    sys.exit(botfile + " file not found.")
    
if os.path.isfile(conf) == True: # Load in the conf.json config file from the repository or exit if it doesn't exist
    with open(conf) as file:
        config = json.load(file)
else:
    sys.exit(conf + " file not found.")

for tophat in config["tophats"]: # Load the values of the config file for tophats into an array
    tophats.append(str(tophat))
    
for fedora in config["fedoras"]: # Load the values of the config file for fedoras into an array
    fedoras.append(str(fedora))

for derp in config["derps"]: # Load the values of the config file for derps into an array
    derps.append(str(derp))

def sendImage(bot, update, dataval): # Funtion to send images or gifs the proper way
    val = dataval.rsplit('.', 1)[1]
    if val == 'gif':
        # Send a gif
        bot.sendDocument(chat_id=update.message.chat_id, document = dataval)
    elif val == 'webm':
        bot.sendMessage(chat_id=update.message.chat_id, text = "The item attempted to be sent is unsupported at the moment.")
    else:
        # Send a Picture
        bot.sendPhoto(chat_id=update.message.chat_id, photo=dataval)

def tophat(bot, update): # Method to send tophats for the event handler to call
    sendImage(bot, update, tophats[randint(0,len(tophats))])

def fedora(bot, update): # Method to send fedoras for the event handler to call
    sendImage(bot, update, fedoras[randint(0,len(fedoras))])

def derp(bot, update): # Method to send derps for the event handler to call
    sendImage(bot, update, derps[randint(0,len(derps))])

def start(bot, update): # Method to send start text that event handler calls
    bot.sendMessage(chat_id=update.message.chat_id, text = config["name"] + " running v" + str(config['version']))

def unknown(bot, update): # Method to send response for unknonwn entries that the event handler calls
    bot.sendMessage(chat_id=update.message.chat_id, text = "Don't try that again!")

def i(bot, update):
    chat=update.message.chat_id
    bot.sendMessage(chat_id=chat, text = "Chat ID: " + str(chat))

#Bot Start
updater    = Updater(token=str(botarr["token"]))
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('tophat', tophat))
dispatcher.add_handler(CommandHandler('fedora', fedora))
dispatcher.add_handler(CommandHandler('derp', derp))
dispatcher.add_handler(CommandHandler('start', start))
# Don't re-enable start
#dispatcher.addUnknownTelegramCommandHandler(unknown)
#telegram.Bot(token=tokenid).sendMessage(chat_id="-55491048", text="Hello World")
# Don't re-enable end
updater.start_polling()
