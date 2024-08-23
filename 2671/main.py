import re
print("NOISE" if (m := re.match(r"(100+(1+(?!00))|01)+", s:=input().strip())) is None or m.end()-m.start() != len(s) else "SUBMARINE")