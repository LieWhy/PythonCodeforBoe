class JustCount:
    __secretCount = 0  # 私有变量
    publicCount = 9  # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)
        # print(self.publicCount)


counter = JustCount()
counter.count()
counter.count()
print(counter.publicCount)
