import csv

class Criteria(object):
	'''
	Is used to handle all of the criteria to create a baby data set 
		For building the architecture of Effective Policies!!!

	This is basically one gigantic dictionary that hashes all of the unique values we need to integers, either 0s or 1s.
		The default is going to be a 0. 

	When we meet the critera,
		we switch the 0 to a 1.

	For the row-by-row iteration in the create_baby_data_set.py,
		We'll pass each row into this class.
		Then we'll index into the critera dictionary.
		If there's a 1,
			we skip the row.
		If there's a 0,
			We write the row to disk, 
			And add a 1 to the dictionary.
	'''

	def __init__(self):
		self.control_state_list = ["Michigan", "Georgia", "Ohio", "Missouri", "Delaware", "Arizona", "Indiana", "NorthCarolina", "Oregon", "Washington"]

		self.year_list = ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014"]

		self.criteria_dictionary = self.create_criteria_dictionary()

		# self.check_criteria()

		self.headers = []

	def set_headers(self, row):
		self.headers = row
		print "Set headers to", row

	def check_criteria(self):
		for y,d in self.criteria_dictionary.items():
			for s,i in d.items():
				print "Looking in state {} in year {}".format(s, y)
				if i == 0:
					print "Haven't found anything yet"
				elif i == 1:
					print "Already found an observation here, moving on"

	def create_criteria_dictionary(self):
		c = {}

		for year in self.year_list:
			
			# make a dictionary for that year
			c[year] = {}

			for state in self.control_state_list:

				c[year][state] = 0


		return c

	def criteria_already_met(self, row):

		age = row[self.headers.index("Age")]

		gender = row[self.headers.index("Gender")]

		race = row[self.headers.index("Race")]

		if age == "Young" and race == "White" and gender == "Female":

			year = row[self.header.index("Year")]

			state = row[self.header.index("State")]

			if self.criteria_dictionary[year][state] == 0:

				self.criteria_dictionary[year][state] == 1

				return False

			else:
				
				return True