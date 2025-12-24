from functions.write_file import write_file

def test():

    print("Result for 'lorem.txt' file")
    return_string = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(return_string)

    print("Result for 'pkg/morelorem.txt' file")
    return_string = write_file("calculator", "lorem.txt", "lorem ipsum dolor sit amet")
    print(return_string)

    print("Result for '/tmp/temp.txt' file")
    return_string = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(return_string)


if __name__ == "__main__":
    test()