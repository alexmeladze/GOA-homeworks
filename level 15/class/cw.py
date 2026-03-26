def simple_multiplication(number) :
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9
    



def get_grade(s1, s2, s3):
    result = s1 + s2 + s3
    average = result // 3
    if 90 <= average <= 100:
        return "A"
    elif 80<= average < 90:
        return "B"
    elif 70 <= average < 80:
        return "C"
    elif 60 <= average < 70:
        return "D"
    elif 0 <=average < 60:
        return "F"
    


a = "code"
b = "wa.rs"
name = a + b



def mouth_size(animal): 
    if animal.lower() == "alligator":
        return "small"
    else:
        return "wide"