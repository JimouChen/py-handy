# !/usr/bin/env python3
# _*_ coding: utf-8 _*_
import json
import os
from typing import Union

from loguru import logger


class FileUtils:
    @staticmethod
    def write2json(json_path: str, data: Union[list, dict]):
        with open(json_path, 'w', encoding='utf-8') as f:
            f.write(json.dumps(data, ensure_ascii=False, indent=4))
        logger.info(f'write json to: {json_path}')

    @staticmethod
    def load_json(json_path: str) -> dict:
        with open(json_path, 'r', encoding='utf-8') as f:
            _ = f.read()
            if _ == '':
                logger.warning(f'Your json file in {json_path} is empty!!!')
                return {}
            data = json.loads(_)
        return data

    @staticmethod
    def check_dir_path(dir_path: str):
        if not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)
            logger.warning(f'mkdir path: {dir_path}')
