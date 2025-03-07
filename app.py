from flask import Flask, render_template, request, redirect, url_for
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

def generate_key(password):
    """Generate a key from a password."""
    password = password.encode()
    salt = b'crypto_magic_salt'  # Fixed salt for simplicity
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key

def encrypt_message(message, password):
    """Encrypt a message using a password."""
    try:
        key = generate_key(password)
        fernet = Fernet(key)
        encrypted_message = fernet.encrypt(message.encode())
        return base64.urlsafe_b64encode(encrypted_message).decode()
    except Exception as e:
        return f"Error: {str(e)}"

def decrypt_message(encrypted_message, password):
    """Decrypt a message using a password."""
    try:
        key = generate_key(password)
        fernet = Fernet(key)
        encrypted_message = base64.urlsafe_b64decode(encrypted_message.encode())
        decrypted_message = fernet.decrypt(encrypted_message).decode()
        return decrypted_message
    except Exception as e:
        return f"Error: Could not decrypt. Please check your key and try again."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    text = request.form.get('text', '')
    key = request.form.get('key', '')
    
    if not text or not key:
        return render_template('index.html', error="Please provide both text and key")
    
    encrypted_text = encrypt_message(text, key)
    return render_template('index.html', encrypted_text=encrypted_text)

@app.route('/decrypt', methods=['POST'])
def decrypt():
    text = request.form.get('text', '')
    key = request.form.get('key', '')
    
    if not text or not key:
        return render_template('index.html', error="Please provide both text and key")
    
    decrypted_text = decrypt_message(text, key)
    return render_template('index.html', decrypted_text=decrypted_text)

if __name__ == '__main__':
    app.run(debug=True)