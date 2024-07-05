def minion_game(string):
    # your code goes here
    vowl = 'AEIOU'
    Stuart = 0
    Kevin = 0
    for i, v in enumerate(string):
        if v.upper() in vowl:
            Kevin = Kevin+len(range(i, len(string)))
        else:
            Stuart = Stuart+len(range(i, len(string)))
    if Stuart > Kevin:
        print(f'Stuart {Stuart}')
    elif Stuart < Kevin:
        print(f'Kevin {Kevin}')
    else:
        print("DRAW")
if __name__ == '__main__':
    s = input()
    minion_game(s)