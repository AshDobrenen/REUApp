from imports import *
from initalTestURL import *
#this is to test the opening of the website file, finding the data-attribute code, and exporting it to a csv. 
#after I will add a new file to do this for all the test websites to one csv, and all the training websites to another

###########
#open and then extracting data-attributes and saving all to database
###########
#open and then extracting data-attributes and saving all to database
def getDataPoints(turls):
  item, pAlt, pKeyword, redirect, pPicText, picTextLength, picKeywords, pAdSymbol, lengthAlt, pVideoTag, code = ([] for n in range(11))
  tFile = open(turls, 'r', encoding="latin-1")
  
  #ad in what values each feature can have, use 0 or 1 rather than true or false
  
  soup = BeautifulSoup(tFile, "html.parser")
  #print(soup)
  #get all of data attributes in the soup
  #loop through it
  item = soup.find_all(attrs = {"data-attribute": True})
  print(item)
  print(len(item))
  #create a table that will be filled in and returnd to the main function
  featuresTable = {}
  #fill in the features and code to the lists individually
  for i in range(0,len(item)):
      #presence of alt text and length if there is some
      if(item[i].find_all("alt")==[]):
          pAlt.append(0)
      else:
          pAlt.append(1)
          lengthAlt.append(len(str(item[i].find("alt"))))
      #presence of ad, advertisement, paid, sponsered, Facebook, Twitter, Instagram, TikTok keywords, 0 if none 1 if there is the keyword
      if(item[i].find_all("ad" or "advertisement" or "paid" or "sponsered" or "Facebook" or "Twitter" or "Instagram" or "TikTok")==[]):
          pKeyword.append(0)
      else:
          pKeyword.append(1)
 
      #if there is a url in the item, does it redirect (0 or 1) as long as its not an image scr
      
      #picture text based ones besides alt text
      #presence of picture text(0 or 1) and length if there is text, will be same as alt text code
      #presence of keywords in picutre (0 or 1) keywords in pictures ad, advertisement, buy now, sign up here, paid, sponsered
      
      #image = item[i].find('img')
      #picSource = image.attrs['src']
     # print(picSource)
    
      #presence of ad symbol (0 or 1) html of that symbol below
      #<img width="19px" height="15px" style="background:transparent !important; margin:0; padding:0; border:none; position:absolute; right:0px; top:0px;" src="https://choices.trustarc.com/get?name=admarker-icon-tr.png">
      
      
      #presence of video lable/tag(0 or 1) 
      if(item[i].find_all("video")==[]):
          pVideoTag.append(0)
      else:
          pVideoTag.append(1)
  
      #is the data-attriburte in this item=="decpetive", code = 1 and vice versa
      if(item[i].find_all("deceptive")==[]):
         code.append(0)
      else:
         code.append(1)
  
  featuresTable[0] = item

  print(pAlt)
  print(pKeyword)
  print(lengthAlt)
  print(pVideoTag)
  print(code)
  #transpose the table to get the rows in the right order
  return  featuresTable
###########
#exporting to a csv
def writeHeaders():
#headers = item, features, code(1 or 0 for deceptive or not)
#item is datapoint
#pAlt includes any alt text, play now, close ad, etc
#pKeyword includes ad, paid/sponsered, socials

  listOfHeaders = ["item", "pAlt", "pKeyword", "redirect", "pPicText", "picTextLength", "picKeywords", "pAdSymbol",  "lengthAlt", "pVideoTag", "code"]

  fullName = "C:\\Users\\bluec\\OneDrive\\Desktop\\ODU\\initalTest.csv"

  with open(fullName, "a", newline="") as h:
    writer = csv.writer(h)
    writer.writerow(listOfHeaders)
 

def writeCSV(itlist):
  fullName = "C:\\Users\\bluec\\OneDrive\\Desktop\\ODU\\initalTest.csv"
  #writing out the content of the database
  with open(fullName, "a", newline="") as c:
    writer = csv.writer(c)
    writer.writerow(itlist)

################################
writeHeaders()
#loop through all websites
for i in range(0,1):
    print(writeCSV(getDataPoints(iturl[i])))
#close file
