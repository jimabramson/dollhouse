import curses
import os
import random
import signal
import subprocess

CMD_PLAY_ONCE = 'omxplayer -b --layer 2'
CMD_PLAY_LOOP = 'omxplayer --loop --no-osd --layer 1'

CLIP_DIR = '/home/pi/dollhouse-clips'
CLIP_DEFAULT = os.path.join(CLIP_DIR, 'Default.mp4')
CLIPS_NO = [ os.path.join(CLIP_DIR, 'No', name) for name in os.listdir(os.path.join(CLIP_DIR, 'No')) if not name.startswith('.') ]
CLIPS_YES = [ os.path.join(CLIP_DIR, 'Yes', name) for name in os.listdir(os.path.join(CLIP_DIR, 'Yes')) if not name.startswith('.') ]


def play_clip(clip):

    subprocess.call('{} {}'.format(CMD_PLAY_ONCE, clip), shell=True)


def main(stdscr):
    
    loop = subprocess.Popen('{} {}'.format(CMD_PLAY_LOOP, CLIP_DEFAULT), stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
    try:
        while 1:
            c = stdscr.getch()
            if c == ord(' '):
                play_clip(random.choice(CLIPS_NO + CLIPS_NO + CLIPS_YES))
                curses.flushinp()            
    finally:
        os.killpg(loop.pid, signal.SIGTERM)


if __name__ == '__main__':
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        print "Got KeyboardInterrupt exception. Exiting..."
        exit() 
