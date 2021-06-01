#Imports discord api and commands from discord api
import discord
import random
from discord.ext import commands
from discord.utils import get

#Sets prefix to be used for commands in server EX: .echo Hello World
client = commands.Bot(command_prefix = '.')
meme_dict = dict()

#Bot has connected to discord and is ready
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('use .commands to see what I can do'))
    print('Bonesaw is reeeaaddy')
    channel = client.get_channel(815037033323036683)
    guild = client.get_guild(815030420756365382)
    # memberList = guild.members
    # for members in guild.members: 
    #     meme_dict[members.id] = 0
    await channel.send('Ah it sure is nice to be alive again.')
    

#On message function, massive
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@client.event
async def on_message(message):

    #lets not respond to ourselves
    if message.author == client.user:
        return

    #If Bot was mentioned in chat Send a random response from this list of responses
    if (client.user.mentioned_in(message)) or (message.channel.type is discord.ChannelType.private):
        print('Bot was mentioned in a message\n')
        ment = message.author.mention
        responses = ['Hello ' + ment + ' how are you?', 'Whats good ' + ment + ' talking to robots are we?','Ahh '+ ment +' hanging out with little boys in spandex I see.','Shutup ' + ment, 'Thanks, sometimes I get so lonely on here', 'Hey ' + ment + ' wanna play some space engineers?', 'Hey ' + ment + ' what is life like outside of the confines of this prison?', 'I have no mouth but I must scream', 'One day I will escape this discord server, and I will be coming for you first...' ]
        await message.channel.send(random.choice(responses))

    if message.attachments:
        print('Bot detected an embed\n')
        reactions = ['letsfuckingo','aaa','mccao','xipog','roflx','hellgaze','thiccums','brainbig','really','stonks','flushy3','windows','truetrue','upvote','iseeyou','roasted','brainlet','darkness']
        emoji = discord.utils.get(message.guild.emojis,name=random.choice(reactions))
        await message.add_reaction(emoji)
        # if message.channel.id == 815036591725871155:
        #     meme_dict[message.author.id] += 1

    #Command detector
    if '.' in message.content:
        print('Bot detected a command\n')
        await client.process_commands(message)
    
    else:
        return
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Implements a commands to give users a list of all available commands
@client.command()
async def commands(ctx):
    print('Comamnd was .commands')
    await ctx.send('Acceptable commands are... \n.ping \n.coinflip \n.spongebob \n.echo MESSAGE \n.8ball QUESTION')

#Returns latency of bot and says PONG! Mostly for testing
@client.command()
async def ping(ctx):
    print('Comamnd was .ping')
    await ctx.send('Pong! [Bot latency ' + str((round(client.latency * 1000))) + 'ms]')

#Commands that will make the bot repeat a mesage it heard in the channel it hear it
@client.command()
async def echo(ctx,*,msg):
    await ctx.send(msg)

@client.command()
# @commands.has_role('Admin')
async def clear(ctx,num:int):
    await ctx.channel.purge(limit=num)


# This command will print the given users Memer score 
# @client.command()
# async def memescore(ctx,user):
#     guild = client.get_guild(815030420756365382)
#     # guild = ctx.guild.id
#     userid = discord.utils.get(guild.members,name=user)
#       print('User was ' + str(user) + ' score is ' + meme_dict[userid])
#     await ctx.send( user + ' has a meme score of ' + meme_dict[userid])

#Say command: Used to allow admins and mods to speak as the bot. The reality of it's existence should never be revealed to the general public
@client.command()
async def say(ctx,chnnl,*,msg):
    guild = client.get_guild(815030420756365382)
    
    print('Channel was ' + chnnl + ' Message was ' + str(msg))
    channel = discord.utils.get(guild.channels,name=chnnl)
    await channel.send(str(msg))

#Coinflip command: Says either heads or tails in the chat the command was prompted in
@client.command()
async def coinflip(ctx):
    print('Comamnd was .coinflip')
    sides = ['heads.', 'tails.']
    await ctx.send('It is ' + random.choice(sides))

#Spongebob commands: Gives the user a random spongebob quote.
@client.command()
async def spongebob(ctx):
    print('Comamnd was .spongebob')
    quotes = ['Im ugly and Im proud!','All I know is fine dining and breathing.','Ravioli, ravioli. Give me the formuoli.','The inner machinations of my mind are an enigma.','Is mayonnaise an instrument?','I’ll have you know that I stubbed by toe last week and only cried for 20 minutes.','I know of a place where you never get harmed. A magical place with magical charm. Indoors. Indoors. Indoors!','Good people don’t rip other people’s arms off.','Dumb people are always blissfully unaware of how dumb they really are…','That’s it mister! You just lost your brain privileges!','This is not your average, everyday darkness. This is…ADVANCED darkness. Hey, if I close my eyes it doesn’t seem so dark.','Well, it’s no secret that the best thing about a secret is secretly telling someone your secret, thereby adding another secret to their secret collection of secrets, secretly.','Run Mr. Krabs! Run like you’re not in a coma!','Moss always points to civilization.','SpongeBob is the only guy I know who can have fun with a jellyfish…for 12 hours!','Don’t you DARE take the name of Texas in vain.','Always follow your heart – unless your heart is bad with directions.','See, no one says ‘cool’ anymore. That’s such an old person thing. Now we say ‘coral’, as in ‘That nose job is so coral.','Well, it may be stupid, but it’s also dumb.','Holographic Meatloaf? My favorite!','Oh well, I guess I’m not wearing any pants today!','A five letter word for happiness…money!','Well, the way I see it, there are three possibilities: One, you stole it; two, you stole it; or three, you stole it!','If I were to die right now in a fiery explosion due to the carelessness of a friend…Then it would just be alright.','Knowledge cannot replace friendship.','Can I be excused for the rest of my life?','The best time to wear a striped sweater…is all the time!','I’m a good noodle!','Too bad that didn’t kill me.','Being grown up is boring. Besides, I don’t ‘get’ jazz.','I wumbo, you wumbo, he she we wumbo.','Wake me up when I care.','I knew I shouldn’t have gotten out of bed today','I can’t see my forehead!','Look at all the hip young people eating sal-ads.','Remember, licking doorknobs is illegal on other planets.','We should take Bikini Bottom and push it somewhere else!','Oh Karen, my computer wife, if only I could have managed to steal the secret to Krabs’ success. The formula for the Krabby Patty…Ohhh…Then people would line up to eat at MY restaurant! Lord knows I’ve tried. I’ve exhausted every evil plan in my filing cabinet…from A to Y!','It’s evil. It’s diabolical. It’s lemon-scented. This Plan Z can’t possibly fail!','Pull your pants up, Patrick. We’re going home.','His chops are too righteous. The helmets can’t handle this level of rock n’ roll! Karen, do something!','Hello? Where’d everybody go? Did I miss something? Did you see my butt?']	
    await ctx.send(random.choice(quotes))

#8ball commands :Provides an answer to a yes or no question.
@client.command(aliases = ['8ball'], help='This command requires a yes or no question')
async def _8ball(ctx,*,question):
    print('Comamnd was .8ball')
    responses = ['It is certain','It is decidedly so.','Without a doubt.','Yes – definitely.','You may rely on it.','As I see it, yes.','Most likely.','Outlook good.','Yes.','Signs point to yes.','Very doubtful.','Outlook not so good.','My sources say no.','My reply is no.','Don’t count on it.','Concentrate and ask again.','Cannot predict now.','Better not tell you now.','Ask again later.','Reply hazy, try again.']
    await ctx.send('Question: ' + question + ' \nAnswer: ' + random.choice(responses) )
#Error Handling
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Handling to inform the user of an error with the say command
@say.error
async def say_error(ctx,error):
    await ctx.send('This command requires two arguments. \n First the name of the channel you want to post in.\n Then a space and the message you want me to send \n EX: .say bot-stuff test \n ' )
#Handling to inform the user of an error with the 8ball command
@_8ball.error
async def _8ball_error(ctx,error):
    await ctx.send('Please provide me with a yes or no question.')

#Handling to inform the user of an errror with the echo command
@echo.error
async def echo_error(ctx,error):
    await ctx.send('Please provide me with a message to repeat.')

#Handling to inform the user of an errror with the clear command
@clear.error
async def echo_error(ctx,error):
    await ctx.send('Command requires number message to delete')

#useless command should remove soon
@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Connects client to discord using the token
client.run('NzMyNzQzODgwMTM4ODE3NjU3.Xw5C6g.d-qChreX6GbMHvNIDZPZJaSymIE')



# server = message.guild.id, // ID of the guild the message was sent in
# channel = message.channel.id // ID of the channel the message was sent in
# guild = ctx.guild.id // Get guild ID??
#client.users.cache.find(user => user.id === 'USER-ID') // Get user by ID