# guid = "c0BBLoT0895d57d97f3b7c0390dc8f7c"
# guid2 = "c0yw1V08272aee1b4991266fcc0615fb"
# guid3 = "c0yvbc0692d2cf1fd697e4d93710d4a2"
# guid4 = "c0yQ5b018508b097b96c8536bf766c33"

# user = "dotrdfshgtfrdeheize4"
# user2 = "dotrdfshhhdheheize1"
# user3 = "dotrdfshghdheheize2"
# user4 = "dotrdfshghdheheize3"

# tim = 2

# from time import sleep
# from rubpy import Client
# import asyncio

# bot = Client("Hadi_taker")

# Number = 4
if Number == 1:

    with bot:
        while 1:
            result = bot.update_channel_username(channel_guid=guid, username=user)
            print(result)
            sleep(tim)
elif Number == 2:

    with bot:
        while 1:
            h1 = bot.update_channel_username(channel_guid=guid, username=user)
            h2 = bot.update_channel_username(channel_guid=guid2, username=user2)
            print(h1, h2)
            sleep(tim)
elif Number == 3:

    with bot:
        while 1:
            h1 = bot.update_channel_username(channel_guid=guid, username=user)
            h2 = bot.update_channel_username(channel_guid=guid2, username=user2)
            h3 = bot.update_channel_username(channel_guid=guid3, username=user3)
            print(h1, h2, h3)
            sleep(tim)
elif Number == 4:

    with bot:
        while 1:
            h1 = bot.update_channel_username(channel_guid=guid, username=user)
            h2 = bot.update_channel_username(channel_guid=guid2, username=user2)
            h3 = bot.update_channel_username(channel_guid=guid3, username=user3)
            h4 = bot.update_channel_username(channel_guid=guid4, username=user4)
            print(h1, h2, h3, h4)
            sleep(tim)
else:
    print(
        """pleease write 1 or 4 in number
	"""
    )
# async def mainc():

#     Number = 4
#     if Number == 1:

#         async def main4():
#             while 1:
#                 h1 = await bot.update_channel_username(channel_guid=guid, username=user)
#                 print(h1)
#                 sleep(tim)

#     if Number == 2:

#         async def main2():
#             while 1:
#                 h1 = await bot.update_channel_username(channel_guid=guid, username=user)
#                 h2 = await bot.update_channel_username(
#                     channel_guid=guid2, username=user2
#                 )
#                 print(h1, h2)
#                 sleep(tim)

#     if Number == 3:

#         async def main3():
#             while 1:
#                 h1 = await bot.update_channel_username(channel_guid=guid, username=user)
#                 h2 = await bot.update_channel_username(
#                     channel_guid=guid2, username=user2
#                 )
#                 h3 = await bot.update_channel_username(
#                     channel_guid=guid3, username=user3
#                 )
#                 print(h1, h2, h3)
#                 sleep(tim)

#     if Number == 4:

#         async def main4():
#             while 1:
#                 h1 = await bot.update_channel_username(channel_guid=guid, username=user)
#                 h2 = await bot.update_channel_username(
#                     channel_guid=guid2, username=user2
#                 )
#                 h3 = await bot.update_channel_username(
#                     channel_guid=guid3, username=user3
#                 )
#                 h4 = await bot.update_channel_username(
#                     channel_guid=guid4, username=user4
#                 )
#                 print(h1, h2, h3, h4)
#                 sleep(tim)

#     else:
#         print(
#             """
# 		در نامبر یک عدد بین ۱ تا ۴ بگذارید
# 		"""
#         )


# asyncio.run(mainc())
