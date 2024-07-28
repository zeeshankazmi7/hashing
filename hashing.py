dataFile = "retailer-info.csv"  # path to the csv file containing retailer information
hashTable = {}  # dictionary to store retailer information with composite key

def hashFunction(key):
    # prime number used as a modulus for hash calculation
    P = 16908799
    # initial hash value
    hashVal = 0
    # convert the key into a string
    key_str = ''.join(str(element) for element in key)
    # iterate through each character in the key string
    for char in key_str:
        # calculate the hash value using the character's ASCII value and a base of 127
        hashVal = (127 * hashVal + ord(char)) % P
    # return the final hash value
    return hashVal    

# open the csv file and read line by line
with open(dataFile, "r") as file:
    for line in file:
        # split each line into fields using comma as delimiter
        fields = line.strip().split(',')
        # extract address components from specific fields
        address = (fields[4], fields[5], fields[6], fields[8])

        # extract retailer's name as key
        key = fields[1]
        # extract retailer's info including type address and code
        value = (fields[3], address, fields[15])
        # create a composite key using retailer's name and postcode
        composite_key = (fields[1], fields[8])
        # calculate the hash key for the composite key
        hashKey = hashFunction(composite_key)

        # store the value in the hashTable using the composite key
        hashTable[composite_key] = value

# prompt user for retailer's name and postcode
retailerInput = input("Enter retailer's name: ")
postcodeInput = input("Enter retailer's post code: ")

# create a user key from the input
user_key = (retailerInput, postcodeInput)

# check if the user key exists in the hashTable
if user_key in hashTable:
    # if found retrieve the corresponding record
    record = hashTable[user_key]
    # display the record details
    print(f"Record for {user_key}: {record[0]}, {record[1]}, {repr(record[2])}")
else:
    # if not found display a no record found message
    print(f"No record found for {user_key}")
