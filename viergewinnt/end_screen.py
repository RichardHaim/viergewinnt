import main


def winner(player):
    """
    add docstring

    Parameters
    ----------
    player

    Returns
    -------

    """
    print(f'''
******************************************
CONGRATULATIONS!! PLAYER {player} has won!
******************************************

If you want to play another round press 'y'

''')
    dec = input()
    if dec == "y":
        print(f'''
        Starting up another round
        ''')
        main.startup()
    else:
        return print(f'Thank you for playing, have a good day')




def loser():
    """
    add docstring

    Returns
    -------

    """
    print(f'''
    ******************************************
    I am sorry, the AI won :/
    ******************************************

    If you want to play another round press 'y'

    ''')
    dec = input()
    if dec == "y":
        print(f'''
            Starting up another round
            ''')
        main.startup()
    else:
        return print(f'Thank you for playing, have a good day')



def draw():
    """
    add docstring

    Returns
    -------

    """
    print(f'''
    ******************************************
    Oh no, there is no winner
    ******************************************

    If you want to play another round press 'y'

    ''')
    dec = input()
    if dec == "y":
        print(f'''
            Starting up another round
            ''')
        main.startup()
    else:
        return print(f'Thank you for playing, have a good day')