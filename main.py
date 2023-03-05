# This file is the entry point of the program, where the user can interact with the RPA bot flow 
# designer and run the RPA bot. The file may also contain helper functions or 
# constants needed for the user interface or input/output operations.

import keyboard
import mss.tools


class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

class SCT:
    def __init__(self, l, t, w, h, i, f):
        self.left = l
        self.top = t
        self.width = w
        self.height = h
        self.increment = i
        self.file_name = f

    def move_left(self): self.left -= self.increment
    def move_right(self): self.left += self.increment
    def move_up(self): self.top -= self.increment
    def move_down(self): self.top += self.increment

    def grow_right(self): self.width += self.increment
    def grow_down(self): self.height += self.increment
    def grow_up(self): 
        self.top -= self.increment
        self.height += self.increment
    def grow_left(self): 
        self.left -= self.increment
        self.width += self.increment

    def shrink_up(self): self.height -= self.increment
    def shrink_left(self): self.width -= self.increment
    def shrink_right(self): 
        self.left += self.increment
        self.width -= self.increment
    def shrink_down(self): 
        self.top += self.increment
        self.height -= self.increment
    def snip(self):
        with mss.mss() as sct:
            sct_img = sct.grab({"left": self.left, "top": self.top - 120, "width": self.width, "height": self.height + 60})
            mss.tools.to_png(sct_img.rgb, sct_img.size, output=self.file_name)

    def set(self):
        getch = _Getch()
        print("up: move screenshot up")
        print("down: move screenshot down")
        print("left: move screenshot left")
        print("right: move screenshot right")
        print("g+up: move screenshot up")
        print("g+down: move screenshot down")
        print("g+left: move screenshot left")
        print("g+right: move screenshot right")
        print("s+up: move screenshot up")
        print("s+down: move screenshot down")
        print("s+left: move screenshot left")
        print("s+right: move screenshot right")
        print(" ")
        print("q: return to menu")
        while True:
            keyboard.add_hotkey('up', lambda: self.move_up())
            keyboard.add_hotkey('down', lambda: self.move_down())
            keyboard.add_hotkey('left', lambda: self.move_left())
            keyboard.add_hotkey('right', lambda: self.move_right())
            keyboard.add_hotkey('g+up', lambda: self.grow_up())
            keyboard.add_hotkey('g+down', lambda: self.grow_down())
            keyboard.add_hotkey('g+left', lambda: self.grow_left())
            keyboard.add_hotkey('g+right', lambda: self.grow_right())
            keyboard.add_hotkey('s+up', lambda: self.shrink_up())
            keyboard.add_hotkey('s+down', lambda: self.shrink_down())
            keyboard.add_hotkey('s+left', lambda: self.shrink_left())
            keyboard.add_hotkey('s+right', lambda: self.shrink_right())
            input_ = getch.__call__()
            if input_ == b'q' : break
            self.snip()

class Action:
    def __init__(self, type_):
        self.type = type_

    def run():
        print("Moving mouse left")


def main():
    active = 1
    getch = _Getch()
    left = 0
    top = 100
    width = 100
    height = 100
    increment = 10

    sct = SCT(left, top, width, height, increment, "img1.png")
    

    while active :
        print("a: set screenshot")
        print("q: quit")
        input_ = getch.__call__()
        if input_ == b'q' : break
        if input_ == b'a' : sct.set()

main()