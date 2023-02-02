#here lies the edited version of Ein's Code now called Calcifer
#Calcifer is suppose to be a more advanced version of Ein
#Use the above code format to de-clutter Calcifers code and dont print things line by line
import random
import json
import requests
import aiohttp
import discord
from discord import Game, Embed, Color, Status, ChannelType
from discord.ext import commands
from discord.ext.commands import Bot
from bs4 import BeautifulSoup
with open("config.json","r") as h:
    config = json.load(h)

#
client = Bot(command_prefix=commands.when_mentioned_or(config['prefix']))
client.remove_command('help')
##################################################
# C O M M A N D  T A B L E  O F  C O N T E N T S #
##################################################
#8ball  #User-Response  #Link-Generators  #Help
#Square #Funny          #NSFW
#Ping   #Misc      

####SQUARE(math)####
@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))
###P I N G###
@client.command(pass_context=True)
async def marco(ctx):
    t = await client.say('Polo!')
    ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 1000
    await client.edit_message(t, new_content='Polo! It took me {}ms to recieve that but other than that it seems the castle is up and running :smile: :fire:'.format(int(ms)))

#############
# F U N N Y #
#############
@client.command(pass_context=True)
async def saveme(ctx):
    am = discord.Embed(
        description="***HAVE NO FEAR!!!! CAUSE I AM HERE***"
    )
    am.set_image(url="https://i.postimg.cc/FR5mp59P/tumblr-p5e5peklin1sam3zlo1-500.png")
    await client.say(embed=am)
#
@client.command(pass_context=True)
async def zr(ctx):
    br = discord.Embed(
        description="**DO A BARREL ROLL**"
    )
    br.set_image(url="https://i.postimg.cc/BvvcrMRN/barrell.gif")
    await client.say(embed=br)
###########
# M I S C #
###########
@client.command(pass_context=True, aliases=['em', 'e'])
async def embd(ctx, *args):
    colors = {
       "red": Color.red(),
        "green": Color.green(),
        "gold": Color.gold(),
        "orange": Color.orange(),
        "blue": Color.blue(),
        "purple": Color.purple(),
        "teal": Color.teal(),
        "magenta": Color.magenta(),
        "grey": Color.lighter_grey()
    }
    if args:
        argstr = " ".join(args)
        if "-c " in argstr:
            text = argstr.split("-c ")[0]
            color_str = argstr.split("-c ")[1]
            color = colors[color_str] if color_str in colors else Color.default()
        else:
            text = argstr
            color = Color.default()

            await client.say(embed=Embed(color=color, description=text))
            await client.delete_message(ctx.message)
################################
# L I N K  G E N E R A T O R S #
################################
#These Commands are used for searching and link generation.

#This command creates a LMGTFY link based on the users given text
@client.command(pass_context=True, aliases=['google'])
async def lmgtfy(ctx, *args):
    if args:
        url = "http://lmgtfy.com/?q=" + "+".join(args)
        await client.say(embed=Embed(description="**[Look here!](%s)**" % url, color=Color.gold()))
    await client.delete_message(ctx.message)

#This Command searches for an IP
@client.command(pass_context=True, aliases=['IP Lookup'])
async def srchip(ctx, *args):
    if args:
        url = "https://whatismyipaddress.com/ip/" + "+".join(args)
        await client.say(embed=Embed(description="**[IP Located!](%s)**" % url, color=Color.gold()))
    await client.delete_message(ctx.message)
################################
# S E A R C H  E N G I N E (S) #
################################
#These Commands are for making it easy to browse the web using their favorite search engine from the comfort of Discord
#The commands even allow for users to search social media platforms from Discord

#This command searches for a term using the Google search engine
@client.command(pass_context=True, aliases=['alphabet'])
async def g(ctx, *args):
    if args:
        url = "https://www.google.com/search?q=" + "+".join(args)
        await client.say(embed=Embed(description="**[Google Search](%s)**" % url, color=Color.gold()))
    await client.delete_message(ctx.message)

#This command searches on Youtube for a specified term
@client.command(pass_context=True, aliases=['youtube'])
async def yt(ctx, *args):
    if args:
        url = "https://www.youtube.com/results?search_query=" + "+".join(args)
        await client.say(embed=Embed(description="**[Youtube Search](%s)**" % url, color=Color.gold()))
    await client.delete_message(ctx.message)

@client.command(aliases=['urba'])
async def ud(*args):
  word = ' '.join(args)
  r = requests.get("http://www.urbandictionary.com/define.php?term={}".format(word))
  soup = BeautifulSoup(r.content, features="html.parser")
  x = soup.find("div",attrs={"class":"meaning"}).text
  y = ("*"+x+"*")
  await client.say(y)
#~~~~~~~~~~~~~~~~~~~~~#
# Social Media Search #
#~~~~~~~~~~~~~~~~~~~~~#

#This command links to a specified Twitter profile
@client.command(pass_context=True, aliases=['twitter'])
async def twt(ctx, *args):
    if args:
        url = "https://www.twitter.com/" + "+".join(args)
        await client.say(embed=Embed(description="**[Twitter Search](%s)**" % url, color=Color.gold()))
    await client.delete_message(ctx.message)

#Searches Google Maps
@client.command(pass_context=True, aliases=[''])
async def locate(ctx, *args):
    if args:
        url = "https://maps.google.com/?q=" + "+".join(args)
        await client.say(embed=Embed(description="**[Found It!!](%s)**" % url, color=Color.gold()))
    await client.delete_message(ctx.message)

#This command searches for a person on Facebook
@client.command(pass_context=True, aliases=['fbooksearch'])
async def fb(ctx, *args):
    if args:
        url = "https://www.facebook.com/search/people/?q=" + "/".join(args)
        await client.say(embed=Embed(description="**[FB Search Results](%s)**" % url, color=Color.blue()))
    await client.delete_message(ctx.message)
###########
# N S F W #
###########
#You cant have a bot WITHOUT it having a naughty side ;)
#These commands allow users to search their favorite Porn sites.

#This command searches PornHub
@client.command(pass_context=True, aliases=['pornhub'])
async def ph(ctx, *args):
    if args:
        url = "https://www.pornhub.com/video/search?search=" + "+".join(args)
        await client.say(embed=Embed(description="**[PornHub](%s)**" % url, color=Color.light_grey()))
    await client.delete_message(ctx.message)

#This command searches YouPorn
@client.command(pass_context=True, aliases=['Youporn'])
async def yp(ctx, *args):
    if args:
        url = "https://www.youporn.com/search/?query=" + "+".join(args)
        await client.say(embed=Embed(description="**[YouPorn](%s)**" % url, color=Color.purple()))
    await client.delete_message(ctx.message)

#This command searches XNXX
@client.command(pass_context=True, aliases=['xnxx'])
async def xnx(ctx, *args):
    if args:
        url = "https://www.xnxx.com/search/" + "+".join(args)
        await client.say(embed=Embed(description="**[XNXX](%s)**" % url, color=Color.dark_blue()))
    await client.delete_message(ctx.message)

#This command searches Fuq
@client.command(pass_context=True, aliases=['fuqdotcom'])
async def fq(ctx, *args):
    if args:
        url = "https://www.fuq.com/search/" + "%20".join(args)
        await client.say(embed=Embed(description="**[Fuq](%s)**" % url, color=Color.lighter_grey()))
    await client.delete_message(ctx.message)
###########
# H E L P #
###########
#Custom Help Command
@client.command(pass_context=True)
async def help(ctx):
    em = discord.Embed(
        colour = discord.Colour.teal()
    )
    em.set_author(name="Help")
    em.add_field(name="square", value="Squares a number", inline=False)
    em.add_field(name="marco", value="Polo!!!", inline=False)
    em.add_field(name="saveme", value="WHO CAN IT BE?!?!?!?!", inline=False)
    em.add_field(name="embd", value="Embeds given text", inline=False)
    em.add_field(name="lmgtfy", value="Generates a lmgtfy link", inline=False)
    em.add_field(name="srchip", value="Searches for given IP address", inline=False)
    em.add_field(name="g", value="Searches using the Google search engine", inline=False)
    em.add_field(name="zr", value="DO A BARREL ROLL", inline=False)
    em.add_field(name="locate", value="Creates Link to map of specified location", inline=False)
    em.add_field(name="yt", value="Searches YouTube", inline=False)
    em.add_field(name="ud", value="Searches Urban Dictionary", inline=False)
    em.set_footer(text="For more commands type `help2` and for nsfw commands type `nsfw`")
    await client.say(ctx.message.author, embed=em)

#Continuation of help
@client.command(pass_context=True)
async def help2(ctx):
    em2 = discord.Embed(
        colour=discord.Colour.teal()
    )
    em2.set_author(name="Help continued...")
    em2.add_field(name="twt", value="Links to specified twitter account", inline=False)
    em2.add_field(name="fb", value="Searches for a person on Facebook", inline=False)
    em2.add_field(name="suggestion", value="Send Your Suggestions to help make the bot better", inline=False)
    em2.add_field(name="aes", value="Generates a random ａｅｓｔｈｅｔｉｃ image", inline=False)
    em2.add_field(name="yums", value="Generates a random ａｅｓｔｈｅｔｉｃ food image", inline=False)
    em2.add_field(name="finger", value="Displays given users info")
    em2.add_field(name="marry", value="marry your lover", inline=False)
    em2.add_field(name="kill", value="kill someone", inline=False)
    em2.add_field(name="punch", value="punch someone", inline=False)
    em2.add_field(name="kiss", value="Kiss your lover", inline=False)
    em2.add_field(name="clear", value="Clears the bots messages")
    em2.add_field(name="fuck", value=":smirk:", inline=False)
    em2.add_field(name="adv", value="Gives Random Bits Advice", inline=False)
    await client.say(ctx.message.author, embed=em2)

#Nsfw Command Help
@client.command(pass_context=True)
async def nsfw(ctx):
    ns = discord.Embed(
        colour=discord.Colour.teal()
    )
    ns.set_author(name="NSFW Commands")
    ns.add_field(name="ph", value="Search PornHub", inline=False)
    ns.add_field(name="yp", value="Search YouPorn", inline=False)
    ns.add_field(name="xnx", value="Search XNXX", inline=False)
    ns.add_field(name="fq", value="Search Fuq", inline=False)
    await client.send_message(ctx.message.author, embed=ns)

#Users Can Leave their suggestions to me
@client.command(pass_context=True)
async def suggestion(ctx, *args):
    argstr = " ".join(args)
    text = argstr
    suggestionsFile = open("suggestions.txt", "a+")
    suggestionsFile.write(text + "\n")
    msg = "{0.author.mention} Added your suggestion! It will be processed and may be added soon! Thanks for the help!".format(ctx)
    await client.say(msg)
####################
# I M A G E   G E N#
####################
@client.command(pass_context=True)
async def adv(ctx):
  await client.say(random.choice(tuple(config['advice'])))
  await client.delete_message(ctx.message)

@client.command(pass_context=True)
async def aes(ctx):
    inbed = discord.Embed(
        colour=discord.Colour.purple()
    )
    inbed.set_image(url=random.choice(tuple(config['aes'])))
    await client.say(embed=inbed)
    await client.delete_message(ctx.message)

#Posts Food Porn
@client.command(pass_context=True)
async def yums(ctx):
    yummy = discord.Embed(
        colour=discord.Colour.dark_green()
    )
    yummy.set_image(url=random.choice(tuple(config['yum'])))
    yummy.set_footer(text="images thanks to ***cami the marshmallow***")
    await client.say(embed=yummy)
    await client.delete_message(ctx.message)

#Users Punch Other users
@client.command(pass_context=True)
async def punch(ctx, member: discord.Member):
    if member.mention == ctx.message.author.mention:
        pnc = discord.Embed(
          colour=discord.Colour.blue()
        )
        pnc.set_image(url=config['punch'])
        await client.say(ctx.message.author.mention, embed=pnc)
        await client.delete_message(ctx.message)
    else:
        await client.say("{} got knocked the fuck out by {}".format(member.mention, ctx.message.author.mention))
    await client.delete_message(ctx.message)
#User Kills another user
@client.command(pass_context=True)
async def kill(ctx, member: discord.Member):
    if member.mention == ctx.message.author.mention:
        await client.say("{} Committed seppuku".format(member.mention, ctx.message.author.mention))
        await client.delete_message(ctx.message)
    else:
        await client.say("{} was killed by {}".format(member.mention, ctx.message.author.mention))
    await client.delete_message(ctx.message)
#User kisses another user
@client.command(pass_context=True)
async def kiss(ctx, member: discord.Member):
    await client.say("{} was kissed by {}".format(member.mention, ctx.message.author.mention))
    await client.delete_message(ctx.message)
#Self-Explanatory
@client.command(pass_context=True)
async def fuck(ctx, member: discord.Member):
    if member.mention == ctx.message.author.mention:
        await client.say("You cant fuck yourself...your dicks too small")
        await client.delete_message(ctx.message)
    else:
        await client.say("{} got their pussy filled, screws loosened, and filled with cum by {}, the sex god".format(member.mention, ctx.message.author.mention))
    await client.delete_message(ctx.message)
#Users can marry other users
client.marriage_active = False
@client.command(pass_context=True)
async def marry(ctx, member: discord.Member):
    mg = discord.Embed(
        colour=discord.Colour.dark_green()
    )
    mg.set_image(url="https://thumbs.gfycat.com/IgnorantShyCicada-size_restricted.gif")
    if client.marriage_active:
        return  # Do nothing
    client.marriage_active = True
    await client.say("{} wanna get married to {}?".format(member.mention, ctx.message.author.mention))
    reply = await client.wait_for_message(author=member, channel=ctx.message.channel, timeout=30)
    if not reply or reply.content.lower() not in ("y", "yes", "yeah"):
        await client.say("Too bad, you lose man", embed=mg)
    else:
        await client.say("Mazel Tov!")
#User can clear bots message
    client.marriage_active = False
@client.command(pass_context=True)
async def clear(ctx):
    async for msg in client.logs_from(ctx.message.channel):
        if msg.author.id == client.user.id:
            try:
                await client.delete_message (msg)
            except:
                pass
    embed = discord.Embed(description="Chat Cleaned! :fire:", color=0x00ff00)
    await client.say (embed=embed)
    await client.delete_message(ctx.message)

#Grabs a Users Info
@client.command(pass_context=True)
async def finger(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.message.author
    roles = [r.name for r in user.roles if r.name != "@everyone"]
    if roles:
        roles = sorted(roles, key=[x.name for x in ctx.message.server.role_hierarchy if x.name != "@everyone"].index)
    else:
        roles = "None"
    print(len(roles))
    if len(roles) > 16:
        roles = "Too much info to show."
    else:
        roles = "   ".join(roles)
    fg = discord.Embed(description="finger {} :".format(
        ctx.message.author.mention), title="User Info", color=0X008CFF)
    if user.avatar_url:
        fg.set_thumbnail(url=user.avatar_url)
    else:
        fg.set_thumbnail(url=user.default_avatar_url)
    fg.add_field(name="User", value=user.name)
    fg.add_field(name="Discrim", value=user.discriminator)
    if user.nick:
        fg.add_field(name="Nick", value=user.nick)
    else:
        fg.add_field(name="Nick", value="None")
    fg.add_field(name="UserID", value=user.id)
    fg.add_field(name="Stats", value=user.status)
    if user.game:
        fg.add_field(name="Currently Playing", value=user.game)
    else:
        fg.add_field(name="Currently Playing", value="Nothing")
    fg.add_field(name="AFK?", value=user.is_afk)
    fg.add_field(name="Bot?", value=user.bot)
    fg.add_field(name="Muted in the server?", value=user.mute)
    fg.add_field(name="Deafened in the server?", value=user.deaf)
    fg.add_field(name="Joined Discord On", value=user.created_at.strftime("%d %b %Y %H:%M"))
    fg.add_field(name="Joined Server On", value=user.joined_at.strftime("%d %b %Y %H:%M"))
    fg.add_field(name="Highest role color", value=user.color)
    fg.add_field(name="Roles", value=roles)
    await client.say(embed=fg)

client.run(config['token'])
