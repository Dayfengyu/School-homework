import math

a, b = map(float, input("請輸入直角三角形邊長:").split())
c = ((a*a)+(b*b))

print("斜邊長為%g公尺" % math.sqrt(c))
