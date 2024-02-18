from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message, Embed
import requests
import json

# Load environment variables
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# Discord client setup
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

# Function to search for products
def search(query):
    base_url = 'https://ac.cnstrc.com/autocomplete/'
    query_params = {
        'c': 'ciojs-client-2.35.2',
        'key': 'key_XT7bjdbvjgECO5d8',
        'i': '7870065f-0570-401f-a5c0-8f46e51c8742',
        's': '1',
        'num_results_Products': '25',
        'num_results_Collections': '20',
        '_dt': '1707708906394'
    }

    url = f'{base_url}{query.replace(" ", "%20")}'
    html = requests.get(url=url, params=query_params)
    output = json.loads(html.text)

    try:
        products = output['sections']['Products']
        if products:
            return products[0]
    except (KeyError, IndexError):
        return None

# Function to send messages with embeds
async def send_message(message: Message, embed: Embed) -> None:
    try:
        await message.channel.send(embed=embed)
    except Exception as e:
        print(e)

# Function to handle the !goat command
async def handle_hello_message(message: Message, query: str):
    result = search(query)
    
    if result:
        try:
            price_in_cents_cad = result['data'].get('retail_price_cents_cad', 0)
            price_in_dollars_cad = price_in_cents_cad / 100
            lowest_price_usd = result['data'].get('lowest_price_cents', 0) / 100
            lowest_price_cad = result['data'].get('lowest_price_cents_cad', 0) / 100
        except KeyError:
            await message.channel.send("Error: Product may not exist or may not be available. Please try again.")
            return

        # Create embed
        embed = Embed(
            title=result['value'],
            url=f'https://www.goat.com/en-ca/sneakers/{result["data"]["slug"]}',
            color=0x000000  # Set color to black
        )
        embed.set_thumbnail(url=result['data']['image_url'])
        embed.add_field(name='Color', value=result['data']['color'].capitalize())
        embed.add_field(name='Category', value=result['data']['category'].capitalize())        
        embed.add_field(name='Style ID', value=result['data']['sku'])
        embed.add_field(name='Retail Price (USD)', value=f'${"{:,.2f}".format(result["data"]["retail_price_cents"] / 100)}')
        embed.add_field(name='Retail Price (CAD)', value=f'${"{:,.2f}".format(price_in_dollars_cad)}')
        embed.add_field(name='Lowest Price (USD)', value=f'${"{:,.2f}".format(lowest_price_usd)}')
        embed.add_field(name='Lowest Price (CAD)', value=f'${"{:,.2f}".format(lowest_price_cad)}')
        embed.set_footer(text="© by MAQ030 and SahajKAT")
        
        await send_message(message, embed)
    else:
        await message.channel.send("Error: No matching product found. Please try again.")

# Event handlers
@client.event 
async def on_ready() -> None:
    print(f'{client.user} is now running!')

@client.event 
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    
    username: str= str(message.author)
    user_message: str = message.content.lower()  # Convert to lowercase for case insensitivity
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    
    if user_message.startswith('!goat '):
        query = user_message[6:]  # Extract the query after "!goat "
        await handle_hello_message(message, query)
    else:
        await send_message(message, user_message)

# Main function
def main() -> None: 
    client.run(token=TOKEN)

if __name__ == "__main__":
    main()
