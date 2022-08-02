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

###########
#open and then extracting data-attributes and saving all to database
def getDataPoints(turls):
  item, pAlt, pKeyword, redirect, pPicText, picTextLength, picKeywords, pAdSymbol, lengthAlt, pVideoTag, code = ([] for n in range(11))
  tFile = open(turls, 'r', encoding="latin-1")
  itemString = []
  readFile = tFile.read()
  #check beautiful soup version = 4.11.1
  
  soup = BeautifulSoup(readFile, "html.parser")
  with open('readme.txt', 'w', encoding = 'utf-8') as f:
    f.write(str(soup.prettify()))
  
  item = soup.select('[data-attribute]')
  
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
      if(re.search("[^a-zA-Z]ad[^a-zA-Z]|[^a-zA-Z]advertisement[^a-zA-Z]|[^a-zA-Z]paid[^a-zA-Z]|[^a-zA-Z]sponsered[^a-zA-Z]|[^a-zA-Z]Facebook[^a-zA-Z]|[^a-zA-Z]Twitter[^a-zA-Z]|[^a-zA-Z]Instagram[^a-zA-Z]|[^a-zA-Z]TikTok[^a-zA-Z]|[^a-zA-Z]Linkedin[^a-zA-Z]|[^a-zA-Z]search[^a-zA-Z]|[^a-zA-Z]google plus[^a-zA-Z]|[^a-zA-Z]reddit[^a-zA-Z]|[^a-zA-Z]email[^a-zA-Z]|[^a-zA-Z]youtube[^a-zA-Z]", itemString[i])!=None):
          pKeyword.append(1)
      else:
          pKeyword.append(0)
 
      #video tag, will be done the same way as keywords
      if(itemString[i].find("video")>=0):
          pVideoTag.append(1)
      else:
          pVideoTag.append(0)
  
      #da == dec, code = 1 and vice versa, same as keywords, search string for full data attr
      if(itemString[i].find('data-attribute="deceptive"')>=0):
         code.append(1)
      else:
         code.append(0)
  
  
  return  pAlt, pKeyword, lengthAlt, pVideoTag, code

#############main
path = "C:/Users/bluec/OneDrive/Desktop/ODU/Webpages"
extenstion = [".html", "_files"]
names = [path+"/The New York Times - Breaking News, US News, World News and Videos",
       path+"/Monkeypox Can Be Airborne, Too - The New York Times",
       path+"/Fox News - Breaking News Updates _ Latest News Headlines _ Photos & News Videos",
       path+"/30 At-Home Workout Moves_ 20-Minute Set, All Levels, Without Equipment",
       path+"/Summer Sale 2022 _ Women's Clothing , Women's Fashion Sale _ SHEIN USA",
       path+"/The Best 10 Website Builders",
       path+"/Mohamed El-Erian Says Inflation Could Hit 9%, Criticizes Fed",
       path+"/Expert Picks_ U.S. Open",
       path+"/SciTechDaily - Science, Space and Technology News 2022",
       path+"/What went wrong for Astra's failed rocket launch_",
       path+"/Ten years after the Higgs, physicists face the nightmare of finding nothing else _ Science _ AAAS",
       path+"/June's strawberry supermoon will take the sky Tuesday night - CBS News",
       path+"/Plants Appear to Be Breaking Biochemistry Rules by Making 'Secret Decisions'",
       path+"/Biofortified tomatoes provide a new route to vitamin D sufficiency _ Nature Plants",
       path+"/Ancient trees form bloodlines that bolster forests for thousands of years _ Live Science",
       path+"/When cats chew catnip it releases mosquito-repelling chemicals _ New Scientist",
       path+"/What Plants Can Do For Your Health _ Healthy Living articles _ Well Being center _ SteadyHealth.com",
       path+"/The Inner Life of Cats - Scientific American",
       path+"/10 Real-Life Horror Stories - True Horror Stories Reported in the News",
       path+"/11 Of The Scariest Ghost Stories From Reddit _ Travel Channel",
       path+"/Amanda Aldridge Google Doodle_ celebrating a legendary British composer and opera... - Classic FM",
       path+"/LeBron James Stats _ Basketball-Reference.com",
       path+"/Amber Heard - IMDb",
       path+"/Amber Heard challenges Johnny Depp to his own interview",
       path+"/Dark Academia « Post45",
       path+"/What is an empath_",
       path+"/How The World Butchered Benjamin Franklin’s Quote On Liberty Vs. Security _ TechCrunch",
       path+"/Breeze Airways debuts 5 non-stop flights out of Richmond",
       path+"/Taco Bell Taco Sauce Recipe - Food.com",
       path+"/Guardian_ Sky News Australia is a global hub for climate misinformation – Watts Up With That_",
       path+"/ML Engineer Teaches Graph Algorithms with Dungeons & Dragons – The New Stack",
       path+"/UVA working to repurpose student furniture",
       path+"/This 52-year-old early retiree left the U.S. for Portugal with his family_ 'We cut our expenses by 50%'",
       path+"/Top 10 Dad Jokes That Will Make You Laugh ... or Groan - GasBuddy",
       path+"/Children’s Chores Improve Brain Function - Neuroscience News",
       path+"/How to Be a Happy Introvert _ Psychology Today",
       path+"/Caitlin Johnstone_ They Fear Information, Not Disinformation – Consortium News",
       path+"/The Truth Behind The Tapping Technique For Watermelons",
       path+"/The 12 Best Dry Red Wines_ A Guide for Beginners _ The Manual",
       path+"/How To Spot An American Tourist Abroad – Auto Overload",
       path+"/Google Is Getting Ready to Kill Off Android Auto for Phones Once and for All - autoevolution",
       path+"/Charles Babbage’s Difference Engine Turns 200",
       path+"/Showing signs of stress could make us more likeable and prompt others to act more positively towards us",
       path+"/Samsung improves Galaxy Buds 2 performance via new update - Sammy Fans",
       path+"/Swiss Daily_ Wind Park Destruction Of 1000-Year Old Untouched German Forest Exposes “Absurdity of Green Energies” – Watts Up With That_",
       path+"/The Real Story of Pinocchio Tells No Lies _ Travel _ Smithsonian Magazine",
       path+"/Trader Joe's Is Selling Bottled Peach Bellinis For Summer",
       path+"/25 Things from Everyday Life in the Middle Ages - Medievalists.net",
       path+"/Samsung One UI 4.1_ Fingerprint Recognition, know the unknown aspects! - Sammy Fans",
       path+"/The US Military Is Building Its Own Metaverse _ WIRED",
       path+"/Repurposed Stained Glass Comprises a Disorienting Illuminated Greenhouse by Heywood & Condie _ Colossal",
       path+"/2,000 Years Old and Still Going Strong_ Aristotle’s Lessons in Storytelling ‹ Literary Hub",
       path+"/I Tried the Pela Lomi Kitchen Composter—Here’s My Honest Review",
       path+"/There are reasons girls don't study physics – and they don't include not liking maths"]


pAlt, pKeyword, lengthAlt, pVideoTag, code = ([] for i in range(5))
 
for i in range(0,54):
    testTable = getDataPoints(names[i]+extenstion[0])
    #print(testTable)
    pAlt.extend(testTable[0])
    pKeyword.extend(testTable[1])
    lengthAlt.extend(testTable[2])
    pVideoTag.extend(testTable[3])
    code.extend(testTable[4])



for n in range(0,54):
    # Get current working directory
    directory = names[n]+extenstion[1]
      
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
         
###########
#write to csv               
dict = {"pAlt": pAlt, "pKeyword": pKeyword, "lengthAlt": lengthAlt, "pVideoTag": pVideoTag, "code": code}
df = DataFrame(dict)
df.to_csv('initalTest.csv')
