#!/usr/bin/env python3

"""一个简单的爬虫示例"""

from io import StringIO
from html.parser import HTMLParser
from bs4 import BeautifulSoup
from formatter import *
import http.client
import os
import sys
import urllib
import urllib.request as request

class MyHTMLParser(HTMLParser):
    """实现 Python3 中没有的 anchorlist 属性"""
    
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.anchorlist = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a' and 'href' in attrs:
            self.anchorlist.append(attrs['href'])

class Retriever:
    """Retriever类获取并解析每个下载到的Web页面"""

    __slots__ = ("url", "file")  # 限制类的属性，降低资源开销

    def __init__(self, url):
        self.url, self.file = self.get_file(url)

    def get_file(self, url, default="index.html"):
        """Create usable local filename from URL"""

        parsed = urllib.parse.urlparse(url)  # 获得一个6元组
        host = parsed.netloc.split('@')[-1].split(':')[0]
        filepath = f"{host}{parsed.path}"
        if not os.path.splitext(parsed.path)[1]:
            # 如果没有文件扩展名后缀，添加index.html
            filepath = os.path.join(filepath, default)
        linkdir = os.path.dirname(filepath)
        if not os.path.isdir(linkdir):  # 如果目录不存在
            if os.path.exists(linkdir):
                os.unlink(linkdir)  # 删除文件路径
            os.makedirs(linkdir)
        return url, filepath

    def download(self):
        """Download URL to specific named file"""

        try:
            retval = request.urlretrieve(self.url, self.file)
        except (IOError, http.client.InvalidURL) as e:
            retval = ((f'*** ERROR: bad URL "{self.url}": {e}'),)
        return retval

    def parse_links(self):
        """Parse out the links found in downloaded HTML file"""

        with open(self.file, 'r') as f:
            data = f.read()

            # StringIO对象吸收标准输出，类似于/dev/null
            # parser = MyHTMLParser(AbstractFormatter(DumbWriter(StringIO)))
            # parser = MyHTMLParser()
            # parser.feed(data)
            # parser.close()
            URLs = []
            for link in BeautifulSoup(data, "html.parser").find_all('a'):
                URLs.append(link.get('href'))

            return URLs

class Crawler:
    """管理整个爬虫进程"""

    count = 0

    def __init__(self, url):
        self.q = [url]
        self.seen = set()
        parsed = urllib.parse.urlparse(url)
        host = parsed.netloc.split('@')[-1].split(':')[0]
        self.dom = '.'.join(host.split('.')[:-2])  # 获取域
    
    def get_page(self, url, media=False):
        """Download page & parse links, add to queue if nec"""

        r = Retriever(url)
        fname = r.download()[0]
        if fname[0] == '*':
            print(fname, "... skipping parse")
            return
        Crawler.count += 1
        print(f"\n({Crawler.count})")
        print(f"URL: {url}")
        print(f"FILE: {fname}")
        self.seen.add(url)
        ftype = os.path.splitext(fname)[1]
        if ftype not in (".html", ".htm", ".php"):
            return

        # 爬取页面下的链接
        for link in r.parse_links():
            if link.startswith("mailto:"):
                print("... discarded, mailto link")
                continue
            if not media:
                ftype = os.path.splitext(link)[1]
                if ftype in (".mp3", ".mp4", ".m4v", ".wav"):
                    print("... discarded, media file")
                    continue
            if not link.startswith("http://"):
                link = urllib.parse.urljoin(url, link)
            print('*', link)
            if link not in self.seen:
                if self.dom not in link:
                    print("... discarded, not in domain")
                else:
                    if link not in self.q:
                        self.q.append(link)
                        print("... new, added to Q")
                    else:
                        print("... discarded, already in Q")
            else:
                print("... discarded, already processed")

    def go(self, media=False):
        """Process next page in queue(if any)"""

        while self.q:
            url = self.q.pop()
            self.get_page(url, media)

def main():
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        try:
            url = input("Enter starting URL: ")
        except (KeyboardInterrupt, EOFError):
            url = ""

    if not url:
        return
    if not url.startswith("http://") and not url.startswith("ftp://"):
        url = f"http://{url}/"

    robot = Crawler(url)
    robot.go()

if __name__ == "__main__":
    main()
