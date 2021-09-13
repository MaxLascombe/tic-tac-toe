board = { 'top left': ' ', 'top middle': ' ', 'top right': ' ', 'left': ' ', 'middle': ' ', 'right': ' ', 'bottom left': ' ', 'bottom middle': ' ', 'bottom right': ' '}

def print_board():
    print()
    print(' ' + board['top left'] + ' | ' + board['top middle'] + ' | ' + board['top right'])
    print('---+---+---')
    print(' ' + board['left'] + ' | ' + board['middle'] + ' | ' + board['right'])
    print('---+---+---')
    print(' ' + board['bottom left'] + ' | ' + board['bottom middle'] + ' | ' + board['bottom right'])
    print()

winning_combinations = [('top left', 'top middle', 'top right'), ('left', 'middle', 'right'), ('bottom left', 'bottom middle', 'bottom right'), ('top left', 'left', 'bottom left'), ('top middle', 'middle', 'bottom middle'), ('top right', 'right', 'bottom right'), ('top left', 'middle', 'bottom right'), ('top right', 'middle', 'bottom left')]
assert len(winning_combinations) == 8

def who_won():
    for a,b,c in winning_combinations:
        if board[a] == board[b] and board[b] == board[c] and board[a] != ' ':
            return board[a]
    return None
    
players = ['X', 'O']
current_player = 0

while ' ' in list(board.values()) and not who_won():
    print_board()
    possible_moves = ''
    for move in board.keys():
        if board[move] == ' ':
            possible_moves += move + ', '
    move = input('Player ' + players[current_player] + ' move (' + possible_moves[:-2] + '): ')
    print(move)
    if not move in board or board[move] != ' ':
        print('Not a valid move.')
        continue
    board[move] = players[current_player]
    current_player = (current_player + 1) % len(players)

print_board()

if not who_won():
    print('It\'s a tie!')
else:
    print('Player ' + who_won() + ' wins!')

