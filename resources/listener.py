import json

import falcon

class ListenerResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps("{ 'hello': 'world' }")