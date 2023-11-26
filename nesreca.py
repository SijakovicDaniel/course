# ako zelim iz pisati brojeve od 1 do 20 i da pored svakog neparnog broja
# pise odd, a pored svakog parnog pise even...te da pored broja 4 i 13 pise unlucky

# pr1

# for num in range(1,21):
#     if num == 4 or num == 13:
#         print(f'{num} is unlucky')
#     elif num % 2 == 0:
#         print(f'{num} is even')
#     else:
#         print(f'{num} is odd')

# pri2


for num in range(1,21):
    if num == 4 or num == 13:
        state = 'unlucky'
    elif num % 2 == 0:
        state = 'even'
    else:
        state = 'odd'
    print(f'{num} is {state}')






    
