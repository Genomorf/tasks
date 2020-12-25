def isAnagram(str1: str, str2: str) -> bool:
    str1_list: list = list(str1)
    str1_list.sort()
    str2_list: list = list(str2)
    str2_list.sort()
    return str1_list == str2_list
