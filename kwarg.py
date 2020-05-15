def intro(**data):
    print("\n Тип нашего аргумента: ", type(data))

    for key, value in data.items():
        print("{} is {}".format(key, value))

intro(first_name = "Petr", last_name = "ivanov")
intro(first_name = "Sascha", last_name = "Semenov")