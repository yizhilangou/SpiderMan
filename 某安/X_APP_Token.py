import hashlib
import datetime
import base64
import re
import bcrypt

X_App_Device = ""


def get_v2_token():
    device_code = X_App_Device  # 抓包headers有，固定即可
    format_base64 = re.compile('\\r\\n|\\r|\\n|=')
    token_part1 = "token://com.coolapk.market/dcf01e569c1e3db93a3d0fcf191a622c?"
    device_code_md5 = hashlib.md5(device_code.encode('utf-8')).hexdigest()
    timestamp = int(datetime.datetime.now().timestamp())
    timestamp_md5 = hashlib.md5(str(timestamp).encode('utf-8')).hexdigest()
    timestamp_base64 = re.sub(format_base64, '', base64.b64encode(str(timestamp).encode('utf-8')).decode())
    token = f'{token_part1}{timestamp_md5}${device_code_md5}&com.coolapk.market'
    token_base64 = re.sub(format_base64, '', base64.b64encode(token.encode('utf-8')).decode())
    token_base64_md5 = hashlib.md5(token_base64.encode('utf-8')).hexdigest()
    token_md5 = hashlib.md5(token.encode('utf-8')).hexdigest()
    arg = f'$2y$10${timestamp_base64}/{token_md5}'
    salt = (arg[:28] + 'u').encode('utf-8')
    crypt = bcrypt.hashpw(token_base64_md5.encode('utf-8'), salt)
    crypt_base64 = base64.b64encode(crypt).decode()
    print('-'*50)
    print(f'v2{crypt_base64}')
    print('-'*50)
    return f'v2{crypt_base64}'

# 示例使用
if __name__ == '__main__':
    print(get_v2_token())
