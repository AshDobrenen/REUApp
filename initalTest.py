from imports import *
#this is to test the opening of the website file, finding the data-attribute code, and exporting it to a csv. 
#after I will add a new file to do this for all the test websites to one csv, and all the training websites to another
###########
#opening and reading the website


###########
#extracting and saving sata-attributes to database

###########
#exporting to a csv
#headers = item, features, code
listOfHeaders = []
savePath = 
fileName = "initalTest.csv"
fullName = os.path.join(savePath, fileName)

with open(fullName, "a", newline="") as h:
  writer = csv.writer(h)
  writer.writerow(listOfHeaders)
 
#writing out the content of the database
with open(fullName, "a", newline="") as c:
  writer = csv.writer(c)
  writer.writerow(tlist)

#with open(fullName, "r", newline="") as r:
#  reader = csv.reader(r)
#  lines = len(list(reader))
#  print("[",lines,"]", "form!")
