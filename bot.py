import discord
import asyncio
import datetime
import random
import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument('--useenvironmentvariables')
parser.add_argument('--skiptimecheck')
parser.add_argument('--clearallmessages')

args = parser.parse_args()

client = discord.Client(intents=discord.Intents.default())

if args.useenvironmentvariables:
	TOKEN = os.environ.get('TOKEN')
	CHANNEL_ID = int(os.environ.get('CHANNEL_ID'))
	NAME = os.environ.get('NAME')
else:
	# Discord-Bot-Token hier einfügen
	TOKEN = 'DEIN_DISCORD_TOKEN'

	# Discord-Textkanal-ID hier einfügen
	CHANNEL_ID = DEINE_CHANNEL_ID

	# Name der Person
	NAME = "NAME_DER_PERSON"

if args.skiptimecheck:
	SKIP_TIME_CHECK = True
else:
	SKIP_TIME_CHECK = False

if args.clearallmessages:
	CLEAR_CHANNEL = True
else:
	# Soll es alle Nachrichten im Channel löschen vorm Abschicken
	CLEAR_CHANNEL = False

# Liste mit 20 personalisierten Guten-Morgen-Nachrichten
messages = [
    f"Guten Morgen {NAME}! Heute wirst du Großes erreichen, wenn du hart arbeitest und niemals aufgibst. 💪🌞",
    f"Guten Morgen {NAME}! Lass deinen Mut und deine Entschlossenheit heute unbesiegbar sein. 🦸‍♀️💪",
    f"Guten Morgen {NAME}! Starte den Tag mit dem Wissen, dass du alles erreichen kannst, was du dir vornimmst. 🌅💪",
    f"Guten Morgen {NAME}! Nutze jeden Moment heute, um deinen Träumen ein Stück näher zu kommen. ✨💭",
    f"Guten Morgen {NAME}! Lass deine Entschlossenheit heute stärker sein als deine Zweifel. 💪❤️",
    f"Guten Morgen {NAME}! Der beste Weg, um den Tag zu beginnen, ist, ihn mit einem klaren Ziel vor Augen zu starten. 🎯🌞",
    f"Guten Morgen {NAME}! Heute ist dein Tag, um zu glänzen und das Beste aus dir herauszuholen. ✨💪",
    f"Guten Morgen {NAME}! Jeder neue Tag ist eine Chance, um das zu erreichen, was gestern noch unmöglich schien. 🌅💪",
    f"Guten Morgen {NAME}! Beginne den Tag mit einem positiven Mindset und dem Wissen, dass du alles erreichen kannst, was du dir vornimmst. 😃💪",
    f"Guten Morgen {NAME}! Heute ist der perfekte Tag, um alle Zweifel und Ängste hinter dir zu lassen und voller Zuversicht nach vorne zu schauen. 💪🌞",
    f"Guten Morgen {NAME}! Sei heute mutig, sei heute stark, sei heute großartig! 💪🌅",
    f"Guten Morgen {NAME}! Nutze den Tag, um deine Träume in die Tat umzusetzen und dein volles Potenzial zu entfalten. 💭💪",
    f"Guten Morgen {NAME}! Beginne den Tag mit der Einstellung, dass alles möglich ist, wenn du hart genug arbeitest und niemals aufgibst. 🚀💪",
    f"Guten Morgen {NAME}! Heute ist dein Tag, um alles zu erreichen, was du dir vorgenommen hast. Glaube an dich selbst und gehe mit Entschlossenheit voran. 💪🌞",
    f"Guten Morgen {NAME}! Starte den Tag mit einem Lächeln und dem Wissen, dass du alles erreichen kannst, was du dir vornimmst. 😊💪",
    f"Guten Morgen {NAME}! Heute ist ein neuer Tag voller Möglichkeiten und Chancen. Nutze sie und mache das Beste daraus! 🌅✨"
]


async def send_guten_morgen():
	channel = client.get_channel(CHANNEL_ID)
	if CLEAR_CHANNEL:
		await channel.purge(check=None)
	await channel.send(random.choice(messages))


@client.event
async def on_ready():
	print(f'{client.user} wurde erfolgreich angemeldet!')
	if SKIP_TIME_CHECK:
		await send_guten_morgen()
	else:
		# Warte bis zum nächsten Morgen und sende dann den Guten Morgen-Text
		while True:
			now = datetime.datetime.now()
			next_morning = datetime.datetime(now.year, now.month, now.day, 7,
			                                 0, 0)
			if next_morning < now:
				next_morning += datetime.timedelta(days=1)
			time_to_wait = (next_morning - now).total_seconds()
			await asyncio.sleep(time_to_wait)
			now = datetime.datetime.now()
			if now.hour < 12:
				await send_guten_morgen()
	exit(0)


client.run(TOKEN)
