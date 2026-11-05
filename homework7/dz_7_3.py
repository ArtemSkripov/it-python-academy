def convert(value, from_unit, to_unit):
    x = 0
    if from_unit == 'cm' and to_unit == 'm':
        x = value / 100
    elif from_unit == 'cm' and to_unit == 'km':
        x = value / 100000 
    elif from_unit == 'm' and to_unit == 'cm':
        x = value * 100          
    elif from_unit == 'm' and to_unit == 'km':
        x = value / 1000         
    elif from_unit == 'km' and to_unit == 'cm':
        x = value * 100000       
    elif from_unit == 'km' and to_unit == 'm':
        x = value * 1000 
    return x
a = convert(5,'cm','m')
print(a)