import requests
import json
from datetime import datetime, timezone

# ========= CONFIG ========= #
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1393291781612769462/Xbc_NFH3kYxcXdhd-F443Y30-DIq2cDeCTz4q9waYplKx_yUzpKseAMCfsgyLAR0DJyL"

# ========= ALERT PAYLOAD ========= #
def generate_alert(ticker, setup, entry_price, exit_price, confidence, zone, coach_msg, summary):
    timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')

    embed = {
        "title": "🚨 ScalpX Trade Alert (LIVE)",
        "color": 16753920,
        "fields": [
            {"name": "📊 Ticker:", "value": f"${ticker}", "inline": True},
            {"name": "🎯 Setup:", "value": setup, "inline": True},
            {"name": "💰 Entry:", "value": f"${entry_price}", "inline": True},
            {"name": "🏁 Target Exit:", "value": f"${exit_price}", "inline": True},
            {"name": "📈 Confidence:", "value": f"{confidence}/10", "inline": True},
            {"name": "🧠 Zone:", "value": zone, "inline": True},
            {"name": "🎤 Coach Says:", "value": coach_msg, "inline": False},
            {"name": "🧠 Summary:", "value": summary, "inline": False}
        ],
        "footer": {
            "text": f"Sent • {timestamp}"
        }
    }

    data = {
        "username": "ScalpX AI Bot",
        "embeds": [embed]
    }

    return data

# ========= SEND ALERT TO DISCORD ========= #
def send_alert():
    alert_data = generate_alert(
        ticker="AAPL",
        setup="VWAP Rejection + RSI 30 Bounce",
        entry_price="210.05",
        exit_price="212.60",
        confidence="9.3",
        zone="🔥 HOT ZONE",
        coach_msg="You didn’t just trade… you attacked that entry.",
        summary="AAPL rejected off VWAP after RSI hit 29.8 and bounced with a bullish engulfing candle. Volume confirmed. This was a sniper-level reversal setup."
    )

    response = requests.post(DISCORD_WEBHOOK_URL, json=alert_data)

    if response.status_code == 204:
        print("✅ Alert successfully sent to Discord.")
    else:
        print(f"❌ Failed to send alert. Status Code: {response.status_code}, Response: {response.text}")

# ========= MAIN TRIGGER ========= #
if __name__ == "__main__":
    send_alert()
