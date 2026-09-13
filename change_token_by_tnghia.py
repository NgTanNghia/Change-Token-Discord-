import httpx
import json
import base64
import random
import string
import brotli
from typing import Optional, Dict
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os
import time
import sys
import threading
from pystyle import Colorate, Colors

def _tnghia_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    art = """
    ╔══════════════════════════════════════════╗
    ║                                          ║
    ║     *** XIN CHAO NGUYEN TAN NGHIA ***    ║
    ║                                          ║
    ╚══════════════════════════════════════════╝
    """
    print(Colorate.Horizontal(Colors.rainbow, art))
    time.sleep(1)

def _tnghia_typewriter(text, delay=0.04):
    for char in text:
        sys.stdout.write(Colorate.Horizontal(Colors.rainbow, char))
        sys.stdout.flush()
        time.sleep(delay)
    print()

def _tnghia_intro():
    _tnghia_banner()
    _tnghia_typewriter('>>> Chao mung Nguyen Tan Nghia den voi he thong!')
    time.sleep(0.3)
    _tnghia_typewriter('>>> Ban la nguoi dep trai nhat server!')
    time.sleep(0.3)
    _tnghia_typewriter('>>> Hom nay la: ' + time.strftime('%d/%m/%Y'))
    time.sleep(0.3)
    _tnghia_typewriter('>>> Thoi gian: ' + time.strftime('%H:%M:%S'))
    time.sleep(0.3)
    compliments = [
        '>>> NTN dz nhat vu tru!',
        '>>> Khong ai dep hon NTN!',
        '>>> NTN la legend!',
        '>>> Server khong co NTN la that hut!',
    ]
    _tnghia_typewriter(random.choice(compliments))
    time.sleep(0.5)

class TnghiaIuEm:
    BASE = "https://discord.com/api/v9"
    UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    BUILD = 373618

    def __init__(self, token: str):
        self.token = token
        self.new_token = None
        self._handoff_key = None
        self._client = httpx.Client(http2=True, verify=True, timeout=30.0)

    def _tnghia_hotboy_decompress(self, r) -> bytes:
        data = r.content
        enc = r.headers.get('content-encoding', '').lower()
        if enc == 'br':
            try:
                data = brotli.decompress(data)
            except:
                pass
        return data

    def _tnghia_hot_props(self) -> str:
        p = {
            "os": "Windows",
            "browser": "Chrome",
            "device": "",
            "system_locale": "en-US",
            "browser_user_agent": self.UA,
            "browser_version": "131.0.0.0",
            "os_version": "10",
            "referrer": "",
            "referring_domain": "",
            "referrer_current": "",
            "referring_domain_current": "",
            "release_channel": "stable",
            "client_build_number": self.BUILD,
            "client_event_source": None
        }
        return base64.b64encode(json.dumps(p, separators=(',', ':')).encode()).decode()

    def _tnghia_hotboy_headers(self, auth=True, fp=None) -> Dict[str, str]:
        h = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "no-cache",
            "Content-Type": "application/json",
            "Origin": "https://discord.com",
            "Referer": "https://discord.com/channels/@me",
            "Sec-Ch-Ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": self.UA,
            "X-Debug-Options": "bugReporterEnabled",
            "X-Discord-Locale": "en-US",
            "X-Discord-Timezone": "Asia/Ho_Chi_Minh",
            "X-Super-Properties": self._tnghia_hot_props(),
        }
        if auth and self.token:
            h["Authorization"] = self.token
        if fp:
            h["X-Fingerprint"] = fp
        return h

    def _tnghia_lay_fp(self) -> Optional[str]:
        try:
            r = self._client.get(f"{self.BASE}/experiments", headers=self._tnghia_hotboy_headers(auth=False))
            if r.status_code == 200:
                return r.json().get("fingerprint")
        except:
            pass
        return None

    def _tnghia_check(self) -> Optional[Dict]:
        try:
            r = self._client.get(f"{self.BASE}/users/@me", headers=self._tnghia_hotboy_headers())
            if r.status_code == 200:
                u = r.json()
                print(Colorate.Horizontal(Colors.rainbow, f"User: {u['username']} (ID: {u['id']})"))
                return u
            print(Colorate.Horizontal(Colors.rainbow, f"Token loi: {r.status_code}"))
        except:
            pass
        return None

    def _tnghia_tao_handoff(self) -> Optional[str]:
        try:
            self._handoff_key = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
            r = self._client.post(
                f"{self.BASE}/auth/handoff",
                headers=self._tnghia_hotboy_headers(),
                json={"key": self._handoff_key}
            )
            if r.status_code == 200:
                content = self._tnghia_hotboy_decompress(r)
                data = json.loads(content.decode('utf-8'))
                ht = data.get("handoff_token")
                if ht:
                    print(Colorate.Horizontal(Colors.rainbow, "Tao handoff token thanh cong"))
                    time.sleep(0.5)
                    return ht
            print(Colorate.Horizontal(Colors.rainbow, f"Handoff that bai: {r.status_code} - {r.text[:100]}"))
        except Exception as e:
            print(Colorate.Horizontal(Colors.rainbow, f"Loi tao handoff: {e}"))
        return None

    def _tnghia_doi_token(self, handoff_token: str) -> Optional[str]:
        try:
            time.sleep(0.5)
            fp = self._tnghia_lay_fp()
            r = self._client.post(
                f"{self.BASE}/auth/handoff/exchange",
                headers=self._tnghia_hotboy_headers(auth=False, fp=fp),
                json={"handoff_token": handoff_token, "key": self._handoff_key}
            )
            if r.status_code == 200:
                content = self._tnghia_hotboy_decompress(r)
                data = json.loads(content.decode('utf-8'))
                tk = data.get("token")
                if tk:
                    print(Colorate.Horizontal(Colors.rainbow, f"Lay duoc token moi: {tk[:30]}..."))
                    self.new_token = tk
                    return tk
                print(Colorate.Horizontal(Colors.rainbow, f"Exchange OK nhung khong co token trong response: {data}"))
            else:
                print(Colorate.Horizontal(Colors.rainbow, f"Exchange that bai: {r.status_code} - {r.text[:100]}"))
        except Exception as e:
            print(Colorate.Horizontal(Colors.rainbow, f"Loi exchange token: {e}"))
        return None

    def _tnghia_logout_cu(self) -> bool:
        try:
            h = self._tnghia_hotboy_headers()
            h["Authorization"] = self.token
            r = self._client.post(
                f"{self.BASE}/auth/logout",
                headers=h,
                json={"provider": None, "voip_provider": None}
            )
            ok = r.status_code in [200, 204]
            print(Colorate.Horizontal(Colors.rainbow, "Logout token cu thanh cong" if ok else f"Logout tra ve {r.status_code} (co the da het han)"))
            return ok
        except Exception as e:
            print(Colorate.Horizontal(Colors.rainbow, f"Loi logout token cu: {e}"))
            return False

    def _tnghia_verify_moi(self) -> bool:
        if not self.new_token:
            print(Colorate.Horizontal(Colors.rainbow, "Khong co token moi de verify"))
            return False
        try:
            h = self._tnghia_hotboy_headers()
            h["Authorization"] = self.new_token
            r = self._client.get(f"{self.BASE}/users/@me", headers=h)
            if r.status_code == 200:
                u = r.json()
                print(Colorate.Horizontal(Colors.rainbow, f"Verify OK: {u.get('username','?')} (ID: {u.get('id','?')})"))
                return True
            print(Colorate.Horizontal(Colors.rainbow, f"Token moi bi loi khi verify: {r.status_code}"))
        except Exception as e:
            print(Colorate.Horizontal(Colors.rainbow, f"Loi verify token moi: {e}"))
        return False

    def _tnghia_fallback(self) -> Optional[str]:
        try:
            self._client.get(f"{self.BASE}/users/@me/settings", headers=self._tnghia_hotboy_headers())
        except:
            pass
        return None

    def tnghia_hot_code(self) -> Optional[str]:
        if not self._tnghia_check():
            print(Colorate.Horizontal(Colors.rainbow, "Token nhap loi hoac da die"))
            return None

        handoff = self._tnghia_tao_handoff()
        if not handoff:
            print(Colorate.Horizontal(Colors.rainbow, "Khong tao duoc handoff token"))
            return self._tnghia_fallback()

        new_tk = self._tnghia_doi_token(handoff)
        if not new_tk:
            print(Colorate.Horizontal(Colors.rainbow, "Khong lay duoc token moi"))
            return self._tnghia_fallback()

        if self._tnghia_verify_moi():
            print(Colorate.Horizontal(Colors.rainbow, "Verify token moi OK — dang logout token cu..."))
            self._tnghia_logout_cu()
            print(Colorate.Horizontal(Colors.rainbow, f"\nToken moi: {new_tk}"))
            return new_tk
        else:
            print(Colorate.Horizontal(Colors.rainbow, "Token moi khong hop le — giu nguyen token cu, bo qua logout"))
            return None

    def __del__(self):
        self._client.close()


if __name__ == "__main__":
    _tnghia_intro()

    print(Colorate.Horizontal(Colors.rainbow, "\n" + "="*60))
    print(Colorate.Horizontal(Colors.rainbow, "        DISCORD TOKEN REFRESHER TOOL - TNGHIA"))
    print(Colorate.Horizontal(Colors.rainbow, "="*60))

    input_file = input(Colorate.Horizontal(Colors.rainbow, "\nNhap file chua token (mac dinh: tokens.txt): ")).strip()
    if not input_file:
        input_file = "tokens.txt"

    if not os.path.exists(input_file):
        print(Colorate.Horizontal(Colors.rainbow, f"Loi: Khong tim thay file '{input_file}'"))
        sys.exit()

    output_file = input(Colorate.Horizontal(Colors.rainbow, "Nhap file luu token moi (mac dinh: new.txt): ")).strip()
    if not output_file:
        output_file = "new.txt"

    with open(input_file, 'r', encoding='utf-8') as f:
        tokens = [l.strip() for l in f if l.strip()]

    if not tokens:
        print(Colorate.Horizontal(Colors.rainbow, "Khong co token nao trong file."))
        sys.exit()

    print(Colorate.Horizontal(Colors.rainbow, f"\nDa tim thay {len(tokens)} token trong '{input_file}'"))
    print(Colorate.Horizontal(Colors.rainbow, f"Se luu ket qua vao '{output_file}'"))

    confirm = input(Colorate.Horizontal(Colors.rainbow, "\nTiep tuc? (y/n): ")).strip().lower()
    if confirm != 'y':
        print(Colorate.Horizontal(Colors.rainbow, "Da huy."))
        sys.exit()

    print(Colorate.Horizontal(Colors.rainbow, "\n" + "="*50))

    new_tokens = []
    for idx, old_token in enumerate(tokens, 1):
        print(Colorate.Horizontal(Colors.rainbow, f"\n[Token {idx}/{len(tokens)}] Dang xu ly..."))
        client = TnghiaIuEm(old_token)
        new_token = client.tnghia_hot_code()
        if new_token:
            new_tokens.append(new_token)
            print(Colorate.Horizontal(Colors.rainbow, f"✓ Token {idx} thanh cong"))
        else:
            print(Colorate.Horizontal(Colors.rainbow, f"✗ Token {idx} that bai"))

    if new_tokens:
        with open(output_file, 'w', encoding='utf-8') as f:
            for nt in new_tokens:
                f.write(nt + '\n')
        print(Colorate.Horizontal(Colors.rainbow, f"\nDa luu {len(new_tokens)} token vao '{output_file}'"))
    else:
        print(Colorate.Horizontal(Colors.rainbow, "\nKhong co token nao duoc lam moi thanh cong."))

    input(Colorate.Horizontal(Colors.rainbow, "\nNhan Enter de thoat..."))
