userID = "admin"
password = "password"
loginx = True

def usercheck (idGuess, passGuess):
    if idGuess == userID and passGuess == password:
        loginSuccess = "Login Successful."
        loginx = False
    else:
        loginSuccess = "Invalid username or password."
        loginx = True
    return loginSuccess

while loginx == True:
    idGuess = input("Enter the username: ")
    passGuess = input("Enter the password: ")
    print(usercheck(idGuess, passGuess))
    loginx = False
