import json

def get_pd_tokens(path:str='secrets.json') -> dict:
  """Gets the API Tokens for PagerDuty from the secrets.json file
  and placing them in variables:
    PD_API_TOKEN, PD_USER_EMAIL

  Args:
    path (str, optional): location of the secrets.json file

  Returns:
    tokens (dict[str:str]): {PD_API_TOKEN,PD_USER_EMAIL}
  """
  with open(path) as secrets_file:
    secrets_dict = json.load(secrets_file)
  PD_API_TOKEN = secrets_dict['PagerDuty_API_Token']
  PD_USER_EMAIL = secrets_dict['PagerDuty_User_Email']
  tokens = {"PD_API_TOKEN":PD_API_TOKEN,"PD_USER_EMAIL":PD_USER_EMAIL}
  return tokens

def get_slack_xoxb_token(path:str='secrets.json') -> str:
  """Gets the Slack Bot XOXB Token from the secrets.json file

  Args:
    path (str, optional): location of the secrets.json file

  Returns:
    SLACK_XOXB_TOKEN (str): The XOXB Token
  """
  with open(path) as secrets_file:
    secrets_dict = json.load(secrets_file)
  SLACK_XOXB_TOKEN = secrets_dict['Slack_XOXB_Token']
  return SLACK_XOXB_TOKEN
  
def get_slack_signing_token(path:str='secrets.json') -> str:
  """Gets the Slack Signing Token from the secrets.json file

  Args:
      path (str, optional): The path of the secrets.json file

  Returns:
      SLACK_SIGNING_TOKEN (str): The Singing Token
  """
  with open(path) as secrets_file:
    secrets_dict = json.load(secrets_file)
  SLACK_SIGNING_TOKEN = secrets_dict['Slack_Signing_Token']
  return SLACK_SIGNING_TOKEN 

  