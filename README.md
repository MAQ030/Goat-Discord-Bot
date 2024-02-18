# Goat-Discord-Bot

This Discord bot retrieves and processes data from GOAT, an online store specializing in sneakers, apparel, and accessories, through web scraping techniques.

## Setup Instructions

### 1. Install Python and Required Libraries:
   - Ensure Python is installed on your system ([Download Python](https://www.python.org/))
   - Install the required libraries using pip:
     ```
     pip install discord.py python-dotenv requests
     ```

### 2. Create a Discord Bot:
   - Navigate to the Discord Developer Portal ([Discord Developer Portal](https://discord.com/developers/applications))
   - Create a new application
   - Navigate to the "Bot" tab and click "Add Bot"
   - Copy the generated token and paste it into your `.env` file as `TOKEN`

### 3. Enable Message Intents:
   - In the Discord Developer Portal, go to the "Bot" tab of your application
   - Enable the "PRESENCE INTENT" and "SERVER MEMBERS INTENT" under the "Privileged Gateway Intents" section

### Note:
- Ensure that you replace `goat_bot` with the appropriate module containing your Discord bot's code.
- Remember to handle environment variables securely.
- You may need to adjust permissions and roles within your Discord server for the bot to function correctly.

## Demonstration 
