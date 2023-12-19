def file_seek(file_name,cont):
    try:
        with open(file_name, 'w') as file:
            file.write(cont)
            print("File written")
        with open(file_name, 'r+') as file:
            file.seek(0)
            file.write("Begin")
            file.seek(2)
            file.write("End")
        with open(file_name, 'r') as file:
            print("Content of file after seeking to both ends of files is:\n")
            print(file.read())
    except Exception as e:
        print(f"Error: {e}")

file_name = "sample3.txt"
cont = input("Enter the initial content of file:")
file_seek(file_name,cont)