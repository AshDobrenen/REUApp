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
  itemString = []
  #ad in what values each feature can have, use 0 or 1 rather than true or false
  readFile = tFile.read()
  #check beautiful soup version = 4.11.1
  
  soup = BeautifulSoup(readFile, "html.parser")
  #print(soup.html)
  with open('readme.txt', 'w', encoding = 'utf-8') as f:
    
     f.write(str(soup.prettify()))
   #read up on traversal
  #for child in soup.recursiveChildGenerator():

       # if child.hasattr("data-attribute"):
            
            #print(child.name)
  #print(soup.prettify())
  #get all of data attributes in the soup
  #loop through it? only getting first instance of attr
  #item = soup.get('data-attribute')#data-attribute="deceptive" or nondeceptive
  #item = soup.find_all('a')
  item = soup.select('[data-attribute]')
  #print(item)
  #print(len(item))
  
  #create a table that will be filled in and returnd to the main function
  featuresTable = {}
  #fill in the features and code to the lists individually
  for i in range(0,len(item)):
      itemString.append(str(item[i]))
      #presence of alt text and length
      if(item[i].has_attr("alt")):
          pAlt.append(1)
          #using attribute, find attribute value, then get length
          lengthAlt.append(len(str(item[i].get("alt"))))
      else:
          pAlt.append(0)
          lengthAlt.append(0)
      #presence of ad, advertisement, paid, sponsered, Facebook, Twitter, Instagram, TikTok
      #convert item to string, then can search in string, look up how to do this
      #finding ad as a partial of a word
      #reg expression of not any other letter before or after ad, so that it can have characters or spaces, but not letters
      #print(itemString[i].find("ad" or "advertisement" or "paid" or "sponsered" or "Facebook" or "Twitter" or "Instagram" or "TikTok"))
      if(re.search("[^a-zA-Z]ad[^a-zA-Z]|advertisement|paid|sponsered|Facebook|Twitter|Instagram|TikTok|search", itemString[i])!=None):
          pKeyword.append(1)
      else:
          pKeyword.append(0)
 
    ##############################
 #will need other libraris, look later
      #redirect url idk
      
      #picture text based ones besides alt text idk, doesnt quite work, but somtheing like this
      #image = item[i].find('img')
      #picSource = image.attrs['src']
     # print(picSource)
      #####################################
      
      #video tag, will be done the same way as keywords
      if(itemString[i].find("video")>=0):
          pVideoTag.append(1)
      else:
          pVideoTag.append(0)
  
      #da == dec, code = 1 and vice versa, same as keywords, convert to string, search string for full data attr
      if(itemString[i].find('data-attribute="deceptive"')>=0):
         code.append(1)
      else:
         code.append(0)
  
  
  #make to a dataframe from dictionaires, then push the dataframe to csv
  #seperate lists of each feature, these will become columns
  #then dictionairy of featuresTable
  #featuresTable = {"pAlt": pAlt, "pKeyword": pKeyword, "lengthAlt": lengthAlt, "pVideoTag": pVideoTag, "code": code}
  #1 is true/deceptive 0 is false/nondeceptive
  #print(featuresTable)
  
  #featuresDF = pd.DataFrame(featuresTable)
  
  return  pAlt, pKeyword, lengthAlt, pVideoTag, code

#############main
#using the testingurls.py
pAlt, pKeyword, lengthAlt, pVideoTag, code = ([] for i in range(5))

for i in range(0,29):
    testTable = getDataPoints(iturl[i])
    #print(testTable)
    pAlt.extend(testTable[0])
    pKeyword.extend(testTable[1])
    lengthAlt.extend(testTable[2])
    pVideoTag.extend(testTable[3])
    code.extend(testTable[4])

dict = {"pAlt": pAlt, "pKeyword": pKeyword, "lengthAlt": lengthAlt, "pVideoTag": pVideoTag, "code": code}
df = DataFrame(dict)
#print(df)
df.to_csv('initalTest.csv')
