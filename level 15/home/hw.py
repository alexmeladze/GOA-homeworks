a = "code"
b = "wa.rs"
name = a + b



def is_even(n): 
    if n % 2 == 0:
        return True
    else:
        return False
    



def main(verb,noun):
    return verb + noun




def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    elif number % 2 != 0:
        return "Odd"
    



    def number_to_string(num):
        return str(num)
    


    def boolean_to_string(b):
        return str(b)
    


    def say_hello(name):
        return f"Hello, {name}"
    

def quarter_of(month):
    if 1 <= month <= 3:
        return 1
    elif 3 < month <= 6:
        return 2
    elif 6 < month <= 9:
        return 3
    elif 9 < month <= 12:
        return 4