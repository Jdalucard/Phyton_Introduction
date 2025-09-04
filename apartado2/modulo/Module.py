from modulo_hello import Hello, My_sum
import sys


Hello("daniel jose")

My_sum(5, 10, 15)

print(My_sum(5, 10, 15))  # Output: 30

sys.path.append("c:/Users/homew/desktop/migithub/Python/apartado2/ImportarModule")
import other_funtions

print(sys.path)

print(other_funtions.Sum(1, 2, 3, 55, 5))
