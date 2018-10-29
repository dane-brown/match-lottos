from entries import Entry
import csv

class Result:
	def __init__(self, mainballs, sub1, sub2):
		self.mainballs = mainballs
		self.sub1 = sub1
		self.sub2 = sub2

	def get_results(self):
		print(self.mainballs)

	def __str__(self):
		return self.mainballs


resultTicket = 'Uploads/norway_06-11-2019_87685_result.csv'

with open(resultTicket) as f:
	reader = csv.DictReader(f, delimiter= ';', fieldnames=('mainballs', 'sub1', 'sub2'))
	next(reader)
	Results = [row for row in reader]

for row in Results:
	row = Result(row['mainballs'], row['sub1'], row['sub2'])
	print(row)
