def change_splitter(before: str, curr_splitter: str, next_splitter: str):
    after = next_splitter.join(str.split(before, curr_splitter))
    return after
