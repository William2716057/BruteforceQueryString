#!/usr/bin/env python3
import requests

base_url = "http://<IP>/<page>/?<parameter>="  # Edit this
#Loops through 1-199
for secret_number in range(1, 100): #Edit numbers to your own needs
    #Constructs URL and appends number to =
    url = base_url + str(secret_number)
    #Sends a GET request to URL
    response = requests.get(url)

    #Checks if response contains the word 
    if "flag" in response.text: #edit "flag" to your own needs
        #Prints URL with appended number if found to exist 
        print(f"found: {url}") #The printed URL can be visited by pasting into browser 
        break
else:
    print("not found")