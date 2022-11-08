book = "In a village of La Mancha, the name of which I have no desire to call to mind, there lived not long since one of those gentlemen that keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound for coursing."
plain_text = "no is no"


def gen_code_keys(book, plain_text):
    return {c: str(book.find(c)) for c in plain_text}


def encrypt(code_keys, plain_text):
    return "*".join([code_keys[c] for c in plain_text])


def gen_decode_keys(book, cipher_text):
    return {s: book[int(s)] for s in cipher_text.split("*")}


def decrypt(decode_keys, cipher_text):
    return "".join([decode_keys[s] for s in cipher_text.split("*")])


code_keys = gen_code_keys(book, plain_text)
cipher_text = encrypt(code_keys, plain_text)
decode_keys = gen_decode_keys(book, cipher_text)
print(decrypt(decode_keys, cipher_text))

pcup_message = "22*13*33*137*59*11*23*11*1*57*6*13*1*2*6*57*2*6*1*22*13*33*137*59*11*23*11*1*57*6*173*7*11"
decode_keys = gen_decode_keys(book, pcup_message)
print(decrypt(decode_keys, pcup_message))
