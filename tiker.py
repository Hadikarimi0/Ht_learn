import  os
os.system("pip install rubpy==6.4.6")
from rubpy.sync import Client
from time import sleep

with Client(session='bot') as client:
	while True:
	
	   h1 = client.update_channel_username(channel_guid=guid, username=user)
	   h2 = client.update_channel_username(channel_guid=guid2, username=user2)

	   sleep(tim)
	   print(h1,h2)
	   
