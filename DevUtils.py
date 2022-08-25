"""Useful functions for developing the PagerDuty Slack bot
These functions are ment to be used here, as means of testing
and gathering ID's and stuffs.
"""
from pprint import pp
from datetime import datetime, timedelta
import pdpyras as pd
from GetSecrets import get_secrets

def main():
    tokens = get_secrets('')
    session = pd.APISession(tokens['PD_API_TOKEN'], default_from=tokens['PD_USER_EMAIL'])
    p = get_pd_user_id("paul.lascar@snyk.io",session)
    pp(p)

def get_pd_user_id(email:str,session:any) -> str:
    """query the PD API for a user's ID

    Args:
        email: User's Email Address (idan.digmi@snyk.io)

    Returns:
        str: User's ID (PK1234AKD)
    """
    user_data = session.find('users', email, attribute='email')
    # print(user_data["contact_methods"][0]["id"])
    pp(user_data)
# user = session.find('schedules', 'idan.digmi@snyk.io', attribute='email')

# print(user["contact_methods"][0]["id"])

# schedule = session.get("/schedules")
# pp(schedule.json())

# for idan in session.iter_all('schedules'):
#     pp(idan)

#  sec_analyst_oncall_schedule = session.find('schedules', 'Security Analyst Oncall', attribute='summary')
#  pp(sec_analyst_oncall_schedule)
# pp(sec_analyst_oncall_data) #TODO remove

# tomorrow_at_eight = (datetime.today()+timedelta(days=2)).strftime('%Y-%m-%d')+'T20:00:00Z' #TODO remove
# tomorrow = datetime.today()+timedelta(days=2)
# print(today_at_eight)

if __name__ == '__main__':
    main()