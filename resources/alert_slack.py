from environs import Env

import slack

env = Env()
env.read_env("conf.d/99-secrets.yaml", recurse=False)
slack_token = env("SLACK_TOKEN")
client = slack.WebClient(token=slack_token)


class SlackResource:
    def send_alert(self):
        client.chat_postMessage(channel="plex", text="this is only a test")
