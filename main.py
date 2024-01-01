#بات جدید

from pyrubi import Client
from random import randint
from requests import get
from random import choice
from re import findall
import requests,json
from time import sleep, time
from textt import *
from threading import Thread
from json import load,dump
import random
import time
import datetime
import threading
from collections import Counter
bot = Client(session="kkkkkkk")
#h = bot.join_chat("https://rubika.ir/joing/FBDAJIJB0CAMXXYDLCVZAHNMHRYIBIAX")['group']['group_guid']
#print(h)

Addmins = ["u0GHqaC0d9a7e57ba4cd79c18990ed66","u0GHXeO087417f6b19ba05dafe2b26c3"]
group =["g0Cl26m0351c826a9edd43267d561974","g0DiDQl0f149fdbc0d3eb2805265424b"]
upload = "HT_USERNAME"
guid = bot.get_chat_info_by_username(upload)['channel']['channel_guid']
guid_hadi = "u0GHXeO087417f6b19ba05dafe2b26c3"
#===============================

dos = """سلام کاربر گرامی برای دیدن قابلیت های ربات میتونید از چنل زیر اقدام کنید 🫡👇

@HT_learn
"""
dastor = """دستور با موفقیت اجرا شد🎉

@@Channel¹ @@(https://rubika.ir/HT_username)
"""

pm = f"""کاربر گرامی برای استفاده از دستورات ربات لطفا عضو اسپانسر های ما شوید!

1 @HT_username
"""
scores = {}


#____________________________________
def font1(m):
	text = m.text.split("font ")[1]
	responsew = get(f"https://api.codebazan.ir/font/?text={text}")
	jokgw = responsew.text
	jdw = json.loads(jokgw)['result']
	resultw = [f"{i}. {jdw[str(i)]}" for i in range(1, 101) if str(i) in jdw]
	m.reply('\n'.join(resultw))
#_______________________________
def font2(m):
	text_fontFa = m.text.split("فونت ")[1]
	web = get(f"https://api.codebazan.ir/font/?type=fa&text={text_fontFa}").json()['Result']
	fonts = "\n".join([web[x] for x in web.keys()])
	m.reply(fonts)
#_______________________________

def my_amar(m):
	member_info = bot.get_chat_info(name)["user"]
	g = member_info["user_guid"]
	n = member_info["first_name"]
	f = member_info["bio"]
	koni = int(ekhtar.count(name))
	j = bot.get_admin_members(m.object_guid,just_get_guids=True)
	if g in j:
		info = f"""
guid : {g}

name : {n}

bio : {f}

admin : ✅

Warning : {koni}
"""
		m.reply(info)
	else:
		info2 = f"""
guid : {g}

name : {n}

bio : {f}

admin : ❌

Warning : {koni}
"""
		m.reply(info2)

#===============================
def join(m):
	Check=bot.check_join(guid,m.author_guid)
	if Check == True:
		print("User is ok joined Channel you")
		return True
	else:
		m.reply(pm)
#____________________________________
def mute(m):
	if m.author_guid in Addmins:
		hh = m.reply_message_id
		target_info = bot.get_messages_by_id(m.object_guid, [hh])["messages"]
		de.append(target_info[0]["author_object_guid"])
		bot.send_text(m.object_guid, "کاربر مورد نظر با موفقیت در لیست سکوت قرار گرفت.")
		
def unmute(m):
	if m.author_guid in Addmins:
		hh = m.reply_message_id
		target_info = bot.get_messages_by_id(m.object_guid, [hh])["messages"]
		de.remove(target_info[0]["author_object_guid"])
		bot.send_text(m.object_guid, "کاربر با موفقیت از لیست سکوت خارج شد.")

def VAZEAT(m):
	
	text_jagh = choice(jagh_text)
	m.reply(f"وضعیت شما به صورت زیر است :\nکصخلی : {randint(0,100)}%\nجقی بودن : {randint(0,100)}%\nکونی بودن : {randint(0,100)}%\nشق بودن کیرت : {randint(0,100)}%\nسگ بودن : {randint(0,100)}%\nگشادبودنت : {randint(0,100)}%\nبه تخمت بودن : {randint(0,100)}%\nمیزان گاییده شدن در کشور : {randint(0,100)}%\nگی بودنت : {randint(0,100)}%\nخایمال بودنت : {randint(0,100)}%\nوضعیت جقی شما: {text_jagh}")
#____________________________________
def chat_gpt(m):
	text = m.text.replace('+ ','')
	gpt = get(f"https://chatgpt-api3.onrender.com?text={text}").json()
	gpt = gpt["message"]
	m.reply(f"**CHAT GPT**:\n{gpt} ")
#_____________________________________
def chat_gpt2(m):
	
	text = m.text.replace('! ','')
	
	gpt = get(f"https://mrapiweb.ir/api/evilgpt.php?key=testkey&emoji=😈&question={text}").json()
	gpt = gpt["javab"]
	m.reply(f"**BREATGPT**:\n{gpt} ")
#_____________________________________
def zed_link(m):
	j = bot.get_admin_members(m.object_guid,just_get_guids=True)
	if m.author_guid in j:
		print("A D M I N +")
	else:
		bot.delete_messages(m.object_guid, [m.message_id])
#		ek_k(m)
#_____________________________________
def blok(m):
	if m.author_guid in Addmins:
		target_info = bot.get_messages_by_id(m.object_guid, [m.reply_message_id])["messages"]
		kkkkk = target_info[0]["author_object_guid"]
		black_list.append(kkkkk)
		bot.send_text(m.object_guid,"کاربر در لیست سیاه ربات قرار گرفت")
	else:
		m.reply("شما ادمین نیستید")
#____________________________________

def logo2(m):
	text = m.text.replace("logo2 ","")
	bot.send_image(m.object_guid, f"https://api.irateam.ir/Logo-Maker/?text={text}&script={ttt}&fontsize=200&textcolor=red", m.message_id, dastor)

def logo(m):
	text = m.text.replace('logo ','')
	bot.send_image(m.object_guid, f"http://api2.haji-api.ir/ephoto360?type=text&id={randint(1, 160)}&text={text}", m.message_id, dastor)
#_____________________________________
def unblok(m):
	if m.author_guid in Addmins:
		target_info = bot.get_messages_by_id(m.object_guid, [m.reply_message_id])["messages"]
		kkkkk = target_info[0]["author_object_guid"]
		black_list.remove(kkkkk)
		bot.send_text(m.object_guid,"کاربر از لیست سیاه ربات خارج شد")
#____________________________________
def laghab(m):
	j = bot.get_admin_members(m.object_guid,just_get_guids=True)
	print(j)
	if m.author_guid in j or Addmins:
		hoviat_text = m.text.split("تنظیم لقب ")[1]
		target_info = bot.get_messages_by_id(m.object_guid, [m.reply_message_id])["messages"]
		kkkkk = target_info[0]["author_object_guid"]
		yadi.update({f"{kkkkk}" : f"{hoviat_text}"})
		m.reply("تنظیم لقب با موفقیت انجام شد")
	else:
		m.reply("شما ادمین نیستید")
#____________________________________
def snajagh(m):
	j = bot.get_admin_members(m.object_guid,just_get_guids=True)
	if m.author_guid in j or Addmins:
		hh = m.reply_message_id
		bot.pin_message(m.object_guid, hh)
		bot.send_text(m.object_guid, "پیام با موفقیت سنجاق شد.", hh)
#_______________________________________
def unsnajagh(m):
	j = bot.get_admin_members(m.object_guid,just_get_guids=True)
	if m.author_guid in j or Addmins:
		hh = m.reply_message_id
		bot.unpin_message(m.object_guid, hh)
		bot.send_text(m.object_guid, "پیام با موفقیت سنجاق شد.", hh)
#_______________________________________
def baste(m):
	j = bot.get_admin_members(m.object_guid,just_get_guids=True)
	if m.author_guid in j or Addmins:
		bot.set_group_default_access(m.object_guid,[])
		m.reply("گروه با موفقیت بسته شد.")
#_______________________________________
def bazz(m):
	j = bot.get_admin_members(m.object_guid,just_get_guids=True)
	if m.author_guid in j or Addmins:
		bot.set_group_default_access(m.object_guid,['SendMessages'])
		m.reply("گروه با موفقیت بار شد.")
#_______________________________________
def ROBOT(m):
	
	text_lis = choice(text_liss)
	
	if not m.author_guid in rel:
		if m.author_guid in yadi:
			m.reply(f"{text_lis} {yadi[f'{m.author_guid}']}")
		else:
			m.reply(text_lis)
	else:
		if m.author_guid in yadi:
			m.reply(f"{text_lis} {yadi[f'{m.author_guid}']}")
		else:
			jo = choice(hadi2)
			m.reply(jo)
#____________________________________
def te_ki(m):
	choice_mtn = choice(matn_ki)
	members_ki = bot.get_all_members(m.object_guid,just_get_guids=True)
	member_ki = choice(members_ki)
	name_ki = bot.get_chat_info(member_ki)['user']['first_name']
	text_ki = m.text.split("کی ")[1]
	m.reply(f"{choice_mtn} @@{name_ki}@@({member_ki}) {text_ki}")
#____________________________________
def dalam(m):
	sl = "باز این پیداش شد", "سلام دختری","همه خفه شید عشقم اومد" ,"سلام قشنگم چطوری؟","ایجون یه دختر"
	sll = choice(sl)
	if m.author_guid in yadi:
		m.reply(f"{sll} {yadi[f'{m.author_guid}']}")
	else:
		m.reply(f"{sll}")
#____________________________________
	
def ek_k2(m):
	ekhtar.append(m.author_guid)
	coun = int(ekhtar.count(m.author_guid))
	if coun == 1:
		bot.send_text(m.object_guid, f"کاربر گرامی از کلمات مستهجن و توهین آمیر استفاده کردید شما 1 اخطار از 3 اخطار دریافت کردید.🩵")
	elif coun == 2:
		bot.send_text(m.object_guid, "کاربر گرامی از کلمات مستهجن و توهین آمیر استفاده کردید شما 2 اخطار از 3 اخطار دریافت کردید.🩵")
	elif coun == 3:
			bot.block_user(m.author_guid)
		
#===============================
def ek_k(m):
	
	ekhtar.append(m.author_guid)
	coun = int(ekhtar.count(m.author_guid))
	if coun == 1:
		bot.send_text(m.object_guid, f"کاربر** {m.author_title} **شما 1 اخطار از 5 اخطار دریافت کردید سعی کنید اخطار دریافت نکنید در غیر این صورت از گپ سیکتیر میشید〽️")
	elif coun == 2:
			bot.send_text(m.object_guid, f"کاربر** {m.author_title} **شما 2 اخطار از 5 اخطار دریافت کردید سعی کنید اخطار دریافت نکنید در غیر این صورت از گپ سیکتیر میشید〽️")
	elif coun == 3:
			bot.send_text(m.object_guid, f"کاربر** {m.author_title} **شما 3 اخطار از 5 اخطار دریافت کردید سعی کنید اخطار دریافت نکنید در غیر این صورت از گپ سیکتیر میشید〽️")
	elif coun == 4:
			bot.send_text(m.object_guid, f"کاربر** {m.author_title} **شما 4 اخطار از 5 اخطار دریافت کردید سعی کنید اخطار دریافت نکنید در غیر این صورت از گپ سیکتیر میشید〽️")
	elif coun == 5:
			bot.send_text(m.object_guid, f"تق ** {m.author_title} **خارکسه 5 تا اخطار دریافت کردی وقت سیکتیر شدنته👺")
			bot.ban_member(m.object_guid,m.author_guid)
		
#===============================
#===============================
def ek_k3(m):
	
	ekhtar.append(jjj[0]["author_object_guid"])
	coun = int(ekhtar.count(jjj[0]["author_object_guid"]))
	if coun == 1:
		bot.send_text(m.object_guid, f"کاربر** {m.author_title} **شما 1 اخطار از 5 اخطار دریافت کردید سعی کنید اخطار دریافت نکنید در غیر این صورت از گپ سیکتیر میشید〽️")
	elif coun == 2:
			bot.send_text(m.object_guid, f"کاربر** {m.author_title} **شما 2 اخطار از 5 اخطار دریافت کردید سعی کنید اخطار دریافت نکنید در غیر این صورت از گپ سیکتیر میشید〽️")
	elif coun == 3:
			bot.send_text(m.object_guid, f"کاربر** {m.author_title} **شما 3 اخطار از 5 اخطار دریافت کردید سعی کنید اخطار دریافت نکنید در غیر این صورت از گپ سیکتیر میشید〽️")
	elif coun == 4:
			bot.send_text(m.object_guid, f"کاربر** {m.author_title} **شما 4 اخطار از 5 اخطار دریافت کردید سعی کنید اخطار دریافت نکنید در غیر این صورت از گپ سیکتیر میشید〽️")
	elif coun == 5:
			bot.send_text(m.object_guid, f"تق ** {m.author_title} **خارکسه 5 تا اخطار دریافت کردی وقت سیکتیر شدنته👺")
			bot.ban_member(m.object_guid,m.author_guid)
		
#===============================
#____________________________________
def angize(m):
	try:
		bot.send_text(m.object_guid, get("http://haji-api.ir/angizeshi").text, m.message_id)
	except:pass
#___________________________
def time(m):
	jd = get("http://api.codebazan.ir/time-date/?td=time").text
	m.reply(f"گلم ساعت **{jd}** هست")	
#___________________________
#___________________________
def dastan(m):
	try:
		bot.send_text(m.object_guid, get("http://api.codebazan.ir/dastan/").text, m.message_id)
	except:pass
#___________________________
def alaki(m):
	try:
		bot.send_text(m.object_guid, get("http://api.codebazan.ir/jok/alaki-masalan/").text, m.message_id)
	except:pass
#___________________________
def jok(m):
	try:
		bot.send_text(m.object_guid, get("https://api.codebazan.ir/jok/json/").json()['result']['jok'], m.message_id)
	except:pass
#___________________________
def bio(m):
	try:
		bot.send_text(m.object_guid, get("https://api.codebazan.ir/bio").text, m.message_id)
	except:pass
#___________________________
def dialog(m):
	try:
		bot.send_text(m.object_guid, get("http://api.codebazan.ir/dialog/").text, m.message_id)
	except:pass
#___________________________
def zekr(m):
	try:
		lpo = get("https://api.pamickweb.com/API/zekr.php").json()['Result']
		h1 = lpo["zekr"]
		h2 = lpo["persian"]
		h3 = lpo["info"]
		m.reply(f"{h1}\n\n{h2}\n\n{h3}")
	except:pass
#___________________________
def pa_na_pa(m):
	if join(m) == True:
		m.reply(get("http://api.codebazan.ir/jok/pa-na-pa").text)
#_______________________________
def hadis(m):
	bot.send_text(m.object_guid, get("http://api.codebazan.ir/hadis/").text, m.message_id)
#_______________________________
def one(m):
	text_liss = "کون", "کیر","ممه"
	jkl = choice(text_liss) 
	m.reply(jkl)
#____________________________________
def two(m):
	m.reply("نمیکنم فشار بخور")
#____________________________________
def three(m):
	text_liss = "نمیدم فشار بخور","کیرم بخور بدمت مشتی","نمیدم","نمیدم فشاری بشیییی"
	jkl = choice(text_liss)
	if not m.author_guid in rel:
		m.reply(jkl)
	else:
		m.reply("باشه بیا بدم بهت")
#____________________________________
def four(m):
	
	hadi = "نخند عشقم جر میخوری","ایجانم تو فقط بخند ","خنده هاتو عشقه"
	lo = choice(text_liss2)
	loo = choice(hadi)
	if not m.author_guid in rel:
		m.reply(lo)
	else:
		m.reply(loo)
#____________________________________
def on_join(m):
	if m.author_guid in Addmins:
		join__guid = False
		m.reply("جوین اجباری با موفقیت خاموش شد.")
	#_______________________________
def off_join(m):
	if m.author_guid in Addmins:
		join__guid = True
		m.reply("جوین اجباری با موفقیت روشن شد.")
#_______________________________
def on_link(m):
	if m.author_guid in Addmins:
		zed__link = True
		m.reply("ضد لینک روشن شد.")
#_______________________________
def dalam2(m):
	sd2 = "اه اه اه چندش عشق چیه","هعی به شما نگا میکنم حسودیم میشه من کسیو ندارم خیلی تنهام","اصلا حال میکنم وقتی میبینم عین این چندشا آخر کلمات میم مالکیت میزاری"
	slll2 = choice(sd2)
	m.reply(slll2)
#_____________________________________
def dalam3(m):
	try:
		voice = choice(voice_random)
		info_message = bot.get_messages_by_id(m.object_guid,[m.reply_message_id])["messages"]
		for info in info_message:
			if hh == info['author_object_guid']:
				bot.send_voice(m.object_guid, voice, m.message_id)
	except:pass
#_____________________________________
def off_link(m):
	if m.author_guid in Addmins:
		zed__link = False
		m.reply("ضد لینک خاموش شد.")
#_____________________________________
def rell(m):
	if not m.author_guid in cut:
		target_info = bot.get_messages_by_id(m.object_guid, [m.message_id])["messages"]
		kkkkk = target_info[0]["author_object_guid"]
		rel.append(kkkkk)
		m.reply("آره عشقم الان تو رل منی و هر وقت صدام کردی دیگه فوشت نمیدم")
	else:
		m.reply("تو خیانت کاری دیگه باهات رل نمیزنم")
#_____________________________________
def cutt(m):
	
	target_info = bot.get_messages_by_id(m.object_guid, [m.message_id])["messages"]
	kkkkk = target_info[0]["author_object_guid"]
	cut.append(kkkkk)
	m.reply("برو دیگه دوست ندارم قلبم تیکه تیکه شد")
#_____________________________________
def nsme1(m):
	j = bot.get_admin_members(m.object_guid,just_get_guids=True)
	if m.author_guid in j or Addmins:
		hh = m.reply_message_id
		hhh = bot.get_messages_by_id(m.object_guid, [hh])["messages"]
		bot.edit_group_info(m.object_guid, title=hhh[0]["text"])
		m.reply("نام گروه با موفقیت تغییر یافت.")
#_______________________________________
def nsme2(m):
	j = bot.get_admin_members(m.object_guid,just_get_guids=True)
	if m.author_guid in j or Addmins:
		bot.edit_group_info(m.object_guid, title=text)
		m.reply("نام گروه با موفقیت تغییر یافت.")
#_______________________________________
def prof(m):
	j = bot.get_admin_members(m.object_guid,just_get_guids=True)
	if m.author_guid in j or Addmins:
		jj = m.reply_message_id
		jjj = bot.get_download_link(m.object_guid,jj)
		bot.upload_avatar(m.object_guid, jjj)
		bot.send_text(m.object_guid, "پروفایل گپ با موفقیت تغییر کرد.",jj)
#____________________________________

def bann(m):
	j = bot.get_admin_members(m.object_guid,just_get_guids=True)
	if m.author_guid in j or Addmins:
		kk = m.reply_message_id
		target_info = bot.get_messages_by_id(m.object_guid, [kk])["messages"]
		bot.ban_member(m.object_guid, target_info[0]["author_object_guid"])
		bot.send_text(m.object_guid, "کاربر مورد نظر با موفقیت ریمو/حذف شد.")
		
		
def unbann(m):
	j = bot.get_admin_members(m.object_guid,just_get_guids=True)
	if m.author_guid in j or Addmins:
		kk = m.reply_message_id
		target_info = bot.get_messages_by_id(m.object_guid, [kk])["messages"]
		bot.unban_member(m.object_guid, target_info[0]["author_object_guid"])
		bot.send_text(m.object_guid, "کاربر مورد نظر با موفقیت از لیست سیاه گروه خارج شد.")
		
def bann2(m):
	j = bot.get_admin_members(m.object_guid,just_get_guids=True)
	if m.author_guid in j or Addmins:
		text_add = m.text.split("@")[1]
		guid_rimo = bot.get_chat_info_by_username(text_add)['user']['user_guid']
		bot.ban_member(m.object_guid, guid_rimo)
		m.reply("کاربر مورد نظر با موفقیت ریمو شد.")

def unbann2(m):
	j = bot.get_admin_members(m.object_guid,just_get_guids=True)
	if m.author_guid in j or Addmins:
		text_add = m.text.split("@")[1]
		guid_rimo = bot.get_chat_info_by_username(text_add)['user']['user_guid']
		bot.unban_member(m.object_guid, guid_rimo)
		m.reply("کاربر مورد نظر با موفقیت از لیست سیاه گپ خارج شد.")

def adminkon(m):
	j = bot.get_admin_members(m.object_guid,just_get_guids=True)
	if m.author_guid in j or Addmins:
		o = m.reply_message_id
		target_info = bot.get_messages_by_id(m.object_guid, [o])["messages"]
		bot.set_admin(m.object_guid,target_info[0]["author_object_guid"],["ChangeInfo"])
		bot.send_text(m.object_guid, "کاربر مورد نظر با موفقیت ادمین شد.")
		
def unadminkon(m):
	j = bot.get_admin_members(m.object_guid,just_get_guids=True)
	if m.author_guid in j or Addmins:
		o = m.reply_message_id
		target_info = bot.get_messages_by_id(m.object_guid, [o])["messages"]
		bot.unset_admin(m.object_guid,target_info[0]["author_object_guid"])
		bot.send_text(m.object_guid, "کاربر مورد نظر با موفقیت عزل شد.")

def up_qavanin(m):
	j = bot.get_admin_members(m.object_guid,just_get_guids=True)
	if m.author_guid in Addmins:
		hh = m.reply_message_id
		hhh = bot.get_messages_by_id(m.object_guid, [hh])["messages"]
		on_and_off.clear()
		on_and_off.append(hhh[0]["text"])
#		rules = open("rules.txt","w",encoding='utf-8').write(str(hhh[0]["text"]))
		bot.send_text(m.object_guid, "قوانین با موفقیت آپدیت شد.", hh)
	else:
		m.reply("شما ادمین نیستید")

usernames = []

def hadi(usernames):
    def handle_most_common_usernames():
        username_counts = Counter(usernames)
        most_common_usernames = username_counts.most_common(3)

        if most_common_usernames:
            i, (username, count) = 0, most_common_usernames[0]
            ii = bot.get_chat_info(username)['user']
            h = ii['first_name']
            hep = f"1 user @@ {h} @@({username}) <==> {count} Message \n\n "

            if len(most_common_usernames) > 1:
                i, (username, count) = 1, most_common_usernames[1]
                ii = bot.get_chat_info(username)['user']
                h = ii['first_name']
                hep += f"2 user @@ {h} @@({username}) <==> {count} Message \n\n "

            if len(most_common_usernames) > 2:
                i, (username, count) = 2, most_common_usernames[2]
                ii = bot.get_chat_info(username)['user']
                h = ii['first_name']
                hep += f"3 user @@ {ii['first_name']} @@({username}) <==> {count} Message \n\n "
            
            return hep

    hep = ''
    try:
        hep = handle_most_common_usernames()
    except Exception as e:
        print(f"An error occurred: {e}")

    if hep:
        m.reply(f"""تعداد پیام ها در ۲۴ ساعت اخیر 
{hep}


تعداد پیام های شیشه ای:
افرادی که ریمو شدن = {rimo}
افرادی که لف دادن = {lef}
افرادی که عضو شدن = {jon}
""")

def send(m,Fuck):
	try:
				ss = m.reply("start")
				for tex in Fuck:
					bot.edit_message(m.object_guid,tex, ss['message_update']['message_id'])
					
	except:pass
def sendDans(m):
	try:
		ss = m.reply("start")
		for tex in Dans:
			bot.edit_message(m.object_guid,tex, ss['message_update']['message_id'])
	except:pass

def heart(m):
	try:
		ss = m.reply("start")
		for tex in Heart:
			bot.edit_message(m.object_guid,tex, ss['message_update']['message_id'])
	except:pass
	
def love(m):
	try:
		ss = m.reply("start")
		for tex in Love:
			bot.edit_message(m.object_guid,tex, ss['message_update']['message_id'])
	except:pass
def Clockk(m):
	try:
		ss = m.reply("start")
		for tex in Clock:
			bot.edit_message(m.object_guid,tex, ss['message_update']['message_id'])
	except:pass
def Countingg(m):
	try:
		ss = m.reply("start")
		for tex in Number:
			bot.edit_message(m.object_guid,tex, ss['message_update']['message_id'])
	except:pass
def Helloo(m):
	try:
		ss = m.reply("start")
		for tex in Hello:
			bot.edit_message(m.object_guid,tex, ss['message_update']['message_id'])
	except:pass
def Rotationn(m):

	try:
		ss = m.reply("start")
		for tex in Rotation:
			bot.edit_message(m.object_guid,tex, ss['message_update']['message_id'])
	except:pass
def pashmm(m):
	try:
		ss = m.reply("start")
		for tex in pashm:
			bot.edit_message(m.object_guid,tex, ss['message_update']['message_id'])
	except:pass
def irans(m,Iran):
	try:
				test=m.reply("ok")
				for tex in Iran:
					bot.edit_message(m.object_guid,tex,test['message_update']['message_id'])
					
	except:pass


def dol(m):
	bot.delete_messages(m.object_guid, [m.message_id])
	print("pak shod")
#

def bloooo(m):
	j = bot.get_admin_members(m.object_guid,just_get_guids=True)
	if m.author_guid in j or Addmins:
		try:	
			td = 0
			hep = ''
			x =  bot.get_banned_members(m.object_guid)
			for x in x['in_chat_members']:
				name = bot.get_chat_info(x['member_guid'])["user"]["first_name"]
				td += 1
				hep = f"""{hep}[{td}] - {name}  \n """
		except:pass
		m.reply(hep)
	
def bloooo2(m):
	j = bot.get_admin_members(m.object_guid,just_get_guids=True)
	if m.author_guid in j or Addmins:
		try:
			x =  bot.get_banned_members(m.object_guid)
			for x in x['in_chat_members']:
				bot.unban_member(m.object_guid,x['member_guid'])
			
		except:pass
		m.reply("لیست سیاه با موفقیت خالی شد")

def ad_min(m):
	try:	
		td = 0
		hep = ''
		j = bot.get_admin_members(m.object_guid,just_get_guids=True)
		for x in set(j):
			name = bot.get_chat_info(x)["user"]["first_name"]
			td += 1
			hep = f"""{hep}[{td}] - {name}  \n """
	except:pass
	m.reply(hep)

#_____________________________________
def voice(m):
	text = m.text.split("صدای مرد ")[1]
	bot.send_voice(m.object_guid, get(f"https://api3.haji-api.ir/majid/tools/tts?text={text}؟&Character=FaridNeural").json()["results"]["url"], m.message_id, dastor
)
#_____________________________________
def voice2(m):
	text = m.text.split("صدای زن ")[1]
	bot.send_voice(m.object_guid, get(f"https://api3.haji-api.ir/majid/tools/tts?text={text}؟&Character=DilaraNeural").json()["results"]["url"], m.message_id, dastor)
lef = 0
jon = 0
on_and_off = []
rimo = 0
on_bot = True
sokhan = True
zed__link = True
onn_bot = True
namoss = True
join__guid = True
yad_begir = True
dastorat_gap = True
Welcome = True
no_gifs = False
no_Image = False
no_Video = False
no_File = False
no_Voice = False
guid_acc = []
ekhtar = []
de =[]
black_list = []
rel = []
cut =[]
yadi = {}
yad_kalame = {}
hh = bot.get_me()["user"]["user_guid"]
print(hh)
guid_acc.append(hh)

def generate_question():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(["+", "-", "*", "/"])
    question = f"{num1} {operator} {num2}"
    answer = eval(question)
    return question, answer

def check_answer(m, answer):
    name = m.author_guid
    kl = m.text.replace("جواب ", "")
    info_message = bot.get_messages_by_id(m.object_guid,[m.reply_message_id])["messages"]
    if "سوال" in info_message[0]['text']:
    	for info in info_message:
    		if hh == info['author_object_guid']:
    		    if float(kl) == answer:
    	        	if name in scores:
    	        		scores[name] += 1
    	        	else:
    	       		 scores[name] = 1
    	       		 m.reply("پاسخ درست است! و شما یک امتیاز دریافت کردید")
    		    else:
    		    	m.reply("پاسخ اشتباه است!")
from json import dump,load
import time
from time import time


g = {}

def read_data():
    global g
    return g

def write_data(data):
    global g 
    g = data

def start_game(m):
    data = read_data()
    if not m.object_guid in data.keys():
        data[m.object_guid] = {
            'name': m.author_title,
            'status': True,
            'timer': time(),
            'players': {
                m.author_guid : {
                    'name': m.author_title,
                    'turn_status': True,
                    'piece': '❌'
                }
            }
        }
    else:
        if not data[m.object_guid]['status']:
            if data[m.object_guid]['timer'] < time():
                data[m.object_guid]['status'] = True
                data[m.object_guid]['players'] = {
                    m.object_guid: {
                        'name': m.author_title,
                        'turn_status': True,
                        'piece': '❌'
                    }
                }
            else:
                remaining = str(data[m.object_guid]['timer'] - time()).split('.')[0]
                return m.reply(f'امکان ایجاد بازی تا {remaining} ثانیه دیگر امکان پذیر نیست !')
        else:
            return m.reply('یک بازی در حال اجرا است لطفا تا پایان آن صبر کنید !')
    write_data(data)
    text = 'بازی ایجاد شد ❗\n\n کاربران با ارسال دستور\n /join\n می توانند در بازی شرکت کنند.'
    m.reply(text)
def save_player2_info(m):
        try:
            data = read_data()
            if data[m.object_guid]['status']:
                if not m.author_guid in data[m.object_guid]['players'].keys():
                    if len(data[m.object_guid]['players']) < 2:
                        data[m.object_guid]['players'][m.author_guid] = {
                            'name': m.author_title,
                            'turn_status': False,
                            'piece': '⭕'
                        }
                        write_data(data)
                        send_game_table(m)
                    else:
                        m.reply('ظرفیت بازیکنان پر است !')
                else:
                    m.reply('شما قبلا وارد بازی شده اید !')
            else:
                m.reply('هیچ بازی در حال اجرا نیست !')
        except KeyError:
            m.reply('هیچ بازی در حال اجرا نیست !')
def send_game_table(m):
        data = read_data()
        players = []
        for i in data[m.object_guid]['players'].keys():
            players.append(data[m.object_guid]['players'][i]['name'])
        msg = f'بازی شروع شد ❗\n\nبازیکنان: {players[0]}, {players[1]}\nاکنون نوبت {players[0]} است.'
        game_table = '├  ①  ┼  ②  ┼  ③  ┤\n\n├  ④  ┼  ⑤  ┼  ⑥  ┤\n\n├  ⑦  ┼  ⑧  ┼  ⑨  ┤'
        m.reply(msg)
        bot.send_text(m.object_guid, game_table)
def turn(m):
        try:
            data = read_data()
            if data[m.object_guid]['status']:
                if m.author_guid in data[m.object_guid]['players'].keys():
                    if m.reply_message_id != None:
                        game_table = bot.get_messages(m.object_guid, m.reply_message_id)["messages"][0]["text"]
                        if '├' in game_table:
                            for i in [('1', '①'),('2', '②'),('3', '③'),('4', '④'),('5', '⑤'),('6', '⑥'),('7', '⑦'),('8', '⑧'),('9', '⑨')]:
                                if m.text == i[0]:
                                    if data[m.object_guid]['players'][m.author_guid]['turn_status']:
                                        game_table = game_table.replace(i[1], data[m.object_guid]['players'][m.author_guid]['piece'])
                                        for p in data[m.object_guid]['players'].keys():
                                            turn_status = data[m.object_guid]['players'][p]['turn_status']
                                            if turn_status:
                                                data[m.object_guid]['players'][p]['turn_status'] = False
                                            else: 
                                                data[m.object_guid]['players'][p]['turn_status'] = True
                                        m.reply(game_table)
                                        bot.delete_messages(m.object_guid,[bot.get_messages(m.object_guid, m.reply_message_id)["messages"][0]["message_id"]])
                                        break
                                    else:
                                        m.reply('نوبت شما نیست !')
                                else:
                                    continue
                            write_data(data)
                            check_result(game_table,m)
                        else:
                            m.reply('این جدول بازی نیست !')
                    else:
                        m.reply('روی جدول بازی ریپلای کنید !')
                else:
                    m.reply('شما جزو شرکت کنندگان بازی نیستید !')
            else:   
                m.reply('هیچ بازی در حال اجرا نیست !')
        except KeyError:print('Error')
def check_result(game_table,m):
        data = read_data()
        for p in data[m.object_guid]['players'].keys():
            piece = data[m.object_guid]['players'][p]['piece']
            piece = [piece, piece ,piece]
            name = data[m.object_guid]['players'][p]['name']
            if piece == [game_table[3], game_table[9], game_table[15]]:
                return send_result(name,m)
            elif piece == [game_table[24], game_table[30], game_table[36]]:
                return send_result(name,m)
            elif piece == [game_table[45], game_table[51], game_table[57]]:
                return send_result(name,m)
            elif piece == [game_table[3], game_table[24], game_table[45]]:
                return send_result(name,m)
            elif piece == [game_table[9], game_table[30], game_table[51]]:
                return send_result(name,m)
            elif piece == [game_table[15], game_table[36], game_table[57]]:
                return send_result(name,m)
            elif piece == [game_table[3], game_table[30], game_table[57]]:
                return send_result(name,m)
            elif piece == [game_table[15], game_table[30], game_table[45]]:
                return send_result(name,m)
            else:  
                continue
        return False
def send_result(name,m):
        data = read_data()
        text = f'بازیکن {name} برنده شد !'
        data={}
        write_data(data)
        bot.send_text(m.object_guid, text)
        g.clear
def mosavi(name,m):
        data = read_data()
        text = f"بازی مساوی شد"
        data={}
        write_data(data)
        bot.send_text(m.object_guid, text)
        g.clear
for m in bot.on_message(filters=[""]):
	try:

		print(m.text)
		word = m.text
		textt = word
		title = m.author_title
		name = m.author_guid
		
		
		
#		data = load(open("yad.json","r"))
		if m.chat_type == "Group":
			if m.text == "لیست قفل ها":
				text = f'''
     🔑لیست قفل ها به شکل زیر است:

قفل گیف : {no_gifs}
قفل ویس : {no_Voice}
قفل ویدیو : {no_Video}
قفل عکس : {no_Image}

🗝دیگر قفل ها:
مدیریت گپ : {dastorat_gap}
سخنگو : {sokhan}
ضد لینک : {zed__link}
پیوی روشن/خاموش : {on_bot}
     '''
				l = text.replace("False","🔓")
				k = l.replace("True","🔒")
				m.reply(k)
			if m.text.startswith("مسدود"):
				Thread(target=blok,args=[m]).start()
			if m.text.startswith("حذف مسدودیت"):
				Thread(target=blok,args=[m]).start()
			if m.text == "پیوی خاموش":
				if m.author_guid in Addmins:
					on_bot = False
					m.reply("ربات خاموش شد.")
			if m.text == "پیوی روشن":
				if m.author_guid in Addmins:
					on_bot = True
					m.reply("ربات روشن شد.")
			if m.text == "قفل گیف روشن":
				admin = bot.get_admin_members(m.object_guid,just_get_guids=True)
				if m.author_guid in admin:
					no_gifs = True
					m.reply("قفل گیف با موفقیت روشن شد.")
			if m.text == "قفل گیف خاموش":
				admin = bot.get_admin_members(m.object_guid,just_get_guids=True)
				if m.author_guid in admin:
					no_gifs = False
					m.reply("قفل گیف با موفقیت خاموش شد.")
					
					
			if m.text == "قفل ویس روشن":
				گ
				if m.author_guid in Addmins:
					no_Voice = True
					m.reply("قفل ویس با موفقیت روشن شد.")
			if m.text == "قفل ویس خاموش":
				
				if m.author_guid in Addmins:
					no_Voice = False
					m.reply("قفل ویس با موفقیت خاموش شد.")
				
						
			if m.text == "قفل ویدیو روشن":
				
				if m.author_guid in Addmins:
					no_Video = True
					m.reply("قفل ویدیو با موفقیت روشن شد.")
			if m.text == "قفل ویدیو خاموش":
				
				if m.author_guid in Addmins:
					no_Video = False
					m.reply("قفل ویدیو با موفقیت خاموش شد.")
					
			if m.text == "قفل عکس روشن":
				
				if m.author_guid in Addmins:
					no_Image = True
					m.reply("قفل عکس با موفقیت روشن شد.")
			if m.text == "قفل عکس خاموش":
				
				if m.author_guid in Addmins:
					no_Image = False
					m.reply("قفل فایل با موفقیت روشن شد.")
			if m.text == "قفل فایل روشن":
				
				if m.author_guid in Addmins:
					no_File = True
					m.reply("قفل عکس با موفقیت روشن شد.")
			if m.text == "قفل فایل خاموش":
				
				if m.author_guid in Addmins:
					no_File = False
					m.reply("قفل فایل با موفقیت خاموش شد.")
					
			elif m.text == "روشن":
				if m.author_guid in Addmins:
					on_bot = True
					m.reply("ربات روشن شد.")
			elif m.text == "مدیریت گپ خاموش":
				if m.author_guid in Addmins:
					onn_bot = False
					m.reply("مدیریت گپ خاموش شد.")
			elif m.text == "مدیریت گپ روشن":
				if m.author_guid in Addmins:
					onn_bot = True
					m.reply("مدیریت گپ روشن شد.")
			elif m.text == "سخنگو خاموش":
				if m.author_guid in Addmins:
					sokhan = False
					m.reply("سرگرمی خاموش شد.")
			elif m.text == "سخنگو روشن":
				if m.author_guid in Addmins:
					sokhan = True
					m.reply("سخنگو روشن شد.")
			elif m.text == "جوین اجباری خاموش":
				if m.author_guid in Addmins:
					join__guid = False
					m.reply("جوین اجباری با موفقیت خاموش شد.")
			elif m.text == "جوین اجباری روشن":
				if m.author_guid in Addmins:
					join__guid = True
					m.reply("جوین اجباری با موفقیت روشن شد.")
			elif m.text == "ضد لینک روشن":
				if m.author_guid in Addmins:
					zed__link = True
					m.reply("ضد لینک روشن شد.")
			elif m.text == "ضد لینک خاموش":
				if m.author_guid in Addmins:
					zed__link = False
					m.reply("ضد لینک خاموش شد.")
			if m.object_guid in group and on_bot == True:
				usernames.append(name)
				
				
				if zed__link == True:
					if name in de:
						Thread(target=dol,args=[m]).start()
					if m.is_forward == True:
						Thread(target=zed_link,args=[m]).start()
					if "@" in m.text or "http" in m.text or "ir" in m.text or "www" in m.text:
						Thread(target=zed_link,args=[m]).start()
				if not m.author_guid in black_list or de:
					if m.text.startswith("تنظیم لقب "):
						Thread(target=laghab,args=[m]).start()
					if m.text.startswith("رل بزنیم") or m.text.startswith("برلیم") or m.text.startswith("رل میزنی؟"):
						Thread(target=rell,args=[m]).start()
					if m.text.startswith("کات"):
						Thread(target=cutt,args=[m]).start()
						
					if m.text.startswith("Bot") or m.text.startswith("بات") or m.text.startswith("ربات"):
						Thread(target=ROBOT,args=[m]).start()
					if m.text.startswith("آمار گپ"):
						Thread(target=hadi,args=[usernames]).start()
					if m.text == "نمایش لیست سیاه":
						Thread(target=bloooo,args=[m]).start()
					if m.text == "نمایش لیست ادمین" or m.text == "نمایش لیست ادمین ها":
						Thread(target=ad_min,args=[m]).start()
					if m.text == "پاکسازی لیست سیاه":
						Thread(target=bloooo2,args=[m]).start()
					if m.text == "آمار من" or m.text == "امار من":
						Thread(target=my_amar,args=[m]).start()
						#مدیریت گپ
				if dastorat_gap == True:
					if m.text == "آپدیت قوانین":
						Thread(target=up_qavanin,args=[m]).start()
					if m.text == "قوانین":
#						rules = open("rules.txt","r",encoding='utf-8').read()
						Thread(target=m.reply, args=[on_and_off[0]]).start()
					if m.text == "mute" or m.text == "میوت":
						Thread(target=mute,args=[m]).start()
					if m.text == "unmute" or m.text == "ان میوت":
						Thread(target=unmute,args=[m]).start()
					if m.text == "ادمین" or m.text == "ارتقا" or m.text == "!admin":
						Thread(target=adminkon,args=[m]).start()
					if m.text == "عزل" or m.text == "برکناری" or m.text == "!back":
						Thread(target=unadminkon,args=[m]).start()
					if m.text.startswith("unban ") or m.text.startswith("آنبن ") or m.text.startswith("انبن "):
						Thread(target=unbann2,args=[m]).start()
					if m.text.startswith("ban ") or m.text.startswith("بن "):
						Thread(target=bann2,args=[m]).start()
					if m.text == "ban" or m.text == "بن":
						Thread(target=bann,args=[m]).start()
					if m.text == "آنبن" or m.text == "انبن":
						Thread(target=unbann,args=[m]).start()
					if m.text == "اخطار":
						if m.author_guid in Addmins:
							
							hh = m.reply_message_id
							jjj = bot.get_messages_by_id(m.object_guid, [hh])["messages"]
							target_info = jjj[0]["author_object_guid"]
							ek_k3(m)
					if m.text == "تغییر پروف" or m.text == "تغییر پروفایل":
						Thread(target=prof,args=[m]).start()
					if m.text == "سنجاق" or m.text == "پین" or m.text == "pin" or m.text == "Pin" or m.text == "!pin":
						Thread(target=snajagh,args=[m]).start()
					if m.text == "برداشتن سنجاق" or m.text == "برداشتن پین" or m.text == "unpin" or m.text == "انپین" or m.text == "آنپین":
						Thread(target=unsnajagh,args=[m]).start()
					if m.text == "ویسکال" or m.text == "کال" or m.text == "voicecall" or m.text == "Voicecall" or m.text == "!call":
						j = bot.get_admin_members(m.object_guid,just_get_guids=True)
						if m.author_guid in j:
							pl = bot.create_voice_chat(m.object_guid)
							voice_chat_id = pl["chat_update"]['chat']['group_voice_chat_id']
							m.reply("ویسکال با موفقیت ایجاد شد.")
							bot.join_voice_chat(m.object_guid,hh,voice_chat_id)
						else:
							m.reply("شما ادمین نیستید.")
					elif m.text == "قطع ویسکال" or m.text == "بستن کال" or m.text == "قطع کال" or m.text == "ان کال" or m.text == "بستن ویسکال":
						j = bot.get_admin_members(m.object_guid,just_get_guids=True)
						if m.author_guid in j:
							bot.discard_voice_chat(m.object_guid, voice_chat_id)
							m.reply("ویسکال با موفقیت قطع شد.")
						else:
							m.reply("شما ادمین نیستید.")
					if m.text == "بستن" or m.text == "بستن گپ" or m.text == "lock" or m.text == "Lock" or m.text == "قفل":
						Thread(target=baste,args=[m]).start()
					if m.text == "باز" or m.text == "انلاک" or m.text == "آنلاک" or m.text == "open" or m.text == "!open":
						Thread(target=bazz,args=[m]).start()
#					if m.text == "تغییر نام ":
#						text = m.text.replace("تغییر نام ","")
#						Thread(target=nsme2,args=[m]).start()
						
					if m.text == "تغییر نام":
						Thread(target=nsme1,args=[m]).start()
						#پیام های شیشه ای
				if Welcome == True:
					if m.event_type == "RemoveGroupMembers":
						rimo += 1
						Thread(target=m.reply, args=["سیکتیر شدی خخخخخ"]).start()
					if m.event_type == "JoinedGroupByLink":
						
						jon += 1
						join_grop = [f"سلام عزیزم به گپ {m.title} خوش اومدی🤍","درود کاربر عزیز ورود شماره به گپ خوش آمد میگم😉","خوش اومدی دوست من خوشحالم که عضو شدی. برای دریافت دستورات کلمه دستورات رو ارسال کن."]
						k = choice(join_grop)
						Thread(target=m.reply, args=[k]).start()
					if m.event_type == "LeaveGroup":
						lef += 1
						join_grop = [f"خداحافظ عزیزم👌","رفتنی همیشه میره...","موندی های های نموندی بای بای"]
						k = choice(join_grop)
						Thread(target=m.reply, args=[k]).start()
						
						
						
				if no_File == True:
					
					kk = m.file_inline['type']
					if kk == "File":
						Thread(target=dol,args=[m]).start()
						
					
				if no_Video == True:
					
					kk = m.file_inline['type']
					if kk == "Video":
						Thread(target=dol,args=[m]).start()
					
				if no_Voice == True:
					
					kk = m.file_inline['type']
					if kk == "Voice":
						Thread(target=dol,args=[m]).start()
					
				if no_Image == True:
					
					kk = m.file_inline['type']
					if kk == "Image":
						Thread(target=dol,args=[m]).start()
					
				if no_gifs == True:
					ghofl = m.file_inline['type']
					if ghofl == "Gif":
						Thread(target=dol,args=[m]).start()
						#سرگرمی ها
						
				if m.text == "راهنما":
					text = '''[🌻] - کاربر گرامی بخش دستورات به شرح زیر است. برای دریافت دستور ها تایپ کنید

[⏰] - بخش دستورات گپ برای ادمین ها :
● تنظیمات گپ ●

[⚙] - بخش سرگرمی و بازی ها :
● سرگرمی ها ●

[💰] - User : @zamingir'''
					Thread(target=m.reply, args=[text]).start()
				if m.text == "تنظیمات گروه" or m.text == "تنظیمات گپ":
					text = f'''
0|[🪴] - کاربر [    {title}    ] به بخش تنظیمات گروه خوش امدید .

1|[🍔]¹ - دستور : [ بن ]
 حذف کاربر با ریپلای 

1|[🍔]³ - دستور : [ بن @info ]
 حذف کاربر با ایدی 

2|[🍖]⁵ - دستور : [ انبن ]
 ان بن کاربر با ریپلای 

2|[🍖]⁷ - دستور : [ انبن @info ]
 ان بن کاربر با ایدی 

3|[🥮]⁹ - دستور : [ بستن گپ ]
 گروه بسته میشود

4|[🫘]¹¹ - دستور : [ انلاک ]
 گروه باز میشود 

5|[⚙]¹² - دستور : [ پین ]
 متن موردنظر با ریپلای پین شده 

6|[🔩]¹³ - دستور : [ انپین ]
 متن موردنظر پین شده با ریپلای ان پین می‌شود

7|[☕️]¹⁴ - دستور : [ تغییر پروفایل ]
روی عکس مورد نظر ریپلای کند تا بزاره پروف

8|[🫕]¹⁵ - دستور : [ تغییر نام ]
رو پیام ریپلای کند تا بزاره برای اسم گپ

9|[💎]¹⁶ - دستور : [ ارتقا ]
 کاربر موردنظر با ریپلای ادمین میشود

10|[🍭]¹⁷ - دستور : [ عزل ]
کاربر موردنظر با ریپلای از ادمین بودن عزل میشود

11|[🔆]¹⁸ - دستور : [ مسدود ]
کاربر موردنظر با ریپلای از به لیست مسدود شده های ربات اضافه میشود و بات دیگه جوابشو نمیده

12|[〽️]¹⁹ - دستور : [ حذف مسدودیت ]
کاربر موردنظر با ریپلای از لیست سیاه ربات خارج میشه

13|[🎲]²⁰ - دستور : [ mute ]
کاربر موردنظر با ریپلای به لیست سکوت اضافه میشود و هر پیامی بدهد پاک میشود 

14|[🎗]²¹ - دستور : [ unmute ]
کاربر موردنظر با ریپلای از لیست سکوت خارج میشود
'''
					Thread(target=m.reply, args=[text]).start()

				if m.text == "سرگرمی ها":
					text = f'''
[🪴] - کاربر [    {title}    ] به بخش سرگرمی ها خوش امدید .

1| [ معادله ریاضی ]
روی سوال ریپلای کنید و جواب رو بنویسید به این صورت [جواب 10]

2| [ دوز ]
بنویسید دوز فقط تا بازی کنید

3| [ ج ح ]
بازی جرعت حقیقت

4 با نوشتن کلمه [ امتیاز های من ] امتیاز هاتون رو نمایش میده 

5| [ کی ... ]
به جای ... متن مورد نطرتونو بنویسید

6| [ ناموسی ]
رو کاربر ریپلای کنید و بنویسید ناموسی فوشش میده

7| [ بگو ... ]
به جای ... متن مورد نطرتونو بنویسید تا ربات متنتونو از زبان خودش بنویسه

8| [ وضعیت من  ]
وضعیتتونو نشون میده


9| [ امار من  ]
امارتونو نشون میده

🩵 چیزایی که نیاز به توضیح ندارن :
ذکر
دیالوگ
تاریخ
ساعت 
بیو
جوک
پ ن پ
حدیث 
الکی
داستان


💎دستورات و سرگرمی های کاربردی : 

1-تنظیم لقب : روی کاربر ریپلای کنید و بنویسد تنظیم لقب ... | دستور برای ادمین ها 

2-رل بزنیم : با ربات رل میزنید و ربات کمتر فوشتون میده 

3-کات : با ربات کات میکنید و باز فوشتون میده

4- دستور [logo1 name] : به جای name اسمتونو بزنید 

5-دستور [logo2 name] : به جای name اسمتونو بزنید

6-صدای زن تکست : ویس با صدای زن به جای تکست متنتونو بزنید 

7-صدای مرد تکست : ویس با صدای زن به جای تکست متنتونو بزنید

8-دستور [font name] : به جای name اسمتونو بزنید

9-دستور [فونت نام] : به جای نام اسمتونو بزنید

10-دستور [+ سلام] : به جای سلام متنتونو بزنید تا هوش مصنوعی جواب بده

11-دستور [! سلام] : به جای سلام متنتونو بزنید تا هوش مصنوعی شیطانی جواب بده
'''
					Thread(target=m.reply, args=[text]).start()
				if sokhan == True:
					
					
					if m.text in ['/doz', '/Doz', 'doz', 'Doz', 'دوز']:
						Thread(target=start_game,args=[m]).start()
					if m.text in ['/left', '/Left','لفت','توقف']:
						data = read_data()
						if m.author_guid in data[m.object_guid]['players']:
							data.clear()
							m.reply("بازی متوقف شد.")
					if m.text in ['/join', '/Join', 'join', 'Join', 'جوین']:
						Thread(target=save_player2_info,args=[m]).start()
					for n in range(10):
						if m.text== str(n):
							Thread(target=turn,args=[m]).start()
					if m.text.startswith("+ ") and join(m):
						Thread(target=chat_gpt,args=[m]).start()
					if m.text.startswith("! ") and join(m):
						Thread(target=chat_gpt2,args=[m]).start()
					if m.text.startswith("logo ") and join(m):
						Thread(target=logo,args=[m]).start()
					if m.text.startswith("logo2 ") and join(m):
						oo = ["graffiti-3d-logo","neon-logo","booking-logo","comics-logo","water-logo","fire-logo","clan-logo","my-love-logo","blackbird-logo","smurfs-logo","style-logo","runner-logo","fluffy-logo","glow-logo","crafts-logo","fabulous-logo","amped-logo","graffiti-logo","graffiti-burn-logo","star-wars-logo","graffiti-3d-logo","scribble-logo","chrominium-logo","harry-potter-logo","world-cup-2014-logo","heavy-metal-logo","thanksgiving1-logo","april-fools-logo","beauty-logo","winner-logo","silver-logo","steel-logo","global-logo","inferno-logo","birdy-logo","roman-logo","minions-logo","superfit-logo","fun-and-play-logo","brushed-metal-logo","birthday-fun-logo","colored2-logo","swordfire-logo","flame-logo","wild-logo","street-sport-logo","surfboard-white-logo","amazing-3d-logo","flash-fire-logo","uprise-logo","sugar-logo","robot-logo","genius-logo","cereal-logo","kryptonite-logo","patriot-logo","holiday-logo","sports-logo","thanksgiving2-logo","trance-logo","spider-men-logo","theatre-logo","vintage-racing-logo","ninja-logo","bumblebee-logo","vampire-logo","sunrise-logo","monsoon-logo","strongman-logo","game-over-logo"]
						ttt = choice(oo)
						Thread(target=logo2,args=[m]).start()
					if m.text.startswith("فونت "):
						Thread(target=font2,args=[m]).start()
					if m.text.startswith("صدای مرد "):
						Thread(target=voice,args=[m]).start()
					if m.text.startswith("صدای زن "):
						Thread(target=voice2,args=[m]).start()
					if m.text.startswith("font "):
						Thread(target=font1,args=[m]).start()
					if m.text =="pa na pa" or m.text.startswith("پ ن پ"):
						Thread(target=pa_na_pa,args=[m]).start()
					if m.text =="جوک" :
						Thread(target=jok,args=[m]).start()
					if m.text =="داستان" :
						Thread(target=dastan,args=[m]).start()
					if m.text =="الکی" and join(m):
						Thread(target=alaki,args=[m]).start()
					if m.text =="حدیث" :
						Thread(target=hadis,args=[m]).start()
					if m.text.startswith("بیو") or m.text.startswith("بیوگرافی"):
						Thread(target=bio,args=[m]).start()
				
					if m.text.startswith("ساعت"):
						Thread(target=time,args=[m]).start()
					if m.text =="دیالوگ" and join(m):
						Thread(target=m.reply, args=[requests.get("http://api.codebazan.ir/dialog/").text]).start()
					if m.text =="ذکر" and join(m):
						Thread(target=zekr,args=[m]).start()
					if m.text.startswith("ج ح") or m.text.startswith("ح ج") or m.text.startswith("جرعت حقیقت") and join(m):
						text = choice(j_h)
						m.reply(text)
					if "معادله ریاضی" in m.text:
						question, answer = generate_question()
						h = f"سوال: {question} \nبه این صورت جواب بدید [جواب ...] \n به جای ... جواب خودتون رو بنویسید"
						user_answer = m.reply(f"{h} \nپاسخ خود را وارد کنید: ")
					elif "جواب " in m.text:
						Thread(target=check_answer,args=[m, answer]).start()
						
					if "امتیاز های من" in m.text:
						if name in scores:
							m.reply(f"امتیاز شما: {scores[name]}")
						else:
							m.reply("شما هنوز بازی نکرده‌اید!")
					if m.text.startswith("کی "):
						Thread(target=te_ki,args=[m]).start()
					if namoss == True:
						if m.text.startswith("ناموسی") and join(m):
							
							text = choice(namosi)
							Thread(target=bot.send_text, args=[m.object_guid, text, m.reply_message_id]).start()
							
					if m.text.startswith("بگو "):
						text_bgo = m.text.split("بگو")[1]
						Thread(target=bot.send_text, args=[m.object_guid, f"{text_bgo}", m.reply_message_id]).start()
					if m.text.startswith("خانومم") or m.text.startswith("نفسم") or m.text.startswith("عشقم") or m.text.startswith("زیدم"):
						sd2 = "اه اه اه چندش عشق چیه","هعی به شما نگا میکنم حسودیم میشه من کسیو ندارم خیلی تنهام","اصلا حال میکنم وقتی میبینم عین این چندشا آخر کلمات میم مالکیت میزاری"
						slll2 = choice(sd2)
						Thread(target=m.reply, args=[slll2]).start()
					if m.text.startswith("چشم") or m.text.startswith("حتما") or m.text.startswith("باشه") or m.text.startswith("باش"):
						sd3 = "آفرین","تو چقد حرف گوش کنی بیا عروس ننم شو","کونم بخوام اینجوری تایید میکنی؟"
						sd4 = "آفرین","تو چقد حرف گوش کنی بیا عروس ننم شو"
						slll3 = choice(sd3)
						sdd = choice(sd4)
						if not m.author_guid in rel:
							Thread(target=m.reply, args=[slll3]).start()
						else:
							Thread(target=m.reply, args=[sdd]).start()
					if m.text == "بوس" or m.text == "بوس بده":
					 	bos_random = "Voice/ی بوس بده بیاد.mp3" , "Voice/جون لبو رد کن بیاد(1).mp3"
					 	bos = choice(bos_random)
					 	Thread(target=bot.send_voice, args=[m.object_guid, bos, m.message_id]).start()
					elif findall("ننت",m.text) or findall("جنده",m.text):
						Thread(target=dalam3,args=[m]).start()
					elif m.text == "صلم" or m.text == "صلام" or m.text == "دلام" or m.text == "سلم" or m.text == "سلام" or m.text == "جلام" or m.text == "سلمح" or m.text == "شلام":
						Thread(target=dalam,args=[m]).start()
					elif m.text.startswith("کس") or m.text.startswith("کص"):
						Thread(target=one,args=[m]).start()
					
					elif m.text.startswith("بکن") or m.text.startswith("بوکون") or m.text.startswith("نمیکنی") or m.text.startswith("کن"):
						Thread(target=two,args=[m]).start()
					elif m.text.startswith("بده") or m.text.startswith("بیده") or m.text.startswith("نمیدی") or m.text.startswith("بیدا"):
						Thread(target=three,args=[m]).start()
					elif m.text.startswith("🤣") or m.text.startswith("🤣🤣") or m.text.startswith("😂"):
						Thread(target=four,args=[m]).start()
					if m.text == "وضعیت من" or m.text == "وضعیت":
						Thread(target=VAZEAT,args=[m]).start()
	except:pass
