import json

WIDGET = r'E:\deepseek工作窗口\昔涟余额插件\2.0\assets\whale-widget.js'
PREFIX = 'var BUBBLE_DEFAULT_ITEMS = '
# 1.0 的字号 -> 2.0：整体缩小约 1.7 倍（用户反馈「占幅太大，缩小 1.5~2 倍刚好」）
SIZE_MAP = {15: 9, 13: 8, 11: 7, 10: 6}

src = open(WIDGET, encoding='utf-8').read()
start = src.index(PREFIX)
i = start + len(PREFIX)
depth = 0
in_str = False
esc = False
end = None
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
    raise SystemExit('array end not found')

items = json.loads(src[start + len(PREFIX):end])
if len(items) == 1 and isinstance(items[0], list):
    items = items[0]

changed = [0]


def walk(node):
    if isinstance(node, dict):
        if node.get('type') == 'random' and isinstance(node.get('lines'), list):
            for line in node['lines']:
                old = line.get('size')
                if old in SIZE_MAP:
                    line['size'] = SIZE_MAP[old]
                    changed[0] += 1
        for value in node.values():
            walk(value)
    elif isinstance(node, list):
        for value in node:
            walk(value)


walk(items)
out = src[:start] + PREFIX + json.dumps(items, ensure_ascii=False, indent=4) + src[end:]
open(WIDGET, 'w', encoding='utf-8', newline='').write(out)
print('resized lines:', changed[0], '| items:', len(items))
