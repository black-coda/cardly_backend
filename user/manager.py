from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Custom manager for the custom user model.
    """

    def create_user(self, email, password = None, **extra_fields):
        """
        Create and return a regular user with an email and password.
        """
        # Validate the email field
        if not email:
            raise ValueError("Email is required")

        # Normalize email and create a new user instance
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields,
        )

        # Set the user's password
        user.set_password(password)

        # Save the user to the database
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password = None, **extra_fields):
        """
        Create and return a superuser with an email, password, and superuser attributes.
        """
        # Validate the email field
        if not email:
            raise ValueError("Email is required")

        # Create a new superuser instance with normalized email
        superuser = self.model(
            email=self.normalize_email(email),
            **extra_fields,
        )

        # Set the user's password
        superuser.set_password(password)

        # Set superuser attributes
        superuser.is_staff = True
        superuser.is_superuser = True
       

        # Save the superuser to the database
        superuser.save(using=self._db)
        return superuser
