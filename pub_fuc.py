# _*_coding:utf-8_*_

import re

def re_fuc(cont,rel_list,id_data):
    """
    :param cont:
    :param rel:
    :param list:
    :param id_data:
    :return:
    """
    for rel in rel_list:
        try:
            c = re.compile(rel)
            ret = re.findall(c,cont)
            if ret:
                return ret
            else:
                break
        except:
            pass
    return None
