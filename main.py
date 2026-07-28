import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Login sebagai {bot.user}")

@bot.command(name="buatkan")
async def buatkan(ctx, *, permintaan: str):
    text = permintaan.lower()

    if "template monetloader" in text:
        lua = '''script_name("Template")
script_author("Discord Bot")

require "lib.moonloader"

function main()
    while not isSampAvailable() do
        wait(100)
    end

    sampAddChatMessage("[Template] Loaded!", 0x00FF00)

    while true do
        wait(0)
    end
end
'''
        await ctx.send(
            file=discord.File(
                fp=discord.File(io.BytesIO(lua.encode()), filename="template.lua")
            )
        )

    elif "hud" in text:
        lua = '''script_name("HUD Example")

function main()
    while true do
        wait(0)
        -- Tambahkan kode HUD di sini
    end
end
'''
        await ctx.send(f"```lua\n{lua}\n```")

    else:
        await ctx.send("Permintaan belum tersedia.")

bot.run(TOKEN)
