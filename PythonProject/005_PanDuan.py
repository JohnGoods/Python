#score = 100
score = int(input("输入你的成绩"))
#age = 1  # 用1代表有车票，0代表没有车票
if score>=90 or score<=100:
    print("本次考试，等级为A")
elif score>=80 and score<90:
    print("本次考试，等级为B")
elif score>=70 and score<80:
    print("本次考试，等级为C")
elif score>=60 and score<70:
    print("本次考试，等级为D")
elif score>=0 and score<60:
    print("本次考试，等级为E")