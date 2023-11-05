import zlib
import base64

with open("Files/test.txt", "r", encoding="utf-8") as file:
    text = file.read()


print("Original Text:")
print(text)


try:
    with open("Files/comp.txt", "r") as fc:
        existing_data = fc.read()
    if existing_data:
        # If there is text in "comp.txt", don't overwrite it
        print("File 'comp.txt' already contains data. Skipping compression and writing.")
    else:
        # Compress the text and encode it in base64
        compressed_data = zlib.compress(text.encode("utf-8"), 9)  # Use compression level 9 for better compression
        base64_encoded_data = base64.b64encode(compressed_data).decode("utf-8")

        print("Compressed and Base64 Encoded Data:")
        print(base64_encoded_data)

        # Write the compressed and encoded data to the file
        with open("Files/comp.txt", "w") as fc:
            fc.write(base64_encoded_data)

        with open("Files/comp.txt", "r") as fc:
            data=fc.read()
            compressed_data = base64.b64decode(data)

            # Then, decompress using zlib
            decompressed_text = zlib.decompress(compressed_data).decode("utf-8")

            # Now, `decompressed_text` contains the original text that was compressed and encoded
            print(decompressed_text)
        

except FileNotFoundError:
    compressed_data = zlib.compress(text.encode("utf-8"), 9) 
    base64_encoded_data = base64.b64encode(compressed_data).decode("utf-8")

    print("Compressed and Base64 Encoded Data:")
    print(base64_encoded_data)

  
    with open("Files/comp.txt", "w") as fc:
        fc.write(base64_encoded_data)
        
    with open("Files/comp.txt", "r") as fc:
        data=fc.read()
        compressed_data = base64.b64decode(data)

        # Then, decompress using zlib
        decompressed_text = zlib.decompress(compressed_data).decode("utf-8")

        # Now, `decompressed_text` contains the original text that was compressed and encoded
        print(decompressed_text)
        

