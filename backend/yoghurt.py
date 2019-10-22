import requests

import discord
from discord.ext import commands

async def get_yoghurt(ctx, lang):
	url1 = "http://localhost:8000"
	# url1 = "http://ishetaltijdvooreenbakkieyoghurt.nl"
	url2 = url1+"/plaintext.php"
	if lang == "en":
		answer = requests.get(url = url2, params = "lang=en")
		title = "Is it already time for a bakkie yoghurt?"
	else:
		answer = requests.get(url = url2)
		title = "Is het al tijd voor een bakkie yoghurt?"
	await ctx.send(embed=discord.Embed(title=title, colour=discord.Colour(0x00FFFF), description=answer.content.decode('utf-8'), url=url1 )
					.set_author(name= url1.replace("http://",""), url=url1, icon_url="https://cdn.discordapp.com/attachments/634351970471247882/634377207564992525/bakkie.png"))