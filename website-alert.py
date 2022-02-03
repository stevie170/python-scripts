# a Python script to alert on any change to a website
# by Stevie Bird
# ******************** THIS IS AN UNFINISHED SCRIPT - WORK IN PROGRESS! ********************

# imports
import time
import hashlib
from urllib.request import urlopen, Request
import smtplib
    
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
            print("the web site changed") # notify
            
            # connect to the gmail server and send an email to notify of change
            # I've commented this code out because it's not actually functional without credentials, and it would be ridiculous to include credentials in the actual code...
            # try:
            #     server = smtplib.SMTP('smtp.gmail.com', 587) # create SMTP session
            #     server.starttls() # start TLS for security
            #     server.login("sender_email_id", "sender_email_id_password") # use credentials to authenticate to gmail
                # how to authenticate without including credentials in the script? not just the password but email addresses too!
            #     message = "Message to send"
            #     server.sendmail("sender_email_id", "receiver_email_id", message) # send the message
            #     s.quit() # terminate the SMTP session
            # except:
            #     print 'Couldn\'t connect to gmail...'
            
            time.sleep(30) # wait 30 seconds
            continue
              
    except Exception as e:     # exception handling
        print("error")
        

## here is one credentials answer I found that could be worth trying: 
## (to be considered later when I work on this project again)
## make a seperate file and save it somewhere outside the project. Now do chmod 600, i.e. allow only root to access the file. 
## Now in your code run read the file by running in the the superuser mode. Or you could also create a different user which 
## can access the file and run the code using that user.
## OR You could use environment variables in your system. You can set one by doing the following in bash shell
## export KEY=some_value
## And then in your Python code
## os.environ.get('KEY')

## Store the email and password outside of the project directory and use the import os library to get it. 
## You want to make sure that it never even gets a chance to be pushed into the public repository.
