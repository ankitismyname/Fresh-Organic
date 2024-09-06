from django.contrib import admin
from .models import UserProfile,ShoppingCartItem

# Register the UserProfile model with the admin site
admin.site.register(UserProfile)
admin.site.register(ShoppingCartItem)



