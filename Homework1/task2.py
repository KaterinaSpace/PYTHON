# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали n журавликов.

# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# Выведите через пробел количество журавликов, сделанных Петей, Катей и Сережей.

# Пример:


# n = 6 -> 1 4 1  
# n = 24 -> 4 16 4    
# n = 60 -> 10 40 10 

n = int(input())
if (n % 6 == 0):
  print('всего журавликов:', n)
else: 
  print('значение не подходит под параметры задачи, впишите другую цифру')
  
n1 = n//6 
n2 = n1
n3 = (n1+n2)*2
print('n','=',n, '- >', n1, n3, n2 )

