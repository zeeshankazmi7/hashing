dataFile = "retailer-info.csv"
hashTable = {}


def hashFunction(key):
    P = 16908799
    hashVal = 0
    key_str = ''.join(str(element) for element in key)
    for char in key_str:
        hashVal = (127 * hashVal + ord(char)) % P
    return hashVal    


with open(dataFile, "r") as file:
    for line in file:
        fields = line.strip().split(',')
        address = (fields[4], fields[5], fields[6], fields[8])

        key = fields[1]
        value = (fields[3], address, fields[15])
        composite_key = (fields[1], fields[8])
        hashKey = hashFunction(composite_key)

        hashTable[composite_key] = value

retailerInput = input("Enter retailer's name: ")
postcodeInput = input("Enter retailer's post code: ")

user_key = (retailerInput, postcodeInput)

if user_key in hashTable:
    record = hashTable[user_key]
    
    print(f"Record for {user_key}: {record[0]}, {record[1]}, {repr(record[2])}")
else:
    print(f"No record found for {user_key}")
