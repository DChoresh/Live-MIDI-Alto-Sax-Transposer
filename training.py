from random import choice
from keyboard import is_pressed

note_list = ['Bb-', 'B-', 'C-', 'Db-',
             'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db',
             'D+', 'Eb+', 'E+', 'F+']


def main():
    if is_pressed('Space'):
        print(f"{choice(note_list)}\n")


if __name__ == '__main__':
    while True:
        main()
