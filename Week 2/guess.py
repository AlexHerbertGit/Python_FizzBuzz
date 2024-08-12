"""
A simple guess the number game
"""

def get_guess():
    """
    Input a prompted guess that is a number
    """
    result = None
    while True:
        try:
            test = input("Guess a number> ")
            result = float(test)
            break
        except:
            print(f'Oops! {test} was not a number')

    return result
    


if __name__ == "__main__":
    print('Your number is {}'.format(get_guess()))
    a = []
    b = (1,'1')
    a = a + [b]
    for i in a :
        print(f'The number is {i[0]}. The phrase is {i[1]}')
    
