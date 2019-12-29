def myfunc():
    word = input("Введите ваше слово: ")
    elem = input("Какую букву вы хотите посчитать: ")
    a = 0
    for i in word:
        if i == elem:
            a += 1
    print("Ваша буква встречается в слове:", a , "раза")
myfunc()