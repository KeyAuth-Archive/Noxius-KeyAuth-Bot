# Bot developed by fran_afp_#0001
# franafp.es
import os
import random

import string
from datetime import datetime
footerall="franafp.es | developed by fran_afp_#0001"
import discord
import fade
import requests
from colorama import Fore
from discord.ext import commands
from discord.utils import get
from pystyle import *
w=Fore.LIGHTWHITE_EX
m=Fore.LIGHTMAGENTA_EX
black=Fore.LIGHTBLACK_EX
g=Fore.LIGHTGREEN_EX
y=Fore.LIGHTYELLOW_EX
r=Fore.LIGHTRED_EX
intents = discord.Intents.all()
intents.members = True
gui="""
        ╔═══════════════════════════╗ ╔═════════════════════╗
        ║    ╔╗╔╔═╗═╗ ╦╦╦ ╦╔═╗      ║ ║ -- [franafp.es] --  ║
        ║    ║║║║ ║╔╩╦╝║║ ║╚═╗      ║ ║                     ║
        ║    ╝╚╝╚═╝╩ ╚═╩╚═╝╚═╝      ║ ║   fran_afp_#0001    ║
        ╚═══════════════════════════╝ ╚═════════════════════╝
        ╔═══════════════════════════════════════════════════╗
        ║             [Noxius KeyAuth Bot]                  ║
        ║            [!] https://franafp.es [!]             ║
        ╚═══════════════════════════════════════════════════╝
"""
guichoice="""
                   ╔═══════════════════════════╗
                   ║   [Noxius KeyAuth Bot]    ║
                   ║                           ║
                   ║                           ║
                   ║   [1] Start Bot           ║
                   ║                           ║
                   ║   [2] franafp.es          ║
                   ║                           ║
                   ║   by fran_afp_#0001       ║
                   ╚═══════════════════════════╝

"""
os.system("cls")
faded_gui=fade.pinkred(gui)
faded_choices=fade.pinkred(guichoice)
prefix= "prefix_here"
token="token_here"
version ="1.0"
ownerid="owner_id"
sellerkey="seller_key"
logsgen="channel_id"
blacklistlogs="channel_id"
disclogs="channel_id"
downloadnoxius="link_here"
deletekeyslogs="channel_id"
redeemlogs="channel_id"
logsdownloads="channel_id"
iconsurl="https://cdn.discordapp.com/attachments/1028763505555406849/1028770051274309672/noxius_rivo_2.0_sticker.png"
resethwidlogs="channel_id"
bot = commands.Bot(command_prefix=prefix, intents=intents)
bot.remove_command("help")
bot.remove_command("clear")
keyssss = {}
print(faded_gui)
print(faded_choices)
choice = input(f"{w}[{m}+{w}] {w}Select an option: {m}")
if choice == "1":
	print("OK")
else:
	os.system("explorer https://franafp.es")

@bot.event
async def on_ready():
    os.system("clear")
    print(faded_gui)
    await bot.change_presence(status=discord.Status.dnd,activity=discord.Game(f"{prefix}help | Developer: fran_afp_#0001"))
@bot.group(invoke_without_command=True)
async def help(ctx):
    embed= discord.Embed(title="***Project Noxius Help***", description="- *List of helps*", colour=0x0001)
    embed.add_field(name="*Noxius General Help*", value=f"```{prefix}help general```")
    embed.add_field(name="*Noxius Staffs Help*", value=f"```{prefix}help staff```")
    embed.add_field(name="*Project Noxius Help*", value=f"```{prefix}help auth```")
    embed.set_footer(text=f"{ctx.author.name} | {footerall}", icon_url="https://cdn.discordapp.com/attachments/1028763505555406849/1028770051274309672/noxius_rivo_2.0_sticker.png")
    embed.set_author(name="Project Noxius", icon_url="https://cdn.discordapp.com/attachments/1028763505555406849/1028770051274309672/noxius_rivo_2.0_sticker.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1028763505555406849/1028770051274309672/noxius_rivo_2.0_sticker.png")
    await ctx.reply(embed=embed)
@help.command()
async def general(ctx):
    embed= discord.Embed(title="*Noxius General Help*", description="- *List of general commands*", colour=0x0001)
    embed.add_field(name="*Bot Ping*", value=f"```{prefix}ping```", inline=True)
    embed.add_field(name="*Bot Info*", value=f"```{prefix}botinfo```", inline=True)
    embed.add_field(name="*Server Info*", value=f"```{prefix}server```", inline=True)
    embed.add_field(name="*User Info*", value=f"```{prefix}userinfo <@user>```", inline=True)
    embed.add_field(name="*Redeem Key*", value=f"```{prefix}redeem <key>```", inline=True)
    embed.add_field(name="*Bot Uptime*", value=f"```{prefix}uptime```", inline=True)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1028763505555406849/1028770051274309672/noxius_rivo_2.0_sticker.png")
    embed.set_footer(text=f"{ctx.author.name} | {footerall}", icon_url="https://cdn.discordapp.com/attachments/1028763505555406849/1028770051274309672/noxius_rivo_2.0_sticker.png")
    embed.set_author(name="Project Noxius", icon_url="https://cdn.discordapp.com/attachments/1028763505555406849/1028770051274309672/noxius_rivo_2.0_sticker.png")
    await ctx.reply(embed=embed)
    await ctx.message.delete()

@help.command()
async def staff(ctx):
    embed=discord.Embed(title="*Noxius Staff Help*", description="- *List of all commands of Staffs*", colour=0x0001)
    embed.add_field(name="*Warn*", value=f"```{prefix}warn <@user> <reason>```", inline=True)
    embed.add_field(name="*Kick*", value=f"```{prefix}kick <@user> <reason>```", inline=True)
    embed.add_field(name="*Ban*", value=f"```{prefix}ban <@user> <reason>```", inline=True)
    embed.add_field(name="*Unban*", value=f"```{prefix}unban <@user> <reason>```", inline=True)
    embed.add_field(name="*Cooldown Channel*", value=f"```{prefix}cooldown <time>```", inline=True)
    embed.add_field(name="*Clear messages*", value=f"```{prefix}clear <messages>```", inline=True)
    embed.add_field(name="*Change Nickname*", value=f"```{prefix}nick <@user> <newname>```", inline=True)
    embed.add_field(name="*Reset Username*", value=f"```{prefix}resetnick <@user>```", inline=True)
    embed.set_author(name="Project Noxius", icon_url="https://cdn.discordapp.com/attachments/1028763505555406849/1028770051274309672/noxius_rivo_2.0_sticker.png")
    embed.set_footer(text=f"{ctx.author.name} | {footerall}", icon_url="https://cdn.discordapp.com/attachments/1028763505555406849/1028770051274309672/noxius_rivo_2.0_sticker.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1028763505555406849/1028770051274309672/noxius_rivo_2.0_sticker.png")
    await ctx.reply(embed=embed)
    await ctx.message.delete()    

@help.command()
async def auth(ctx):
    embed=discord.Embed(title="*Noxis Auth Help*", description=f"*List of all commands of Auth*", colour=0x00001)
    embed.set_author(name="Project Noxius", icon_url="https://cdn.discordapp.com/attachments/1028763505555406849/1028770051274309672/noxius_rivo_2.0_sticker.png")
    embed.set_footer(text=f"{ctx.author.name} | {footerall}", icon_url="https://cdn.discordapp.com/attachments/1028763505555406849/1028770051274309672/noxius_rivo_2.0_sticker.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1028763505555406849/1028770051274309672/noxius_rivo_2.0_sticker.png")
    embed.add_field(name="*Key Gen*", value=f"```{prefix}keygen <expire>```", inline=True)
    embed.add_field(name="*Reset Hwid*", value=f"```{prefix}resethwid <username>```", inline=True)
    embed.add_field(name="*Delete User*", value=f"```{prefix}deleteuser <username>```", inline=True)
    embed.add_field(name="*Delete License*" ,value=f"```{prefix}deletelicense <license>```", inline=True)
    embed.add_field(name="*Blacklist*", value=f"```{prefix}blacklist <ip/hwid/reason> <reason>```", inline=True)
    embed.add_field(name="*Extend License Time*", value=f"```{prefix}extend <username> <subs> <days>```", inline=True)
    embed.add_field(name="*Unblacklist*", value=f"```{prefix}unblacklist <ip/hwid/username> <reason>```", inline=True)
    embed.add_field(name="*Account Info*", value=f"```{prefix}userinfo <username>```", inline=True)
    await ctx.reply(embed=embed)
    await ctx.message.delete()

@bot.event
async def on_command_error(ctx,error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.reply(embed=discord.Embed(title="*Project Noxius Invalid Command*",description=f"{ctx.author.name}, Invalid command, you can do `!help` for all commands!",colour=0xff0000))
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.reply(embed=discord.Embed(title="*Project Noxius Missin Arguments*",description=f"{ctx.author.name}, Command Missing Argument!",colour=0x00000))
	print(f"        {m}[{w}x{m}] {r}{error} {m}[{w}x{m}]")

@bot.command()
@commands.has_permissions(administrator = True)
async def clear(ctx):
    os.system("clear")
    print(faded_gui)
    await ctx.author.send(embed=discord.Embed(title="Project Noxius | Console sucesfully cleaned", description=f"*{ctx.author.mention} Console cleaned*", colour=0x00001))
    await ctx.message.delete()
@bot.command()
@commands.has_permissions(kick_members=True) 
async def kick(ctx, member: discord.Member, *, reason=None):
	try:
		await member.kick(reason=reason)
		embed=discord.Embed(title="*Project Noxius | User kicked sucesfully*",description=f"{member}, Has been Kicked from {ctx.guild.name}.\nReason is `{reason}`. This Kick was requested from\n{ctx.author.mention}",colour=0x00000)
		embed.add_field(name="*Expiration:*", value=f"```Permantly```", inline=True)
		embed.add_field(name="*Kicked By:*", value=f"```{ctx.author}```", inline=True)
		await ctx.send(embed=embed)
		logs_channel = bot.get_channel(int(disclogs))
		await logs_channel.send(embed=embed)
	except Exception as e:
		await ctx.reply(f"*Failed to kick:* {e}  ")
@bot.command()
@commands.has_permissions(ban_members=True) 
async def ban(ctx, member: discord.Member, *, reason=None):
	try:
		await member.ban(reason=reason)
		embed=discord.Embed(title="*Project Noxius | User banned sucesfully*",description=f"{member}, Has been banned from **{ctx.guild.name}**.\n This ban was requested from\n{ctx.author.mention}",colour=0x00000)
		embed.add_field(name="*Expiration:*", value=f"```Permantly```", inline=True)
		embed.add_field(name="*Banned By:*", value=f"```{ctx.author}```", inline=True)
		embed.add_field(name="*Reason:*", value=f"```{reason}```")
		await ctx.send(embed=embed)
		logs_channel = bot.get_channel(int(disclogs))
		await logs_channel.send(embed=embed)
	except Exception as e:
		await ctx.reply(f"*Failed to ban: {e}*")
@bot.command()
@commands.has_permissions(manage_messages=True)
async def cooldown(ctx, seconds:int):
	await ctx.channel_edit.edit(slowmode_delay=seconds)
	await ctx.send(embed=discord.Embed(title="Project Noxius | Cooldown Specificated",description=f"*SlowMode Is {seconds} in {ctx.channel.mention}+",colour=0x00000))
	logs_channel = bot.get_channel(int(disclogs))
	await logs_channel.send(embed=discord.Embed(title="<a:zzzzz:1030767093613862962> SlowMode!",description=f"SlowMode Is {seconds} in {ctx.channel.mention}",colour=0x00000))
@bot.command()
@commands.has_permissions(ban_members=True) 
async def unban(ctx, username,*, reason=None):
	banlist = ctx.guild.bans()
	user = None
	for ban in banlist:
		if ban.user.name == username:
			user = ban.user
	await ctx.guild.unban(user,reason=reason)
	embed=discord.Embed(title="*Project Noxius | User unbanned sucesfully*",description=f"*{user}, Has been Unbanned from ProjectNoxius \n Reason is `{reason}`. This Unban was requested from*\n{ctx.author.mention}",colour=0x00000)
	embed.add_field(name="*Unbanned By:*", value=f"`{ctx.author}`", inline=True)
	await ctx.send(embed=embed)
	logs_channel = bot.get_channel(int(disclogs))
	await logs_channel.send(embed=embed)
@bot.command()
async def ping(ctx):
	await ctx.reply(embed=discord.Embed(title="*:ping_pong: Project Noxius Pong!*",description=f"*The bot latency is {round(bot.latency * 1000)}ms*",colour=0x00000))
@bot.command(aliases=['purge','clear'])
@commands.has_permissions(manage_messages=True)
async def clean(ctx,tot:int):
	if tot == 0:
		await ctx.reply("Please specify the number of messages you want to delete!")
	elif tot <= 0:
		await ctx.reply("The number must be bigger than 0!")
	else:
		await ctx.channel.purge()
@bot.command()
@commands.has_permissions(change_nickname=True)
async def nick(ctx, member: discord.Member, nick=None):
	await member.edit(nick=nick)
	await ctx.reply(f'Nickname was changed to {nick}')
	await ctx.reply(embed=discord.Embed(title="<:bot:1030494760089165886> Nickname!",description=f'Nickname was changed to {nick}',colour=0x00000))
@bot.command()
async def botinfo(ctx):
	members = 0
	for guild in bot.guilds:
		members += guild.member_count - 1
	embed=discord.Embed(title="**Project Noxius Information**",colour=0x00000)
	embed.add_field(name="*Bot Status:*", value=f"<a:yesverify:1030494749804744765> Working | {version}", inline=True)
	embed.add_field(name="*Developer*", value=f"```fran_afp_#0001```", inline=True)
	await ctx.reply(embed=embed)	
@bot.command()
@commands.has_permissions(manage_messages=True)
async def warn(ctx, member: discord.Member, *, reason=None):
	try:
		embed=discord.Embed(title="*Project Noxius: User was warned sucesfully*",description=f"{member.mention}, has been warned from {ctx.author.mention} Reason is ``{reason}``.\nThis warn was requested from {ctx.author.mention}",colour=0x00000)
		embed.add_field(name="**Expiration:**", value=f"``Permantly``", inline=True)
		embed.add_field(name="**Warned By:**", value=f"``{ctx.author}``", inline=True)
		embed.set_footer(text=f"{ctx.author} | {footerall}")
		await ctx.send(embed=embed)
		await member.send(embed=discord.Embed(title="**You Have Been Warned**",description=f"{member}, you been warned from {ctx.author.mention} Reason is ``{reason}``.\nThis warn was requested from {ctx.author}",colour=0x00000))
		logs_channel = bot.get_channel(int(disclogs))
		await logs_channel.send(embed=embed)
	except:
		await ctx.send(embed=discord.Embed(title="**You Have Been Warned**",description=f"{member}, you been warned from {ctx.author.mention} Reason is ``{reason}``.\nThis warn was requested from {ctx.author.mention}",colour=0x00000))
@bot.command()
async def redeem(ctx,lic):
	global keyssss
	role = discord.utils.get(ctx.guild.roles, name="User")

	if role not in ctx.author.roles:
		logsgen2=bot.get_channel(int(redeemlogs))
		await logsgen2.send(embed=discord.Embed(title=f"Someone tried redeem a key without {role}", description=f"{ctx.author.mention} in his MD", colour=0x00001))
		await ctx.message.delete()
		return
	try:
		password = "".join(random.choice(string.ascii_letters+string.digits) for i in range(10))
		username = f"{ctx.author.id}"
		req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=activate&user={username}&key={lic}&pass={password}")
		if req.json()["success"] == True:
			expire = req.text.split('"expiry":"')[1].split('"')[0]
			expire = datetime.utcfromtimestamp(int(expire)).strftime('%Y-%m-%d %H:%M:%S')
			sub = keyssss[lic]
			keyssss.pop(lic)
			role = discord.utils.get(ctx.guild.roles, name="Customer")
			user =ctx.message.author
			await user.add_roles(role)
			await ctx.reply(embed=discord.Embed(title="*License Activated*",description=f"{ctx.author.mention}, Your **{sub}** key has been activated. Your Subscription expires: `{expire}`",colour=0x00000))
			embed=discord.Embed()
			embed.add_field(name="*Username:*", value=f"```{username}```", inline=True)
			embed.add_field(name="*Password:*", value=f"```{password}```", inline=True)
			embed.add_field(name="*Key:*", value=f"```{lic}```", inline=True)
			embed.add_field(name="*Redeemed ID:*", value=f"```{ctx.author} : {ctx.author.id}```", inline=True)
			embed.add_field(name="*Expire:*", value=f"```{expire}```", inline=True)
			await ctx.author.send(embed=embed)
			logs_channel = bot.get_channel(int(redeemlogs))
			await logs_channel.send(embed=discord.Embed(title="Project Noxius Key Redeem", description=f"```Key: {lic} | Redeemed by {ctx.author}```", colour=0x000001))
			await ctx.message.delete()
		else:
			await ctx.reply(embed=discord.Embed(title="*Account creation failure!*",description=f"License is invalid, sent information to DM {ctx.author.mention}",colour=0x00000))
			await ctx.author.send(req.json()["message"])
			logsgen2=bot.get_channel(int(redeemlogs))
			await logsgen2.send(embed=discord.Embed(title=f"Someone tried redeem a invalid key", description=f"{ctx.author.mention} in {ctx.guild.name} or his MD", colour=0x00001))
			await ctx.message.delete()
			return
	except Exception as m:
		await ctx.reply("ERROR !")
		await ctx.reply(m)
@bot.command()
@commands.has_permissions(administrator = True)
async def resethwid(ctx,user,reason):
	role = discord.utils.get(ctx.guild.roles, name="Manager") 
	if role not in ctx.author.roles:
		return
	req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=resetuser&user={user}")
	
	if req.json()["success"] == True:
		await ctx.reply(embed=discord.Embed(title="*Reset Completed!*",description=f"Reset For User `{user}` was reset for reason `{reason}`",colour=0x00000))
		logs_channel = bot.get_channel(int(resethwidlogs))
		await logs_channel.send(embed=discord.Embed(title="*Reset Completed!*",description=f"{ctx.author.mention}, Used Reset command for `{user}`  reset  reason `{reason}`",colour=0x00000))
	else:
		await ctx.reply("Failed To Reset The User!")
@bot.command()
@commands.has_permissions(administrator = True)
async def deleteuser(ctx,user):
	req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=deluser&user={user}")
	if req.json()["success"] == True:
		await ctx.reply(embed=discord.Embed(title="Username Deleted!",description='Succesfully Deleted User',colour=0x0000))
	else:
		await ctx.reply("Failed To Delete The User!")
@bot.command()
@commands.has_permissions(administrator = True)
async def banaccount(ctx,user,*,reason=None):
	req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=banuser&user={user}&reason={reason}")
	if req.json()["success"] == True:
		embed=discord.Embed(title="**Project Noxius: User was Banned**",description=f"{user}, Has been banned from {ctx.guild.name} .\nReason is `{reason}`. This ban was requested from\n{ctx.author.mention}",colour=0x00000)
		embed.add_field(name="Expiration:", value=f"``Permantly``", inline=True)
		embed.add_field(name="Banned By:", value=f"``{ctx.author}``", inline=True)
		await ctx.reply(embed=embed)
	else:
		await ctx.reply("Failed To Ban The User!")
@bot.command()
@commands.has_permissions(administrator = True)
async def unbanaccount(ctx,user):
	req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=unbanuser&user={user}")
	if req.json()["success"] == True:	
		embed=discord.Embed(title="**Project Noxius: User was unbanned**",description=f"{user}, Has been unbanned from {ctx.guild.name}.\n",colour=0x00000)
		embed.add_field(name="Unbanned By:", value=f"``{ctx.author}``", inline=True)
		await ctx.reply(embed=embed)
	else:
		await ctx.reply("Failed To Unban The User!")
@bot.command()
async def deletelicense(ctx,lic):
	req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=del&key={lic}")
	if req.json()["success"] == True:
		await ctx.reply(embed=discord.Embed(title="Licnese Deleted!",description='Succesfully Deleted License',colour=0x00000))
		logs_channel= bot.get_channel(int(deletekeyslogs))
		await logs_channel.send(embed=discord.Embed(title="Project Noxius License Deleted!",description=f'Succesfully Deleted License ({lic}) by {ctx.author.mention}',colour=0x00001))
	else:
		await ctx.reply("Something went wrong.")
@bot.command()
@commands.has_permissions(administrator = True)
async def extend(ctx,user,sub,days):
	req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=extend&user={user}&sub={sub}&expiry={days}")
	print(req.text)
	if req.json()["success"] == True:
		await ctx.reply(embed=discord.Embed(title="Extended!",description='Succesfully Extended User',colour=0x00000))
	else:
		await ctx.relpy("Failed To Extend The User!")
@bot.command()
@commands.has_permissions(administrator = True)
async def blacklist(ctx,inputofuser):
	role = discord.utils.get(ctx.guild.roles, name="Manager") 
	if role not in ctx.author.roles:
		return
	if len(inputofuser) == 44:
		oii = f"hwid={inputofuser}"
	else:
		oii = f"ip={inputofuser}"
	req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=black&{oii}")
	if req.json()["success"] == True:
		await ctx.reply(embed=discord.Embed(title="**Succesfully BlackListed!**",description=f"{ctx.author.mention}, Added {inputofuser} To Blacklist",colour=0x00000))
		await blacklistlogs.send(embed=discord.Embed(title="**Succesfully BlackListed!**",description=f"{ctx.author.mention}, Added {inputofuser} To Blacklist",colour=0x00000))
		
	else:
		await ctx.reply(embed=discord.Embed(title="**Failure BlackListed!**",description=f"{ctx.author.mention}, Cannot Blacklist!",colour=0x00000))
@bot.command()
@commands.has_permissions(administrator = True)
async def unblacklist(ctx,inputofuser):
	role = discord.utils.get(ctx.guild.roles, name="Manager") 
	if role not in ctx.author.roles:
		return
	if len(inputofuser) == 44:
		oii = f"hwid={inputofuser}"
	else:
		oii = f"ip={inputofuser}"
	req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=delblack&{oii}")
	if req.json()["success"] == True:
		await ctx.reply(embed=discord.Embed(title="**Succesfully UnBlackListed!**",description=f"{ctx.author.mention}, Unblacklisted {inputofuser}",colour=0x00000))
		logs_channel = bot.get_channel(int(blacklistlogs))
		await logs_channel.send(embed=discord.Embed(title="**Succesfully UnBlackListed!**",description=f"{ctx.author.mention}, Unblacklisted {inputofuser}",colour=0x00000))
	else:
		await ctx.reply(embed=discord.Embed(title="**Failure UnBlackList!**",description=f"{ctx.author.mention}, something went wrong",colour=0x00000))
@bot.command()
@commands.has_permissions(administrator = True)
async def keygen(ctx,day:int):
	
	global keyssss
	role = discord.utils.get(ctx.guild.roles, name=".") 
	if role not in ctx.author.roles:
		logsgen2=bot.get_channel(int(logsgen))
		await logsgen2.send(embed=discord.Embed(title="Someone tried gen a key", description=f"{ctx.author.mention} tried a gen key", colour=0x00001))
		await ctx.message.delete()
		return
	req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=add&expiry={day}&mask=NOӾIUS-XXXXXX-XXXXXX&level=1&amount=1&format=json")
	if req.json()["success"] == True:
		key = req.json()["key"]
		keyssss[key] = day
		embed1=discord.Embed(title="**Project Noxius Key Generated**",description=f"```{key}```",colour=0x00001)
		embed1.set_author(name="Project Noxius", icon_url=iconsurl)
		embed1.set_footer(text=footerall, icon_url=iconsurl)
		embed1.set_thumbnail(url=iconsurl)
		logsgen2=bot.get_channel(int(logsgen))
		embed=discord.Embed(title="**Key Generated**",description=f"{ctx.author.mention} ```Generated 1 key, (expire in {day} days)``` ",colour=0x00001)
		embed.set_author(name="Project Noxius" ,icon_url=iconsurl)
		embed.set_footer(text=footerall, icon_url=iconsurl)
		embed.set_thumbnail(url=iconsurl)
		await logsgen2.send(embed=embed)
		await ctx.reply(embed=embed)
		await ctx.author.send(embed=embed1)
	else:
		await ctx.send("Failed To Gen The Key!")
@bot.command()
async def prices(ctx):
	embed=discord.Embed(title="***ProjectNoxius Prices <:noxiusrivo2:1034370627043344414>***", description="- *1 Month Key* <:arrow:1034476786056175688> **10€**\n - *Lifetime Key* <:arrow:1034476786056175688> **15€**\n **__Reseller Plan__ <a:_creditcard:1034366627791261706> **\n - *Buy 3 Keys of 50%*\n - *Later you can Buy only a Key yo 60%*\n **__Infinite Gen Keys__ <:lean:1034370612799475712> **\n - *Infinite gen monthly Keys* <:arrow:1034476786056175688> **40€**\n - *All kinds of keys* <:arrow:1034476786056175688> **60€** \n - *No limits or cooldowns*", colour=0x00000)
	embed.set_author(name="ProjectNoxius", icon_url=iconsurl)
	embed.set_footer(text=footerall, icon_url=iconsurl)
	embed.set_thumbnail(url=iconsurl)
	await ctx.reply(embed=embed)
	await ctx.message.delete()
@bot.command()
async def status(ctx):
	embed=discord.Embed(title="***Project Noxius Status***", description="\n *FiveM Unban* <:arrow:1034476786056175688> **Working** <a:yesverify:1034461680144502814> \n *Fortnite Unban* <:arrow:1034476786056175688> **Working** <a:yesverify:1034461680144502814> \n *Apex Unban* <:arrow:1034476786056175688> **Working** <a:yesverify:1034461680144502814> \n *Valorant Unban* <:arrow:1034476786056175688> **Working** <a:yesverify:1034461680144502814> \n *FiveM Cheat* <:arrow:1034476786056175688> **Developing** <:code:1034367846391746590> ", colour=0x00001)
	embed.set_author(name="Project Noxius",icon_url=iconsurl)
	embed.set_footer(text=footerall, icon_url=iconsurl)
	embed.set_thumbnail(url=iconsurl)
	await ctx.reply(embed=embed)
	await ctx.message.delete()
@bot.command()
async def download(ctx):
	role = discord.utils.get(ctx.guild.roles, name="Customer")
	if role not in ctx.author.roles:
		logsgen2=bot.get_channel(int(logsdownloads))
		await logsgen2.send(embed=discord.Embed(title="Someone tried download", description=f"{ctx.author.mention} tried download", colour=0x00001))
		return
	else:
		embed=discord.Embed(title="*Project Noxius Download*", description=f"{downloadnoxius}", colour=0x000001)
		embed.set_author(name="Project Noxius", icon_url=iconsurl)
		embed.set_footer(text=footerall, icon_url=iconsurl)
		embed.set_thumbnail(url=iconsurl)
		await ctx.author.send(embed=embed)
		logsgen2=bot.get_channel(int(logsdownloads))
		await ctx.reply(embed=discord.Embed(title="Project Noxius download <:Caixa:1034575086738485289> ", description=f"Check your DM", colour=0x00001))
		await ctx.message.delete()
		await logsgen2.send(embed=discord.Embed(title="Project Noxius download <:Caixa:1034575086738485289> ", description=f"{ctx.author.mention} <:arrow:1034476786056175688>  download", colour=0x00001))
bot.run(token)
