__author__ = 'Constantin Serban'

import optparse
import csv
import re

# TODO download all .jpg images


def get_items(f_obj):
    items = []
    with open(f_obj, 'rU') as file:
        reader = csv.DictReader(file, dialect=csv.excel_tab)
        for line in reader:
            items.append(line['description'])
    return items


def get_links(items):
    links = []
    for item in items:
        if item is not None and isinstance(item, (str, unicode)):
            # TODO get only image links from the post contents
            links.append(re.search(r"(http(s?):([/|.|\w|\s])*\.(?:jpg|gif|png))", item).group(0))
    return links


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


if __name__ == "__main__":
    main()