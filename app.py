import os

import falcon
import slack

from resources.listener import ListenerResource

slack_token = os.environ.get('SLACK_TOKEN')
client = slack.WebClient(token=slack_token)

app = falcon.API()
lister_resource = ListenerResource()

# client.chat_postMessage(channel='plex', text='this is only a test')

app.add_route('/notify', lister_resource)