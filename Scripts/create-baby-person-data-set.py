import csv
from criteria import Criteria


if __name__ == "__main__":

	c = Criteria()

	with open("../Inputs/test_policy_data.csv", "rB") as i, open("../Outputs/baby_people_data.csv", "w") as o:
		writer = csv.writer(o)

		for row in i.readlines():

			print row[0]


			# arbitrary header check
			if "State" in row[0]:
				c.set_headers(row)
				
				continue

			elif c.criteria_already_met(row):
				continue

			else:

				writer.writerow(row)