import re

def Open(file_name, mode):
    try:
        file = open(file_name, mode)

    except:
        print("File", file_name, "wasn't opened!")
        return None

    else:
        print("File", file_name, "was opened!")
        return file


file1_name = "TF2_1.txt"
file2_name = "TF2_2.txt"

file_1_w = Open(file1_name, "w")

if(file_1_w != None):
    file_1_w.write("Це рядок з числом 3.14 і ще одним 42.0\n")
    file_1_w.write("Інший рядок з числами 123.456 і 78\n")
    file_1_w.write("Рядок без чисел\n")
    file_1_w.write("Від'ємне число -9.8 і нуль 0.0 тут\n")
    print("Information was succesfully added to TF2_1.txt!")

    file_1_w.close();
    print("File TF2_1.txt was closed!")

file_2_r = Open(file1_name, "r")
file_2_w = Open(file2_name, "w")

if file_2_r is not None and file_2_w is not None:
    content = file_2_r.read()
    numbers = re.findall(r'-?\d+\.\d+|-?\d+', content)
    file_2_w.write(" ".join(numbers))
    print("Information was succesfully added to TF2_2.txt!")

    file_2_r.close()
    file_2_w.close()
    print("Files TF14_1.txt and TF14_2.txt were closed!")

file_3_r = Open(file2_name, "r")

if file_3_r is not None:
    numbers = [float(num) for num in file_3_r.read().split()]

    if numbers:
        max_value = max(numbers)
        print("New sequence:")

        for num in numbers:
            print(num)

        print(f"Найбільше значення: {max_value}")

    else:
        print("Файл не містить чисел.")

    file_3_r.close()
    print("File TF14_2.txt was closed!")