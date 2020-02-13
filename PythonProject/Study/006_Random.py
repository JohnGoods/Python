import  random
flag = 1
while (flag):
    player = int(input("请输入：剪刀(0)  石头(1)  布(2):"))
    # 产生随机整数：0、1、2 中的某一个
    computer = random.randint(0,2)
    #print('player=%d,computer=%d',(player,computer))
    if player > 2 :
        print("请输入正确数字")
        continue
    if computer> player:
        print('输了，不要走，洗洗手接着来，决战到天亮')
    elif computer == player:
        print('平局，要不再来一局')
    else:
        print('获胜，哈哈，你太厉害了')