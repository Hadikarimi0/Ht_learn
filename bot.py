from pyrubi import Client
from threading import Thread
from re import findall
bot = Client(session="bot2")
mahrom = []
admin = ("u0GHqaC0d9a7e57ba4cd79c18990ed66","u0F6ccd0cf261acdf907bdf9d1d922cd")
on_off = True
guid = 'g0EEISJ0e87252af54d2c1aa957d9f11'
shoabe = []
for m in bot.on_message(filters=[""]):
	if m.object_guid == guid:
		try:
			text = m.text
			print(m.text)
			if on_off == True:
				if m.text.startswith("new") or m.text.startswith("New"):
					for ad in admin:
						if m.author_guid in ad:
							for branch in bot.get_messages_by_id(m.object_guid, [m.reply_message_id])["messages"]:
								if branch['forwarded_from']['type_from'] == 'Channel':
									shoabe.clear()
									shoabe.append(branch['forwarded_from']['object_guid'])
									m.reply("دریافت شد.")
				if "فور" in m.text:
					h = bot.forward_messages(m.object_guid,[m.message_id],shoabe[0])
					
				if m.is_forward == True:
					h = bot.forward_messages(m.object_guid,[m.message_id],shoabe[0])
				if findall(r'\w\n\n\w',m.text) or findall(r'\w\n\n\n\w',m.text) or findall(r'\w\n\n\n\n\w',m.text) or findall(r'\w\n\n\n\n\n\w',m.text) or findall(r'\w\n\n\n\n\n\n\w',m.text) or findall(r'\w\n\n\n\n\n\n\n\w',m.text) or findall(r'\w\n\n\n\n\n\n\n\n\w',m.text) or findall(r'\w\n\n\n\n\n\n\n\n\n\w',m.text) or findall(r'\w\n\n\n\n\n\n\n\n\n\n\w',m.text) or findall(r'\w\s\n\n\w',m.text) or findall(r'\w\s\n\n\n\w',m.text) or findall(r'\w\s\n\n\n\n\w',m.text) or findall(r'\w\s\n\n\n\n\n\w',m.text) or findall(r'\w\s\n\n\n\n\n\n\w',m.text) or findall(r'\w\s\n\n\n\n\n\n\n\w',m.text) or findall(r'\w\s\n\n\n\n\n\n\n\n\w',m.text) or findall(r'\w\s\n\n\n\n\n\n\n\n\n\w',m.text) or findall(r'\w\s\n\n\n\n\n\n\n\n\n\n\w',m.text) or findall(r'\s\w\n\n\w',m.text) or findall(r'\s\w\n\n\n\w',m.text) or findall(r'\s\w\n\n\n\n\w',m.text) or findall(r'\s\w\n\n\n\n\n\w',m.text) or findall(r'\s\w\n\n\n\n\n\n\w',m.text) or findall(r'\s\w\n\n\n\n\n\n\n\w',m.text) or findall(r'\s\w\n\n\n\n\n\n\n\n\w',m.text) or findall(r'\s\w\n\n\n\n\n\n\n\n\n\w',m.text) or findall(r'\s\w\n\n\n\n\n\n\n\n\n\n\w',m.text) or findall(r'\w\n\n\s\w',m.text) or findall(r'\w\n\n\n\s\w',m.text) or findall(r'\w\n\n\n\n\s\w',m.text) or findall(r'\w\n\n\n\n\n\s\w',m.text) or findall(r'\w\n\n\n\n\n\n\s\w',m.text) or findall(r'\w\n\n\n\n\n\n\n\s\w',m.text) or findall(r'\w\n\n\n\n\n\n\n\n\s\w',m.text) or findall(r'\w\n\n\n\n\n\n\n\n\n\s\w',m.text) or findall(r'\w\n\n\n\n\n\n\n\n\n\n\s\w',m.text):
					
					try:
						if not "فور" in m.text:
							if not m.is_forward == True:
								bot.send_text(shoabe[0],m.text)
					except:pass
			if m.text == "#off":
					for ad in admin:
						if m.author_guid in ad:
							on_off = False
							m.reply("آفلاین شد.")
			if m.text == "#on":
					for ad in admin:
						if m.author_guid in ad:
							on_off = True
							m.reply("آنلاین شد.")
		except:pass
