# !/usr/bin/env python3
# _*_ coding: utf-8 _*_
import warnings


class EnvUtils:
    @staticmethod
    def init_env():
        """
        to filter warning massage
        :return:
        """
        warnings.filterwarnings('ignore')
