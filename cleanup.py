import os
import stashy
from datetime import datetime, timedelta

stash = stashy.connect(os.environ['BB_HOST'], os.environ['BB_USER'], os.environ['BB_PASSWORD'])
for user in stash.admin.users.list():
    if user['directoryName'] == 'Delegated LDAP Authentication':
        try:
            last_login = datetime.fromtimestamp(user['lastAuthenticationTimestamp']/1000)
            time_diff = datetime.now() - last_login
            if time_diff > timedelta(days=365):
                print('%s - %s' % (user['displayName'], last_login.ctime()))
        except:
                print(user['displayName'])
