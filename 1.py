with open("game.txt", 'r', 1, "UTF_8") as f:
    r = f.readlines()
    # Импортирование файла
    f1 = open("game_new.csv", 'w', 1, "UTF_8")
    f1.write(r[0])
    for i in range(1, len(r)):
        res = r[i].split('$')
        if res[2].count('55'):
            # Проверка на наличее в названии ошибкии числа 55 и вывод отсчета
            print(f"У персонажа\t{r[0]}\tв игре\t{r[1]}\tнашлась ошибка с кодом:\t{r[2]}\tДата фиксации:\t {r[3]}")
            res[2] = "Done"
            res[3] = "0000-00-00"
            f1.write("&".join(res) + "\n")
        else:
            f1.write(r[i])
    f1.close()
