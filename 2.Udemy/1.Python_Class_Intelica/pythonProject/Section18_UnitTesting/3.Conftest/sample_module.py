def reverse_text(text: str) -> str:
    if isinstance(text, str):
        return text[::-1]
    else:
        raise TypeError


# Too expensive for testing
def get_api_data() -> str:
    return "ORIGINAL DATA"
