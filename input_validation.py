import re   #regular Expressions

def is_valid_email(email:str) -> bool:
    """
    Uses regular expression to validate email.

    Returns:
    True -- email is valid 
    False -- email is not valid
    """
    pattern = r'^[\w!#$%&\'*+\-/=?^_`{|}~]+(\.[\w!#$%&\'*+\-/=?^_`{|}~]+)*' \
              r'@(((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|' \
              r'(([a-zA-Z0-9\-]+\.)+[a-zA-Z]{2,})))$'
    return re.match(pattern, email) is not None
