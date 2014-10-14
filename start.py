__author__ = 'Constantin Serban'

import re
import urllib
from multiprocessing.dummy import Pool as ThreadPool
from sql_connect import main as gr


def get_links(items):
    # TODO if a post has multiple image links get them all.
    links = []
    for item in items:
        if item is not None:
            result = re.search(r"(http(s?):([/|.|\w|\s])*\.(?:jpg|gif|png))", item[0])
            if result:
                links.append(result.group(0))
    return links


def parallel_start(links):
    pool = ThreadPool(4)
    results = pool.map(download_files, links)
    pool.close()
    pool.join()


def download_files(link):
    # TODO allow download location selection
    f = open(str("d:\\repos\\fever_saved_download\\down\\" + link[link.rfind('/')+1:]),'wb')
    f.write(urllib.urlopen(link).read())
    f.close()


def main():
    items = gr()
    links = get_links(items)
    parallel_start(links)

if __name__ == "__main__":
    main()