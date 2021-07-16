import re

p = re.compile("b.{1}b.{1}b")
print(re.findall(p, "abbbcbbbc"))
