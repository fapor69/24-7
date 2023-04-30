import keep_alive
import discord
from discord.ext import commands
import os

client=commands.Bot(command_prefix=':', self_bot=True, help_command=None)

GUILD_ID = id
CHANNEL_ID = id

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd)
    print(f'Logged in as {client.user} ({client.user.id})')
    vc = discord.utils.get(client.get_guild(GUILD_ID).channels, id = CHANNEL_ID)
    await vc.guild.change_voice_state(channel=vc, self_mute=False, self_deaf=False)
    print(f"Successfully joined {vc.name} ({vc.id})")

keep_alive.keep_alive()
token = os.environ.get("token")
client.run(token)
