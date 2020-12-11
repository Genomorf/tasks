def find_path(paths: list) -> str:
    dict_path: dict = dict(paths)
    for city in dict_path.values():
        if not dict_path.get(city):
            return city
