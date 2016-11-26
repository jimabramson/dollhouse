import curses
import subprocess

CMD_PLAY_ONCE = '/Applications/VLC.app/Contents/MacOS/VLC --play-and-exit'

CLIP_DEFAULT = '/Users/jim/dev/pyg/MVI_0784.h264'
CLIP_A = '/Users/jim/dev/pyg/MVI_0785.h264'
CLIP_B = '/Users/jim/dev/pyg/MVI_0786.h264'


def play_clip(clip):

    subprocess.call('{} {}'.format(CMD_PLAY_ONCE, clip), shell=True)


def main(stdscr):
    
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    stdscr.bkgd(curses.color_pair(1))
    stdscr.refresh()

    win = curses.newwin(5, 20, 5, 5)
    win.bkgd(curses.color_pair(2))
    win.box()
    win.addstr(2, 2, "Hallo, Welt!")
    win.refresh()

    while 1:
        c = stdscr.getch()
        if c == ord('a'):
            play_clip(CLIP_A)
            # TODO flush buffer
        elif c == ord('b'):
            play_clip(CLIP_B)
            # TODO flush buffer


if __name__ == '__main__':
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        print "Got KeyboardInterrupt exception. Exiting..."
        exit() 
