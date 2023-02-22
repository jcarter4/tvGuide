#I habitually add these to my python because I use their functions frequently 
# (not in this case though so they can be removed)
import sys
import os
#the csv and json are imported so I can manipulate the two filetypes
import csv
import json
#not gonna explain this one
import re


#check to see if we have leftover information from previous run....and removes it
if os.path.exists('channels.csv'):
    os.remove('channels.csv')
if os.path.exists('test_channel.txt'):
    os.remove('test_channel.txt')

# or this one
regex = r"('id': ([0-9]+), \'label\': '(.*?))', 'type'.*?('physicalid': ([0-9]+).*? 'programid': ([0-9]+)).*?('url': (.*?), 'port': ([0-9]+))"

# this is simply opening the json when files are open this way
# they will close even if the script fails so we don't have open files that we can't close
# it should always be done this way
with open('eo_channel.json') as f:
    data = json.load(f)
    
        
# this one is fun the str(input something here) just takes another object and converts it to a string
# data.items just dumps the whole JSON
test_str = str(data.items()).replace('&amp;', '&')

#this runs the regex to pull the whole list of matches
matches = re.finditer(regex, test_str, re.MULTILINE)


#create spaghetti json useful for seeing how python gets the data
with open("test_channel.txt", "w", newline='')as testFile:
    testFile.write(str(data.items()))

# same as the JSON but now in csv flavor a+ is just append with prejudice the newline= is so we dont get any \n weirdness in the CSV
with open("channels.csv", 'a+', newline='')as file:


    writer = csv.writer(file)

    # writes the first row outside of the loop so it only happens once
    writer.writerow(["Channel", "Name", "Major", "Minor", "MCast", "port"])


    # this seperates each match into different callable groups and enumerate gives them an ID 
    for matchNum, match in enumerate(matches, start=1):
        
        writer.writerow([match.group(2),match.group(3),match.group(5),match.group(6),match.group(8),match.group(9)])

print("Done")