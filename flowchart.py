max_number = int(0)
    
while True:
    number = int(input("Masukkan bilangan (input 0 untuk berhenti): "))
        
    if number == 0:
        break
        
    if number > max_number:
        max_number = number
    
print("Bilangan terbesar: ", max_number)