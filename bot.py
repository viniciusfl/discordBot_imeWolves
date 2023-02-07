import sys
sys.path.append('/home/viniciushfl/desktop/tudo/faculdade/projetos/secret')
import os; os.getcwd()
import discord
import responses
from discord.ext.commands import Bot
from discord.ext import commands
from random import random

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
    #client = discord.Client(intents=intents)
    bot = commands.Bot(command_prefix='$', intents=intents)

    @bot.event
    async def on_ready():
        print(f'{bot.user} is now running!')

    @bot.event
    async def on_message(message):
        # Make sure bot doesn't get stuck in an infinite loop
        if message.author == bot.user:
            return
        
        

        # Get data about the user
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # Debug printing
        print(f"{username} said: '{user_message}' ({channel})")

        # If the user message contains a '?' in front of the text, it becomes a private message
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
        times = calculaTimes()
        for i in range(2):
            message += (f"# Campeões da {i+1}° equipe: \n")
            message += ("     Semana grátis:")
            for j in range(4):
                message += (f" {times[i][j]},")
            message += (f" {times[i][4]}\n")

            message += ("     Resto:")
            for j in range(5, 14):
                message += (f" {times[i][j]},")
            message += (f" {times[i][14]}\n\n")
        message += ("```\n")
        await ctx.send(message)

    # Remember to run your bot with your personal TOKEN
    bot.run(returnToken())


# -------------------------

def calculaTimes():
    todosCampeoes = ["Aatrox", "Ahri", "Akali", "Akshan", "Alistar", "Amumu", "Anivia", "Annie", "Aphelios", "Ashe", "Aurelion Sol", "Azir", "Bard", "Bel’Veth", "Blitzcrank", "Brand", "Braum", "Caitlyn", "Camille", "Cassiopeia", "Cho’Gath", "Corki", "Darius", "Diana", "Dr. Mundo", "Draven", "Ekko", "Elise", "Evelynn", "Ezreal", "Fiddlesticks", "Fiora", "Fizz", "Galio", "Gangplank", "Garen", "Gnar", "Gragas", "Graves", "Gwen", "Hecarim", "Heimerdinger", "Illaoi", "Irelia", "Ivern", "Janna", "Jarvan IV", "Jax", "Jayce", "Jhin", "Jinx", "K'Sante", "Kai’Sa", "Kalista", "Karma", "Karthus", "Kassadin", "Katarina", "Kayle", "Kayn", "Kennen", "Kha’Zix", "Kindred", "Kled", "Kog’Maw", "LeBlanc", "Lee Sin", "Leona", "Lillia", "Lissandra", "Lucian", "Lulu", "Lux", "Malphite", "Malzahar", "Maokai", "Master Yi", "Miss Fortune", "Mordekaiser", "Morgana", "Nami", "Nasus", "Nautilus", "Neeko", "Nidalee", "Nilah", "Nocturne", "Nunu & Willump", "Olaf", "Orianna", "Ornn", "Pantheon", "Poppy", "Pyke", "Qiyana", "Quinn", "Rakan", "Rammus", "Rek’Sai", "Rell", "Renata Glasc", "Renekton", "Rengar", "Riven", "Rumble", "Ryze", "Samira", "Sejuani", "Senna", "Seraphine", "Sett", "Shaco", "Shen", "Shyvana", "Singed", "Sion", "Sivir", "Skarner", "Sona", "Soraka", "Swain", "Sylas", "Syndra", "Tahm Kench", "Taliyah", "Talon", "Taric", "Teemo", "Thresh", "Tristana", "Trundle", "Tryndamere", "Twisted Fate", "Twitch", "Udyr", "Urgot", "Varus", "Vayne", "Veigar", "Vel’Koz", "Vex", "Vi", "Viego", "Viktor", "Vladimir", "Volibear", "Warwick", "Wukong", "Xayah", "Xerath", "Xin Zhao", "Yasuo", "Yone", "Yorick", "Yuumi", "Zac", "Zed", "Zeri", "Ziggs", "Zilean", "Zoe", "Zyra"]
    # array com o nome de todos os campeões
    campeoesSemanaGratis = ["Braum", "Camille", "Corki", "Draven", "Fiora", "Garen", "Heimerdinger", "Jarvan IV", "Kayn", "LeBlanc", "Lee Sin", "Nunu & Willump", "Samira", "Tryndamere", "Vex", "Yuumi"]
    
    times = []

    for i in range(1, 3):
        # array que vai guardar o time
        time = []

        # sorteio dos cinco campeões da semana grátis
        for _ in range(5):
            n = len(campeoesSemanaGratis)
            # sorteia um campeão
            campeao = campeoesSemanaGratis[int(n*random())-1]
            # remove das outras duas listas
            todosCampeoes.remove(campeao)
            campeoesSemanaGratis.remove(campeao)

            # adiciona ele no time
            time.append(campeao)

        # sorteio dos dez campeões restantes
        for _ in range(10):
            n = len(todosCampeoes)
            # sorteia um
            campeao = todosCampeoes[int(n*random())-1]

            # remove das duas listas
            todosCampeoes.remove(campeao)
            if campeao in campeoesSemanaGratis:
                campeoesSemanaGratis.remove(campeao)

            # adiciona ele no time
            time.append(campeao)

        times.append(time)
    return times