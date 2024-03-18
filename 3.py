ans = []
with open("game.txt", 'r', 1, "UTF_8") as f:
    r = f.readlines()
    # Импортирование файла
    for i in range(1, len(r)):
        res = r[i].split('$')
        # Добавление элементов
        ans.append([res[1], res[0]])
# сортировка
ans = sorted(ans)
a = input()
while a != "game":
    l = 0
    r = len(ans)
    # бин поиск
    while l + 1 < r:
        mid = (l + r) >> 1
        if ans[mid][0] < a:
            l = mid
        else:
            r = mid
    # вывод
    if r == len(ans) or ans[r][0] != a:
        print("Этого персонажа не существует")
    else:
        cnt = 0
        while r < len(ans) and cnt < 5 and ans[r][0] == a:
            print(ans[r][1])
            r += 1
            cnt += 1
    a = input()
