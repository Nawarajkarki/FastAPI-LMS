from ..test_main import client, db_session
from fastapi.testclient import TestClient



# Test function to test the create user endpoint POST "/api/users"

def test_create_user(db_session):
    
    test_user_data = {
        "name" : "Pytest_user",
        "email" : "pytest@user.com",
        "membership_date" : "2024-04-06"
    }
    response = client.post('/api/users', json=test_user_data)
    
    assert response.status_code == 200
    
    response_data = response.json()
    
    assert response_data["name"] == "Pytest_user"
    assert response_data["email"] == "pytest@user.com"
    assert response_data["membership_date"] == "2024-04-06T00:00:00"
    
    get_user = client.get('api/users/1')
    print(f"The response is {get_user}")
    response = get_user.json()
    assert get_user.status_code == 200
    assert response['name'] == 'Pytest_user'
    
 


 
# # Test function to test the get user endpoint GET "/api/users/{user_id}"
def test_get_user(db_session):

    # test_user_data = {
    #     "name" : "Pytest_user_second",
    #     "email" : "pytest_user_second@user.com",
    #     "membership_date" : "2024-04-06"
    # }
    # response = client.post('/api/users', json=test_user_data)
    
    # assert response.status_code == 200
    
    
    # get_user = client.get('api/users/1')
    # print(response)
    # assert get_user.status_code == 200
    
    # data = get_user.json()
    
    # assert data['name'] == "Pytest_user_second"    
    test_user_data = {
        "name" : "Pytest_user",
        "email" : "pytest@user.com",
        "membership_date" : "2024-04-06"
    }
    
    response = client.post('/api/users', json=test_user_data)
    
    assert response.status_code == 200
    
    get_user = client.get('/api/users/1')
    
    response = get_user.json()
    assert get_user.status_code == 200
    assert response['id'] == 1
    assert response['name'] == 'Pytest_user'
    
