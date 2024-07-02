import random

rsp = ['가위', '바위', '보']
x, y, z = 0, 0, 0
while True:
    com = random.choice(rsp)
    print('가위바위보 게임을 합시다!')

    while True:
        player = input('가위, 바위, 보! 중에 선택해 주세요! ')
        if player not in rsp:
            continue
        if player == com:
            print('비겼습니다.')
            z += 1
            break

        else:
            if com == '가위':
                if player == '바위':
                    print('플레이어 승리!')
                    x += 1
                else:
                    print('플레이어 패배')
                    y += 1

            elif com == '바위':
                if player == '보':
                    print('플레이어 승리!')
                    x += 1
                else:
                    print('플레이어 패배')
                    y += 1

            elif com == '보':
                if player == '가위':
                    print('플레이어 승리!')
                    x += 1
                else:
                    print('플레이어 패배')
                    y += 1
            break

    game_replay = input('계속 하고싶다면 아무키나 입력해 주세요! 만약 그만하고 싶다면 no를 입력해주세요. ')

    if game_replay.lower() == 'no':
        print('게임을 종료합니다.')
        print(f'매치 결과: 승리{x} 패배{y} 무승부{z}')
        break


    else:
        print(f'지금까지 매치 결과: 승리{x} 패배{y} 무승부{z} 입니다.')
