import glob

if __name__ == "__main__":
    # ? - matches a single character
    print(glob.glob("?ndex.js"))

    # * - matches everything
    print(glob.glob("*.py"))

    # [] - matches any character in the sequence
    print(glob.glob("[il]*.js)"))

    # [!] - matches any character not in the sequence
    print(glob.glob("![il]*.js)"))

    print(
        glob.glob(
            "**/*.js",
            root_dir="E:/Codeando/repository_coding",
            recursive=True,
            include_hidden=True,
        )
    )

    globs = glob.iglob(
        "**/*.js",
        root_dir="E:/Codeando/repository_coding",
        recursive=True,
        include_hidden=True,
    )

    for i, file in enumerate(globs):
        print(i, file, sep=":")
