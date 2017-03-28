# coding=utf-8

"""
@company:广东浩迪创新科技有限公司
@version: ??
@author: AA-ldc
@file: crawl.py
@time: 2017/3/22 9:45
@function：web爬虫
"""
import urlparse
import os
import urllib
import httplib
from htmllib import HTMLParser
import formatter
import cStringIO


class Retriever(object):
    __slots__ = ('url', 'file')

    def __init__(self, url):
        self.url, self.file = self.get_file(url)

    def get_file(self, url, default='index.html'):
        # 将url拆分成6元组
        parsed = urlparse.urlparse(url)
        host = parsed.netloc.split('@')[-1].split(':')[0]
        filepath = '%s%s' % (host, parsed.path)
        if not os.path.splitext(parsed.path)[1]:
            filepath = os.path.join(filepath, default)
        linkdir = os.path.dirname(filepath)
        print linkdir
        # 是否非文件夹
        if not os.path.isdir(linkdir):
            # Does a path exist?
            if os.path.exists(linkdir):
                # Remove a file(same as remove(path)).
                os.unlink(linkdir)
            os.makedirs(linkdir)
        return url, filepath

    def download(self):
        try:
            # 下载完整的html，另存为文件
            retval = urllib.urlretrieve(self.url, self.file)
        except (IOError, httplib.InvalidURL) as e:
            retval = (('bad url %s : %s' % self.url, e),)

        return retval

    def parse_links(self):
        f = open(self.file,'r')
        data = f.read()
        f.close()
        paeser = HTMLParser(formatter.AbstractFormatter(formatter.DumbWriter(cStringIO.StringIO())))
        paeser.feed(data)
        paeser.close()
        return paeser.anchorlist

class Crawler(object):
    count = 0
    def __init__(self, url):
        self.q = [url]
        self.seen = set()
        parsed = urlparse.urlparse(url)
        host = parsed.netloc.split('@')[-1].split(':')[0]
        self.dom = '.'.join(host.split('.')[-2:])

    def get_page(self, url, media=False):
        r = Retriever(url)
        fname = r.download()[0]
        if fname[0] == '*':
            return
        Crawler.count += 1
        self.seen.add(url)
        ftype = os.path.splitext(fname)[1]
        if ftype not in ('.htm','.html'):
            return
        for link in r.parse_links():
            if link.startswith('mailto:'):
                continue
            if not media:
                ftype = os.path.splitext(link)[1]
                if ftype in ('.mp3','.mp4','.m4v','.wav'):
                    continue
            if not link.startswith('http://'):
                link = urlparse.urljoin(url,link)
            print link
            if link not in self.seen:
                pass

