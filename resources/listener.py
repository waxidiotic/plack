import json

import falcon

from .alert_slack import SlackResource

slack_resource = SlackResource()

class ListenerResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        if req.media['event'] == 'library.new':
            slack_resource.send_alert()
        else:
            pass