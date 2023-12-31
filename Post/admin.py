from django.contrib import admin
from .models import Post,PostFragment,PostLike,PostComment

admin.site.register(Post)
admin.site.register(PostFragment)
admin.site.register(PostLike)
admin.site.register(PostComment)


