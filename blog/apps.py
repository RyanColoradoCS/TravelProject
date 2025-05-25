from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
    
    # this is so the blog app picks up signala
    def ready(self):
        import blog.signals  # Import signals here
