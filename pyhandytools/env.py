# !/usr/bin/env python3
# _*_ coding: utf-8 _*_
import sys
import warnings


class EnvUtils:
    @staticmethod
    def init_env():
        """
        to filter warning massage
        :return:
        """
        warnings.filterwarnings('ignore')

    @staticmethod
    def get_platform() -> str:
        """
        get current platform system
        :return: linux|win|darwin/macOS
        """
        return sys.platform.lower()
