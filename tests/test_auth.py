from src.storage.json_storage import JsonStorage
from src.interfaces.welcome import welcome_and_role_determination

# Note: First, manually create sample JSON files as per previous step

def test_auth():
    storage = JsonStorage()
    
    # Simulate input (use monkeypatch in real pytest, but for simple test:)
    # Assuming manual input during run
    user = welcome_and_role_determination(storage)
    assert user is not None, "Login failed"
    print("Login test passed!")

if __name__ == "__main__":
    test_auth()