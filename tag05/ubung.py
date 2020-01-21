#Teile die 10 durch alle Zahlen: range()



# for i in range(-10,10):
#     try:
#         i=(10//i)
#         print(i)
#     except:
#         print("Teilung durch 0")
#kann der code falsch ausgeführt werden, was kann ich abfangen

def i_number(n):
    try:
        float(n)
        return True
    except:
        return False

while True:
    e=input("Zahl")
    if i_number(e):
        break
    else:
        print("wrong")
