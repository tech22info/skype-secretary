#!/usr/bin/python
# -*- coding: utf-8 -*-
import Skype4Py
import psycopg2
import sys
import time

reload(sys)
sys.setdefaultencoding('utf-8')
skype = Skype4Py.Skype(Transport='x11')
skype.Attach(Wait=True)

connection_string=open('./.dbconfig.dat','r').read()
cn=psycopg2.connect(connection_string)
cr=cn.cursor()

def message(msg, status):
	# Записываем сообщение в базу данных
	MessageID=msg.Id
	MessageStatus=status
	MessageFrom=msg.FromHandle
	MessageText=msg.Body
	MessageDateTime=msg.Datetime
	MessageChatName=msg.ChatName
	# Добавляем всех недобавленных друзей
	for user in skype.UsersWaitingAuthorization:
		user._SetIsAuthorized(1)
	cr.execute('INSERT INTO skype_messages( skype_id, status, "from", body, message_date,chat_name) \
	VALUES (%s, %s, %s, %s, %s,%s); \
	',(MessageID,MessageStatus,MessageFrom,MessageText,MessageDateTime,MessageChatName,))
	cn.commit()
	return True

skype.OnMessageStatus = message
print ('Демон запущен!')

while(True):
	time.sleep(1)
	try:
		cr.execute('SELECT id, "to", message, send FROM skype_net_send WHERE NOT send ORDER BY id ASC LIMIT 1;')
		message=cr.fetchall()[0]
		message_present=True
	except:
		message_present=False
	if message_present:
		skype.SendMessage(message[1],message[2])
		cr.execute('UPDATE skype_net_send SET send=True WHERE id=%s;',(message[0],))
		cn.commit()

cr.close()
cn.close()