import hashlib

message = input("Enter a string : ").encode("utf-8")

message_md5 = hashlib.md5(message).hexdigest()

print("Message encryption using md5 : " + message_md5)

message_sha256 = hashlib.sha256(message).hexdigest()

print("Message encryption using sha256 : " + message_sha256)

message_blake2s = hashlib.blake2s(message).hexdigest()

print("Message encryption using blake2s : " + message_blake2s)
