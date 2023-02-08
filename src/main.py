from config import settings
from telethon import TelegramClient, events

class EntryClass(object):
    client: TelegramClient

    def __init__(self, client: TelegramClient):
        self.client = client
        # @client.on(events.NewMessage)
        # async def event_handler(event):
        #     self.event_handler(event)
        # self.client = TelegramClient(self.get_session_name(str(settings.TG_APP_AI)), settings.TG_APP_AI, settings.TG_APP_HASH)
        

    # client.on(events.NewMessage)
    def event_handler(self, event):
        print('========================================')
        print(event.raw_text)
        print('========================================')
        print('========================================')

def main():
    print(settings.TG_APP_HASH)
    client = TelegramClient(get_session_name(str(settings.TG_APP_AI)), settings.TG_APP_AI, settings.TG_APP_HASH)
    obj = EntryClass(client)
    @client.on(events.NewMessage)
    async def ev_handler(event):
        obj.event_handler(event)
    client.start(settings.TG_PHONE)
    client.run_until_disconnected()

def get_session_name(app_id: str) -> 'str' :
    return 'session_' + app_id 

main()