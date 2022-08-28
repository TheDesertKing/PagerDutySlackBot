"""Usefull functions for the PagerDuty API.
Designed for use in a Slack+PagerDuty integration
for daily oncall notifications, for team Sonar

Author: Amit Avi Eshel
Date: 25/08/2022 
"""
from pprint import pp
from datetime import datetime, timedelta
import pdpyras as pd
from GetSecrets import get_pd_secrets


def main():
    tokens = get_pd_secrets()
    session = pd.APISession(tokens['PD_API_TOKEN'], default_from=tokens['PD_USER_EMAIL'])
    user_ids_to_emails = get_pd_user_ids_of_team("Security Analysts",session)
    oncall_users_id = get_oncall_analysts_today(session)
    oncall_users_emails = []
    for id in oncall_users_id:
        oncall_users_emails.append(user_ids_to_emails[id])
    print(oncall_users_emails)




def get_pd_user_id(email:str,session:any) -> str:
    """query the PD API using email to get ID

    Args:
        email: User's Email Address (idan.digmi@snyk.io)
        session (any): the PD API session

    Returns:
        user_id (str): User's ID (PK1234AKD)
    """
    user_data = session.find('users', email, attribute='email')
    user_id = user_data['id']
    return user_id


def get_pd_user_email(id:str,session:any) -> str:
    """query the PD API using email to get ID

    Args:
        id: User's PD ID (PAXSEW123)
        session (any): the PD API session

    Returns:
        str: User's email (idan.digmi@snyk.io)
    """
    user_data = session.rget('/users/'+id)
    return user_data['email']
    

def get_pd_team_id_by_name(team_name:str,session:any) -> str:
    """query the PD API for a team's ID by the team's name

    Args:
        team_name (str): The team's name on PD
        session (any): the PD API session

    Returns:
        team_id (str): Team's ID (PK1234AKD)
    """
    team_data = session.find('teams',team_name,attribute='name')
    team_id = team_data['id']
    return team_id


def get_pd_user_ids_of_team(team_name:str,session:any) -> dict:
    """query the PD API for all user ID's of a team 

    Args:
        team_name (str): the team description from PD
        session (any): the PD API session

    Returns:
        dict: {user email:user ID}
    """
    user_ids_to_emails = {}
    team_id = get_pd_team_id_by_name(team_name,session)
    team_members_data = session.rget('/teams/'+team_id+'/members')
    user_id_list = [user_data['user']['id'] for user_data in team_members_data]
    for id in user_id_list:
        user_ids_to_emails[id] = get_pd_user_email(id,session)
    
    return user_ids_to_emails


def get_oncall_analysts_today(session) -> str:
  """gets who's oncall today and returns their ids in a list
  
  Returns:
    sec_analyst_oncall_mails: list[str<snyk-email>] (example@snyk.io)
  """
  today_at_eight = datetime.today().strftime('%Y-%m-%d')+'T20:00:00Z'
  today_at_eight = (datetime.today()+timedelta(days=1)).strftime('%Y-%m-%d')+'T20:00:00Z' #TODO! remove
  # It's eight cause tommorow's first shift always starts at nine (21:00:00 UTC, I think)
  
  sec_analyst_oncall_data = session.list_all("oncalls",params={'schedule_ids[]':['PY7RFKD'],'until':today_at_eight})
  sec_analyst_oncall_ids = [oncall_data['user']['id'] for oncall_data in sec_analyst_oncall_data]
  return sec_analyst_oncall_ids


if __name__ == '__main__':
    main()