from functions.get_files_info import get_files_info
from functions .get_file_content import get_file_content


def main():
    result = get_file_content("calculator", "main.py")
    print("Result from current directory:")
    print(result)
    print("")

    result = get_file_content("calculator", "pkg/calculator.py")
    print("Result from pkg:")
    print(result)

    result = get_file_content("calculator", "/bin/cat")
    print("Result from bin")
    print(result)

    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print("Result from invalid pkg")
    print(result)
if __name__ == "__main__":
    main()
