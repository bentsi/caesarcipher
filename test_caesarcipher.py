from caesarcipher.encrypt import encrypt
from caesarcipher.decrypt import decrypt


def test_encrypt():
    result = encrypt(text="abcd", step=1)
    assert result == "bcde"
    result = encrypt(text="xyz", step=1)
    assert result == "yza"
    result = encrypt(text="ben", step=1)
    assert result == "cfo"


def test_decrypt():
    result = decrypt(encrypted_text="bcde", step=1)
    assert result == "abcd"


if __name__ == '__main__':
    test_encrypt()
    # test_decrypt()




