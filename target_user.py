from telethon import TelegramClient
from telethon.tl.functions.channels import CreateChannelRequest, UpdateUsernameRequest
import asyncio

API_ID = 380
API_HASH = 'a1680....'
PHONE_NUMBER = '+99888......'
TARGET_USERNAME = ''

async def main():
    client = TelegramClient('session_name', API_ID, API_HASH)
    await client.start(PHONE_NUMBER)

    async def check_and_take_username():
        while True:
            try:
                entity = await client.get_entity(TARGET_USERNAME)
                print(f"{TARGET_USERNAME} hali band. Qayta tekshirilmoqda...")
            except Expection as e:
                if "Clooud not found" in str(e) or "No user has" in str(e):
                    print(f"{TARGET_USERNAME} bo'sh! Kanal ochilmoqda...")

                    channel = await client(CreateChannelRequest(
                        title=f"{TARGET_USERNAME} kanali",
                        about="Avtomatik ochilgan kanal",
                        megagroup=False
                    ))

                    channel_id = channel.chats[0].id

                    try:
                        await client(UpdateUsernameRequest(
                            channel=channel_id,
                            username=TARGET_USERNAME
                        ))
                        print(f"{TARGET_USERNAME} usernami muvaffaqiyatli olindi!")
                    except Exception as username_error:
                        print(f"Username berishda xatolik: {username_error}")
                    break
                else:
                    print(f"Xatolik: {e}")
 
                await asyncio.sleep(1)

            await check_and_take_username()
            await client.disconnect()

        if __name__ == '__main__':
            asyncio.run(main())