This Python-based program stores and retrieves retailer information from a csv file using a hash table and allows fast and efficient lookup of retailer details based on the retailer's name and postcode.

Features:
  -
  - Retailer information is stored in a hash table with composite keys comprising the retailer's name and postcode
  - A custom hash function is used to calculate the hash key for each composite key
  - The function utilises a prime number as a modulus to reduce the likelihood of collisions

Prerequisites:
  -
  - Python 3 is required to run the code
  - The csv file named retailer-info.csv should be present in the same directory as the program

How To Use:
  - Run the code in a Python environment
  - Enter a retailer's name and post code to recieve its corresponding record
