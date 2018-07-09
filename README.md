# zubybot-py
## A Discord bot written in Python 3.x using Discord.py

###### Commands

The commands of this bot are:
>1. !coloradd <hex value> <color name>
>2. !deletecolor <hex value> <color name>
>3. !deleterole <role name>
>4. !color <color name>
>5. !help
  
###### Commands that only a certain user(s) can use.

>!coloradd
>!deletecolor
>!deleterole - **CANNOT REVERSE THIS ACTION**

###### How to edit people who can access certain commands or convert a command to certain users.

The following code is how you convert a command to be accessed by only certain people.
```
if message.author.id in [config.{NAME_ID}, config.{NAME_ID}]:
		*rest of the code*
else:
		return
```
**Note:** The code has to come after the command, for example

```
if message.content.startswith('!deletecolor'):
    if message.author.id in [config.{NAME_ID}, config.{NAME_ID}]:
```

###### Commands useable by everyone.

>!color
>!help

###### How to edit !help.

The embed is located in this section of the file, lines 21 -30.
```
    if type == 1:
        embed = discord.Embed(title="Help",
                              description="The commands are:\n!color <name>\n\n Colors located at: https://www.zubyk.co.uk/",
                              colour=discord.Colour(0xa020f0),
                              timestamp=datetime.datetime.utcfromtimestamp(currenttime))
        embed.set_author(name="Zuby Bot",
                         icon_url="https://i.imgur.com/jqIsh9f.png")
        embed.set_footer(text="Zuby Bot",
                         icon_url="https://i.imgur.com/jqIsh9f.png")
        return embed
  ```
  This is what it should look like when the command is executed.
  
  
  ![!help embed](https://i.imgur.com/KffTCBX.png)
  
	
###### How to set up your config.py file
To set up your config file first you need to create a file in the same directory as bot.py and name it '*config.py*'.
Your config **MUST** contain at least the following:

```
TOKEN = 'YOUR BOT TOKEN' # This is your bot token.
NAME_ID = 'USER_ID' # This will be the ID of the account of the user.
```

Next in bot.py you must import the config file.

```
import config
```

**Example of usage**
```
client.run(config.TOKEN)
```

This hides your config token if you decide to make your own bot from this code.
Do **NOT** upload your config.py to GitHub

  
