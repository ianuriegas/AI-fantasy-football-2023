import requests

webhook_url = "https://discord.com/api/webhooks/1145048736398049361/goDZcLfOC1Hk07pfBufmUkAP9s3JBsS158yeqsUFr7mIZMzvHVxmvru3QANmqOvjdMir"
starter_list = "data/starter_list/starter_list.txt"

# Read the contents of the file
with open(starter_list, "r") as f:
    file_contents = f.read()

# Send a message with file contents
payload = {
    "content": f"Optimal starting lineups for this week:\n{file_contents}"
}
requests.post(webhook_url, json=payload)
