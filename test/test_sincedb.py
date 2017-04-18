from core import sincedb
import logging

logging.basicConfig(level=logging.DEBUG)


def test_get_files():
    sincedb.get_files('.')


def test_parse_sincedb():
    sincedb.parse_sincedb('./test_dir/sincedb')


def test_merge_path_stats():
    sincedb.merge_path_stats(sincedb.parse_sincedb('./test_dir/sincedb'), sincedb.get_files('.'))

def test_merge_path_stats_with_ignore():
    sincedb.merge_path_stats(sincedb.parse_sincedb('./test_dir/sincedb'), sincedb.get_files('.'), ignore_missing='y')


test_get_files()
test_parse_sincedb()
test_merge_path_stats()
test_merge_path_stats_with_ignore()
