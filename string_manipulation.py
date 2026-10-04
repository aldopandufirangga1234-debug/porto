def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()# : bersihkan spasi + lowercase
    reversed_text = cleaned[::-1]# TODO: balik string-nya
    return cleaned == reversed_text# TODO: bandingkan cleaned dengan reversed_text

print(is_palindrome("Was it a car or a cat I saw"))
