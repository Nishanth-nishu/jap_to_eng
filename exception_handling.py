import logging

def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.exception(f"An unexpected error occurred: {e}")
            return None  # Or handle the exception appropriately
    return wrapper
