import os
import slack

slack_token = os.environ.get('SLACK_TOKEN')

client = slack.WebClient(token=slack_token)
client.chat_postMessage(channel='plex', text='this is only a test')