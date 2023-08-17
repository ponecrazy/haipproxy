"""
Spider rules.Scheduler will provide crawling tasks according to the rules and
spiders will parse response content according to the rules.
"""
from ..config.settings import (
    SPIDER_COMMON_TASK, SPIDER_AJAX_TASK,
    SPIDER_GFW_TASK, SPIDER_AJAX_GFW_TASK,
    INIT_HTTP_QUEUE, VALIDATED_HTTP_QUEUE,
    VALIDATED_HTTPS_QUEUE, TEMP_HTTP_QUEUE,
    TEMP_HTTPS_QUEUE, TTL_HTTP_QUEUE,
    TTL_HTTPS_QUEUE, SPEED_HTTPS_QUEUE,
    SPEED_HTTP_QUEUE, TEMP_WEIBO_QUEUE,
    VALIDATED_WEIBO_QUEUE, TTL_WEIBO_QUEUE,
    SPEED_WEIBO_QUEUE, TEMP_ZHIHU_QUEUE,
    VALIDATED_ZHIHU_QUEUE, TTL_ZHIHU_QUEUE,
    SPEED_ZHIHU_QUEUE, TEMP_TGSTAT_QUEUE,
    VALIDATED_TGSTAT_QUEUE, TTL_TGSTAT_QUEUE,
    SPEED_TGSTAT_QUEUE)


__all__ = ['CRAWLER_TASKS', 'VALIDATOR_TASKS', 'CRAWLER_TASK_MAPS',
           'TEMP_TASK_MAPS', 'SCORE_MAPS', 'TTL_MAPS',
           'SPEED_MAPS']


CRAWLER_TASKS = [
    {
        'name': 'my-proxy.com',
        'resource': [
            'https://www.my-proxy.com/free-elite-proxy.html',
            'https://www.my-proxy.com/free-anonymous-proxy.html',
            'https://www.my-proxy.com/free-socks-4-proxy.html',
            'https://www.my-proxy.com/free-socks-5-proxy.html'
        ],
        'task_queue': SPIDER_COMMON_TASK,
        # if the parse method is specified, set it in the Spider's parser_maps
        'parse_type': 'myproxy',
        'interval': 60,
        'enable': 1,
    },

    {
        'name': 'us-proxy.org',
        'resource': ['https://www.us-proxy.org/'],
        'task_queue': SPIDER_COMMON_TASK,
        'parse_type': 'common',
        'parse_rule': {
            'pre_extract_method': 'xpath',
            'pre_extract': '//tbody//tr',
            'infos_pos': 0,
            'infos_end': None,
            'detail_rule': 'td::text',
            'ip_pos': 0,
            'port_pos': 1,
            'extract_protocol': True,
            'split_detail': False,
            'protocols': None
        },
        'interval': 60,
        'enable': 1,
    },
    {
        'name': 'socks-proxy.net',
        'resource': [
            'https://www.socks-proxy.net/',
        ],
        'task_queue': SPIDER_COMMON_TASK,
        'parse_type': 'common',
        'parse_rule': {
            'pre_extract_method': 'xpath',
            'pre_extract': '//tbody//tr',
            'infos_pos': 0,
            'infos_end': None,
            'detail_rule': 'td::text',
            'ip_pos': 0,
            'port_pos': 1,
            'extract_protocol': True,
            'split_detail': False,
            'protocols': None
        },
        'interval': 60,
        'enable': 1,
    },
    {
        'name': 'sslproxies.org/',
        'resource': ['https://www.sslproxies.org/'],
        'task_queue': SPIDER_COMMON_TASK,
        'parse_type': 'common',
        'parse_rule': {
            'pre_extract_method': 'xpath',
            'pre_extract': '//tbody//tr',
            'infos_pos': 0,
            'infos_end': None,
            'detail_rule': 'td::text',
            'ip_pos': 0,
            'port_pos': 1,
            'extract_protocol': True,
            'split_detail': False,
            'protocols': None
        },
        'interval': 60,
        'enable': 1,
    },
    {
        'name': 'atomintersoft.com',
        'resource': [
            'http://www.atomintersoft.com/high_anonymity_elite_proxy_list',
            'http://www.atomintersoft.com/anonymous_proxy_list',
        ],
        'task_queue': SPIDER_COMMON_TASK,
        'parse_type': 'common',
        'parse_rule': {
            'pre_extract_method': 'xpath',
            'pre_extract': '//tr',
            'infos_pos': 1,
            'infos_end': None,
            'detail_rule': 'td::text',
            'ip_pos': 0,
            'port_pos': 1,
            'extract_protocol': True,
            'split_detail': True,
            'protocols': None
        },
        'interval': 60,
        'enable': 1,
    },
    {
        'name': 'proxydb.net',
        'resource': ['http://proxydb.net/?offset=%s' % (15 * i) for i in range(20)],
        'task_queue': SPIDER_AJAX_TASK,
        'parse_type': 'common',
        'parse_rule': {
            'detail_rule': 'a::text',
            'split_detail': True,
        },
        'interval': 3 * 60,
        'enable': 1,
    },
    {
        'name': 'cool-proxy.net',
        'resource': ['https://www.cool-proxy.net/proxies/http_proxy_list/country_code:/port:/anonymous:1/page:%s'
                     % i for i in range(1, 11)],
        'task_queue': SPIDER_AJAX_TASK,
        'parse_type': 'common',
        'parse_rule': {
            'pre_extract_method': 'xpath',
            'pre_extract': '//tr',
            'infos_pos': 1,
            'infos_end': -1,
            'detail_rule': 'td::text',
            'ip_pos': 0,
            'port_pos': 1,
            'extract_protocol': True,
            'split_detail': False,
            'protocols': None
        },
        'interval': 30,
        'enable': 1,
    },
    {
        'name': 'free-proxy-list.net',
        'resource': [
            'https://free-proxy-list.net/',
            'https://free-proxy-list.net/uk-proxy.html',
            'https://free-proxy-list.net/anonymous-proxy.html',
        ],
        'task_queue': SPIDER_COMMON_TASK,
        'parse_type': 'common',
        'parse_rule': {
            'pre_extract_method': 'xpath',
            'pre_extract': '//tbody//tr',
            'infos_pos': 0,
            'infos_end': None,
            'detail_rule': 'td::text',
            'ip_pos': 0,
            'port_pos': 1,
            'extract_protocol': True,
            'split_detail': False,
            'protocols': None
        },
        'interval': 60,
        'enable': 1,
    },

    {
        'name': 'proxylistplus',
        'resource': [
            'http://list.proxylistplus.com/Fresh-HTTP-Proxy-List-1',
            'http://list.proxylistplus.com/SSL-List-1'
        ],
        'task_queue': SPIDER_COMMON_TASK,
        'parse_type': 'common',
        'parse_rule': {
            'pre_extract_method': 'xpath',
            'pre_extract': '//tr[contains(@class, "cells")]',
            'infos_pos': 1,
            'infos_end': -1,
            'detail_rule': 'td::text',
            'ip_pos': 0,
            'port_pos': 1,
            'extract_protocol': False,
            'split_detail': False,
            'protocols': None
        },
        'interval': 3 * 60,
        'enable': 1,
    },

    {
        'name': 'free-proxy.cz',
        'resource': ['http://free-proxy.cz/en/proxylist/main/%s' % i for i in range(1, 30)],
        'task_queue': SPIDER_AJAX_TASK,
        'parse_type': 'free-proxy',
        'interval': 3 * 60,
        'enable': 1,
    },
    {
        'name': 'proxy-list.org',
        'resource': ['https://proxy-list.org/english/index.php?p=%s' % i for i in range(1, 11)],
        'task_queue': SPIDER_AJAX_TASK,
        'parse_type': 'common',
        'parse_rule': {
            'pre_extract_method': 'css',
            'pre_extract': '.table ul',
            'infos_pos': 1,
            'infos_end': None,
            'detail_rule': 'li::text',
            'ip_pos': 0,
            'port_pos': 1,
            'extract_protocol': True,
            'split_detail': True,
            'protocols': None
        },
        'interval': 60,
        'enable': 1,
    },
    {
        'name': 'ab57.ru',
        'resource': ['http://ab57.ru/downloads/proxyold.txt'],
        'task_queue': SPIDER_COMMON_TASK,
        'parse_type': 'text',
        'parse_rule': {
            'pre_extract': None,
            'delimiter': '\r\n',
            'redundancy': None,
            'protocols': None
        },
        'interval': 60,
        'enable': 1,
    },
    {
        'name': '66ip.cn',
        'resource': ['http://www.66ip.cn/%s.html' % i for i in range(1, 3)] +
                    ['http://www.66ip.cn/areaindex_%s/%s.html' % (i, j)
                     for i in range(1, 35) for j in range(1, 3)],
        'task_queue': SPIDER_COMMON_TASK,
        'parse_type': 'common',
        'parse_rule': {
            'pre_extract_method': 'xpath',
            'pre_extract': '//tr',
            'infos_pos': 4,
            'infos_end': None,
            'detail_rule': 'td::text',
            'ip_pos': 0,
            'port_pos': 1,
            'extract_protocol': True,
            'split_detail': False,
            'protocols': None
        },
        'interval': 2 * 60,
        'enable': 1
    },
    {
        'name': 'baizhongsou.com',
        'resource': ['http://ip.baizhongsou.com/'],
        'task_queue': SPIDER_COMMON_TASK,
        'parse_type': 'common',
        'parse_rule': {
            'pre_extract_method': 'xpath',
            'pre_extract': '//tr',
            'infos_pos': 1,
            'infos_end': None,
            'detail_rule': 'td::text',
            'ip_pos': 0,
            'port_pos': 1,
            'extract_protocol': True,
            'split_detail': True,
            'protocols': None
        },
        'interval': 30,
        'enable': 1
    },
    {
        'name': 'data5u.com',
        'resource': [
            'http://www.data5u.com/free/index.shtml',
            'http://www.data5u.com/free/gngn/index.shtml',
            'http://www.data5u.com/free/gwgn/index.shtml'
        ],
        'task_queue': SPIDER_COMMON_TASK,
        'parse_type': 'common',
        'parse_rule': {
            'pre_extract_method': 'xpath',
            'pre_extract': '//ul[contains(@class, "l2")]',
            'infos_pos': 0,
            'infos_end': None,
            'detail_rule': 'span li::text',
            'ip_pos': 0,
            'port_pos': 1,
            'extract_protocol': True,
            'split_detail': False,
            'protocols': None
        },
        'interval': 10,
        'enable': 1,
    },
    {
        'name': 'ip3366.net',
        'resource': ['http://www.ip3366.net/free/?stype=1&page=%s' % i for i in range(1, 3)] +
                    ['http://www.ip3366.net/free/?stype=3&page=%s' % i for i in range(1, 3)],
        'task_queue': SPIDER_COMMON_TASK,
        'parse_type': 'common',
        'parse_rule': {
            'pre_extract_method': 'xpath',
            'pre_extract': '//tr',
            'infos_pos': 1,
            'infos_end': None,
            'detail_rule': 'td::text',
            'ip_pos': 0,
            'port_pos': 1,
            'extract_protocol': True,
            'split_detail': False,
            'protocols': None
        },
        'interval': 30,
        'enable': 1
    },
]

# crawler will fetch tasks from the following queues
CRAWLER_TASK_MAPS = {
    'common': SPIDER_COMMON_TASK,
    'ajax': SPIDER_AJAX_TASK,
    'gfw': SPIDER_GFW_TASK,
    'ajax_gfw': SPIDER_AJAX_GFW_TASK
}

# validator scheduler will fetch tasks from resource queue and store into task queue
VALIDATOR_TASKS = [
    {
        'name': 'http',
        'task_queue': TEMP_HTTP_QUEUE,
        'resource': VALIDATED_HTTP_QUEUE,
        'interval': 5,  # 20 minutes
        'enable': 1,
    },
    {
        'name': 'https',
        'task_queue': TEMP_HTTPS_QUEUE,
        'resource': VALIDATED_HTTPS_QUEUE,
        'interval': 5,
        'enable': 1,
    },
    {
        'name': 'weibo',
        'task_queue': TEMP_WEIBO_QUEUE,
        'resource': VALIDATED_WEIBO_QUEUE,
        'interval': 5,
        'enable': 1,
    },
    {
        'name': 'zhihu',
        'task_queue': TEMP_ZHIHU_QUEUE,
        'resource': VALIDATED_ZHIHU_QUEUE,
        'interval': 5,
        'enable': 1,
    },
    {
        'name': 'tgstat',
        'task_queue': TEMP_TGSTAT_QUEUE,
        'resource': VALIDATED_TGSTAT_QUEUE,
        'interval': 5,
        'enable': 1,
    },
]

# validators will fetch proxies from the following queues
TEMP_TASK_MAPS = {
    'init': INIT_HTTP_QUEUE,
    'http': TEMP_HTTP_QUEUE,
    'https': TEMP_HTTPS_QUEUE,
    'weibo': TEMP_WEIBO_QUEUE,
    'zhihu': TEMP_ZHIHU_QUEUE,
    'tgstat': TEMP_TGSTAT_QUEUE,
}

# target website that use http protocol
HTTP_TASKS = ['http']

# target website that use https protocol
HTTPS_TASKS = ['https', "tgstat"]

# todo the three maps may be combined in one map
# validator scheduler and clients will fetch proxies from the following queues
SCORE_MAPS = {
    'http': VALIDATED_HTTP_QUEUE,
    'https': VALIDATED_HTTPS_QUEUE,
    'weibo': VALIDATED_WEIBO_QUEUE,
    'zhihu': VALIDATED_ZHIHU_QUEUE,
    'tgstat': VALIDATED_TGSTAT_QUEUE,
}

# validator scheduler and clients will fetch proxies from the following queues which are verified recently
TTL_MAPS = {
    'http': TTL_HTTP_QUEUE,
    'https': TTL_HTTPS_QUEUE,
    'weibo': TTL_WEIBO_QUEUE,
    'zhihu': TTL_ZHIHU_QUEUE,
    'tgstat': TTL_TGSTAT_QUEUE,
}

SPEED_MAPS = {
    'http': SPEED_HTTP_QUEUE,
    'https': SPEED_HTTPS_QUEUE,
    'weibo': SPEED_WEIBO_QUEUE,
    'zhihu': SPEED_ZHIHU_QUEUE,
    'tgstat': SPEED_TGSTAT_QUEUE,
}

