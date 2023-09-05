import requests
import logging
import datetime

logging.basicConfig(level=logging.DEBUG)  # Set logging level to DEBUG
logger = logging.getLogger(__name__)
webhook_url = "https://discord.com/api/webhooks/1145048736398049361/goDZcLfOC1Hk07pfBufmUkAP9s3JBsS158yeqsUFr7mIZMzvHVxmvru3QANmqOvjdMir"
starter_list = "data/starter_list/starter_list.txt"

# Read the contents of the file
with open(starter_list, "r") as f:
    file_contents = f.read()

# Split the input text into individual league entries
entries = file_contents.split("===============================================================================================")

# Get the current date and time
current_datetime = datetime.datetime.now()

# Format the date and time as a string
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

# Process each entry and send as separate messages
header_printed = False  # Flag to keep track of whether the header has been printed
for entry in entries:
    if entry.strip():
        if not header_printed:
            payload = {
                "content": f"**@everyone**\n**Optimal starting lineups for this week ({formatted_datetime}):**\n" +
                "==============================================================================================="
            }
            try:
                logger.debug("Sending request to webhook for header...")
                requests.post(webhook_url, json=payload)
                logger.debug("Header request sent successfully.")
            except Exception as e:
                logger.error("An error occurred while sending header:", exc_info=True)
            
            header_printed = True
        
        payload = {
            "content": f"{entry}" +
            "==============================================================================================="
        }

        try:
            logger.debug("Sending request to webhook for entry...")
            requests.post(webhook_url, json=payload)
            logger.debug("Entry request sent successfully.")
        except Exception as e:
            logger.error("An error occurred while sending entry:", exc_info=True)
