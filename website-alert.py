# a Python script to alert on any change to a website
# by Stevie Bird

# imports
import time
import hashlib
from urllib.request import urlopen, Request

# what url to monitor?
url = Request('https://www.infragard.org/') #InfraGard is currently not accepting applications, and I want to be notified when they begin again

# get the content of the website and create an initial hash
response = urlopen(url).read()
currentHash = hashlib.sha224(response).hexdigest()
print("checking")
time.sleep(15) # wait 15 seconds

while True:
    try:
        # get the current contents of the web site and hash it
        response = urlopen(url).read()
        currentHash = hashlib.sha224(response).hexdigest()
        time.sleep(30) # wait 30 seconds
          
        # get the new contents of the web site and hash it
        response = urlopen(url).read()
        newHash = hashlib.sha224(response).hexdigest()
  
        # compare the two hashes
        if newHash == currentHash: # no change
            continue
        else: # something changed on the site
            print("the web site changed") # change this so it emails me? How to get this to constantly run?
            time.sleep(30) # wait 30 seconds
            continue
              
    # exception handling
    except Exception as e:
        print("error")
        
