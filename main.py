def main():
    email = input('Enter your email: ')
    
    # condition1: must start with the alphabet character ( ‘a~z’, ‘A~z’)
    if not email[0].isalpha():
        return False
    
    # condition2: email string length is greater than 5 and less than 30
    if len(email) <= 5 or len(email) >= 30:
        return False
    
    # condition3: It must include the letter '@' and must include at least one '.' after ‘@’
    at_index = email.find('@')
    if at_index == -1:
        return False
    
    dot_index = email.find('.', at_index)
    if dot_index == -1:
        return False
    
    return True

if __name__ == '__main__':
    result = main()
    print(result)
