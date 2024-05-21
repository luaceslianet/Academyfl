
import numpy as np
 
class AddressBook:
    def __init__(self, addresses):
        self.addresses = np.array(addresses)
 
    def get_address_at_index(self, index):
        try:
            return self.addresses[index]
        except IndexError:
            print(f"Index {index} is out of range.")
            return None
 
    def get_addresses_in_range(self, start, end):
        try:
            return self.addresses[start:end+1]  # Include end index in the range
        except IndexError:
            print("Invalid range.")
            return None
 
# Example usage
addresses = [
    "123 Main Street, Anytown, USA",
    "456 Elm Avenue, Springfield, CA",
    "789 Oak Drive, Lakeside, NY",
    "321 Pine Lane, Mountain View, TX",
    "101 Business Park Road, Suite 200, Metropolis, IL"
]
 
address_book = AddressBook(addresses)
 
# Get address at a specific index
index = 2
address = address_book.get_address_at_index(index)
if address is not None:
    print(f"Address at index {index}: {address}")
 
# Get addresses in a range
start_index = 1
end_index = 3
addresses_in_range = address_book.get_addresses_in_range(start_index, end_index)
if addresses_in_range is not None:
    print(f"Addresses in range [{start_index}, {end_index}]:")
    for addr in addresses_in_range:
        print(addr)
 

for idx, x in np.ndenumerate(address_book.addresses):
  print(idx, x)
