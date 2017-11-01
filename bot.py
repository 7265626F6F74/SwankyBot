#!/usr/bin/python
__author__ = '7265626F6F74'
# Imports
from telegram.ext import Updater, CommandHandler
from random import randint
import telegram, json, os.path, sys

# Variables
conf = "/bot/SwankyBot-master/config.json" # This file contains the configuration values used within this bot. The /root folder is used because this bot is designed to run in an alpine container.
tophats=[]
fedoras=[]
derps=[]
memes=[]

if ((len(sys.argv) == 2) and (len(sys.argv[1]) > 1) and (str(sys.argv[1:]) != 'null')):
    token = str(sys.argv[1])
else:
    print "Error: No Token Provided. Quitting!"
    sys.exit()

if os.path.isfile(conf) == True: # Load in the conf.json config file from the repository or exit if it doesn't exist
    with open(conf) as file:
        config = json.load(file)
else:
    sys.exit(conf + " file not found.")

for tophat in config["tophats"]: # Load the tophats array values from the config file into an array for python
    tophats.append(str(tophat))

for fedora in config["fedoras"]: # Load the fedoras array values from the config file into an array for python
    fedoras.append(str(fedora))

for derp in config["derps"]: # Load the derps array values from the config file into an array for python
    derps.append(str(derp))

for meme in config["memes"]: # Load the memes array values from the config file into an array for python
    memes.append(str(meme))

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

def meme(bot, update): # Method to send memes for the event handler to call
    if memes:
        sendImage(bot, update, memes[randint(0,len(memes))])
    else:
        bot.sendMessage(chat_id=update.message.chat_id, text = "The / memes handler has been created, but no memes have been added. To request adding a meme, please let the bot owner know. @ScarletFloppy will add the meme to the bot.")

def start(bot, update): # Method to send start text that event handler calls
    bot.sendMessage(chat_id=update.message.chat_id, text = config["name"] + " running v" + str(config['version']))

def unknown(bot, update): # Method to send response for unknonwn entries that the event handler calls
    bot.sendMessage(chat_id=update.message.chat_id, text = "Don't try that again!")

def i(bot, update):
    chat=update.message.chat_id
    bot.sendMessage(chat_id=chat, text = "Chat ID: " + str(chat))

#Bot Start
updater    = Updater(token=token)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('tophat', tophat))
dispatcher.add_handler(CommandHandler('fedora', fedora))
dispatcher.add_handler(CommandHandler('derp', derp))
dispatcher.add_handler(CommandHandler('meme', meme))
dispatcher.add_handler(CommandHandler('i', i))
dispatcher.add_handler(CommandHandler('start', start))
# Don't re-enable start
#dispatcher.addUnknownTelegramCommandHandler(unknown)
#telegram.Bot(token=tokenid).sendMessage(chat_id="", text="Hello World")
# Don't re-enable end
updater.start_polling()
