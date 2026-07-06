import requests
import os

def glados_checkin(cookie_str):
    checkin_url = "https://glados.rocks/api/user/checkin"
    status_url = "https://glados.rocks/api/user/status"
    
    headers = {
        "cookie": cookie_str,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "content-type": "application/json;charset=UTF-8",
        "origin": "https://glados.rocks",
        "referer": "https://glados.rocks/console"
    }
    
    payload = '{"token": "glados.one"}'
    
    print("====== 开始执行 GLaDOS 自动签到 ======")
    try:
        response = requests.post(checkin_url, headers=headers, data=payload, timeout=10)
        res_json = response.json()
        print(f"【签到状态】: {res_json.get('message', '未知响应')}")
        
        status_response = requests.get(status_url, headers=headers, timeout=10)
        status_json = status_response.json()
        
        if status_json.get("code") == 0 and "data" in status_json:
            print(f"【账户账号】: {status_json['data']['email']}")
            print(f"【当前余额】: 您的套餐还剩 {int(float(status_json['data']['leftDays']))} 天")
        else:
            print("【状态查询】: 未能获取到账户天数，请检查 Cookie。")
    except Exception as e:
        print(f"【系统错误】: {e}")
    print("======================================")

if __name__ == "__main__":
    # 这里保持空字符串即可，GitHub Actions 会在运行时自动把 Secret 塞进这里
    MY_COOKIE = ""
    glados_checkin(MY_COOKIE)
