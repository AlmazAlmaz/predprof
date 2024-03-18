p = 666228999
mod = 10**9 + 7
ans = []
with open("game.txt", 'r', 1, "UTF_8") as f:
    r = f.readlines()
    # Импортирование файла
    f1 = open("game_with_hash.csv", 'w', 1, "UTF_8")
    f1.write("hash&" + r[0])
    for i in range(1, len(r)):
        res = r[i].split('$')
        s = res[1] + res[0]
        h = 0
        s = s[::-1]
        # Получение строки
        for j in s:
            h = (h * p + ord('g') + 1) % mod
        # хеш
        f1.write(f"{h}&" + r[i])
    f1.close()
