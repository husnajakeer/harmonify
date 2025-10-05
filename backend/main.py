from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Harmonify backend running"}

@app.get("/login")
def login():
    url = get_auth_url()
    return RedirectResponse(url)

@app.get("/callback")
def callback(code: str):
    tokens = get_tokens(code)
    access_token = tokens.get("access_token")
    refresh_token = tokens.get("refresh_token")
    user_tokens["user"] = {
        "access_token": access_token,
        "refresh_token": refresh_token}
    return {"message": "Authentication successful"}

@app.get("/playlists")
def playlists():
    token_info = user_tokens.get("user")
    if not token_info:
        return {"error": "User not authenticated"}
    access_token = token_info["access_token"]
    return get_user_playlists(access_token)