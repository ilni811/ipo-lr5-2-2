str = input("введите строку ") #вводим строку с клавиатуры
count = 0 #объявляем переменную с ихначальным значением 0
for i in str: #цикл от i до str
 if i == "и" or i == "И": #через условный оператор проверяем есть ли букава "и"
  count += 1 #если да, то +1

print(count) #вывод