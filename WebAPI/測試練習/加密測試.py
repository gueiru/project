from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()
password = 'thissiapasswordgivenbyagoodandverykinduser'
bcrypt.generate_password_hash(password=password)
hashed_password = bcrypt.generate_password_hash(password=password)
print(hashed_password)
check_password = bcrypt.check_password_hash(hashed_password,'thissiapasswordgivenbyagoodandverykinduser')
print(f'check : {check_password}')