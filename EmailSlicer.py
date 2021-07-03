email = input("Enter your Email address: ").strip()
userName = email[ : email.index("@")]
domainName = email[email.index("@") + 1 : ]
print(f"Username: '{userName}' and domain name: '{domainName}'")