from challenges.challenge_encrypt_message import encrypt_message
import pytest

def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message('Harry', '5')
    
    with pytest.raises(TypeError):
        encrypt_message(543, 5)

    assert encrypt_message('Harry', 5) == 'yrr_aH'
    assert encrypt_message('Harry', 0) == 'H_arry'
