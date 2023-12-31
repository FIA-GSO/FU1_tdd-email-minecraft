import re   #regular Expressions

def is_valid_email(email:str) -> bool:
    """
    Uses regular expression to validate email.

    Returns:
    True -- email is valid 
    False -- email is not valid
    """
    pattern = r'^[\w!#$%&\'*+\-/=?^_`{|}~]+(\.[\w!#$%&\'*+\-/=?^_`{|}~]+)*@(((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z0-9\-]+\.)+[a-zA-Z]{2,})))$'
    return re.match(pattern, email) is not None


def is_valid_password(password:str) -> bool:

    kleinbuchstabe = r'(?=.*[a-z])'
    grossbuchstabe = r'(?=.*[A-Z])'
    ziffer = r'(?=.*\d)'
    sonderzeichen = r'(?=.*[@#$%^&+=!])'
    keine_leerzeichen = r'[^\s]+'
    regex_muster = ""
    
    if len(password) == 8:
        mindestlaenge = r'(?=.{8})'
        kleinbuchstabe = r'(?=.*[a-zA-Z])'
        regex_muster = f'^{kleinbuchstabe}{ziffer}{sonderzeichen}{mindestlaenge}{keine_leerzeichen}$'
        
    if len(password) > 8 and  len(password) <= 20:
        mindestlaenge = r'(?=.{8,20})'
        regex_muster = f'^{kleinbuchstabe}{grossbuchstabe}{ziffer}{sonderzeichen}{mindestlaenge}{keine_leerzeichen}$'
        
    if len(password) >= 25:
        mindestlaenge = r'(?=.{25,})'
        regex_muster = f'^{kleinbuchstabe}{sonderzeichen}{mindestlaenge}{keine_leerzeichen}$'
        
    """print(regex_muster)"""
    return re.match(regex_muster,password) is not None
    