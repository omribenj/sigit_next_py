import functools
def main():
    # ex 1
    # print the longest name from names.txt
    with open("names.txt", "r") as f: 
        print(max([name for name in f.read().split("\n")]))
        

    # ex 2
    # print the sum of all the lengths of all the names from names.txt
    with open("names.txt", "r") as f: 
        print(functools.reduce(lambda x, y: x + len(y),[name for name in f.read().split("\n")], 0))
        
    # ex 3
    # print the shortest names from names.txt
    with open("names.txt", "r") as f:
        sorted_file = sorted([name for name in f.read().split("\n")], key=len)
        print("\n".join([x for x in sorted_file if len(x) == len(sorted_file[0])]))
        
    # ex 4
    # write to name_legth.txt all the lengths of all the names from names.txt
    with open("names.txt", "r") as f1:
         with open("name_length.txt", "w") as f2:
             f2.write("\n".join([str(len(name)) for name in f1.read().split("\n")]))
    
    # ex 5
    # print the all the names from names.txt that are the same length as the length entered by user
    name_length = int(input("Enter name length: "))
    with open("names.txt", "r") as f:
        print("\n".join([name for name in f.read().split("\n") if len(name) == name_length] ))


if __name__ == "__main__":
    main()