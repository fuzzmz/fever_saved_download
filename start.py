__author__ = 'Constantin Serban'

import optparse
import csv
import re
import urllib
from multiprocessing.dummy import Pool as ThreadPool


def get_items(f_obj):
    items = []
    with open(f_obj, 'rU') as file:
        reader = csv.DictReader(file, dialect=csv.excel_tab)
        for line in reader:
            items.append(line['description'])
    return items


def get_links(items):
    # TODO if a post has multiple image links get them all.
    links = []
    for item in items:
        if item is not None and isinstance(item, (str, unicode)):
            result = re.search(r"(http(s?):([/|.|\w|\s])*\.(?:jpg|gif|png))", item)
            if result:
                links.append(result.group(0))
    return links


def parallel_start(links):
    # TODO download all images
    # Make the Pool of workers and set the pool size to 4
    pool = ThreadPool(4)
    # Open the urls in their own threads and return the results
    results = pool.map(download_files, links)
    # Close the pool and wait for the work to finish
    pool.close()
    pool.join()


def download_files(link):
    f = open(str(link[link.rfind('/')+1:]),'wb')
    f.write(urllib.urlopen(link).read())
    f.close()


def main():
    parser = optparse.OptionParser()
    parser.add_option('-f', '--file',
                      dest='csv_file',
                      action='store',
                      help='CSV file')

    (opts, args) = parser.parse_args()
    csv_file = opts.csv_file

    items = get_items(csv_file)
    links = get_links(items)
    parallel_start(links)

if __name__ == "__main__":
    main()