import gps
import MySQLdb
import sys
import time

con = MySQLdb.connect("wisudapenstelkom13.com","d3tb13","12345qwerty","d3tb13_data")
cur = con.cursor()

# Listen on port 2947 (gpsd) of localhost
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

while True:
	try:
		#z=time.time()
		report = session.next()
		
		if hasattr(report, 'lat'):
			print 'latitude:  ' , report.lat
		if hasattr(report, 'lon'):
			print 'longitude: ' , report.lon
		if hasattr(report, 'time'):
			print 'time: ' , report.time

			lat=float(report.lat)
			lon=float(report.lon)
			time=report.time			

			sql = "INSERT INTO `koordinat` (`lat`,`lng`,`time`) VALUE ('%g', '%g', '%s')" % (lat, lon, time)
 
			try:
				cur.execute(sql)
				con.commit()
				print "Input Data Berhasil"
			    	print cur._last_executed
			
			except:
			   	con.rollback()
			   	print "Input Data Gagal"
			   	print cur._last_executed
			       	
	except KeyError:
		pass
	except KeyboardInterrupt:
		quit()
	except StopIteration:
		session = None
		print "GPSD has terminated"

