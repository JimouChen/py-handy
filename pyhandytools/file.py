# !/usr/bin/env python3
# _*_ coding: utf-8 _*_
import base64
import json
import os
import shutil
from typing import Union

from loguru import logger


class FileUtils:
    @staticmethod
    def write2json(json_path: str, data: Union[list, dict], way='w'):
        """
        write dict or list data to jsonfile
        :param json_path: json file path
        :param data: dict data or list data
        :param way: w|w+|a|a+
        :return:
        """
        with open(json_path, way, encoding='utf-8') as f:
            f.write(json.dumps(data, ensure_ascii=False, indent=4))
        logger.info(f'write json to: {json_path}')

    @staticmethod
    def write2jsonl(jsonl_path: str, data: list[dict]):
        try:
            with open(jsonl_path, 'w', encoding='utf-8') as file:
                # 遍历数据列表
                for _ in data:
                    file.write(f'{json.dumps(_)}\n')
            logger.success(f'write jsonl to {jsonl_path} successfully!')
        except Exception as e:
            logger.error(f'write jsonl to {jsonl_path} failed: {e}')

    @staticmethod
    def load_json(json_path: str) -> Union[list, dict]:
        """
        load json file, only read
        :param json_path: json file path
        :return: a dict or a list
        """
        with open(json_path, 'r', encoding='utf-8') as f:
            _ = f.read()
            if _ == '':
                logger.warning(f'Your json file in {json_path} is empty!!!')
                return {}
            data = json.loads(_)
        return data

    @staticmethod
    def load_jsonl(jsonl_path: str) -> list[dict]:
        """
        parse jsonl file
        :param jsonl_path: jsonl file path
        :return: [{'k': v}, {...}]
        """
        data = []
        try:
            with open(jsonl_path, 'r', encoding='utf-8') as file:
                for line in file:
                    data.append(json.loads(line))
        except Exception as e:
            logger.error(e)
        return data

    @staticmethod
    def check_dir_path(dir_path: str):
        """
        check the dir path is existed
        :param dir_path: the dir path to be checked
        :return:
        """
        if not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)
            logger.warning(f'mkdir path: {dir_path}')

    @staticmethod
    def count_file_number(dir_path: str) -> int:
        """
        count the file number of the dir path
        :param dir_path: the dir path to be counted
        :return: the number of files
        """
        return len(os.listdir(dir_path))

    @staticmethod
    def check_jsonfile_existed(file_path: str):
        """
        to check is the json file existed
        :param file_path: json file path
        :return:
        """
        if not os.path.exists(file_path):
            FileUtils.write2json(file_path, [])

    @staticmethod
    def pretty_json(data: Union[list, dict], indent: int = 4) -> Union[str, None]:
        """
        :param data: list or dict data
        :param indent: indent
        :return: pretty json string
        """
        if data is None:
            logger.warning('data is required not to be None!')
            return None
        return json.dumps(data, ensure_ascii=False, indent=indent)

    @staticmethod
    def cp_and_rm(old_file_path: str, new_file_path: str) -> bool:
        """
        copy file and remove file
        :param old_file_path: old file path
        :param new_file_path: new file path
        :return: bool
        """
        try:
            if os.path.exists(old_file_path):
                shutil.copy(old_file_path, new_file_path)
                os.remove(old_file_path)
                return True
            logger.warning(f'{old_file_path} is not existed!')
            return False
        except Exception as e:
            logger.error(f'copy and remove file failed: {e}')
            return False


class ImageUtil:
    @staticmethod
    def base64_encode_img(img_path: str) -> str:
        with open(img_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")

        return encoded_string

    @staticmethod
    def base64_decode_img(encoded_string: str, save_img_path: str) -> bool:
        """
        decode base64 code to image.
        :param encoded_string: base64 encoded string
        :param save_img_path: save image path after decoding
        :return:
        """
        decoded_data = base64.b64decode(encoded_string)
        try:
            with open(save_img_path, "wb") as new_image_file:
                new_image_file.write(decoded_data)
            logger.success(f'base64 decode successfully! save path: {save_img_path}')
            return True
        except Exception as e:
            logger.error(f'base64 decode failed! {e}')
            return False
