import sys
import base64

def merge_files(output_file):
    with open(output_file, 'wb') as out_file:
        index = 0
        while True:
            file_name = f'{output_file}_{index}.txt'
            print(file_name)
            try:
                with open(file_name, 'r') as in_file:
                    text_data = in_file.read()
                    binary_data = base64.b64decode(text_data.encode('utf-8'))
                    out_file.write(binary_data)
            except:
                print(index)
                break
            index += 1
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Use: python decode-merge.py outputfile")
        exit(-1)
    else:
        output_file = sys.argv[1]
         
# Merge the smaller pieces back into the original file
    merge_files(output_file)
