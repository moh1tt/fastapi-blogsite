from fastapi import Depends, HTTPException, status

from fastapi.security import OAuth2PasswordBearer
from Blogs import token

oauth2_scheme = oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

async def get_current_user(t: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return token.verfy_token(t, credentials_exception)
    