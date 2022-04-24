import string

alphabet = " " + string.ascii_lowercase
positions = dict([(char, idx) for idx, char in enumerate(alphabet)])

def encoding(input_msg, key):
    """
    Encode a message using Caesar Cipher with any given encryption key.
    """
    keys_list = list(positions.keys())
    result = ""
    for char in input_msg:
        char_idx = keys_list.index(char)
        result += keys_list[(char_idx + key) % 27]
    return result
