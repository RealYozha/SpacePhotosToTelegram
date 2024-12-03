def change_splitter(istr: str, curr: str, next: str):
    return next.join(str.split(istr, curr))
