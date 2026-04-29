import re

datum = r"""ygigaiuiuuafui123-214-1124jkbadbviuabweuiebuiubfu124-117-4126asfweiubuewbfuiuaeefb
ygigaiuiuuafui123-212-1241jkbadbviuabw000-0000-000euiebuiubfu124-176-4163asfweiubuewbfuiuaeefb \n\n\d iuuafui
123-214-1246jkbadbviuabw000-000-0100euiebuiubfu124-1576-416asfweiubuewbfuiua
iuuafui123-212-1247jkbadbviuabw000-010-0000euiebuiubfu124-176-4162asfweiubuewbfuiua
iuuafui123-282-1214jkbadbviuabw000-020-0000euiebuiubfu124-196-4116asfweiubuewbfuiua"""


def extract_phone_numbers(text: str) -> list[str]:
    pattern = r"\d{3}-\d{3}-\d{4}"
    return re.findall(pattern, text)


s = "Call me at 123-456-7890 or at 987-654-3210."
print("Found these phone numbers in the given datum: ")
print(*extract_phone_numbers(datum), sep="\n ")
