from GetSecrets import get_pd_secrets
from datetime import datetime,timedelta
import pdpyras as pd
from pprint import pp





def main():
  tokens = get_pd_secrets()
  session = pd.APISession(tokens['PD_API_TOKEN'], default_from=tokens['PD_USER_EMAIL'])
  oncall_analysts_today = get_oncall_analysts_today(session)
  pp(oncall_analysts_today)


if __name__ == "__main__":
  main()