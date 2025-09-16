from functions.get_files_info import get_files_info
from functions .get_file_content import get_file_content
from functions.write_file import write_file

def main():
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print("lorem test:")
    print(result)

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print("pkg test:")
    print(result)

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print("temp test:")
    print(result)

if __name__ == "__main__":
    main()
