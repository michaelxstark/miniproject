import re
import sys

s = sys.stdin
so = sys.stdout
xs = s.readlines()
xss = ' '
xsss = xss.join(xs)
y = re.findall("\* \[+\w+ \d+\]+\n", xsss)
d = 0
clean = ''
for i in range(len(xs)):
    if '**' not in xs[i] and '&ndash;' not in xs[i]:
        if i == 0:
            d = 0
        else:
            d += 1
    elif "**" in xs[i]:
        x = re.sub("\*{2} ", y[d].strip('\n') + " &ndash; ", xs[i])
        clean += x
    else:
        clean += xs[i]
so.write(clean)
