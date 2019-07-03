## Nuke The Duplicates
## Deletes Computers in list that exist in another list
## Dan Pullan (https://danielpullan.co.uk) 02/07/2019

## import needed stuff
import csv


## list of machines with 2016
with open('has2016.csv', 'r') as f:
		reader = csv.reader(f)
		has_2016 = list(reader)


## list of computers that exist
with open('exist.csv', 'r') as f:
		reader = csv.reader(f)
		exists = list(reader)

## for every item in exists, see if exists in 2016 list
## if it does, print it to the output file
## if it doesn't, just print "no2016" for debugging purposes
with open("output.txt", "a") as f:
	for x in exists:
		if x in has_2016:
			print("has2016")
			print(x, file=f)
		else:
			print("no2016")