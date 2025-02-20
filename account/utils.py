from rest_framework_simplejwt.tokens import RefreshToken

class CustomRefreshToken(RefreshToken):
    """Custom refresh token class to include additional user details in the token."""

    def for_user(self, user):
        """
        Override the for_user method to include additional fields in the payload.
        """
        refresh = self.__class__()
        refresh.payload.update({
            'user_id': user.id,
            'name': user.name,
            'email': user.email,
            'phone_number': user.phone_number,
            'role': getattr(user, 'role', None),  # Include role if exists in user model
        })
        return refresh
