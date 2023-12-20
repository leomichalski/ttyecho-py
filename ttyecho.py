# USAGE:
# sudo python2 ttyecho.py
# sudo python3 ttyecho.py

import os
import termios
from fcntl import ioctl

# To find out the terminal devpts file, run "tty" command in it.
DEV_PTS = "/dev/pts/1"
CMD_LIST = ['ls\n']*20

fd = os.open(DEV_PTS, os.O_RDWR)

for cmd in CMD_LIST:
    for c in cmd:
        ioctl(fd, termios.TIOCSTI, c)

os.close(fd)
