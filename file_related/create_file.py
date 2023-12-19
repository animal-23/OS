def create_file(file_name):
    try:
        with open(file_name, 'w'):
            pass
        print(f"File '{file_name}' created successfully.")
    except Exception as e:
        print(f"Error: {e}")

file_name = "sample.txt"

create_file(file_name)
