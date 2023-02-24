import tweepy
import secretthings
import json

userID = 0 # the id of the user who is following the accounts you want information about
followingIDs = []
nextPage = None

client = tweepy.Client(secretthings.bearer_token)

while(True):
    following = client.get_users_following(userID, max_results=1000, pagination_token=nextPage)
    actualFollowing = following[0]

    for user in actualFollowing:
        followingIDs.append(user["id"])

    if ("next_token" in following[3]):
        nextPage = following[3]["next_token"]
    else:
        break

output = {"ids" : followingIDs}
with open("followingIDs.json", "w", encoding="utf8") as f:
    json.dump(output, f, indent=4, ensure_ascii=False)

