from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView

from apto.settings import env


# https://dj-rest-auth.readthedocs.io/en/latest/installation.html#social-authentication-optional

# Google OAuth2 flow:
# 1. User clicks "Sign in with Google"
# https://accounts.google.com/o/oauth2/v2/auth?
# redirect_uri=<GOOGLE_CALLBACK_URL>&
# prompt=consent&
# response_type=code&
# client_id=<YOUR_CLIENT_ID>&
# scope=openid%20email%20profile&
# access_type=offline
# 2. Google returns code to (callback url) on frontend
# 3. Frontend then sends code to GoogleLogin view on backend
# 4. GoogleLogin view on backend returns jwt tokens to frontend


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = env.str("GOOGLE_CALLBACK_URL")
    client_class = OAuth2Client
