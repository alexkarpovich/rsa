from pkg.lib import gen_rsa, encrypt, decrypt

private, public = gen_rsa(32)
print(private, public)

message = """
The mode indicates how the file is to be opened: 'r' for reading, 'w' for writing (truncating an existing file), 'a' for appending, 'r+' for reading/writing, 'w+' for reading/writing (truncating an existing file), 'a+' for reading/appending. The Python 'b' flag is ignored, since SSH treats all files as binary. The 'U' flag is supported in a compatible way.
"""
cipher = encrypt(message, public)
decrypted_message = decrypt(cipher, private)

print(f'private={private}\npublic={public}\nmessage={message}\ncipher={cipher}\ndecrypted={decrypted_message}')

