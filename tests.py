from functions.get_files_info import get_files_info
from functions .get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def main():
    print("Usage:")
    result = run_python_file("calculator", "main.py") 
    print(result)

    print("3 + 5:")
    print(run_python_file("calculator", "main.py", ["3 + 5"])) 
    
    print("Run tests:")
    print(run_python_file("calculator", "tests.py"))
    
    print("Test ../")
    print(run_python_file("calculator", "../main.py")) 
    
    print("nonexistent.py:")
    print(run_python_file("calculator", "nonexistent.py")) 

if __name__ == "__main__":
    main()
