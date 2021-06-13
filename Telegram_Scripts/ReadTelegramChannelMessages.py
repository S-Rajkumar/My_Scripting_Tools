from telethon import TelegramClient
import asyncio

"""
#requirements.txt
1.pip install telethon
2.pip install asyncio

#get API id and hash id
1. Login to https://my.telegram.org 
2. click API Developement
3. Fill first Two Boxes and click Create
4. Note API ID nad API Hash (don't share with anyone)

# Note
# First time running this program you need to enter mobile number for login verification
# and don't change session name for next time running this program because you need to login again

"""

apiID = "123456" #replace with your API ID
apiHash = "zyxwvutsrqponmlkjihgfedcba" #replace with your API Hash
sessionName = "Raj"

client = TelegramClient(sessionName, apiID, apiHash)
client.start()
print("connected to telegram")

async def getChannelMessages(channel_link):
    chat = await client.get_entity(channel_link)
    #channel details
    #print(chat.stringify())
    print("Extracting Data From Channel ....")
    channel_messages = []
    
    ##message read newer -> older
    async for message in client.iter_messages(chat):
        if message.text == None or message.text == "" :
            continue
        #print(message.id, message.text)
        channel_messages.append(message.text)
    
    """
    ##message read older -> newer
    async for message in client.iter_messages(chat, reverse=True):
        if message.text == None or message.text == "" :
            continue
        #print(message.id, message.text)
        channel_messages.append(message.text)
    """
    """
    #message with sender name
    async for message in client.iter_messages(chat, reverse=True):
        #print(message.id, message.text)
        if message.text == None or message.text == "" :
            continue
        channel_messages.append(str(message.sender.first_name) + " : " + str(message.text))
    """
    return channel_messages

channel_link = "t.me/pygroup"
loop = asyncio.get_event_loop()
messages = loop.run_until_complete(getChannelMessages(channel_link))

print("Total Messages : " + str(len(messages)))

with open("messages.txt", "w", encoding="utf-8") as file :
    for message in messages :
        file.write(str(message) + "\n")
print("Completed")