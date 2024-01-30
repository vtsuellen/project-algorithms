from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message('teste', '5')
    with pytest.raises(TypeError):
        encrypt_message(543, 5)

    assert encrypt_message('teste', 5) == 't_este'
    assert encrypt_message('teste', 0) == 'etse_t'
