from lib.repositories.user_repository import UserRepository
from lib.models.user_authentication import *
from lib.models.user import User
from datetime import datetime


def test_get_all_users(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    repository = UserRepository(db_connection)
    users = repository.all()

   
    assert len(users) == 7

    assert users[0].name == 'Tony Bourne'
    assert users[0].email == 'tonyb@example.com'
    assert users[0].password_hash == 'hash_for_tony'
    assert isinstance(users[0].created_at, datetime)

    assert users[5].name == 'Jazzy Argues'
    assert users[5].email == 'jazzya@example.com'
    assert users[5].password_hash == 'hash_for_jazzy'

def test_find_user_by_id(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    repository = UserRepository(db_connection)
    user = repository.find(2) 
    assert user.name == 'Margot Bourne'
    assert user.email == 'margotb@example.com'

def test_find_by_email(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    repository = UserRepository(db_connection)
    
    user = repository.find_by_email('tonyb@example.com')
    assert user.id == 1
    assert user.name == 'Tony Bourne'

def test_login_success(db_connection):
    repository = UserRepository(db_connection)
    user = repository.find_by_email("tonyb@example.com")
    

    assert user is not None
    assert user.password_hash == "hash_for_tony" 


def test_create_user(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    repository = UserRepository(db_connection)

    new_user = User(None, "Test User", "test@example.com", "test_hash")
    repository.create(new_user)

    all_users = repository.all()
   
    assert len(all_users) == 8
    assert all_users[-1].name == "Test User"

def test_delete_user(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    repository = UserRepository(db_connection)
    repository.delete(1) 

    all_users = repository.all()
    
    assert len(all_users) == 6
    assert all_users[0].name == 'Margot Bourne'

def test_password_validation():
    assert valid_password("Short1!") == False 
    assert valid_password("LongEnoughButNoSpecial") == False
    assert valid_password("ValidPass!") == True

