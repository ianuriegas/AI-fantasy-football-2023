import time
import requests

webhook_url = "https://discord.com/api/webhooks/1145048736398049361/goDZcLfOC1Hk07pfBufmUkAP9s3JBsS158yeqsUFr7mIZMzvHVxmvru3QANmqOvjdMir"
starter_list = "data/starter_list/starter_list.txt"

# Function to check if the current time has minutes ending in :00
def wait_until_end_of_hour():
    while True:
        current_minute = time.localtime().tm_min
        if current_minute == 20:
            break
        time.sleep(60)  # Wait for a minute before checking again

# Wait until the end of the hour (when minutes are :00)
wait_until_end_of_hour()

# Read the contents of the file
with open(starter_list, "r") as f:
    file_contents = f.read()

# Send a message with file contents
payload = {
    "content": f"**@everyone**\n**Optimal starting lineups for this week:**\n{file_contents}"
}
requests.post(webhook_url, json=payload)
