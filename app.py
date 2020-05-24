import falcon

from resources.listener import ListenerResource

app = falcon.API()
lister_resource = ListenerResource()

# client.chat_postMessage(channel='plex', text='this is only a test')

app.add_route("/notify", lister_resource)
