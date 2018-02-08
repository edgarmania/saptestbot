import sys
import time

from starterbot import parse_slack_output, slack_client, BOT_ID

# COMMANDS
from commands.osinfo import get_platform, get_release

cmd_names = ('platform', 'release')
cmd_functions = (get_platform, get_release)
COMMANDS = {
     "platform" : get_platform,
     "release"  : get_release
}

def handle_command(cmd, channel):
    cmd = cmd.split()
    cmd, args = cmd[0], cmd[1:]

    if cmd in COMMANDS:
        if args:
            response = COMMANDS[cmd](*args)
        else:
            response = COMMANDS[cmd]()
    else:
        response = ('Not sure what you mean'
                    'I can help you with these commands:\n'
                    '{}'.format('\n'.join(cmd_names)))

    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)

if __name__ == '__main__':
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("saptestbot connected and running")
        while True:
            command,channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
