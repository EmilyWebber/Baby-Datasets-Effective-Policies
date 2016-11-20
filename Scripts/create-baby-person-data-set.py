import csv
import pandas as pd
from criteria import Criteria
import random

def get_writer(filename):
	o = open(filename, "w")
	writer = csv.writer(o)
	writer.writerow(["State", "Year", "Age", "Gender", "Race", "Household Income"])
	return writer

def write_test_data(c, writer):

	for state in ["Michigan", "Georgia", "Ohio", "Missouri", "Delaware", "Arizona", "Indiana", "NorthCarolina", "Oregon", "Washington"] :
		for year in ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014"]:
			hhincome = random.randint(0, 100000)
			row = [state, year, "6-16", "Black", "Female", hhincome]
			# print "About to write {} to disk".format(row)
			writer.writerow(row)


if __name__ == "__main__":

	c = Criteria()

	writer = get_writer("../Outputs/baby-test-file.csv")

	write_test_data(c, writer)