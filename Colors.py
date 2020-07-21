import random

def Colors(selected = 'any'):
    """
    Function for color-code sets.
    """

    colors = {
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

    if selected == 'any':
        return colors[[i for i in colors.keys()][random.randint(0,len(colors)-1)]]
    else:
        return colors[selected]

def main():
    random_color = Colors()
    print(f'Random Color Set: {random_color}')

if __name__ == "__main__":
    main()

