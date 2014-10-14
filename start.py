from optparse import OptionParser
__author__ = 'Constantin Serban'

import re
import urllib
from multiprocessing.dummy import Pool as ThreadPool
from sql_connect import main as gr


def get_links(items):
    links = []
    for item in items:
        matches = 0
        if item is not None:
            matches = re.findall(r"(http(s?):([/|.|\w|\s])*\.(?:jpg|gif|png))", item[0])
            match_no = len(matches)
            if matches:
                while match_no:
                    match_no -= 1
                    link = matches[match_no]
                    links.append(link)
    return links


def parallel_start(links):
    pool = ThreadPool(4)
    results = pool.map(download_files, links)
    pool.close()
    pool.join()


def download_files(link):
    # TODO allow download location selection
    f = open(str("d:\\repos\\fever_saved_download\\down\\" + link[link.rfind('/')+1:]), 'wb')
    f.write(urllib.urlopen(link).read())
    f.close()


def main():
    parser = OptionParser()
    parser.add_option("-s", "--save", action="store_true", dest="keep_saved", default=False,
                      help="Do not mark items as unsaved")
    (options, args) = parser.parse_args()
    keep_saved = options.keep_saved
    items = gr(keep_saved)
    links = get_links(items)
    parallel_start(links)

if __name__ == "__main__":
    main()