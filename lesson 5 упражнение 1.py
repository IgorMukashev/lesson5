
input_str = input("Введите следующую строку: " )
with open("File", "w") as file:
    while input_str:
        file.write(input_str+'\n')
        input_str = input("Введите следующую строку: ")