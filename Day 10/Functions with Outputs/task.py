def format_name(f_name, l_name):
   formated_f_name= f_name.title()
   formated_l_name = l_name.title()
   return f"{formated_f_name} {formated_l_name}"

print(format_name("ecem" , "özen"))

def function_1(text):
    return text + text

def funciton_2(text):
    return text.title()

output = funciton_2(function_1("hello"))
print(output)