import re
inputStr="hello python,ni hao c,zai jian python"
replaceStr=re.sub(r"hello (\w+),ni hao (\w+),zai jian \1","\g<1>",inputStr)
print(replaceStr)
