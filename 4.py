ans = {}
with open("game.txt", 'r', 1, "UTF_8") as f:
    r = f.readlines()
    # Импортирование файла
    for i in range(1, len(r)):
        res = r[i].split('$')
        # Добавление элементов
        if ans.get(res[0]) is None:
            ans[res[0]] = 1
        else:
            ans[res[0]] += 1
res = []
for i in ans:
    res.append([ans[i], i])
res = sorted(res)
with open("game.txt", 'r', 1, "UTF_8") as f:
    f1 = open("game_counter.csv", 'w', 1, "UTF_8")
    f1.write(r[0][:-1] + "&count\n")
    # Запись в файл
    for i in range(1, len(r)):
        res = r[i].split('$')
        if i != len(r) - 1:
            f1.write(r[i][:-1] + f"&{ans[res[0]]}\n")
        else:
            f1.write(r[i] + f"&{ans[res[0]]}")
    f1.close()