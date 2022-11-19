
import tweepy   # library for accessing twitter api more easily, pip install tweepy
import json     # for reading and writing json files
import time     # for getting info about the running time of the program
import secretthings # extra file i have storing api key stuff

# create client to connect to twitter through tweepy
# if you want to run yourself, will need to set up twitter developer stuff and get
# a bearer token (OAuth 2.0 Bearer Token (App-Only))
# https://docs.tweepy.org/en/stable/authentication.html#id2
client = tweepy.Client(secretthings.bearer_token)

# load json file containing the account ids we want
jsonData = []
with open("following.json", "r") as file:
    jsonData = json.load(file)

# put account ids from file data into a list
accountIds = []
for jd in jsonData:
    accountIds.append(jd["following"]["accountId"])

outputData = [] # data which will be written to output file at end of program
userFields = ["url", "description", "entities"] # need to specify extra info we want from twitter
# url: the main url on the profile
# description: the description of the profile
# links get converted to t.co/whatever, entities contains what they originally were

batchStart = 0 # get data in batches of 100, so we want to start at a set of 100 in
               # the list of accountIds. this is that starting point

while batchStart < len(accountIds):
    # the end point of the batch, will go from batchStart to batchEnd-1
    # batch end is either batchStart + 100, or the end of the list if there
    # are less than 100 items left
    batchEnd = min(batchStart + 100, len(accountIds)) 

    # list of ids to get info about in this batch
    batchIds = accountIds[batchStart:batchEnd]

    # get_users returns a list with 1 item, which contains the list we actually want
    # so users is that 1 item containing what we want (which is why theres the [0] at the end)
    users = client.get_users(ids=batchIds, user_fields=userFields)[0]

    # we have a batch of users, go through each one and get the data we want
    for user in users:
        handle = user.username
        displayname = user.name
        description = user.description
        links = []

        # this parts a bit of a mess...
        # reccommend reading the response fields here:
        # https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-id
        # also note, there they call things like entities.url.urls, but we have to access
        # as a dictionary
        # user.entities is a dictionary, so is indexed with ["itemname"] instead of .itemname
        # it may contain a main url, a description, both or neither

        # first, did the user data even contain an entities entry
        if user.entities != None:
            # did that entry have a "url" entry, and did that "url" entry
            # also contain a "urls" entry (it probably always should, but just
            # double checking)
            if (
            "url" in user.entities and
            "urls" in user.entities["url"]
            ):
                # even though there can only be one main url, it still returns as a list
                # so for simplicity, iterate the list. nicer to have url instead of user.entities["url"]["urls"][0]
                for url in user.entities["url"]["urls"]:
                    # also check if the url entry contained an expanded_url
                    # expanded url is what the url was before converted to t.co
                    if "expanded_url" in url:
                        # we have the link we want, add it to the list of links
                        links.append(url["expanded_url"])
            
            # same as above, but for the description
            # entities.description.urls contains all the urls which were in the
            # description and got converted to t.co
            if (
            "description" in user.entities and
            "urls" in user.entities["description"]
            ):
                for url in user.entities["description"]["urls"]:
                    if "expanded_url" in url:
                        links.append(url["expanded_url"])
        
        # we have all the user data we want, put it together
        userData = {
            "handle" : handle,
            "displayname" : displayname,
            "description" : description,
            "links" : links
        }

        # add a new entry in the output dataset with this user's data, then move
        # on to next user in this batch
        outputData.append(userData)

    # batch finished, print for progress info (just nice to have)
    print(time.asctime(), " : ", batchStart, " to ", batchEnd - 1)
    # increment start location in list of all user ids
    batchStart += 100

# sort user entries based on the displayname within the entry, a-z
outputData.sort(key=lambda x: x["displayname"])

# all ids have been checked and had their info added to outputData
# now write outputData to a file
# require encoding=utf8 for the emojis and other stuff people have,
# along with ensure_ascii in json.dump
# indent=4 specifies how the pretty printing will look, without it we just get
# one giant line
with open("newfollowing.json", "w", encoding='utf8') as file:
    json.dump(outputData, file, indent=4, ensure_ascii=False)