# !/usr/bin/env python3
# _*_ coding: utf-8 _*_
from bs4 import BeautifulSoup
from lxml.html.clean import Cleaner


class ParserUtil:
    """
    to clean html label and get pure text
    """
    enter, space = '\\n', ' '
    labels = [
        'a', 'abbr', 'acronym', 'address', 'applet', 'area', 'article', 'aside', 'audio', 'b', 'base', 'basefont',
        'bdi', 'bdo', 'big', 'blockquote', 'body', 'br', 'button', 'canvas', 'caption', 'center', 'cite', 'code',
        'col', 'colgroup', 'command', 'data', 'datalist', 'dd', 'del', 'details', 'dir', 'div', 'dfn', 'dialog',
        'dl', 'dt', 'em', 'embed', 'fieldset', 'figcaption', 'figure', 'font', 'footer', 'form', 'frame', 'frameset',
        'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'head', 'header', 'hr', 'html', 'i', 'iframe', 'img', 'input', 'ins',
        'isindex', 'kbd', 'keygen', 'label', 'legend', 'li', 'link', 'main', 'map', 'mark', 'menu', 'menuitem',
        'meta', 'meter', 'nav', 'noframes', 'noscript', 'object', 'ol', 'optgroup', 'option', 'output', 'p', 'param',
        'pre', 'progress', 'q', 'rp', 'rt', 'ruby', 's', 'samp', 'script', 'section', 'select', 'small', 'source',
        'span', 'strike', 'strong', 'style', 'sub', 'summary', 'sup', 'svg', 'table', 'tbody', 'td', 'template',
        'textarea', 'tfoot', 'th', 'thead', 'time', 'title', 'tr', 'track', 'tt', 'u', 'ul', 'var', 'video', 'wbr'
    ]

    @classmethod
    def clear_text(cls, html: str) -> str:
        tree = BeautifulSoup(html, features='lxml')
        clean_txt = tree.prettify()
        clean_txt = ParserUtil.sanitize(clean_txt)
        clean_txt = BeautifulSoup(clean_txt, 'html.parser').get_text()
        clean_txt = clean_txt.replace('\n', '').replace('\r', '').replace('<div>', '').replace(
            '</div>', '').strip(' ')

        clean_txt = cls.delete_extra_flag(clean_txt, cls.enter).strip(cls.enter)
        clean_txt = cls.delete_extra_flag(clean_txt, cls.space)
        return clean_txt

    @staticmethod
    def sanitize(dirty_html: str):
        cleaner = Cleaner(
            page_structure=True,
            meta=True,
            embedded=True,
            links=True,
            style=True,
            processing_instructions=True,
            inline_style=True,
            scripts=True,
            javascript=True,
            comments=True,
            frames=True,
            forms=True,
            annoying_tags=True,
            remove_unknown_tags=True,
            safe_attrs_only=True,
            remove_tags=ParserUtil.labels
        )

        return cleaner.clean_html(dirty_html)

    @classmethod
    def delete_extra_flag(cls, text: str, extra_flag: str) -> str:
        """
        删除额外的字符
        :param text: 需要处理的文本字符串
        :param extra_flag: 需要删除的额外字符子串
        :return: 处理后的文本字符串
        """
        while extra_flag * 2 in text:
            text = text.replace(extra_flag * 2, extra_flag)
        return text
