from telethon.sync import TelegramClient, events
import re

api_id = '#############'
api_hash = '###########'
session = 'tele.session'

client = TelegramClient(session, api_id, api_hash)

# Listening Incoming Messages
@client.on(events.NewMessage)
async def handle_incoming_message(event):
    print(event.text)
    #
    #
    #

print("Listening for messages...")

with client:
    client.run_until_disconnected()
