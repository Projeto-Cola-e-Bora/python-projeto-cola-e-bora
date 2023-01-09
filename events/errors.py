from django.core.exceptions import ValidationError


class ValidationDateError(ValidationError):
    """An error while validating dates."""
