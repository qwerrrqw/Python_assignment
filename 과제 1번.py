import random

high_try = []
while True:
    com = random.randint(1, 100)
    print('업다운 게임!')
    count = 0
    while True:
        player = input('숫자를 입력해주세요.')
        player_num = int(player)
        if player_num not in range(1, 101):
            print('1~100사이의 숫자를 입력해 주세요. 게임이 다시 시작됩니다.')
            continue

        count += 1

        if player_num > com:
            print(f'down! {player_num}보다 낮은 숫자입니다.')

        elif player_num < com:
            print(f'up! {player_num}보다 높은 숫자입니다.')

        else:
            print(f'정답입니다! {count}번째 시도만에 맞췄습니다.')
            high_try.append(count)
            break

    game_replay = input('계속 하고싶다면 아무키나 입력해 주세요! 만약 그만하고 싶다면 no를 입력해주세요. ')

    if game_replay.lower() == 'no':
        print('게임을 종료합니다.')
        break
    else:
        print(f'최고 시도 횟수는 {max(high_try)}입니다.')

