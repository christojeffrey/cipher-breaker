import math
import random

def affine_cipher(hex_values, m, b, n):
    cipher_hex = []
    for i in range(len(hex_values)):
        C = hex((m * int(hex_values[i], 16) + b) % n)
        cipher_hex.append(C)
    return cipher_hex


def read_image_to_hex(image_path):
    try:
        with open(image_path, "rb") as image:
            f = image.read()
            b = bytearray(f)
            array_of_hex = [hex(byte) for byte in b]
            return array_of_hex
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except ValueError as e:
        print("Error:", e)
        return None


def array_of_hex_to_bytearray(array_of_hex):
    bytearray_data = bytearray()
    for hex_value in array_of_hex:
        if hex_value.startswith('0x'):
            hex_value = hex_value[2:]
        byte_value = int(hex_value, 16)
        bytearray_data.append(byte_value)
    return bytearray_data
def create_file_from_bytes(file_path, bytes_data):
    try:
        with open(file_path, "wb") as file:
            file.write(bytes_data)
        print("File berhasil dibuat:", file_path)
    except Exception as e:
        print("Error:", e)

def decyrpt_affine_cipher(hex_values, inv_m, b, n):
    decrypted_hex = []
    for i in range(len(hex_values)):
        C = hex((inv_m * (int(hex_values[i], 16) - b)) % n)
        decrypted_hex.append(C)
    return decrypted_hex

def main():
    image_path = "./chall.jpg"
    n = 256
    b = 201
    inv_m = 137 # https://www.omnicalculator.com/math/inverse-modulo m = 185
    
    hex_values = read_image_to_hex(image_path)
    if hex_values is not None:
        plain_hex = decyrpt_affine_cipher(hex_values, inv_m, b, n)
        bytearray_cipher = array_of_hex_to_bytearray(plain_hex)
        
        create_file_from_bytes("./result.jpg", bytearray_cipher)

if __name__ == "__main__":
    main()