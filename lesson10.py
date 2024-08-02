#while 1 > 0:
#    num = int(input("Введите число "))
#    if num % 2 == 0:
#        print("чет")
#    else:
#        print("нечет")
#       break
#print("VSE8")
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
while a < len(my_list):
    print(my_list[a])
    a = a + 1
    if my_list[a] == 0:
        a = a + 1
    if my_list[a] < 0:
        break