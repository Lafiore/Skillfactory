def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:

        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

array = list(map(int, input("Введите любые целые числа через пробел").split()))
element = int(input("Введите число из списка"))

for i in range(len(array)):
    for j in range(len(array) - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print(array)
left = int(array[0])
right = int(array[-1])
if left > element < right:
    print("Число вне диапазона")
else:
    print(binary_search(array, element, 0, len(array) -1))