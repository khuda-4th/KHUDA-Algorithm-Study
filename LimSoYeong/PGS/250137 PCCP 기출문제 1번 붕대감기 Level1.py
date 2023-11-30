def solution(bandage, health, attacks):
    time = 1
    max_health = health
    t, x, y = bandage[0], bandage[1], bandage[2]
    while time <= attacks[-1][0]:
        if health <= 0: # 죽으면
            return -1
        
        if time in [a[0] for a in attacks]: # 공격당하면
            health -= [a[1] for a in attacks if a[0]==time][0]
            t = bandage[0]
            if health <= 0:
                return -1
            
        else: # 힐
            t -= 1
            if t == 0: # t 시간 연속성공하면
                health = min(max_health, health+x+y)
                t = bandage[0] # 다시 t 초기화
            else:
                health = min(max_health, health+x)

        print('time:',time, 'health:', health)
        time += 1
    return health