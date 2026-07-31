# Apr. 29th 2025

import requests
import network
import json
from time import sleep

WIFI_SSID = 'YOUR_WIFI_SSID'
WIFI_PASS = 'YOUR_WIFI_PASSWORD'

# DiscordのチャンネルURL
url = 'YOUR_DISCORD_WEBHOOK_URL'

# 送信するメッセージとユーザ名をセット
MESSAGE = "Hello Discord"
USER = '0P01023'

# WiFi接続関数
def connect_wifi():
    wifi = network.WLAN(network.STA_IF) 
    wifi.active(True)
    sleep(0.5)
    
    while not wifi.isconnected():
        print("Connecting to WiFi", end="")
        wifi.connect(WIFI_SSID, WIFI_PASS)
        sleep(1)
        while not wifi.isconnected():
            print(".", end="")
            sleep(1)
            pass
       
    ip = wifi.ifconfig()[0]
    rssi = wifi.status('rssi')
    return ip, rssi

# Discordメッセージ送信関数
def discord_send(message, user):
    # 辞書型データ作成
    data = {
        'content': message,  # メッセージ内容
        'username': user
    }

    # 辞書型のdataをJSON形式の文字列に変換し、UTF-8にエンコーディング
    json_data = json.dumps(data).encode("utf-8")

    # ヘッダー作成
    header = {
        "content-type": "application/json; charset=utf-8"
    }

    print(json_data)

    # DiscordのWebhookに送信
    response = requests.post(url,  data=json_data, headers=header)

    if response.status_code == 204:
        print("メッセージが送信されました。")
    else:
        print(f"エラーが発生しました: {response.status_code}")
        print(response.text)


# ここからメイン
if __name__ == '__main__':
    # WiFi接続
    ip, rssi = connect_wifi()
    print("IP:", ip, "RSSI:", str(rssi))

    # Discordメッセージ送信
    discord_send(MESSAGE, USER)
