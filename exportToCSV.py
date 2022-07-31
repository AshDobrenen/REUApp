from bs4 import BeautifulSoup
import csv
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from numpy import mean
from numpy import std
import requests
import sys
import re
import os
#this is to test the opening of the website file, finding the data-attribute code, and exporting it to a csv. 
#after I will add a new file to do this for all the test websites to one csv, and all the training websites to another

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
path = "C:/Users/bluec/OneDrive/Desktop/ODU/Webpages"
iturl = [path+"/The New York Times - Breaking News, US News, World News and Videos.html",
       path+"/Monkeypox Can Be Airborne, Too - The New York Times.html",
       path+"/Fox News - Breaking News Updates _ Latest News Headlines _ Photos & News Videos.html",
       path+"/30 At-Home Workout Moves_ 20-Minute Set, All Levels, Without Equipment.html",
       path+"/Summer Sale 2022 _ Women's Clothing , Women's Fashion Sale _ SHEIN USA.html",
       path+"/The Best 10 Website Builders.html",
       path+"/Mohamed El-Erian Says Inflation Could Hit 9%, Criticizes Fed.html",
       path+"/Expert Picks_ U.S. Open.html",
       path+"/SciTechDaily - Science, Space and Technology News 2022.html",
       path+"/What went wrong for Astra's failed rocket launch_.html",
       path+"/Ten years after the Higgs, physicists face the nightmare of finding nothing else _ Science _ AAAS.html",
       path+"/June's strawberry supermoon will take the sky Tuesday night - CBS News.html",
       path+"/Plants Appear to Be Breaking Biochemistry Rules by Making 'Secret Decisions'.html",
       path+"/Biofortified tomatoes provide a new route to vitamin D sufficiency _ Nature Plants.html",
       path+"/Ancient trees form bloodlines that bolster forests for thousands of years _ Live Science.html",
       path+"/When cats chew catnip it releases mosquito-repelling chemicals _ New Scientist.html",
       path+"/What Plants Can Do For Your Health _ Healthy Living articles _ Well Being center _ SteadyHealth.com.html",
       path+"/The Inner Life of Cats - Scientific American.html",
       path+"/10 Real-Life Horror Stories - True Horror Stories Reported in the News.html",
       path+"/11 Of The Scariest Ghost Stories From Reddit _ Travel Channel.html",
       path+"/Amanda Aldridge Google Doodle_ celebrating a legendary British composer and opera... - Classic FM.html",
       path+"/LeBron James Stats _ Basketball-Reference.com.html",
       path+"/Amber Heard - IMDb.html",
       path+"/Amber Heard challenges Johnny Depp to his own interview.html",
       path+"/Dark Academia « Post45.html",
       path+"/What is an empath_.html",
       path+"/How The World Butchered Benjamin Franklin’s Quote On Liberty Vs. Security _ TechCrunch.html",
       path+"/Breeze Airways debuts 5 non-stop flights out of Richmond.html",
       path+"/Taco Bell Taco Sauce Recipe - Food.com.html",
       path+"/Guardian_ Sky News Australia is a global hub for climate misinformation – Watts Up With That_.html"]
#paths to the subfolders for each website
folderPath = [path+"/The New York Times - Breaking News, US News, World News and Videos_files",
       path+"/Monkeypox Can Be Airborne, Too - The New York Times_files",
       path+"/Fox News - Breaking News Updates _ Latest News Headlines _ Photos & News Videos_files",
       path+"/30 At-Home Workout Moves_ 20-Minute Set, All Levels, Without Equipment_files",
       path+"/Summer Sale 2022 _ Women's Clothing , Women's Fashion Sale _ SHEIN USA_files",
       path+"/The Best 10 Website Builders_files",
       path+"/Mohamed El-Erian Says Inflation Could Hit 9%, Criticizes Fed_files",
       path+"/Expert Picks_ U.S. Open_files",
       path+"/SciTechDaily - Science, Space and Technology News 2022_files",
       path+"/What went wrong for Astra's failed rocket launch__files",
       path+"/Ten years after the Higgs, physicists face the nightmare of finding nothing else _ Science _ AAAS_files",
       path+"/June's strawberry supermoon will take the sky Tuesday night - CBS News_files",
       path+"/Plants Appear to Be Breaking Biochemistry Rules by Making 'Secret Decisions'_files",
       path+"/Biofortified tomatoes provide a new route to vitamin D sufficiency _ Nature Plants_files",
       path+"/Ancient trees form bloodlines that bolster forests for thousands of years _ Live Science_files",
       path+"/When cats chew catnip it releases mosquito-repelling chemicals _ New Scientist_files",
       path+"/What Plants Can Do For Your Health _ Healthy Living articles _ Well Being center _ SteadyHealth.com_files",
       path+"/The Inner Life of Cats - Scientific American_files",
       path+"/10 Real-Life Horror Stories - True Horror Stories Reported in the News_files",
       path+"/11 Of The Scariest Ghost Stories From Reddit _ Travel Channel_files",
       path+"/Amanda Aldridge Google Doodle_ celebrating a legendary British composer and opera... - Classic FM_files",
       path+"/LeBron James Stats _ Basketball-Reference.com_files",
       path+"/Amber Heard - IMDb_files",
       path+"/Amber Heard challenges Johnny Depp to his own interview_files",
       path+"/Dark Academia « Post45_files",
       path+"/What is an empath__files",
       path+"/How The World Butchered Benjamin Franklin’s Quote On Liberty Vs. Security _ TechCrunch_files",
       path+"/Breeze Airways debuts 5 non-stop flights out of Richmond_files",
       path+"/Taco Bell Taco Sauce Recipe - Food.com_files",
       path+"/Guardian_ Sky News Australia is a global hub for climate misinformation – Watts Up With That__files"]


pAlt, pKeyword, lengthAlt, pVideoTag, code = ([] for i in range(5))
 
for i in range(0,29):
    testTable = getDataPoints(iturl[i])
    #print(testTable)
    pAlt.extend(testTable[0])
    pKeyword.extend(testTable[1])
    lengthAlt.extend(testTable[2])
    pVideoTag.extend(testTable[3])
    code.extend(testTable[4])



for n in range(0,29):
    # Get current working directory
    directory = folderPath[n]
      
    # for all the files present in that
    # directory
    for filename in os.listdir(directory):
          
        # check whether the file is having
        # the extension as html and it can
        # be done with endswith function
        if filename.endswith('.html'):
              
            # os.path.join() method in Python join
            # one or more path components which helps
            # to exactly get the file
            fname = os.path.join(directory, filename)
            #print("Current file name ..", os.path.abspath(fname))
              
            testTable2 = getDataPoints(fname)
            pAlt.extend(testTable2[0])
            pKeyword.extend(testTable2[1])
            lengthAlt.extend(testTable2[2])
            pVideoTag.extend(testTable2[3])
            code.extend(testTable2[4])
"""           
print(pAlt)
print(pKeyword)
print(lengthAlt)
print(pVideoTag)
print(code)
"""            
###########
#write to csv               
dict = {"pAlt": pAlt, "pKeyword": pKeyword, "lengthAlt": lengthAlt, "pVideoTag": pVideoTag, "code": code}
df = DataFrame(dict)
#print(df)
df.to_csv('initalTest.csv')
