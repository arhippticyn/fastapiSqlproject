import jwt 

headers = {
    'alg': 'HS256',
    'type': "JWT"
}

payload = {
    'username': 'tester_user',
    'email': 'tester@gmail.com',
    'is_active': False
}

secret = 'secret_1234'

token_encode = jwt.encode(headers=headers, payload=payload, key=secret)

try:
    token_decoded = jwt.decode(token_encode, secret, algorithms=['HS256'])
    print(token_decoded)
except jwt.InvalidTokenError:
    print('invalid token')
except jwt.DecodeError:
    print('decode error')
    
    
# def fake_hash_password(password: str):
#     return 'fakehash' + password 

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

# class User(BaseModel):
#     username: str
#     email: str | None = None
#     full_name: str | None = None
#     disabled: bool | None = None
    
# class UserInDB(User):
#     hashed_password: str
    
# def get_user(db, username: str):
#     if username in db:
#         user_dict = db[username]
#         return UserInDB(**user_dict)
    
# def fake_decode_token(token):
#     user = get_user(fake_users_db, token)
#     return user

# async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
#     user = fake_decode_token(token=token)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail='invalid',
#             headers={'www-Authenticate': 'Bearer'}
#         )
#     return user

# async def get_active_current_user(current_user: Annotated[User, Depends(get_current_user)]):
#     if current_user.disabled:
#         raise HTTPException(status_code=400, detail='Inactive user')
#     return current_user

# @app.post('/token')
# async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
#     user_dict = fake_users_db.get(form_data.username)
#     if not user_dict:
#         raise HTTPException(status_code=400, detail='Incorrect username or password')
#     user = UserInDB(**user_dict)
#     hashed_password = fake_hash_password(form_data.password)
#     if not hashed_password == user.hashed_password:
#         raise HTTPException(status_code=400, detail='Incorrect username or password')
    
#     return {'access_token': user.username, 'token_type': 'bearer'}

# @app.get('/users/me', response_model=User)
# async def read_users(current_user: Annotated[User, Depends(get_active_current_user)]):
#     return current_user