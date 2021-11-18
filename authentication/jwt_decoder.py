# JWT Decoder sample script
# https://github.com/brunocamps/python-toolkit



import jwt


# encoded = jwt.encode({"some": "something"}, "4kuizLgSPviOs6UoDEqjfdun2nxgaOiGzo8ut80N3bc", algorithm="HS256")
# print(encoded)

# un = jwt.decode(encoded, "4kuizLgSPviOs6UoDEqjfdun2nxgaOiGzo8ut80N3bc", algorithms=["HS256"])
# print(un)

token = "insert_jwt_token"

header = jwt.get_unverified_header(token)
decoded = jwt.decode(token, options={"verify_signature": False})
print (header)
print(decoded)
#print (decoded['sub'])