import json
from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from bot.config import get_session
from bot.config import save_session
from bot.config import settings

session = get_session()

with TelegramClient(
    session=StringSession(session), api_id=settings.API_ID, api_hash=settings.API_HASH
) as client:
    client: TelegramClient
    client.get_dialogs()

    if not session:
        session_token = StringSession.save(client.session)
        save_session(session_token)

    async def get_partisipants() -> dict:
        group = await client.get_entity(settings.GROUP_LINK)
        partisipants_dict = {}
        async for user in client.iter_participants(group):
            if user.username == None:
                continue
            partisipants_dict[user.username] = {
                "name": user.first_name,
                "last_name": user.last_name,
            }
        return partisipants_dict
    partisipants_dict = client.loop.run_until_complete(get_partisipants())
    with open("partisipants.json", "w") as file:
        json.dump(partisipants_dict, file, indent=4, ensure_ascii=False)
    