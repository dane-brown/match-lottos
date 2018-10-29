import csv

# Tickets
entryTicket = 'Uploads/norway_06-11-2019_87685.csv'

# Results
resultTicket = 'Uploads/norway_06-11-2019_87685_result.csv'


with open(entryTicket) as f:
	reader = csv.DictReader(f, delimiter= ';', fieldnames=('ticket_id', 'mainballs', 'sub1', 'sub2'))
	next(reader)
	Entries = [row for row in reader]

with open(resultTicket) as f:
	reader = csv.DictReader(f, delimiter= ';', fieldnames=('mainballs', 'sub1', 'sub2'))
	next(reader)
	Results = [row for row in reader]

for row in Entries:
	matched_mainball = []
	matched_sub1 = []
	matched_sub2 = []
	mainballs = [int(x) for x in row['mainballs'].split(':')]
	sub1 = row['sub1']
	sub2 = row['sub2']
	ticket_id = row['ticket_id']

	for row in Results:
		mainballs_result = [int(x) for x in row['mainballs'].split(':')]
		sub1_result = row['sub1']
		sub2_result = row['sub2']

		# Match Mainballs
		for number in mainballs_result:
			if(number in mainballs):
				matched_mainball.append(number)


		# Match Sub 1
		for number in sub1_result:
			if(number in sub1):
				matched_sub1.append(number)

		# Match Sub 2
		for number in sub2_result:
			if(number in sub2):
				matched_sub2.append(number)

	# Console Display
	print "ID - " + ticket_id
	print "Matched Mainballs " + str(matched_mainball) + " (" + str(len(matched_mainball)) + ")"
	print "Matched Sub1 " + str(matched_sub1) + " (" + str(len(matched_sub1)) + ")"
	print "Matched Sub2 " + str(matched_sub2) + " (" + str(len(matched_sub2)) + ")"
	if (len(matched_mainball) == len(mainballs_result) and len(matched_sub1) == len(sub1_result) and len(matched_sub2) == len(sub2_result)):
		print "!!! JACKPOT !!!"
	print "---------------"

	# Write to file
	with open('results.txt', "a") as f:
		f.write("ID - " + ticket_id + '\n')
		f.write("Matched Mainballs " + str(matched_mainball) + " (" + str(len(matched_mainball)) + ")" + '\n')
		f.write("Matched Sub1 " + str(matched_sub1) + " (" + str(len(matched_sub1)) + ")" + '\n')
		f.write("Matched Sub2 " + str(matched_sub2) + " (" + str(len(matched_sub2)) + ")" + '\n')
		if (len(matched_mainball) == len(mainballs_result) and len(matched_sub1) == len(sub1_result) and len(matched_sub2) == len(sub2_result)):
			f.write("!!! JACKPOT !!!" + '\n')
		f.write("---------------" + '\n')

