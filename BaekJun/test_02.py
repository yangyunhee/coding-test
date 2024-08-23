'''
2869번 달팽이는 올라가고 싶다 

땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.
달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.
달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어진다. (1 ≤ B < A ≤ V ≤ 1,000,000,000)

출력
첫째 줄에 달팽이가 나무 막대를 모두 올라가는데 며칠이 걸리는지 출력한다.
'''


# 하루에 올라가는 높이 = A - B


# 2 1 5:
# 첫날 : 0에서 2 만큼 가서 -1 => 1
# 둘째 : 1에서 2 만큼 가서 3 -> -1 => 2
# 셋째:  2에서 2만큼 올라가서 4 -> -1 => 3
# 넷째:  3에서 2만큼 올라가서 5

# up, down, target_h = map(int,input().split())

def day_routine(up, down, target_h):
    day_cnt = 0
    total_move = 0

    while True:
        day_cnt += 1
        total_move += up
        if total_move >= target_h:
            break
        total_move -= down
        
    return day_cnt


result = day_routine(100, 99, 1000000000)
print(result)
