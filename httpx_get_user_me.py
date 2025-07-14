import httpx  # Импортируем библиотеку HTTPX

# Данные для входа в систему
login_payload = {
    "email": "user@example.com",
    "password": "123456"
}

# Выполняем запрос на аутентификацию
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

# Сохраняем accessToken
accessToken = login_response_data["token"]["accessToken"]

# Выполняем GET запрос
headers = {"Authorization": f"Bearer {accessToken}"}
me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
me_response_data = me_response.json()

# Выводим полученныё ответ и статус код
print("Me response:", me_response_data)
print("Status Code:", me_response.status_code)
