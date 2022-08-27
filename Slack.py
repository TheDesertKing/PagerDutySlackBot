import os
from GetSecrets import get_slack_xoxb_token,get_slack_signing_token
from slack_bolt import App


app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)


def set_env_vars():
    os.environ['SLACK_BOT_TOKEN'] = get_slack_xoxb_token()
    os.environ['SLACK_SIGNING_TOKEN'] = get_slack_signing_token()


def main():
    set_env_vars()
    app.start(port=int(os.environ.get("PORT", 3000)))


if __name__ == "__main__":
    main()