import hmac
import hashlib

secret_key = b"my-super-secret"
message = b"Transfer $500 to John"

signature = hmac.new(secret_key, message, hashlib.sha256).hexdigest()

print(signature)