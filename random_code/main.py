# a = []
# for i in input(): a.append(int(i))
# print(a)
#
# result = []
# remove = ['[', ']', ',', ' ']
# for i in input():
#     if i not in remove:
#         result.append(int(i))
# print(result)
#
# st = input()
# st = st.replace("[","").replace("]", "")
# print(st.split(', '))
#
# arr = []
# num = 0
# for i in range(len(result)):
#     num += result[i]
#     arr.append(num)
# print(arr)
#
# list_1 = input().split(' ')
# ls = []
# for i in list_1:
#     ls.append(int(i))
# list_2 = []
# for i in ls:
#     if i > 0:
#         list_2.append(i)
# print(min(list_2))

#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

# list_1 = map(int, input().split(' '))
# list_2 = []
# for i in list_1:
#     if i > 0:
#         list_2.append(i)
# print(min(list_2))


# бинарный поиск
def lbs(a, x):
    l = -1
    r = len(a) - 1
    while l + 1 != r:
        c = (l + r) // 2
        if a[c] < x:
            l = c
        else:
            r = c
    return r

def rbs(a, x):
    l = 0
    r = len(a)
    while l + 1 != r:
        c = (l + r) // 2
        if a[c] > x:
            r = c
        else:
            l = c
    return l
a = [1, 2, 20, 20, 20, 30]
x = 20
print(lbs(a, x))
print(rbs(a, x))

def binary_search(list, item):
  # в low и high хранятся границы части списка, где выполняется поиск
  low = 0
  high = len(list) - 1
  # Пока не останется один элемент
  while low <= high:
    # Проверяем средний элемент
    mid = (low + high) // 2
    guess = list[mid]
    # Значение найдено
    if guess == item:
      return mid
    # Значение велико
    elif guess > item:
      high = mid - 1
    # Значение мало
    else:
      low = mid + 1

  # Значение не найдено
  return None

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3)) # => 1 (позиция элемента в списке)

# 'None' в Python означает "ничто". Элемент не найден.
print(binary_search(my_list, -1)) # => None

# Сортировка массива
def BubbleSort(a):
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a
a = [1, 3, 2, 44, 23, 0, 5, 11]
print(BubbleSort(a))

# Сумма 2х самых больших чисел в масиве
a = [1, 3, 2, 44, 23, 0, 5, 11]
msum = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] + a[j] > msum:
            msum  = a[i] + a[j]
print(msum)

# 2й вариант
a = [1, 3, 2, 44, 23, 0, 5, 11]
m, sm = 0, 0
for x in a:
    if x > m:
        sm = m
        m = x
    elif x > sm:
        sm = x
print(m + sm)
