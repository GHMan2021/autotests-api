from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
# Вместо CreateUserRequestDict импортируем CreateUserRequestSchema
from clients.users.users_schema import CreateUserRequestSchema

# Инициализируем клиент PublicUsersClient
public_users_client = get_public_users_client()

# Инициализируем запрос на создание пользователя
create_user_request = CreateUserRequestSchema()
create_user_response = public_users_client.create_user(create_user_request)
print('Create user data:', create_user_response)

# Используем атрибуты вместо ключей
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
private_users_client = get_private_users_client(authentication_user)

# Используем атрибуты вместо ключей
get_user_response = private_users_client.get_user(create_user_response.user.id)
print('Get user data:', get_user_response)
