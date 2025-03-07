# CryptoMagic 🔐

Hey there! This is my cool encryption tool that I made to help you send secret messages. It's super easy to use and looks pretty nice too!

## What this thing does

- You can **encrypt** any text so nobody can read it without your secret password
- You can **decrypt** messages if you have the right password
- It has a nice colorful design so it's not boring to look at
- It's secure - I'm using real encryption, not just some random character swapping

## How to set it up

1. **Clone this repo**
   ```
   git clone https://github.com/yourusername/crypto-magic.git
   cd crypto-magic
   ```

2. **Set up a virtual environment**
   ```
   python -m venv venv
   
   # If you're on Windows (like me)
   venv\Scripts\activate
   
   # If you're on Mac/Linux
   source venv/bin/activate
   ```

3. **Install the stuff it needs**
   ```
   pip install flask==2.0.1 cryptography==3.4.8 werkzeug==2.0.2
   ```

4. **Run it!**
   ```
   python app.py
   ```

5. **Check it out in your browser**
   ```
   http://127.0.0.1:5000/
   ```

## How to use it

### To encrypt something:
1. Type your message in the box
2. Make up a secret password (don't forget it!)
3. Hit the "Encrypt Message" button
4. Copy the weird-looking text that shows up

### To decrypt something:
1. Paste the encrypted message
2. Type in the same password you used before
3. Hit the "Decrypt Message" button
4. Read your secret message!

## Project structure

```
crypto-magic/
├── app.py                 # The main Python file
├── static/
│   └── styles.css         # Makes everything look nice
├── templates/
│   └── index.html         # The webpage you see
├── requirements.txt       # List of Python packages needed
└── README.md              # This file you're reading now
```

## Technical notes

- Uses Fernet encryption from the cryptography library
- Built with Flask because it's simple and works well
- All the encryption happens on your computer - nothing gets saved anywhere

## Common issues

- If you see an error about "url_quote", make sure you're using the right version of werkzeug
- If the page doesn't load, check that all your files are in the right folders
- If encryption fails, make sure you're not using weird characters in your password

---

made by : Sangam