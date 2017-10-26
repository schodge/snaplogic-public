#!/usr/bin/python3
"""
lib_fake_data.py
Copyright 2017 Snaplogic

Helper library for fake_data.py
"""

import argparse


def setup_parser():
    '''Set up argparse.'''
    parser = argparse.ArgumentParser(
        description='Fake Data Generator',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '-b', '--batch',
        action='store',
        type=int,
        default=50000,
        help=('Batch size (number of rows to compute at once. The higher you'
              ' can make this the better performance will be, but at the'
              ' expense of requiring more memory). If mod this != 0, will'
              ' round up to the next multiple of this.'))
    parser.add_argument(
        '-c', '--config_file',
        action='store',
        help=('Path to config file. Arguments set in this file will override '
              'arguments set on the command line unless --use_cmd_args is set,'
              ' with the exception of --verbose, --output, and --use_cmd_args, '
              'which always override what is in the file.'))
    parser.add_argument(
        '-f', '--faker',
        action='store',
        type=int,
        default=10000,
        help=('Number of entries in the data generated by the faker library.'
              'This tends to be slow to compute.'))
    parser.add_argument(
        '-n', '--numeric',
        action='store',
        type=int,
        default=100000,
        help=('Number of entries in the numeric data generated. This is fast'
              'to create.'))
    parser.add_argument(
        '-o', '--output',
        action='store',
        default='fake_data',
        help=('Output file path including base name (no extension), '
              'e.g., "/usr/me/testa" will create files in /usr/me/ of the '
              'form testa*.csv . Leaving off the path will treat the '
              'argument as a basename for use in the current directory.'))
    parser.add_argument(
        '-r', '--rows',
        action='store',
        type=int,
        default=250000,
        help='Total number of rows to generate.')
    parser.add_argument(
        '-s', '--seed',
        action='store',
        type=int,
        default=4242,
        help='Seed for RNGs.')
    parser.add_argument(
        '-u', '--users',
        action='store',
        type=int,
        default=1000,
        help='Number of distinct users and distinct products.')
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Turn on some debug messaging to stdout.')
    parser.add_argument(
        '--use_cmd_args',
        action='store_true',
        help=('Uses command line arguments instead of arguments in the config'
              ' file. This includes unspecified args that this help identifies'
              ' as having default values. Otherwise, the arguments specified'
              ' in the config file control.'))
    return parser


def fake_logging(verbose, message):
    if verbose:
        print(message)
