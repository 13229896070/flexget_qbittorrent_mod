import chardet


class NetUtils:
    @staticmethod
    def decode(response):
        if response is None:
            return None
        content = response.content
        charset_encoding = chardet.detect(content).get('encoding')
        if charset_encoding == 'ascii':
            charset_encoding = 'unicode_escape'
        elif charset_encoding == 'Windows-1254':
            charset_encoding = 'utf-8'
        return content.decode(charset_encoding if charset_encoding else 'utf-8', 'ignore')

    @staticmethod
    def cookie_str_to_dict(cookie_str):
        cookie_dict = {}
        for line in cookie_str.split(';'):
            if '=' in line:
                i = line.index('=')
                cookie_dict[line[0:i]] = line[i + 1:]
        return cookie_dict

    @staticmethod
    def dict_merge(dict1, dict2):
        for i in dict2:
            if isinstance(dict1.get(i), dict) and isinstance(dict2.get(i), dict):
                NetUtils.dict_merge(dict1[i], dict2[i])
            else:
                dict1[i] = dict2[i]
