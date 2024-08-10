from telethon.sync import TelegramClient

api_id = '21346711'
api_hash = 'fd9a5c2d2d8cde393adaab0dfcc9d300'

with TelegramClient('sesi1.session', api_id, api_hash) as client:
    print("Sukses")