import database
import smtplib
from email.mime.text import MIMEText
def send_sharing_email(address, time, duration, rid):
	db = database.Database()
	roomSpecs = db.queryRoomSpecs(rid)
	text = "Hi, this is a notification Email of a room reservation that expects you to attend. The reservation is at " + time + " at " + roomSpecs[0][1] + " for " + duration
	msg = MIMEText(text)
	msg['Subject'] = "Confirmation From GroupSpace"
	msg['From'] = "noreply@groupspaceuiuc.com"
	msg['To'] = address
	s = smtplib.SMTP('localhost')
	s.sendmail('noreply@groupspaceuiuc.com', [address], msg.as_string())
	s.quit()	
