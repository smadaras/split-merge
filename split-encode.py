import sys
import base64

def split_file(input_file, chunk_size):
    with open(input_file, 'rb') as file:
        index = 0
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            text_data = base64.b64encode(chunk).decode('utf-8')
            chunk_file = f'{input_file}_{index}.txt'
            with open(chunk_file, 'w') as f:
                f.write(text_data)
            index += 1


if __name__ == "__main__":
    # the output is less than 1,048,575
    chunk_size = 786000

    if len(sys.argv) < 2:
        print(f"Use: python split-encode.py input.bin [chunk size]")
        exit(-1)
    input_file = sys.argv[1]
    if len(sys.argv) > 2:
        chunk_size = int(sys.argv[2])          
# Split the long binary file into smaller pieces
    split_file(input_file, chunk_size)