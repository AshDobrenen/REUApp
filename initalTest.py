from imports import *
from initalTestURL import *
#this is to test the opening of the website file, finding the data-attribute code, and exporting it to a csv. 
#after I will add a new file to do this for all the test websites to one csv, and all the training websites to another

###########
#open and then extracting data-attributes and saving all to database
def getDataPoints(turls):
  item, pAlt, pKeyword, redirect, pPicText, picTextLength, picKeywords, pAdSymbol,  lengthAlt, pVideoTag, code = ([] for n in range(11))
  tFile = open(turls, 'r')
  
  soup = BeautifulSoup(tFile,"html5lib")
  #get all of data attributes in the soup
  item = soup.find_all('data-attribute')
  #use that number to create a table that will be filled in and returnd to the main function
  featuresTable = DataFrame()
  #fill in the features and code to the lists individually
  
  #da == dec, code = 1 and vice versa
  #if (
  
  featuresTable[0] = item
  featuresTable[1] = pAlt
  featuresTable[2] = pKeyword
  featuresTable[3] = redirect
  featuresTable[4] = pPicText
  featuresTable[5] = picTextLength
  featuresTable[6] = picKeywords
  featuresTable[7] = pAdSymbol
  featuresTable[8] = lengthAlt
  featuresTable[9] = pVideoTag
  featuresTable[10] = code
 
  #transpose the table to get the rows in the right order
  return  featuresTable.T
###########
#exporting to a csv
def writeHeaders():
#headers = item, features, code(1 or 0 for deceptive or not)
#item is datapoint
#pAlt includes any alt text, play now, close ad, etc
#pKeyword includes ad, paid/sponsered, socials

  listOfHeaders = ["item", "pAlt", "pKeyword", "redirect", "pPicText", "picTextLength", "picKeywords", "pAdSymbol",  "lengthAlt", "pVideoTag", "code"]
  savePath = "C:\\Users\\bluec\\OneDrive\\Desktop\\ODU\\"
  fileName = "initalTest.csv"
  fullName = os.path.join(savePath, fileName)

  with open(fullName, "a", newline="") as h:
    writer = csv.writer(h)
    writer.writerow(listOfHeaders)
 

def writeCSV(itlist):
  savePath = "C:\\Users\\bluec\\OneDrive\\Desktop\\ODU\\"
  fileName = "initalTest.csv"
  fullName = os.path.join(savePath, fileName)
  #writing out the content of the database
  with open(fullName, "a", newline="") as c:
    writer = csv.writer(c)
    writer.writerows(itlist)

def main():
  writeHeaders()
  #loop through all websites
  for i in range(0,2):
    print(writeCSV(getDataPoints(iturl[i])))
