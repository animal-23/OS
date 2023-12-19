import subprocess

def find_pattern(file_name,pattern):
    try:
        result = subprocess.run(['grep',pattern,file_name], stdout=subprocess.PIPE, text=True)
        print(f"Results of {pattern} in {file_name} file:\n")
        print(result.stdout)
    except Exception as e:
        print(f"Error: {e}")

file_name = "file.txt"
pattern = input("Enter the pattern has to be searched: ")
find_pattern(file_name,pattern)