def copy_file(source_file,destination_file):
    try:
        with open(source_file,'r') as source:
            with open(destination_file,'w') as destination:
                for line in source:
                    destination.write(line)
        print(f"Contents from '{source_file}' successfully copied to '{destination_file}' ")
        
    except FileNotFoundError:
        print("Error:One or both of the files not found.")
    except Exception as e:
        print(f"An error occured:{e}")

if __name__=="__main__":
    source_file="source.txt"
    destination_file="destination.txt"
    copy_file(source_file,destination_file)
