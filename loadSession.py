from telethon.sync import TelegramClient, events
import re

api_id = '21346711'
api_hash = 'fd9a5c2d2d8cde393adaab0dfcc9d300'
session = '6285156393610.session'

client = TelegramClient(session, api_id, api_hash)

@client.on(events.NewMessage)
async def handle_incoming_message(event):
    print(event.text)
    # otp = re.search(r'\b(\d{5})\b', event.raw_text)
    # if otp:
    #     print("OTP : ", otp.group(0))

print("Listening for messages...")

with client:
    client.run_until_disconnected()