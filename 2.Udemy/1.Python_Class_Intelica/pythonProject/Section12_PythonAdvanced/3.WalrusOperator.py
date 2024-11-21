def get_info(text: str) -> dict:
    return {
        "text": text,
        "letters": (length := len(text.replace(" ", ""))),
        "words": (words := text.split()),
        "total_words": (word_length := len(words)),
        "avg_per_word": round(length / word_length, 2),
    }


if __name__ == "__main__":
    # for key, value in get_info('This is some text!').items():
    #    print(key, value, sep=': ')
    while user_input := input("You: "):
        print(">>", user_input)
    else:
        print("We are done here...")
