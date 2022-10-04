### Recibe un Array de Integers por parámetro. Devuelve el número menor posible NO presente en dicho array y que sea POSITIVO.

def solution(integer_array):
    buffer = 0
    solution = 1

    integer_array.sort()

    for number in integer_array:
        if number > 0:
            if number-buffer > 1:
                solution = number - (number-buffer)+1
                return solution
            buffer = number
    
    if number > 0:
        return number+1
    else: 
        return 1


## TESTS ##


integer_array = [-5,-4,0,1,2,4,5]

print(solution(integer_array))