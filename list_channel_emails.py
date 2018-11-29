#!/usr/bin/env python
from slackclient import SlackClient
import argparse
import os
import sys

parser = argparse.ArgumentParser(description="Get emails for slack channel. Access token must be provided by SLACK_TOKEN environment variable or the -t optional argument.")
parser.add_argument("channel", type=str, help="requested channel")
parser.add_argument("-t", type=str, help="access token (or use env var SLACK_TOKEN)", default=os.environ.get("SLACK_TOKEN"))

args = parser.parse_args()

if not args.t:
    parser.print_help(sys.stderr)
    sys.exit(2)

sc = SlackClient(args.t)
channels = sc.api_call("channels.list", exclude_archived=1)
for channel in sc.api_call("channels.list", exclude_archived=1)["channels"]:
    if channel["name"] == args.channel:
        channel_id = channel["id"]
        break
else:
    raise Exception("Could not find channel: {}".format(args.channel))

all_users = sc.api_call("users.list")["members"]
channel_members = sc.api_call("channels.info", channel=channel_id)["channel"]["members"]

for user in all_users:
    if user["id"] in channel_members and not user["deleted"]:
        email = user.get("profile", {}).get("email")
        if email:
            print(email)
