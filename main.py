str1 = input("Введите первую строку: ")
str2 = input("Введите вторую строку: ")

str1 = str1.lower().replace(" ", "")
str2 = str2.lower().replace(" ", "")

if len(str1) != len(str2):
  print("Строки не являются анаграммами.")
else:
  for char in str1:
     if char not in str2:
        print("Строки не являются анаграммами.")
        break
  else:
    print("Строки являются анаграммами.")

