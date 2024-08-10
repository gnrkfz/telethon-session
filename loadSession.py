from telethon.sync import TelegramClient, events
import re

api_id = '###'
api_hash = '######'
session = '###.session'

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
