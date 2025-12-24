from functions.get_file_content import get_file_content

def test():

    print("Result for 'main.py' file")
    return_string = get_file_content("calculator", "main.py")
    print(return_string)

    print("Result for 'pkg/calculator.py' file")
    return_string = get_file_content("calculator", "pkg/calculator.py")
    print(return_string)

    print("Result for '/bin/cat' file")
    return_string = get_file_content("calculator", "/bin/cat")
    print(return_string)

    print("Result for 'pkg/does_not_exist.py' file")
    return_string = get_file_content("calculator", "pkg/does_not_exist.py")
    print(return_string)

    print("Result for 'calculator/lorem.txt' file")
    return_string = get_file_content("calculator", "lorem.txt")
    print(return_string)


if __name__ == "__main__":
    test()