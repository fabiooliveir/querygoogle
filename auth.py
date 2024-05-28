from google_auth_oauthlib.flow import InstalledAppFlow

flow = InstalledAppFlow.from_client_secrets_file(
    'client_secret.json',
    scopes=['https://www.googleapis.com/auth/adwords']
)

flow.run_local_server()

credentials = flow.credentials

print(f"Refresh Token: {credentials.refresh_token}")
