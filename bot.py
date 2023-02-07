import sys
sys.path.append('/home/viniciushfl/desktop/tudo/faculdade/projetos/secret')

import discord
import responses
from discord.ext.commands import Bot
from discord.ext import commands
from random import random

# Import token locally for security reasons
from module1 import returnToken 


# Send messages
async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    intents = discord.Intents().all()
    bot = commands.Bot(command_prefix='$', intents=intents)

    @bot.event
    async def on_ready():
        print(f'{bot.user} is now running!')

    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")

        if user_message[0] == '$':
            await bot.process_commands(message)
        else:
            await send_message(message, user_message, is_private=False)


    @bot.command()
    async def test(ctx, arg):
        await ctx.send(arg)

    @bot.command(pass_context=True)
    async def times(ctx):
        message = "```markdown\n"
        teams = calculateTeams()
        for i in range(2):
            message += (f"# Campeões da {i+1}° equipe: \n")
            message += ("     Semana grátis:")
            for j in range(4):
                message += (f" {teams[i][j]},")
            message += (f" {teams[i][4]}\n")

            message += ("     Resto:")
            for j in range(5, 14):
                message += (f" {teams[i][j]},")
            message += (f" {teams[i][14]}\n\n")
        message += ("```\n")
        await ctx.send(message)


    bot.run(returnToken())

# --- ---  auxiliary functions  ---  ---  

def calculateTeams():
    allChamps = ["Aatrox", "Ahri", "Akali", "Akshan", "Alistar", "Amumu", "Anivia", "Annie", "Aphelios", "Ashe", "Aurelion Sol", "Azir", "Bard", "Bel’Veth", "Blitzcrank", "Brand", "Braum", "Caitlyn", "Camille", "Cassiopeia", "Cho’Gath", "Corki", "Darius", "Diana", "Dr. Mundo", "Draven", "Ekko", "Elise", "Evelynn", "Ezreal", "Fiddlesticks", "Fiora", "Fizz", "Galio", "Gangplank", "Garen", "Gnar", "Gragas", "Graves", "Gwen", "Hecarim", "Heimerdinger", "Illaoi", "Irelia", "Ivern", "Janna", "Jarvan IV", "Jax", "Jayce", "Jhin", "Jinx", "K'Sante", "Kai’Sa", "Kalista", "Karma", "Karthus", "Kassadin", "Katarina", "Kayle", "Kayn", "Kennen", "Kha’Zix", "Kindred", "Kled", "Kog’Maw", "LeBlanc", "Lee Sin", "Leona", "Lillia", "Lissandra", "Lucian", "Lulu", "Lux", "Malphite", "Malzahar", "Maokai", "Master Yi", "Miss Fortune", "Mordekaiser", "Morgana", "Nami", "Nasus", "Nautilus", "Neeko", "Nidalee", "Nilah", "Nocturne", "Nunu & Willump", "Olaf", "Orianna", "Ornn", "Pantheon", "Poppy", "Pyke", "Qiyana", "Quinn", "Rakan", "Rammus", "Rek’Sai", "Rell", "Renata Glasc", "Renekton", "Rengar", "Riven", "Rumble", "Ryze", "Samira", "Sejuani", "Senna", "Seraphine", "Sett", "Shaco", "Shen", "Shyvana", "Singed", "Sion", "Sivir", "Skarner", "Sona", "Soraka", "Swain", "Sylas", "Syndra", "Tahm Kench", "Taliyah", "Talon", "Taric", "Teemo", "Thresh", "Tristana", "Trundle", "Tryndamere", "Twisted Fate", "Twitch", "Udyr", "Urgot", "Varus", "Vayne", "Veigar", "Vel’Koz", "Vex", "Vi", "Viego", "Viktor", "Vladimir", "Volibear", "Warwick", "Wukong", "Xayah", "Xerath", "Xin Zhao", "Yasuo", "Yone", "Yorick", "Yuumi", "Zac", "Zed", "Zeri", "Ziggs", "Zilean", "Zoe", "Zyra"]
    # TODO: What happens when free week champs change?
    freeWeekChamps = ["Braum", "Camille", "Corki", "Draven", "Fiora", "Garen", "Heimerdinger", "Jarvan IV", "Kayn", "LeBlanc", "Lee Sin", "Nunu & Willump", "Samira", "Tryndamere", "Vex", "Yuumi"]
    
    teams = []

    for i in range(1, 3):
        team = []

        for _ in range(5):
            n = len(freeWeekChamps)

            campeao = freeWeekChamps[int(n*random())-1]

            allChamps.remove(campeao)
            freeWeekChamps.remove(campeao)


            team.append(campeao)

        for _ in range(10):
            n = len(allChamps)
            campeao = allChamps[int(n*random())-1]

            allChamps.remove(campeao)
            if campeao in freeWeekChamps:
                freeWeekChamps.remove(campeao)

            team.append(campeao)

        teams.append(team)
    return teams