from discord import Intents, Client, Message, Interaction, app_commands
from datetime import time
from dotenv import load_dotenv
from os import getenv

intents = Intents.all()
intents.guilds = True
intents.reactions = True


client = Client(intents=intents)
tree = app_commands.CommandTree(client)


@tree.command(name="start_vote", description="Start a Poll")
async def startVote(interaction: Interaction, message: str, options: int, end_time: str = None):
    t = await interaction.channel.send(message)
    tt = ["\U00000030\U0000fe0f\U000020e3", "\U00000031\U0000fe0f\U000020e3", "\U00000032\U0000fe0f\U000020e3",
          "\U00000033\U0000fe0f\U000020e3", "\U00000034\U0000fe0f\U000020e3", "\U00000035\U0000fe0f\U000020e3"]
    for i, x in enumerate(tt):
        if (i < options):
            await t.add_reaction(x)
    await interaction.response.send_message("Poll started, it will end at the given time", ephemeral=True)


@client.event
async def on_ready():
    await tree.sync()

load_dotenv()
client.run(getenv("token"))
