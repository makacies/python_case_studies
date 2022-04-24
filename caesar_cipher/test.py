import cipher as cph

message = "hi my name is caesar"

encoded_message = cph.encoding(message, 3)
print(encoded_message)

decoded_message = cph.encoding(encoded_message, -3)
print(decoded_message)
