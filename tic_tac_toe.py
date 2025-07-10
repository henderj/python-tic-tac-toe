# Python Tic Tac Toe Game

# Initialize the game board
def initialize_board():
    return [' ' for _ in range(9)]

# Display the game board
def display_board(board):
    print('---------')
    for i in range(3):
        print('| ' + ' | '.join(board[i*3:(i+1)*3]) + ' |')
        print('---------')

# Check for a win or a draw
def check_win_draw(board):
    # Define winning combinations
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]
    
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return board[combo[0]] + ' wins'

    if ' ' not in board:
        return 'Draw'

    return None

# Main game loop
def main():
    board = initialize_board()
    current_player = 'X'
    
    while True:
        display_board(board)
        move = int(input(f'Player {current_player}, enter your move (1-9): ')) - 1
        if board[move] == ' ':
            board[move] = current_player
            result = check_win_draw(board)
            if result:
                display_board(board)
                print(result)
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print('Invalid move, try again.')

if __name__ == '__main__':
    main()