import json
import re
import sys

WIDGET = r'E:\deepseek工作窗口\昔涟余额插件\assets\whale-widget.js'
LINES_FILE = r'E:\昔涟.txt'

# ---- collect the dialogue lines from the user's text file -------------------
lines = []
with open(LINES_FILE, encoding='utf-8') as f:
    for raw in f:
        text = raw.strip()
        if text and text not in lines:
            lines.append(text)
print('lines:', len(lines))


def size_for(text):
    n = len(text)
    if n <= 10:
        return 15
    if n <= 18:
        return 13
    if n <= 26:
        return 11
    return 10


entries = [{"t": t, "w": 5, "bold": True, "size": size_for(t)} for t in lines]

src = open(WIDGET, encoding='utf-8').read()
start_marker = 'var BUBBLE_DEFAULT_ITEMS = ['
start = src.index(start_marker)
i = start + len(start_marker) - 1
depth = 0
end = None
in_str = False
esc = False
while i < len(src):
    ch = src[i]
    if in_str:
        if esc:
            esc = False
        elif ch == '\\':
            esc = True
        elif ch == '"':
            in_str = False
    else:
        if ch == '"':
            in_str = True
        elif ch == '[':
            depth += 1
        elif ch == ']':
            depth -= 1
            if depth == 0:
                end = i + 1
                break
    i += 1
if end is None:
    sys.exit('could not find array end')

block = src[start:end]
json_text = block[len(start_marker) - 1:]
items = json.loads(json_text)
print('items:', len(items))

replaced = [0]


def walk(node):
    if isinstance(node, dict):
        if node.get('type') == 'random' and isinstance(node.get('lines'), list):
            node['lines'] = [dict(e) for e in entries]
            replaced[0] += 1
        for value in node.values():
            walk(value)
    elif isinstance(node, list):
        for value in node:
            walk(value)


walk(items)
print('random modules replaced:', replaced[0])

new_block = start_marker + '\n' + json.dumps(items, ensure_ascii=False, indent=4) + ']'
out = src[:start] + new_block + src[end:]
open(WIDGET, 'w', encoding='utf-8', newline='').write(out)
print('written, bytes:', len(out.encode('utf-8')))
