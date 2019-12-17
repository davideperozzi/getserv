import argparse
import sys
import socket

from drivers.base_driver import BaseDriver
from drivers.digital_ocean_driver import DigitalOceanDriver

drivers = [ DigitalOceanDriver ]

def create_parser():
  parser = argparse.ArgumentParser(
    description='Get master node from a cluster'
  )

  parser.add_argument(
    '--test-port',
    default=22,
    type=int,
    help='The port to use for a connection test'
  )

  return parser;

def is_server_reachable(ip: str, port: int = 22):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  try:
    s.connect((ip, port))
    s.shutdown(socket.SHUT_WR)
    return True
  except:
    return False


def main():
  main_parser = argparse.ArgumentParser(
    description='Get master node from a cluster'
  )

  main_parser.add_argument(
    '-p',
    '--test-port',
    default=22,
    type=int,
    help='The port to use for a connection test'
  )

  sub_parsers = main_parser.add_subparsers(help='drivers', dest='driver')
  driver_parsers = {}

  for driver in drivers:
    parser = driver.create_parser(sub_parsers)
    driver_parsers[driver.get_name()] = driver.init_parser(parser)

  main_args = main_parser.parse_args()

  if main_args.driver == None:
    main_parser.print_help()
  else:
    driver_class = None

    for drv in drivers:
      if drv.get_name() == main_args.driver:
        driver_class = drv

    if driver_class == None:
      raise Exception('Driver "' + main_args.driver + '" not found')

    driver = driver_class(driver_parsers[main_args.driver])
    server_ips = driver.run(main_args)

    for ip in server_ips:
      if (is_server_reachable(ip, main_args.test_port)):
        print(ip)
        break

if __name__ == "__main__":
  main()
