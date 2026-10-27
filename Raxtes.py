import requests, threading, time, webview, os
from flask import Flask, render_template_string, request

app = Flask(__name__)

WHATSAPP_NUMBER = "256755207966"
MOMO_NUMBER = "0755207966"
MOMO_NAME = "Mubiru Bakali"
PREMIUM_KEY = "RAXTES-2026"
PREMIUM_PRICE_UG = "5,000 UGX"
PREMIUM_PRICE_INT = "$3 USD"
PAYPAL_EMAIL = "your-paypal@gmail.com"
PAYPAL_ME_LINK = "https://paypal.me/yourname/3"
FLUTTERWAVE_LINK = "https://flutterwave.com/pay/raxtes"
MONETAG_ZONE_ID = "YOUR_ZONE_ID"
TMDB_API_KEY = "YOUR_TMDB_API_KEY"

ANILIST_URL = "https://graphql.anilist.co"

BASE_HTML = '''
<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>RAXTES ULTIMATE</title>
<script>(function(d,z,s){s.src='https://'+d+'/400/'+z;try{(document.body||document.documentElement).appendChild(s)}catch(e){}})('groleegni.net',{{monetag_zone}},document.createElement('script'))</script>
<style>
*{box-sizing:border-box}body{margin:0;background:#070710;color:#fff;font-family:Arial}
.header{background:#0f0f1a;padding:12px 15px;display:flex;justify-content:space-between;align-items:center;position:sticky;top:0;z-index:100;border-bottom:1px solid #222;flex-wrap:wrap;gap:10px}
.logo{font-weight:900;font-size:22px;color:#ff2e63}
.tabs{display:flex;gap:6px;flex-wrap:wrap}
.tab{padding:8px 14px;border-radius:20px;background:#1a1a2a;cursor:pointer;font-size:12px;font-weight:700;border:1px solid #333}
.tab.active{background:#ff2e63;border-color:#ff2e63}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:12px;padding:15px}
.card{background:#15151f;border-radius:12px;overflow:hidden;border:1px solid #222;cursor:pointer}
.card img{width:100%;height:200px;object-fit:cover}
.card-info{padding:8px}
.card-info h3{font-size:12px;margin:0;height:32px;overflow:hidden}
.badge{background:#ff2e63;padding:2px 5px;border-radius:4px;font-size:9px}
.ad-box{background:#1a1a2e;border:1px dashed #444;padding:12px;text-align:center;margin:10px;border-radius:10px;color:#888;font-size:12px}
.btn{padding:10px 18px;border-radius:20px;font-weight:700;cursor:pointer;border:none;display:inline-block;text-decoration:none;font-size:13px;margin:4px}
.btn-pink{background:#ff2e63;color:#fff}.btn-dark{background:#222;color:#fff}.btn-gold{background:gold;color:#000}.btn-green{background:#00c853;color:#fff}.
