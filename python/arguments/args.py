import argparse


def launch_instance(region, instanceType):
    print(f"region is: {region}, instance is: {instanceType}")


def main():
    # var = input("please enter: ")
    parser = argparse.ArgumentParser(
        description='Generate a file number')
    parser.add_argument('region', help='region please type')
    parser.add_argument('instanceType', help='instance type')
    parser.add_argument('expiration', nargs='?', default=3600, help='Expiration in seconds')
    args = parser.parse_args()
    # print(type(args))

    launch_instance(args.region, args.instanceType)


if __name__ == '__main__':
    main()
