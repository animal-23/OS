def write_file(file_name,cont):
    try:
        with open(file_name, 'w') as file:
            file.write(cont)
        print(f"File '{file_name}' created successfully and written given content into it")
    except Exception as e:
        print(f"Error: {e}")

file_name = "sample.txt"
cont = input("Enter the content of file: ")

write_file(file_name,cont)
