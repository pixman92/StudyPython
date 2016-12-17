#here we go!
import requests
import requests
# ==================
#turn glossary warning off!
# from requests.packages.urllib3.exceptions import InsecureRequestWarning

# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# ====================

enter = raw_input("Run?\n")

#Test, just to see if the GET function works
def runMe(passMe):
  r = requests.get("http://studypython.gomix.me/dreams/"+passMe)
  print r.text
  
  
# GET definition of sent word
def getDef(param):
  r = requests.get("http://studypython.gomix.me/dictionary/" + param)
  print "====\n" + r.text + "\n====\n"
  
def getThesaurus(param):
  r = requests.get("http://studypython.gomix.me/thesaurus/" + param)
  print "====\n" + r.text + "\n====\n"
  
  

  
if enter == "runMe":
  enter2 = raw_input("vars?\n")
  if enter2 != '':
    runMe(enter2)
  else:
    runMe()
    
if enter == "getDef":
  enter2 = raw_input("vars?\n")
  if enter2 != '':
    getDef(enter2)
  else:
    getDef()
  
if enter == "getThesaurus":
  enter2 = raw_input("vars?\n")
  if enter2 != '':
    getThesaurus(enter2)
  else:
    getThesaurus()
    
    