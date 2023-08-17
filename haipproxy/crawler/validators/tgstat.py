from haipproxy.config.settings import (
    TEMP_TGSTAT_QUEUE, VALIDATED_TGSTAT_QUEUE,
    TTL_TGSTAT_QUEUE, SPEED_TGSTAT_QUEUE)
from ..redis_spiders import ValidatorRedisSpider
from .base import BaseValidator

class TgStatValidator(BaseValidator, ValidatorRedisSpider):
    """This validator checks the liveness of zhihu proxy resources"""
    name = 'tgstat'
    urls = [
        'https://tgstat.ru/tags/theme'
    ]
    task_queue = TEMP_TGSTAT_QUEUE
    score_queue = VALIDATED_TGSTAT_QUEUE
    ttl_queue = TTL_TGSTAT_QUEUE
    speed_queue = SPEED_TGSTAT_QUEUE
    success_key = 'Подборки Telegram-каналов'