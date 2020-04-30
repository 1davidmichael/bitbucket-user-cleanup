import os
import click
import stashy
from datetime import datetime, timedelta

stash = stashy.connect(os.environ['BB_HOST'], os.environ['BB_USER'], os.environ['BB_PASSWORD'])

users_for_cleanup = []

for user in stash.admin.users.list():
    if user['directoryName'] == 'Delegated LDAP Authentication':
        try:
            last_login = datetime.fromtimestamp(user['lastAuthenticationTimestamp']/1000)
            time_diff = datetime.now() - last_login
            if time_diff > timedelta(days=365):
                users_for_cleanup.append(user)
        except:
                users_for_cleanup.append(user)


for old_user in users_for_cleanup:
    if click.confirm(f"Delete {old_user['name']}?",default=True):
        stash.admin.users.delete(old_user['name'])
