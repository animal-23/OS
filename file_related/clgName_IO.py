def file_io(file_name,cont):
    try:
        with open(file_name, 'w') as file:
            file.write(cont)
        with open(file_name, 'r') as file:
            print("Content of the file is:\n",file.read())
    except Exception as e:
        print(f"Error: {e}")

file_name = "sample4.txt"
cont = input("Enter your college name: ")
file_io(file_name,cont)