from imports import *
from initalTestURL import *
#this is to test the opening of the website file, finding the data-attribute code, and exporting it to a csv. 
#after I will add a new file to do this for all the test websites to one csv, and all the training websites to another
###########
#opening and reading the website
def getWebCode(urls)
  tFile = open(urls, 'r')
  
  soup = BeautifulSoup(tFile,"html5lib")
  
  
###########
#extracting and saving sata-attributes to database
def getDataPoints(turls):
  smth = getWebCode(turls)
  
  
###########
#exporting to a csv
def writeHeaders():
#headers = item, features, code
  listOfHeaders = []
  savePath = "C:\Users\bluec\OneDrive\Desktop\ODU"
  fileName = "initalTest.csv"
  fullName = os.path.join(savePath, fileName)

  with open(fullName, "a", newline="") as h:
    writer = csv.writer(h)
    writer.writerow(listOfHeaders)
 

def writeCSV(itlist):
  savePath = "C:\Users\bluec\OneDrive\Desktop\ODU"
  fileName = "initalTest.csv"
  fullName = os.path.join(savePath, fileName)
  #writing out the content of the database
  with open(fullName, "a", newline="") as c:
    writer = csv.writer(c)
    writer.writerow(tlist)

  #with open(fullName, "r", newline="") as r:
  #  reader = csv.reader(r)
  #  lines = len(list(reader))
  #  print("[",lines,"]", "form!")

def main():
  writeHeader()
  #loop through all websites
  for i in range(0,2):
    print(writeCSV(getDataPoints(iturl[i])))
