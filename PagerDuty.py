from datetime import datetime, timedelta
import pdpyras as pd
from pprint import pp

TEAM_SONAR_PD_IDS = {:'idan'}


  
"""Important IDs:
For the security analysts team:
type:team_reference
summary:Security Analysts
id:POF6OXV

For the security analyst oncall schedule
type:schedule
summary:Security
Analyst Oncall
id:PY7RFKD

Team members user IDs:
Idan:PGHHHNJ
Havaya:PVMKF6G
Amit:PQPFJEG
Paul:PP12QXD
"""


def get_oncall_analysts_today(session) -> list[str]:
  """gets who's oncall today and returns their ids in a list
  
  Returns:
    sec_analyst_oncall_mails: list[str<snyk-email>] (example@snyk.io)
  """
  today_at_eight = datetime.today().strftime('%Y-%m-%d')+'T20:00:00Z'
  # It's eight cause tommorow's first shift always starts at nine (21:00:00 UTC, I think)
  
  sec_analyst_oncall_data = session.list_all("oncalls",params={'schedule_ids[]':['PY7RFKD'],'until':today_at_eight})
  # pp(sec_analyst_oncall_data) #TODO remove
  sec_analyst_oncall_ids = [oncall_data['user']['id'] for oncall_data in sec_analyst_oncall_data]
  return sec_analyst_oncall_ids



def main():
  get_secrets('./')
  session = pd.APISession(PD_API_TOKEN, default_from=PD_USER_EMAIL)
  oncall_analysts_today = get_oncall_analysts_today(session)


if __name__ == "__main__":
  main()