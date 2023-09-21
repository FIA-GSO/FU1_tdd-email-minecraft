import pytest
from input_validation import is_valid_email,is_valid_password

@pytest.mark.parametrize("email", [
    ("test@email.com")
,   ("t.est@email.com")
,   ("test@em.ail.com")
,   ("test@email.co.uk")
,   ("te-st@email.com")
,   ("te_st@email.com")
,   ("test1@email.com")
])
def test_is_valid_email__gueltige_Adressen(email):
    # arrange
    email_adress_to_be_tested = email
    
    # act
    response = is_valid_email(email)
    
    # assert
    assert response is True


@pytest.mark.parametrize("email", [
    ("testemail.com")   # Fehlendes @-Zeichen
,   ("test@email.")      # Fehlende Top-Level-Domain
,   ("test@em@ail.com") # Mehrfaches @-Zeichen
,   ("++test@em@ail.com") # Mehrfaches +-Zeichen
,   ("ätöüest@gmail.com") # ÄÜÖ 
,   ("iopjroiiowcioweoiwednoqoiodoiqwdoiwendoweniwniowendiweoidijsdjascoiwcnweoilajsdjknoicniowesadniowenwe@gmail.com")
,    
])
def test_is_valid_email__ungueltige_Adressen(email):
    # arrange
    email_adress_to_be_tested = email
    
    # act
    response = is_valid_email(email)
    
    # assert
    assert response is False

@pytest.mark.parametrize("passwords", [
   ("test1234"),   # Password 8 Zeichen lang
   ("teSt!234"),      # Passwort mit 8 Zeichen, Sonderzeichen und Großbuchstaben
   ("nigeroOderS0binKEINj4p4n3r!!!"), # Hakans Passwort 
   ("ABCdfg!23")
])

def test_is_valid_password(passwords):
    response = is_valid_password(passwords)
    assert response is True

@pytest.mark.parametrize("password", [
   (r"!$%&/()"), # Passwort nur mit Sonderzeichen
   ("12345678"), # Passwort nur mit Zahlen
   ("asdjncrj"), # Passwort nur mit Buchstaben
   ("ASDFghbj"), # Passwort mit Groß und Klein buchstaben
   ("")
])

def test_is_valid_password_is_not_valid(password):
    responses = is_valid_password(password)
    assert responses is False