import sqlite3
import time
import string
import secrets
import subprocess
import re
import time
import datetime
import sys
from datetime import date
import csv
from random import randint


listdbase = ['AllSegForce_34018_2020-04-03.db',
	'AllSegForce_45028_2020-04-03.db',
	'AllSegForce_25084_2020-04-06.db',
	'AllSegForce_42619_2020-04-06.db',
	'AllSegForce_85247_2020-04-06.db',
	'AllSegForce_23455_2020-04-06.db',
	'AllSegForce_74262_2020-04-06.db',
	'AllSegForce_28373_2020-04-06.db',
	'AllSegForce_16995_2020-04-06.db',
	'AllSegForce_78662_2020-04-06.db',
	'AllSegForce_64875_2020-04-06.db',
	'AllSegForce_76390_2020-04-06.db',
	'AllSegForce_81703_2020-04-06.db',
	'AllSegForce_67492_2020-04-06.db',
	'AllSegForce_23611_2020-04-06.db',
	'AllSegForce_42829_2020-04-06.db',
	'AllSegForce_35603_2020-04-06.db',
	'AllSegForce_76334_2020-04-06.db',
	'AllSegForce_40029_2020-04-06.db',
	'AllSegForce_28003_2020-04-06.db',
	'AllSegForce_12936_2020-04-06.db',
	'AllSegForce_71560_2020-04-06.db',
	'AllSegForce_22586_2020-04-06.db',
	'AllSegForce_32234_2020-04-06.db',
	'AllSegForce_71737_2020-04-06.db',
	'AllSegForce_10549_2020-04-06.db',
	'AllSegForce_51401_2020-04-06.db',
	'AllSegForce_6832_2020-04-06.db',
	'AllSegForce_3357_2020-04-06.db',
	'AllSegForce_89745_2020-04-06.db',
	'AllSegForce_3158_2020-04-06.db',
	'AllSegForce_74771_2020-04-06.db',
	'AllSegForce_45922_2020-04-06.db',
	'AllSegForce_5972_2020-04-06.db',
	'AllSegForce_6798_2020-04-06.db',
	'AllSegForce_78998_2020-04-06.db',
	'AllSegForce_56572_2020-04-06.db',
	'AllSegForce_27868_2020-04-06.db',
	'AllSegForce_5600_2020-04-06.db']


def GEN_TABLE_MERGE():
	conn = sqlite3.connect("MergedResults.db")
	c = conn.cursor()
	cmd = ("create table IF NOT EXISTS  ctf4(val int, vald int, timerA float, timerB float, timerC float, timerD float )")
	c.execute(cmd)
	
	# Save (commit) the changes
	conn.commit()

	# We can also close the connection if we are done with it.
	# Just be sure any changes have been committed or they will be lost.
	conn.close()

def GEN_TABLE(database):
	conn = sqlite3.connect(database)
	c = conn.cursor()
	
	cmd = ("create table IF NOT EXISTS resultsText (val_a int, cmd varchar(2000), cmt varchar(2000))")
	
	c.execute(cmd)
	
	# Save (commit) the changes
	conn.commit()

	# We can also close the connection if we are done with it.
	# Just be sure any changes have been committed or they will be lost.
	conn.close()
	
	
def loopSegment(database, val, cmds, comment):
	conn = sqlite3.connect(database)
	c = conn.cursor()
	
	
	cmd = ("INSERT INTO resultsText VALUES (%s,'%s','%s')") % (val, cmds, comment)
	c.execute(cmd)
	conn.commit()
	conn.close()
	
def select_all_tasks(src_db, dest_db):
	conn_src = sqlite3.connect(src_db)
	conn_dest = sqlite3.connect(dest_db)
	
	c_src = conn_src.cursor()
	c_dest = conn_dest.cursor()
	
	c_src.execute("SELECT * FROM ctf4")
 	
	rows = c_src.fetchall()
	for row in rows:
		val = row[0]
		vald = row[1]
		timerA = row[2]
		timerB = row[3]
		timerC = row[4]
		timerD = row[5]
		cmd = ("INSERT INTO ctf4 VALUES (%s,%s,%f,%f,%f,%f)") % (val, vald, timerA,timerB,timerC,timerD)
		c_dest.execute(cmd)
		conn_dest.commit()

	conn_src.close()
	conn_dest.close()

				
def insertResults(database, val, cmds, comment):
	conn = sqlite3.connect(database)
	c = conn.cursor()
	cmd = ("INSERT INTO resultsText VALUES (%s,'%s','%s')") % (val, cmds, comment)
	c.execute(cmd)
	conn.commit()
	conn.close()


GEN_TABLE_MERGE()
for listdb in listdbase:
	select_all_tasks(listdb, "MergedResults.db")


