"""
2014


%book%
%title%abc%title%
%publish%2011%publish%
%author%qwer%author%
%book%

%book%
%title%def%title%
%publish%2012%publish%
%author%asdf%author%
%book%

%book%
%title%ghi%title%
%publish%2014%publish%
%author%zxcv%author%
%book%

%book%
%title%back to 2014%title%
%publish%1999%publish%
%author%poiu%author%
%book%

key = 2014
my_list = [
     ["c", 1999, "z"],
     ["b", 2014, "z"],
     ["back to 2014", 1999, "x"]
]
"""

# import re

# def split_on_empty_lines(s):

#     # greedily match 2 or more new-lines
#     blank_line_regex = r"(?:\r?\n){2,}"
#     return re.split(blank_line_regex, s.strip())

# option 1
import sys


def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text


d = {
    "%book%": "",
    "%title%": "",
    "%publish%": "",
    "%author%": ""
}

my_list = []
s = sys.stdin.read()
s = replace_all(s, d)
s = s.split("\n\n")
for i in s:
    print("i is ", i)
    if i:
        my_list.append(i)

key = my_list[0]
new_list = []
for item in my_list[1:]:
    if item.split("\n") != "":
        new_list.append(item.split("\n"))
print(new_list)
print(key)
for i in new_list:
    if key in i[0] or key in i[1] or key in i[2]:
        print("title: ", str(i[0])+";", "publish: ",
              str(i[1])+";", "author: ", str(i[2])+";")


"""
c z 7
b z 2
c x 1
a z 3
a x 1
b y 5
a x 4
a y 1
b x 3
c y 1
b z 3
b y 2
c x 8
c x 2
b x 1
c y 2
a y 2
a z 7
a x 1
b x 1
c z 1
"""

my_list = []
# read from stdin and save into my_list split by new line
for line in sys.stdin:
    my_list.append(line.split())

res = [i for i in sorted(my_list, key=lambda x:(x[1], x))]

results = {}
for k in res:
    k[2] = int(k[2])
    if (k[0], k[1]) in results:
        results[(k[0], k[1])] += k[2]
    else:
        results[(k[0], k[1])] = k[2]

for k, v in results:
    print(k, v, results[(k, v)])
