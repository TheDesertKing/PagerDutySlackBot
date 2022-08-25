import json

def get_secrets(path:str) -> dict:
  """Gets the API Tokens for PagerDuty and Slack
  and placing them in variables:
    PD_API_TOKEN, PD_USER_EMAIL

  Args:
    path: location of the secrets file

  Returns:
    tokens: {PD_API_TOKEN,PD_USER_EMAIL}
  """
  with open(path+"secrets.json") as secrets_file:
    secrets_dict = json.load(secrets_file)
  PD_API_TOKEN = secrets_dict['PagerDuty_API_Token']
  PD_USER_EMAIL = secrets_dict['PagerDuty_User_Email']
  tokens = {"PD_API_TOKEN":PD_API_TOKEN,"PD_USER_EMAIL":PD_USER_EMAIL}
  return tokens
  