a, b, c = map(int, input("輸入時間：(時：分：秒 )").split())

print("%.0f:%.0f:%.0f = %.1f" % (a, b, c, (a+(b/60)+(c/3600))))
