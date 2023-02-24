# Twitter-User-Info-Getter
Takes in a list of twitter user IDs and outputs their handle, display name, description and links

Program made for a friend who wanted to archive info about people they follow on Twitter before its seemingly inevitable demise,
so they can continue find them elsewhere (though it looks like this program won't be usable much longer for free)

# How to use
First, set the userID in getFollowing.py to that of the user who is following the accounts you want the information about.
Then run it, and it will create a json with a list of IDs of the followed accounts. This is then used by UserInfoGetter.py to create an output like the one below.
I have included an example webpage made to display the information.

# Example Output
These are just ones I found in their list that didn't seem too "unsavoury"...
```
[
    {
        "handle": "Totalbiscuit",
        "displayname": "TotalBiscuit",
        "description": "As a man, I’m flesh & blood. I can be ignored. I can be destroyed. But as a symbol, I can be incorruptible. I can be everlasting.",
        "links": [
            "http://youtube.com/totalhalibut"
        ]
    },
    {
        "handle": "Myndflame",
        "displayname": "Myndflame, Squirrel Whisperer.",
        "description": "Former Youtuber, Streamer, Composer. Currently a Father, Christian, and squirrel whisperer.",
        "links": [
            "http://www.youtube.com/user/Myndflame"
        ]
    },
    {
        "handle": "JesseCox",
        "displayname": "Jesse Cox - Monster Roadtrip Out Now!",
        "description": "🎮 Producer of @monsterprom franchise, @GestaltGame, and Max Gentlemen Sexy Business!🦋 Streaming/Creating/Goofing since 2010 Inquiries: JesseCoxBiz@gmail.com",
        "links": [
            "http://www.jessecox.com"
        ]
    }
]
```
