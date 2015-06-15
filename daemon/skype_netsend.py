#!/usr/bin/python
# -*- coding: utf-8 -*-
import Skype4Py
import psycopg2
import sys
import time

connection_string=open('./.dbconfig.dat','r').read()
cn=psycopg2.connect(connection_string)
cr=cn.cursor()

cr.execute('INSERT INTO skype_net_send("to", message) VALUES (%s, %s);',(sys.argv[1],sys.argv[2]))
cn.commit()

cr.close()
cn.close()