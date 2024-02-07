from ..test_main import client, db_session




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
    
 


 
# # Test function to test the get user endpoint GET "/api/users/{user_id}"
def test_get_user(db_session):
    
    
    response = client.get('/api/users/1')
    print(response)
    assert response.status_code == 404
    
#     # test_user_data = {
    #     "name" : "Pytest_user",
    #     "email" : "pytest@user.com",
    #     "membership_date" : "2024-04-06"
    # }
    
    # response = client.post('/api/users', json=test_user_data)
    
    # assert response.status_code == 200
    
    # get_user = client.get('/api/users/1')
    
    # assert get_user.status_code == 200
    # # assert response['id'] == 1
    # assert get_user['name'] == 'pytest_user'
    