import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True  # sehr wichtig!

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot is online as {bot.user}")

@bot.command()
async def info(ctx):
    embed = discord.Embed(
        title="Payment Methods",
        description="Here are the available payment options:",
        color=0x2F3136
    )
    embed.add_field(name="Paypal f&f", value="✔ Available", inline=True)
    embed.add_field(name="Paysafecard (German)", value="✔ Available", inline=True)
    embed.add_field(name="Paypal Email", value="resellfivem@gmail.com", inline=False)
    embed.set_footer(text="Feel free to contact for more details.")
    await ctx.send(embed=embed)

@bot.command()
async def website(ctx):
    if ctx.author.id == ctx.guild.owner_id:
        embed = discord.Embed(
            title="🛍️ Visit our Webstore",
            description="Looking to purchase FiveM products safely and easily?\n\nCheck out our secure and fast shop below:",
            color=0x5865F2
        )
        embed.add_field(name="🌐 Store Link", value="[Click here to open the store](https://fivem-resell.mysellauth.com)", inline=False)
        embed.set_footer(text="Fast delivery. Secure checkout. Instant access.")
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Only the server owner can use this command.")

bot.run("MTM3NTkxOTczMTAyNjAzODg2NA.G-TlmV.XPDTFfTe8csfy8PaErK4DCiQpH2mP1uQ6qr158")
