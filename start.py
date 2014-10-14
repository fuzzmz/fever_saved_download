__author__ = 'Constantin Serban'

import optparse
import csv


# TODO download all .jpg images


def get_links(f_obj):
    # TODO read description column
    pass


def main():
    parser = optparse.OptionParser()
    parser.add_option('-f', '--file',
                      dest='csv_file',
                      action='store',
                      help='CSV file')

    (opts, args) = parser.parse_args()
    csv_file = opts.csv_file

    with open(csv_file) as f_obj:
        links = get_links(f_obj)


if __name__ == "__main__":
    main()