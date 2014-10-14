__author__ = 'Constantin Serban'

import re
import urllib
from multiprocessing.dummy import Pool as ThreadPool
from sql_connect import main as gr
from optparse import OptionParser
import os


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


def parallel_start(download_map):
    pool = ThreadPool(4)
    results = pool.map(download_files, download_map)
    pool.close()
    pool.join()


def download_files(download_map):
    location = download_map[1]
    link = download_map[0][0]
    f = open((location + "\\" + link[link.rfind('/') + 1:]), 'wb')
    try:
    f.write(urllib.urlopen(link).read())
    f.close()
    except IOError:
        print "Couldn't download image from " + link + "\n"
        return


def main():
    parser = OptionParser()
    parser.add_option("-s", "--save", action="store_true", dest="keep_saved", default=False,
                      help="Do not mark items as unsaved")
    parser.add_option("-d", "--download", action="store", dest="download_location", default=False,
                      help="Download location")
    (options, args) = parser.parse_args()
    keep_saved = options.keep_saved
    download_location = options.download_location
    if not download_location:
        download_location = os.path.dirname(os.path.abspath(__file__)) + "\\down"
    if not os.path.exists(download_location):
        os.makedirs(download_location)
    items = gr(keep_saved)
    links = get_links(items)
    download_map = []
    for a in links:
        download_map.append((a, download_location))
    parallel_start(download_map)

if __name__ == "__main__":
    main()