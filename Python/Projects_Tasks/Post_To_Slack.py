from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Set up the Slack app credentials and the message to post
client = WebClient(token='xoxb-5269633703504-5242306948566-2uYCVfPieutWz9Q7z64d9nKs')
channel_id = 'D0577UL6K9B'
message = 'Hello there, this message sended from python code from Laptop of Hossam'

# Post the message to the specified channel
try:
    response = client.chat_postMessage(channel=channel_id, text=message)
    print("Message posted: ", response['ts'])
except SlackApiError as e:
    print("Error posting message: {}".format(e))
    