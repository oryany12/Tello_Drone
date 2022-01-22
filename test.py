import time
import winwifi

# winwifi.WinWiFi.connect("Diralhaskir_Rooms")
# s = "awdasdasd"
# print(list(s))


def int5(N):
    flag = 0
    if N < 0:
        N = str(-N)[::-1]
        flag = 1
    temp = str(N)
    index = -1

    for i, val in enumerate(temp):
        if int(val) < 5:
            index = i
            break
    if index == -1:
        ans = int(temp + '5')
    else:
        ans = int(temp[:index] + '5' + temp[index:])
    if flag == 1:
        return int(str(ans)[::-1])*-1
    return ans