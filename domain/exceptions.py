class InvalidInputError(Exception):
    """Custom exception for invalid input values."""
    def __init__(self, message: str):
        super().__init__(message)
