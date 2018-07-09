# Zuby-Bot by Zuby
# Multifunctional
# Colour bot

import discord
import datetime
import time
import json
import os.path
import config

client = discord.Client()
botStartTime = datetime.datetime.now()

t0 = time.time()
coloursFile = 'colours.json'

def embedMaker(type):
    currenttime = time.time()
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


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!help'):
        embed = embedMaker(1)  # Function to setup the embed message title etc
        await client.send_message(message.channel, embed=embed)


    elif message.content.startswith('!addcolor'):  # to add colours to the colour file
        if message.author.id in [config.zubyID, config.nigelID]:

            command = ''.join(message.content.split('!addcolor ',
                                                    1))  # splitting the first bit of the message off, as we don't need it
            data = []
            if len(command.split(" ")) < 2:  # checking if there are enough arguments
                await client.send_message(message.channel,
                                          'Not enough arguments, please do !addcolor <hex> <colorname>')
                return
            elif len(command.split(" ")) > 2:
                await client.send_message(message.channel,
                                          'Too many arguments, please do !addcolor <hex> <colorname>')
                return
            else:
                colourHex, colourName = command.split(" ")  # if there are 2 arguments, then split it into two variables

            if not os.path.exists(coloursFile):  # if the file does not exist, create it with some default values
                with open(coloursFile, 'w') as f:
                    entry = {'white': 'ffffff', 'black': '000000'}
                    json.dump(entry, f)
                    f.close()

            with open(coloursFile, 'r') as f:  # open file and load the data as json
                data = json.load(f)
                f.close()

            # checking if the name/hex we are trying to add already exists
            for name, hex in data.items():  # iterate through each key and value pair
                if name == colourName:  # if the name is already in use
                    await client.send_message(message.channel, 'This name is already in use, for hex value: ' + hex)
                    return
                elif hex == colourHex:  # if the hex value is already in use
                    await client.send_message(message.channel, 'This hex value is already assigned with name: ' + name)
                    return

            # if all went well, add colour to the file
            with open(coloursFile, 'w+') as f:  # write data over file again
                print("Writing to file")
                data[colourName] = colourHex  # add the colour to the data array
                json.dump(data, f)  # dump the data dictionary as a json file
                f.close()

            await client.send_message(message.channel, 'Added color: %s with hex value %s' % (colourName, colourHex))
        else:
            return

    if message.content.startswith('!deletecolor'):  # to delete a colour from the file
        if message.author.id in [config.zubyID, config.nigelID]:
            command = ''.join(message.content.split('!deletecolor ',
                                                    1))  # splitting the first bit of the message off, as we don't need it
            data = []
            if len(command.split(" ")) < 1:  # checking if there are enough arguments
                await client.send_message(message.channel, 'Not enough arguments, please do !deletecolor <colorname>')
                return
            elif len(command.split(" ")) > 1:
                await client.send_message(message.channel, 'Too many arguments, please do !deletecolor <colorname>')
                return
            else:
                colourName = command.split(" ")
            if not os.path.exists(coloursFile):  # if file does not exist, create it with some default values
                with open(coloursFile, 'w') as f:
                    entry = {'white': 'ffffff', 'black': '000000'}
                    json.dump(entry, f)
                    f.close()
            with open(coloursFile, 'r') as f:  # open file and load as json
                data = json.load(f)
                f.close()
            # checking if the name/hex is already stored
            found = False
            for name, hex in data.items():  # iterate through the colours
                if name == colourName[0]:  # if found, delete it from the data dictionary
                    del data[name]
                    found = True
                    break
            if not found:  # if its not found, tell the user
                await client.send_message(message.channel, 'Color not found')
                return
            # writing the data to the file
            with open(coloursFile, 'w') as f:
                print("Writing to file")
                json.dump(data, f)
                f.close()
            await client.send_message(message.channel, 'Deleted entry: %s, %s ' % (name, hex))
        else:
            return

    elif message.content.startswith('!deleterole'):
        if message.author.id in [config.zubyID, config.nigelID]:
            command = ''.join(message.content.split('!deleterole ',
                                                    1))  # splitting the first bit of the message off, as we don't need it
            if len(command.split(" ")) < 1:  # checking if there are enough arguments
                await client.send_message(message.channel, 'Not enough arguments, please do !deleterole <rolename>')
                return
            elif len(command.split(" ")) > 1:
                await client.send_message(message.channel, 'Too many arguments, please do !deleterole <rolename>')
                return
            else:
                roleName = command.split(" ")  # Getting the name of the role to delete
                roleName = roleName[0]

            role = discord.utils.get(message.server.roles, name=roleName)  # attempt to get the role from the server
            if role is None:  # if it returns None then the role doesn't exist
                await client.send_message(message.channel, 'Role: %s does not exist.' % roleName)
                return
            else:
                await client.delete_role(message.server, role)
                await client.send_message(message.channel, 'Deleted Role: %s' % roleName)

        else:
            return

    elif message.content.startswith('!color'):  # setting colour role
        command = ''.join(message.content.split('!color ', 1))  # removing the !colour
        if len(command.split(" ")) < 1:  # checking if there are enough arguments
            await client.send_message(message.channel, 'Not enough arguments, please do !color <colorname>')
            return
        elif len(command.split(" ")) > 1:
            await client.send_message(message.channel, 'Too many arguments, please do !color <colorname>')
            return
        else:
            colourName = command.split(" ")
            colourName = colourName[0]
        if not os.path.exists(coloursFile):  # if file does not exist, create it with some default values
            with open(coloursFile, 'w') as f:
                entry = {'white': 'ffffff', 'black': '000000'}
                json.dump(entry, f)
                f.close()
        with open(coloursFile, 'r') as f:  # open file and load as json
            data = json.load(f)
        f.close()
        # checking if the name/hex is already stored
        found = False
        colourHex = 0
        for name, hex in data.items():  # iterate through and delete if the name is found
            if name == colourName:
                found = True
                colourHex = hex
                break
        if not found:
            await client.send_message(message.channel, 'Color not found')
            return
        for r in message.author.roles:  # going through the roles that the user has to make sure they don't already have a colour role
            if r.name in data.keys():
                await client.remove_roles(message.author, r)  # if they do, remove it

        colourInt = int(colourHex, 16)  # work out the integer value for the colour
        roleColour = discord.Colour(value=colourInt)  # create the discord colour object from the integer value

        if discord.utils.get(message.server.roles,
                             name=colourName) is None:  # if the role for the colour doesn't exist, make it
            await client.create_role(message.author.server, name=colourName, colour=roleColour)

        role = discord.utils.get(message.server.roles,
                                 name=colourName)  # get the role that we either just made or already existed
        while role is None:  # sometimes the role isn't made before it tries to get it, so keep looping round until its made
            role = discord.utils.get(message.server.roles, name=colourName)
        '''
        numberRoles = len(
            message.server.roles) - 3  # get the number of roles in the server and take two (the bot will be 1st or second highest)
        await client.move_role(message.server, role,
                               position=numberRoles)  # move the role to a higher point so that it shows above other roles
        '''
        await client.add_roles(message.author, role)  # add the role to the user
        await client.send_message(message.channel, 'I have added color **' + colourName + '** to user ' + message.author.mention)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name="!help in #colors for help."))


client.run(config.TOKEN)
