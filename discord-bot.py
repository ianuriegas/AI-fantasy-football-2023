from discordwebhook import Discord

discord = Discord(url="https://discord.com/api/webhooks/1145048736398049361/goDZcLfOC1Hk07pfBufmUkAP9s3JBsS158yeqsUFr7mIZMzvHVxmvru3QANmqOvjdMir")
discord.post(content="Hello, world.")