#!/usr/bin/env python

import curses
import logging
import os
import random
import signal
import subprocess
import sys


logging.basicConfig(filename='/home/pi/dollhouse-control.log', level=logging.INFO)
log = logging.getLogger()

CMD_PLAY_ONCE = '/usr/bin/omxplayer -b --no-keys --layer 2'
CMD_PLAY_LOOP = '/usr/bin/omxplayer -b --no-keys --loop --no-osd --layer 1'


def get_clips(clip_dir, path):
    dirname = os.path.join(clip_dir, path)
    return [os.path.join(dirname, name) for name in os.listdir(dirname) if not name.startswith('.')]


def play_clip(clip):

    try:
        subprocess.call('{} {}'.format(CMD_PLAY_ONCE, clip), shell=True)
    except Exception, e:
        log.exception('could not play clip')
        raise


def main(stdscr, clip_dir):
    
    clip_default = os.path.join(clip_dir, 'Default.mp4')
    clips_no = get_clips(clip_dir, 'No')
    clips_yes = get_clips(clip_dir, 'Yes')

    # startup diagnostics
    log.info('using default clip: %s', clip_default)
    log.info('using "No" clips (%s):', len(clips_no))
    for clip in clips_no:
        log.info('\t%s', clip)
    log.info('using "Yes" clips (%s):', len(clips_yes))
    for clip in clips_yes:
        log.info('\t%s', clip)
    # end diagnostics

    loop = subprocess.Popen('{} {}'.format(CMD_PLAY_LOOP, clip_default), stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
    try:
        while 1:
            c = stdscr.getch()
            if c == ord(' '):
                play_clip(random.choice(clips_no + clips_no + clips_yes))
                curses.flushinp()            
    finally:
        os.killpg(loop.pid, signal.SIGTERM)


if __name__ == '__main__':
    
    log.info('starting up')
    clip_dir = sys.argv[1]
    log.info('clip_dir: %s', clip_dir)
    try:
        curses.wrapper(main, clip_dir)
    except KeyboardInterrupt:
        log.info('keyboard interrupt, exiting')
    
    log.info('shutting down')    
    exit()

