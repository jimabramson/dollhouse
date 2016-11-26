import curses
import os
import subprocess

CMD_PLAY_ONCE = 'omxplayer -b'

CLIP_DIR = '/home/pi'
CLIP_DEFAULT = ''
CLIP_A = 'test_640x480.mp4'


def play_clip(clip):

    clip_path = os.path.join(CLIP_DIR, clip)
    subprocess.call('{} {}'.format(CMD_PLAY_ONCE, clip_path), shell=True)


def main(stdscr):
    
    while 1:
        c = stdscr.getch()
        if c == ord(' '):
            play_clip(CLIP_A)
            curses.flushinp()            


if __name__ == '__main__':
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        print "Got KeyboardInterrupt exception. Exiting..."
        exit() 
