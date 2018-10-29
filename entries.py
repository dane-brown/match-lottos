import csv

class Entry:
	def __init__(self, ticket_id, mainballs, sub1, sub2):
		self.ticket_id = ticket_id
		self.mainballs = mainballs
		self.sub1 = sub1
		self.sub2 = sub2

	def __str__(self):
		return self.ticket_id
	
entryTicket = 'Uploads/norway_06-11-2019_87685.csv'

with open(entryTicket) as f:
	reader = csv.DictReader(f, delimiter= ';', fieldnames=('ticket_id', 'mainballs', 'sub1', 'sub2'))
	next(reader)
	Entries = [row for row in reader]	

for row in Entries:
	row = Entry(row['ticket_id'], row['mainballs'], row['sub1'], row['sub2'])
	# print(row)


