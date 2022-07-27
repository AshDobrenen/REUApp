from imports import *
from initalTestURL import *
#this is to test the opening of the website file, finding the data-attribute code, and exporting it to a csv. 
#after I will add a new file to do this for all the test websites to one csv, and all the training websites to another

###########
#open and then extracting and saving sata-attributes to database
def getDataPoints(turls):
  #item, pAlt, pKeyword, redirect, pPicText, picTextLength, picKeywords, pAdSymbol,  lengthAlt, pVideoTag, code
  tFile = open(turls, 'r')
  
  soup = BeautifulSoup(tFile,"html5lib")
  
  item = soup.find_all('data-attribute')
  
  
  #
  if (
  
  
  
  return  item, pAlt, pKeyword, redirect, pPicText, picTextLength, picKeywords, pAdSymbol,  lengthAlt, pVideoTag, code
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
