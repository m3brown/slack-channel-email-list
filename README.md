# slack-channel-email-list

A simple script to list the emails of all users in a Slack channel

# Prerequisites

Essentially, you'll need to have Python and [python-slackclient](https://github.com/slackapi/python-slackclient) installed.

Guidance for installing Python: https://wiki.python.org/moin/BeginnersGuide/Download

I suggest using pipenv.  If you don't already have pipenv installed:

```
pip install pipenv
```

# Installation

```
git clone git@github.com:m3brown/slack-channel-email-list
cd slack-channel-email-list
pipenv install
```

# Running the app

```
pipenv run ./list_emails.py -t <your_token> <channel_name>
```
