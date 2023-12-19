import shutil

def copy_file(src, dest):
    try:
        shutil.copy(src, dest)
        print(f"File '{src}' copied to '{dest}'")
    except Exception as e:
        print(f"Error: {e}")

src= 'file.txt'  
dest = '/home/prakash/Documents/OS/process_related/'
copy_file(src, dest)
