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
