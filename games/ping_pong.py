import os
import time
import keyboard

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_board(ball_pos, left_paddle_pos, right_paddle_pos):
    clear_screen()
    board = [[' '] * 40 for _ in range(20)]

    ball_x, ball_y = ball_pos
    board[ball_y][ball_x] = 'O'

    left_paddle_x, left_paddle_y = left_paddle_pos
    for i in range(4):
        board[left_paddle_y + i][left_paddle_x] = '|'

    right_paddle_x, right_paddle_y = right_paddle_pos
    for i in range(4):
        board[right_paddle_y + i][right_paddle_x] = '|'

    for row in board:
        print(''.join(row))

def main():
    ball_pos = [20, 10]
    ball_dir = [1, 1]

    left_paddle_pos = [0, 8]
    right_paddle_pos = [39, 8]

    while True:
        draw_board(ball_pos, left_paddle_pos, right_paddle_pos)

        if keyboard.is_pressed('w') and left_paddle_pos[1] > 0:
            left_paddle_pos[1] -= 1
        if keyboard.is_pressed('s') and left_paddle_pos[1] < 16:
            left_paddle_pos[1] += 1

        ball_pos[0] += ball_dir[0]
        ball_pos[1] += ball_dir[1]

        if ball_pos[1] <= 0 or ball_pos[1] >= 19:
            ball_dir[1] = -ball_dir[1]
        
        if ball_pos[0] == 1 and left_paddle_pos[1] <= ball_pos[1] <= left_paddle_pos[1] + 3:
            ball_dir[0] = -ball_dir[0]

        if ball_pos[0] == 38 and right_paddle_pos[1] <= ball_pos[1] <= right_paddle_pos[1] + 3:
            ball_dir[0] = -ball_dir[0]

        time.sleep(0.1)

if __name__ == "__main__":
        main()
        
        