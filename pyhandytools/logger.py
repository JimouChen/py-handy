# !/usr/bin/env python3
# _*_ coding: utf-8 _*_
import loguru
from loguru import logger
from loguru._logger import Logger


class LoggerUtils:
    default_log_format = "{time:YYYY-MM-DD HH:mm:ss.SSSS} | {level} | {name} | {function}:{line} | {message}"
    _version_prefix = "V"

    @classmethod
    def init_logger(
            cls,
            logger_path: str,
            filter_word: str = "",
            service_name: str = None,
            level: str = "DEBUG",
            rotation: str = "200 MB",
            retention: str = "7 days",
            enqueue: bool = True,
            log_format: str = None,
            version: str = None
    ) -> Logger:
        ret_logger = logger.bind(name=service_name) if service_name else logger
        log_format = log_format if log_format else cls.default_log_format
        version_prefix = f'{cls._version_prefix}{version} ' if version else ''
        ret_logger.add(
            logger_path,
            rotation=rotation,
            format=f'{version_prefix} {log_format}',
            level=cls.parse_level(level),
            filter=lambda x: x['extra'].get('name') == service_name if service_name else filter_word in x['message'],
            encoding='utf-8',
            enqueue=enqueue,
            retention=retention
        )
        ret_logger.info(f'log file load in ===> {logger_path}')

        return ret_logger

    @classmethod
    def parse_level(cls, level: str) -> str:
        return level.upper()

    @classmethod
    def new_generic_logger(
            cls,
            service_name: str,
            logger_path: str,
            level: str = "DEBUG"
    ) -> Logger:
        """
        init a default config logger
        :param service_name: your log name
        :param logger_path: the path of logger file
        :param level: log level: DEBUG|INFO|SUCCESS|WARNING|ERROR
        :return: logger obj
        """
        service_logger = cls.init_logger(
            logger_path=logger_path,
            level=level,
            service_name=service_name
        )
        service_logger.info(f'{service_name=} init...')

        return service_logger
