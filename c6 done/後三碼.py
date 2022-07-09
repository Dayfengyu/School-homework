a = input("請輸入統一發票號碼：")
a = str(a)
ans = [num for num in a]
print("最後三碼為%c%c%c" % (ans[-3], ans[-2], ans[-1]))
print("%c+%c+%c=%d" % (ans[-3], ans[-2], ans[-1],
                       (int(ans[-3]))+(int(ans[-2]))+(int(ans[-1]))))
