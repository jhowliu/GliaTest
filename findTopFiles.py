import re

urls = [
    "http://www.google.com/a.txt",
    "http://www.google.com.tw/a.txt",
    "http://www.google.com/download/c.jpg",
    "http://www.google.co.jp/a.txt",
    "http://www.google.com/b.txt",
    "https://facebook.com/movie/b.txt",
    "http://yahoo.com/123/000/c.jpg",
    "http://gliacloud.com/haha.png",
]

counter = {}

def findTop3(data):
    filename = re.compile(r'(\w+.\w+)$')

    for url in urls:
        m = filename.search(url)
        if m:
            _file = m.group(len(m.groups())-1)
            if _file in counter:
                counter[_file] += 1
            else:
                counter[_file] = 1

    result = sorted(counter.items(), key=lambda k: k[1], reverse=True)[:3]

    # print results
    for k, v in result:
        print(k, v)

if __name__ == '__main__':
    findTop3(urls)

