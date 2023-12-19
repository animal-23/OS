def copy_file(file_name,cont):
    try:
        with open(file_name, 'w') as file:
            file.write(cont)
        print("File written successfully")
    except Exception as e:
        print(f"Error {e}")

file_name = "sample2.txt"
read_file = "sample.txt"
try:
    with open(read_file, 'r') as file:
        cont = file.read()
    print("File read successfully")
    copy_file(file_name,cont)
except Exception as e:
    print(f"Error {e}")