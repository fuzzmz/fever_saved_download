__author__ = 'Constantin Serban'

import optparse
import csv
import re


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


def download_files(links):
    # TODO download all images
    pass


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
    download_files(links)

if __name__ == "__main__":
    main()