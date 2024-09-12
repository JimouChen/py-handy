# !usr/bin/env python3
# -*- coding:utf-8 -*-
import asyncio

import aiohttp
from loguru import logger


class AsyncApiUtil:
    """
    AsyncApiUtil Demo：

    ```python
    async def main():
        data_list = [{"prompt": f'1234_{_}', "msg_id": _} for _ in range(60)]
        url = 'http://11.22.33.44/llm/mock'
        workers = 100
        tasks = [AsyncApiUtil.req_post(url=url, data=data, workers=workers) for data in data_list]
        responses = await asyncio.gather(*tasks)
        for response in responses:
            # handle the response
            print(response)

    if __name__ == '__main__':
        asyncio.run(main())
    ```
    """
    __headers = {'Content-Type': "application/json"}
    __default_workers = 2

    @classmethod
    async def post(
            cls, url: str,
            payload: dict = None,
            headers: dict = None,
            verify: bool = False,
            proxy: dict = None,
            timeout: float = None
    ):
        """ 异步发送POST请求到指定的URL

        :param url: 请求的目的url
        :param payload: 请求体
        :param headers: 自定义请求头信息，设置如内容类型、认证令牌等
        :param verify: 是否验证SSL证书，若为True，则会验证服务器的SSL证书
        :param proxy: 设置代理服务器信息
        :param timeout: 若是None，则客户端将无限期地等待服务器的响应，除非遇到其他类型的超时（例如连接超时或响应超时）
        :return:
        """
        headers = headers if headers else cls.__headers
        try:
            timeout = aiohttp.ClientTimeout(total=timeout)
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.post(url, json=payload, headers=headers, ssl=verify, proxy=proxy) as resp:
                    logger.debug(f'{url=}, {headers=}, {payload=}, response: {await resp.json() if resp else resp}')
                    return await resp.json()
        except Exception as err:
            logger.error(f'{url=}, {err=}, {headers=}, {payload=}')
            return {}

    @classmethod
    async def req_post(cls, url: str, data: dict, workers: int = None):
        """
        异步协程post请求
        :param url:  请求的url
        :param data: 请求体
        :param workers: 限制并发数
        :return:
        """
        workers = workers if workers else cls.__default_workers
        semaphore = asyncio.Semaphore(workers)
        async with semaphore:
            resp = await AsyncApiUtil.post(url, payload=data)
            return resp
