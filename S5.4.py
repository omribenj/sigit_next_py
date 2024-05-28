class IDIterator:
    """
    Iterator class for iterating on valid id numbers.
    """
    def __init__(self, id=0):
        self._id = id
    
    def __iter__(self):
        return self
    
    def __next__(self):
        """
        the __next__ function for the iterator of valid ids.
        :return: the next valid id
        :rtype: int
        """
        self._id += 1
        if not self._id < 999999999:
            raise StopIteration
        while not check_id_valid(self._id): 
            self._id += 1
            if not self._id < 999999999:
                raise StopIteration
        return self._id

def check_id_valid(id_number):
    """
    function to check if the id is valid
    :param id_number: the id number
    :type id_number: int
    :return: if the id is valid or not
    :rtype: boolean
    """
    # make list of the digits 
    dig_lst = [int(d) for d in [*str(id_number)]]
    # multiply by the factors and reduce non one-digit numbers back to one digit
    for i in range(len(dig_lst)):
        dig_lst[i] = dig_lst[i] * (i % 2 + 1)
        # reduce the 2 dig numbers
        if dig_lst[i] > 9:
            dig_lst[i] = int(str(dig_lst[i])[0]) + int(str(dig_lst[i])[1])
    # check the sum
    if sum(dig_lst) % 10 == 0:
        return True
    return False

def id_generator(start_id):
    """
    generator function for valid ids
    :param start_id: the id from wich the generator starts generating
    :type start_id: int
    :return: the next valid id
    :rtype: int
    """
    while True: 
        start_id += 1
        if start_id == 999999999:
            raise StopIteration
        if check_id_valid(start_id):
            yield start_id

def main():
    # ask user for id
    id = int(input("Enter ID: "))
    # ask user for generator or iterator option
    it_or_gen = input("Generator or Iterator? (gen/it)? ")

    # if user picked generator 
    if it_or_gen == "gen":
        id_gen = id_generator(id)
        for i in range(10):
            print(next(id_gen))
    else:
        # user picked iterator 
        id_iterator = iter(IDIterator(id))
        for i in range(10):
            print(next(id_iterator))
    



if __name__ == "__main__":
    main()
        
    