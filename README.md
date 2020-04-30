# BitBucket Server User Cleanup

In BitBucket Server users once logged in count against the user license. This
script looks for users who have authed with AD and haven't logged in for more than
a year. They are potential candidates for cleanup.

## Install
```
pipenv install
```

## Usage
Export `BB_HOST`, `BB_USER`, `BB_PASSWORD` as environment variables.

```
pipenv shell
python cleanup.py
```
