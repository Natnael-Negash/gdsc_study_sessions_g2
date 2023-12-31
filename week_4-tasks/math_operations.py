def basic_operations(a, b):
    try:
        return{
    'addition': a + b,
    'subtruction': a - b,
    'multiplication': a * b,
    'division': a / b
  }
    except ZeroDivisionError:
        print("error: division by zero is not allowed.")



def power_operation(base, exponent, **kwargs):
    try:
       result_power = base ** exponent
       modulo_value = kwargs.get('modulo')
       if modulo_value is not None:
            result_power %= modulo_value
    except Exception as error:
        result_power = {'error': str(error)}
        return result_power

def apply_operations(operation_list):
    return list(map(lambda x:x[0](*x[1]), operation_list))