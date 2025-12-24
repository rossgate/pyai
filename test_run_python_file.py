from functions.run_python_file import run_python_file

def test():

    return_string = run_python_file("calculator", "main.py")
    print(return_string)

    return_string = run_python_file("calculator", "main.py", ["3 + 5"])
    print(return_string)

    return_string = run_python_file("calculator", "tests.py")
    print(return_string)

    return_string = run_python_file("calculator", "../main.py") 
    print(return_string)

    return_string = run_python_file("calculator", "nonexistent.py")
    print(return_string)

    return_string = run_python_file("calculator", "lorem.txt")
    print(return_string)


if __name__ == "__main__":
    test()