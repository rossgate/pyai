from functions.get_files_info import get_files_info

def test():

    #current dir
    print("Result for current directory")
    return_string = get_files_info("calculator", ".")
    print(return_string)

    #pkg dir
    print("Result for 'pkg' directory")
    return_string = get_files_info("calculator", "pkg")
    print(return_string)

    #/bin dir
    print("Result for '/bin' directory")
    return_string = get_files_info("calculator", "/bin")
    print(return_string)

    #../ dir
    print("Result for '../' directory")
    return_string = get_files_info("calculator", "../")
    print(return_string)


if __name__ == "__main__":
    test()