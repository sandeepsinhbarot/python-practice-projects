
def main():
 print("welcome to email slicer")
 print("")
 
 email_input = input("Input your email slicer ")
 
 (username,domain) = email_input.split("@")
 (domain,extension) = domain.split(".")
 
 print("Username :",username)
 print("Domain :",domain)
 print("Extension:",extension)
 
 while True:
     main()
     