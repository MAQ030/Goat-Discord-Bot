from message_handling import client, TOKEN, handle_hello_message, send_message
from discord import Message

# Event handler for when the bot is ready
@client.event 
async def on_ready() -> None:
    print(f'{client.user} is now running!')

# Event handler for when a message is received
@client.event 
async def on_message(message: Message) -> None:
    # Ignore messages sent by the bot itself
    if message.author == client.user:
        return
    
    # Extract relevant information from the message
    username: str = str(message.author)
    user_message: str = message.content.lower()  # Convert to lowercase for case insensitivity
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    
    # Check if the message starts with the command prefix "!goat"
    if user_message.startswith('!goat '):
        query = user_message[6:]  # Extract the query after "!goat "
        await handle_hello_message(message, query)
    else:
        await send_message(message, user_message)

# Main function to run the bot
def main() -> None: 
    client.run(token=TOKEN)

# Entry point for the script
if __name__ == "__main__":
    main()