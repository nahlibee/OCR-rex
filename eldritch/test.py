import re
full_text="BJ475685 gdggs"



x = re.search(r"[A-Z]{2}\d*", full_text)
print(x)