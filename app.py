# Grab a user's parameters
	# Phone Number
	# Year (default: 2017)
	# Semester (default: spring)
	# Subject (course abbreviation)
	# Course (course number)
# Randomly space out time b/w API calls (rate limit or nah?)
	# 'http://courses.illinois.edu/cisapp/explorer/schedule/' + year + '/' + semester + '/' + subject + '/' + course + '.xml?mode=detail'
	# Use lxml to parse the XML file
# Check for a change in enrollment status
	# Log the <enrollmentStatus> from previous API call and compare w/ current call
		# Closed, Open, Open (Restricted)
# If there is a change, send a txt msg notification (using Twilio) with details

import time
import random
import urllib
from xml.etree import ElementTree as ET

###############GLOBALS###############

#ACCOUNT_SID = "AC5f8590705776c63da7c45356f0ab63d5" 
#AUTH_TOKEN = "98afdef9bd6bfb566f4d69f24f126261" 

#client = TRC(ACCOUNT_SID, AUTH_TOKEN) 

counter = range(1, 8)

phone = raw_input('Enter your phone number (no space): ')
year = raw_input('Enter the term year: ')
semester = raw_input('Enter the semester: ')
subject = raw_input('Enter the subject (course abbreviation): ')
course = raw_input('Enter the course number: ')

url = 'http://courses.illinois.edu/cisapp/explorer/schedule/' + str(year) + '/' + semester + '/' + subject + '/' + course + '.xml?mode=detail'
root = ET.parse(urllib.urlopen(url)).getroot()

###############MAIN###############

while True:
	log = {}
	pres = {}
	result = {'Subject': subject, 'CourseNum': course, 'SectionNum': '', 'Status': '', 'OGStatus': ''}

	for child in root:
		if child.tag == 'detailedSections':
			for node in child:
				for sub in node:
					if sub.tag == 'sectionNumber':
						section = str(sub.text)
					if sub.tag == 'enrollmentStatus':
						log[section] = sub.text

	print log

	time.sleep(60*(random.choice(counter)))

	for child in root:
		if child.tag == 'detailedSections':
			for node in child:
				for sub in node:
					if sub.tag == 'sectionNumber':
						section = str(sub.text)
					if sub.tag == 'enrollmentStatus':
						pres[section] = sub.text

	print pres

	if len(log) == len(pres):
		for key in pres:
			if pres[key] != log[key]: # Enrollment status doesn't match




# Dict = {}
# While True:
	# Append each status to a {Section1: 'Status', Section2: 'Status', ...}
	# Delay randomly
	# Append new status' to {Section1: 'Status', Section2: 'Status', ...}
	# Compare dictionaries by section; if there's a change, append SectionNum, Status, and OGStatus to the result dict
		# Send text message using Mike's function
	# Delay