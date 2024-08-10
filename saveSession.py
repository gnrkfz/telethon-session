from telethon.sync import TelegramClient

api_id = '###'
api_hash = '######'

with TelegramClient('sesi1.session', api_id, api_hash) as client:
    print("Session Berhasil")
