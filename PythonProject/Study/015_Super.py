class Master(object):
    def __init__(self):
        self.kongfu = "古法煎饼果子配方"  # 实例变量，属性

    def make_cake(self):  # 实例方法，方法
        print("[古法] 按照 <%s> 制作了一份煎饼果子..." % self.kongfu)


# 父类是 Master类
class School(Master):
    def __init__(self):
        self.kongfu = "现代煎饼果子配方"

    def make_cake(self):
        print("[现代] 按照 <%s> 制作了一份煎饼果子..." % self.kongfu)
        super().__init__()  # 执行父类的构造方法
        super().make_cake()  # 执行父类的实例方法


# 父类是 School 和 Master
class Prentice(School, Master):  # 多继承，继承了多个父类
    def __init__(self):
        self.kongfu = "猫氏煎饼果子配方"

    def make_cake(self):
        self.__init__()  # 执行本类的__init__方法，做属性初始化 self.kongfu = "猫氏...."
        print("[猫氏] 按照 <%s> 制作了一份煎饼果子..." % self.kongfu)

    def make_all_cake(self):
        # 方法3. super()的简化版，只支持新式类
        super().__init__()  # 执行父类的 __init__方法
        super().make_cake()  # 执行父类的 实例方法
        self.make_cake()  # 执行本类的实例方法


damao = Prentice()
damao.make_cake()
damao.make_all_cake()

# print(Prentice.__mro__)