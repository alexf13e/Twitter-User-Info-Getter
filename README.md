# Twitter-User-Info-Getter
Takes in a list of twitter user IDs and outputs their handle, display name, description and links

Program made for a friend who wanted to archive info about people they follow on Twitter before its seemingly inevitable demise,
so they can continue find them elsewhere

# Example Input
I believe they got this from a load of data you can find by requesting data twitter holds about you. I don't actually use twitter so idk...
```
[
  {
    "following" : {
      "accountId" : "16747981",
      "userLink" : "https://twitter.com/intent/user?user_id=16747981"
    }
  },
  {
    "following" : {
      "accountId" : "18106205",
      "userLink" : "https://twitter.com/intent/user?user_id=18106205"
    }
  },
  {
    "following" : {
      "accountId" : "55793637",
      "userLink" : "https://twitter.com/intent/user?user_id=55793637"
    }
  }
]
```

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
