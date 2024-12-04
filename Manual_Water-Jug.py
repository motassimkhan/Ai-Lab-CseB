import math

a = int(input("Enter capacity of jug A: "))
b = int(input("Enter capacity of jug B: "))
ai = int(input("Enter Initial state jug A: "))
bi = int(input("Enter Initial state jug B: "))
af = int(input("Enter Final state of jug A: "))
bf = int(input("Enter Final State of jug B: "))

if a <= 0 or b <= 0:
    print("Jug capacities must be positive.")
    exit(1)
if ai < 0 or bi < 0 or af < 0 or bf < 0:
    print("Negative values are not allowed.")
    exit(1)

def wjug(a,b,ai,bi,af,bf):
    print('''
    Options:
    1. Fill Jug A Completely
    2. Fill Jug B Completely
    3. Empty Jug A Completely
    4. Empty Jug B Completely
    5. Pour From Jug A till Jug B is full or A becomes empty
    6. Pour From Jug B till Jug A is full or B becomes empty 
    7. Pour all from Jug A to Jug B
    8. Pour all from Jug B to Jug A
    ''')
    
    while ai != af or bi != bf:
        ch = int(input("Enter your choice: "))
        
        if ch == 1:
            ai = a
        elif ch == 2:
            bi = b
        elif ch == 3:
            ai = 0
        elif ch == 4:
            bi = 0
        elif ch == 5:
            pour_amt = min(ai, b-bi)
            ai -= pour_amt
            bi += pour_amt
        elif ch == 6:
            pour = min(bi, a-ai)
            bi -= pour
            ai += pour
        elif ch == 7:
            pour_amt = min(ai, b-bi)
            ai -= pour_amt
            bi += pour_amt
        elif ch == 8:
            pour = min(bi, a-ai)
            bi -= pour
            ai += pour
        else:
            print("Invalid operation. Please choose a number between 1 and 8.")
            continue
        
        print(f"Jug A: {ai}, Jug B: {bi}")

        if ai == af and bi == bf:
            print("Final State Reached: Jug A =", ai, ", Jug B =", bi)
            return
        
gcd = math.gcd(a, b)

if (af <= a and bf <= b) and (af % gcd == bf % gcd == 0):
    wjug(a, b, ai, bi, af, bf)
else:
    print("The final state is not achievable with the given capacities.")
    exit(1)