#!/usr/bin/env python3

from fcntl import lockf, LOCK_EX

print("Content-type: image/svg+xml\n")

DATA_FILENAME = "../data/counter.dat"

with open(DATA_FILENAME, "r+") as f:
    lockf(f, LOCK_EX)
    conts = f.read()
    try:
        count = int(conts)
    except:
        count = 0
    count += 1
    count %= 10000000000
    f.truncate()
    f.seek(0)
    f.write(str(count))

print('<?xml version="1.0" standalone="no"?>')
print('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">')
print('<svg width="372" height="68" viewBox="0 0 1860 340" xmlns="http://www.w3.org/2000/svg" version="1.1">')

print('<rect x="0" y="0" width="1860" height="340" fill="#333333" stroke="none" />')

pattern = [
    "1110111",
    "0010010",
    "1011101",
    "1011011",
    "0111010",
    "1101011",
    "1101111",
    "1010010",
    "1111111",
    "1111011",
]

color = {
    "0": "#3d3d3d",
    "1": "#ffffcc",
}

n = "%010d" % count

for i in range(10):
    print(f'<g transform="translate({i * 180 + 60},50)" fill="red" stroke="none">')
    sx, sy, w, h, d, t = 0, 0, 120, 120, 15, 5
    pat = pattern[int(n[i])]
    print(f'<polyline fill="{color[pat[0]]}" points="{sx+t},{sy} {sx+t+d},{sy-d} {sx+w-t-d},{sy-d} {sx+w-t},{sy} {sx+w-t-d},{sy+d} {sx+t+d},{sy+d}" />')
    print(f'<polyline fill="{color[pat[1]]}" points="{sx},{sy+t} {sx-d},{sy+t+d} {sx-d},{sy+h-t-d} {sx},{sy+h-t} {sx+d},{sy+h-t-d} {sx+d},{sy+t+d}" />')
    print(f'<polyline fill="{color[pat[2]]}" points="{sx+w},{sy+t} {sx-d+w},{sy+t+d} {sx-d+w},{sy+h-t-d} {sx+w},{sy+h-t} {sx+d+w},{sy+h-t-d} {sx+d+w},{sy+t+d}" />')
    print(f'<polyline fill="{color[pat[3]]}" points="{sx+t},{sy+h} {sx+t+d},{sy-d+h} {sx+w-t-d},{sy-d+h} {sx+w-t},{sy+h} {sx+w-t-d},{sy+d+h} {sx+t+d},{sy+d+h}" />')
    print(f'<polyline fill="{color[pat[4]]}" points="{sx},{sy+t+h} {sx-d},{sy+t+d+h} {sx-d},{sy+h-t-d+h} {sx},{sy+h-t+h} {sx+d},{sy+h-t-d+h} {sx+d},{sy+t+d+h}" />')
    print(f'<polyline fill="{color[pat[5]]}" points="{sx+w},{sy+t+h} {sx-d+w},{sy+t+d+h} {sx-d+w},{sy+h-t-d+h} {sx+w},{sy+h-t+h} {sx+d+w},{sy+h-t-d+h} {sx+d+w},{sy+t+d+h}" />')
    print(f'<polyline fill="{color[pat[6]]}" points="{sx+t},{sy+h*2} {sx+t+d},{sy-d+h*2} {sx+w-t-d},{sy-d+h*2} {sx+w-t},{sy+h*2} {sx+w-t-d},{sy+d+h*2} {sx+t+d},{sy+d+h*2}" />')
    print('</g>')

print('</svg>')

