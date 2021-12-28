#!/usr/bin/env python
import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Generate an AWS S3 pre-signed URL to access an S3 object without logging in')
    parser.add_argument('file', help='File Name')
    parser.add_argument('number', help='Number')
    parser.add_argument('expiration', nargs='?', default=3600, help='Expiration of URL in seconds')
    args = parser.parse_args()

    print(f"File is : {args.file}")
    print(f"Number is : {args.number}")
    print(f"Expiration is : {args.expiration}")


if __name__ == '__main__':
    main()
