from telethon import events
from telethon.events.newmessage import NewMessage
from telethon.sessions import StringSession
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.types import User

from bot.captcha_solve import handlers_bots
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

    async def join_chat() -> None:
        group = await client.get_entity(settings.GROUP_LINK)

        await client(JoinChannelRequest(group))

    @client.on(
        events.NewMessage(
            blacklist_chats=list(handlers_bots.keys()),
            forwards=False,
            from_users=list(handlers_bots.keys()),
            incoming=True,
        )
    )
    async def handler(event: NewMessage.Event):
        bot_user: User = await client.get_me()
        await handlers_bots[event.message.from_id.user_id].solve_capcha(
            event.message, bot_user
        )

    client.loop.run_until_complete(join_chat())
    client.run_until_disconnected()
