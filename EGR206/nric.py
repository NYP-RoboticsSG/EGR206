nric_number = []
nric_weight = [2,7,6,5,4,3,2]
count =0
const_check_digit ={
    1 : 'A',
    2 : 'B',
    3 : 'C',
    4 : 'D',
    5 : 'E',
    6 : 'F',
    7 : 'G',
    8 : 'H',
    9 : 'I',
    10: 'Z',
    11: 'J'
}


nric = input("Please entered the NRIC number:").upper().split('S')
#print(nric)
while len(nric) > 9:
    nric = input("Please entered the NRIC number:")
#print(nric[1])
#print(nric_weight[count])
for nric_ch in nric[1]:
    if nric_ch.isdigit():
        nric_mul = int(nric_ch) * nric_weight[count]
        nric_number.append(nric_mul)
    else:
        nric_text=nric_ch.upper()
    # print(nric_weight[count])
    count = count + 1

sum_nric_number = sum(nric_number)
#print(nric_number,nric_mul)
remain = sum_nric_number % 11
check_digit = 11-remain
check_alpha= const_check_digit.get(check_digit)
if check_alpha == nric_text:
    print("Your IC is valid.")
else:
    print("You IC is invalid and is illegal !")
#print(nric_number)
#print(check_alpha,nric_text)
