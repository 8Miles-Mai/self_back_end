__author__ = 'miles'
from back_end import mysql_util


def query_store_info(comp_id):
    if comp_id is None or comp_id <= 0:
        comp_id = 0
    data = mysql_util.get_store_info_by_id(comp_id)
    return data