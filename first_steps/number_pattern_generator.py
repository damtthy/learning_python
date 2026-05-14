def number_pattern(n):

#  --- otra posibilidad :  if not isinstance(n, int): ---
    if type(n) != int:
        return 'Argument must be an integer value.'
    
    if n < 1:
        return 'Argument must be an integer greater than 0.'
    
    numbers = []
#   --- no debe mostrar el cero y debe terminar en el número ingresado ---
    for i in range(1, n + 1):
        numbers.append(str(i))
    
    return " ".join(numbers)