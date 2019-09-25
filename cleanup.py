import stashy
import os

stash = stashy.connect(os.environ['BB_HOST'], os.environ['BB_USER'], os.environ['BB_PASSWORD'])
for user in stash.admin.users.list():
    print(user)
