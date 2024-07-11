from PIL import Image
import numpy as np
import sys

def encrypt_image(input_image_path, output_image_path, key):
    # Open the input image
    image = Image.open(input_image_path)
    pixels = np.array(image)

    # Apply encryption operation (simple XOR with key)
    encrypted_pixels = pixels ^ key

    # Create a new image from the encrypted pixels
    encrypted_image = Image.fromarray(encrypted_pixels)
    encrypted_image.save(output_image_path)

def decrypt_image(input_image_path, output_image_path, key):
    # Open the input encrypted image
    encrypted_image = Image.open(input_image_path)
    encrypted_pixels = np.array(encrypted_image)

    # Apply decryption operation (simple XOR with key)
    decrypted_pixels = encrypted_pixels ^ key

    # Create a new image from the decrypted pixels
    decrypted_image = Image.fromarray(decrypted_pixels)
    decrypted_image.save(output_image_path)

# Example usage
key = 123  # Encryption key (must be the same for encryption and decryption)
encrypt_image('input.jpg', 'encrypted.png', key)
decrypt_image('encrypted.png', 'decrypted.jpg', key)


def main():
    if len(sys.argv) != 5:
        print("Usage: python image_encryptor.py <encrypt/decrypt> <input_image> <output_image> <key>")
        return

    operation = sys.argv[1]
    input_image = sys.argv[2]
    output_image = sys.argv[3]
    key = int(sys.argv[4])

    if operation == 'encrypt':
        encrypt_image(input_image, output_image, key)
    elif operation == 'decrypt':
        decrypt_image(input_image, output_image, key)
    else:
        print("Invalid operation. Use 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()

