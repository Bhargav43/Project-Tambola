""" Module Returns Hex-Color Sets as Required by tambola_printer.py"""

# pylint: disable= C0301, R1721

import random

def colors(selected='any'):
    """
    Function for color-code sets.
    """
    cols = {
        # Order : ( text, ticket, blank )
        'sky': ('#0795C9', '#5BCFD2', '#EEFFFF'),
        'blue': ('#0D1C80', '#141495', '#DDEAFA'),
        'green': ('#08C414', '#28AE31', '#D5FFD8'),
        'yellow': ('#FFCD2C', '#FFD700', '#FFFFCC'),
        'pink': ('#FF1493', '#FF69B4', '#FFF5EE'),
        'grey': ('#8A8985', '#A9A9A9', '#F2F2F2'),
        'orange': ('#D2691E', '#F4A460', '#FFDEAD'),
        'brown': ('#8B4513', '#CD853F', '#F5DEB3')
        }

    return cols[[i for i in cols][random.randint(0, len(cols)-1)]] if selected == 'any' else cols[selected]

def main():
    """ Main Functions Helps in Printing Sample Return Value """
    print(f'Random Color Set: {colors()}')

if __name__ == "__main__":
    main()
