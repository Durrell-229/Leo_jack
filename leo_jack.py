#!/usr/bin/env python3
"""
╦  ╔═╗╔═╗   ╦╔═╗╔═╗╦╔═
║  ║╣ ║ ║───║╠═╣║  ╠╩╗
╩═╝╚═╝╚═╝  ╚╝╩ ╩╚═╝╩ ╩
     Cybersecurity Toolkit
        by leo-jack v1.0
"""

import sys
import os
import socket
import subprocess
import platform
import ipaddress
import urllib.request
import urllib.error
import json
import re
import hashlib
import base64
import ssl
import struct
import time
import threading
from datetime import datetime

# ─── COLORS ─────────────────────────────────────────────
class C:
    RED    = "\033[91m"
    GREEN  = "\033[92m"
    YELLOW = "\033[93m"
    BLUE   = "\033[94m"
    CYAN   = "\033[96m"
    WHITE  = "\033[97m"
    BOLD   = "\033[1m"
    DIM    = "\033[2m"
    RESET  = "\033[0m"

# Windows: enable ANSI
if platform.system() == "Windows":
    os.system("color")
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    except:
        pass

# ─── BANNER ──────────────────────────────────────────────
BANNER = f"""
{C.CYAN}{C.BOLD}
  ██╗     ███████╗ ██████╗       ██╗ █████╗  ██████╗██╗  ██╗
  ██║     ██╔════╝██╔═══██╗      ██║██╔══██╗██╔════╝██║ ██╔╝
  ██║     █████╗  ██║   ██║      ██║███████║██║     █████╔╝ 
  ██║     ██╔══╝  ██║   ██║ ██   ██║██╔══██║██║     ██╔═██╗ 
  ███████╗███████╗╚██████╔╝ ╚█████╔╝██║  ██║╚██████╗██║  ██╗
  ╚══════╝╚══════╝ ╚═════╝   ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
{C.RESET}{C.DIM}  ─────────────── Cybersecurity Toolkit v1.0 ───────────────{C.RESET}
{C.YELLOW}  [?] Éducatif uniquement. Usage éthique et légal seulement.{C.RESET}
"""

MENU = f"""
{C.BOLD}{C.WHITE}  ╔══════════════════════════════════════╗
  ║         MENU PRINCIPAL               ║
  ╠══════════════════════════════════════╣{C.RESET}
{C.GREEN}  ║  [1]  Scanner de ports               ║
  ║  [2]  Info réseau / IP               ║
  ║  [3]  Ping & traceroute              ║
  ║  [4]  Analyse DNS                    ║
  ║  [5]  Hash d'un fichier/texte        ║
  ║  [6]  Encodage Base64                ║
  ║  [7]  Vérif. SSL/HTTPS               ║
  ║  [8]  Scanner sous-réseau            ║
  ║  [9]  Infos système                  ║
  ║  [10] Bannière de service            ║
  ║  [0]  Quitter                        ║{C.RESET}
{C.BOLD}{C.WHITE}  ╚══════════════════════════════════════╝{C.RESET}
"""

# ─── UTILITIES ────────────────────────────────────────────
def log(msg, level="info"):
    icons = {"info": f"{C.CYAN}[*]{C.RESET}", "ok": f"{C.GREEN}[+]{C.RESET}",
             "warn": f"{C.YELLOW}[!]{C.RESET}", "err": f"{C.RED}[-]{C.RESET}"}
    print(f"  {icons.get(level,'[?]')} {msg}")

def separator(title=""):
    w = 44
    if title:
        pad = (w - len(title) - 2) // 2
        print(f"\n{C.CYAN}  {'─'*pad} {title} {'─'*pad}{C.RESET}")
    else:
        print(f"{C.DIM}  {'─'*w}{C.RESET}")

def prompt(msg):
    return input(f"\n{C.YELLOW}  ▶ {msg}: {C.RESET}").strip()

def clear():
    os.system("cls" if platform.system() == "Windows" else "clear")

# ─── MODULE 1: PORT SCANNER ───────────────────────────────
def port_scanner():
    separator("SCANNER DE PORTS")
    target = prompt("Cible (IP ou domaine)")
    if not target:
        return
    try:
        ip = socket.gethostbyname(target)
        log(f"Résolution: {target} → {ip}", "ok")
    except socket.gaierror:
        log("Impossible de résoudre l'hôte.", "err"); return

    mode = prompt("Mode: [1] Rapide (top 20) | [2] Standard (1-1024) | [3] Personnalisé")
    
    top20 = [21,22,23,25,53,80,110,135,139,143,443,445,
             3306,3389,5900,6379,8080,8443,9200,27017]

    if mode == "1":
        ports = top20
    elif mode == "2":
        ports = range(1, 1025)
    elif mode == "3":
        p = prompt("Plage (ex: 80-443 ou 22,80,443)")
        try:
            if "-" in p:
                a, b = p.split("-")
                ports = range(int(a), int(b)+1)
            else:
                ports = [int(x) for x in p.split(",")]
        except:
            log("Format invalide.", "err"); return
    else:
        ports = top20

    log(f"Scan de {ip} en cours...", "info")
    open_ports = []
    lock = threading.Lock()

    def scan_port(port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((ip, port))
            s.close()
            if result == 0:
                try:
                    svc = socket.getservbyport(port)
                except:
                    svc = "?"
                with lock:
                    open_ports.append((port, svc))
                    print(f"  {C.GREEN}[OUVERT]{C.RESET} Port {C.BOLD}{port}{C.RESET} ({svc})")
        except:
            pass

    threads = []
    for p in ports:
        t = threading.Thread(target=scan_port, args=(p,))
        t.start()
        threads.append(t)
        if len(threads) >= 100:
            for th in threads: th.join()
            threads = []
    for t in threads: t.join()

    separator()
    if open_ports:
        log(f"{len(open_ports)} port(s) ouvert(s) trouvé(s).", "ok")
    else:
        log("Aucun port ouvert détecté.", "warn")

# ─── MODULE 2: IP INFO ────────────────────────────────────
def ip_info():
    separator("INFO RÉSEAU / IP")
    target = prompt("IP ou domaine (vide = ma propre IP)")

    if not target:
        target = "me"

    try:
        url = f"http://ip-api.com/json/{target}?fields=status,message,country,regionName,city,isp,org,as,query,mobile,proxy,hosting"
        req = urllib.request.urlopen(url, timeout=5)
        data = json.loads(req.read().decode())

        if data.get("status") == "success":
            separator("RÉSULTATS")
            fields = {
                "IP":          data.get("query"),
                "Pays":        data.get("country"),
                "Région":      data.get("regionName"),
                "Ville":       data.get("city"),
                "FAI":         data.get("isp"),
                "Org":         data.get("org"),
                "AS":          data.get("as"),
                "Proxy/VPN":   "Oui" if data.get("proxy") else "Non",
                "Hébergeur":   "Oui" if data.get("hosting") else "Non",
                "Mobile":      "Oui" if data.get("mobile") else "Non",
            }
            for k, v in fields.items():
                print(f"  {C.CYAN}{k:<14}{C.RESET} {v}")
        else:
            log(f"Erreur: {data.get('message','Inconnu')}", "err")
    except Exception as e:
        log(f"Échec de la requête: {e}", "err")

# ─── MODULE 3: PING & TRACEROUTE ─────────────────────────
def ping_trace():
    separator("PING & TRACEROUTE")
    target = prompt("Cible (IP ou domaine)")
    if not target:
        return

    action = prompt("[1] Ping | [2] Traceroute")
    system = platform.system()

    if action == "1":
        log(f"Ping vers {target}...", "info")
        if system == "Windows":
            cmd = ["ping", "-n", "4", target]
        else:
            cmd = ["ping", "-c", "4", target]
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
            print(f"\n{C.DIM}{result.stdout}{C.RESET}")
        except FileNotFoundError:
            log("Commande ping non disponible.", "err")
        except subprocess.TimeoutExpired:
            log("Timeout.", "warn")

    elif action == "2":
        log(f"Traceroute vers {target}...", "info")
        if system == "Windows":
            cmd = ["tracert", "-h", "15", target]
        else:
            cmd = ["traceroute", "-m", "15", target]
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            print(f"\n{C.DIM}{result.stdout or result.stderr}{C.RESET}")
        except FileNotFoundError:
            log("traceroute non disponible. Installer avec: apt install traceroute", "err")
        except subprocess.TimeoutExpired:
            log("Timeout.", "warn")

# ─── MODULE 4: DNS LOOKUP ─────────────────────────────────
def dns_lookup():
    separator("ANALYSE DNS")
    domain = prompt("Domaine (ex: example.com)")
    if not domain:
        return

    log(f"Résolution DNS de {domain}...", "info")

    # Basic A record
    try:
        ips = socket.getaddrinfo(domain, None)
        unique_ips = list(set(r[4][0] for r in ips))
        for ip in unique_ips:
            fam = "IPv6" if ":" in ip else "IPv4"
            log(f"A/AAAA  → {ip} ({fam})", "ok")
    except Exception as e:
        log(f"Résolution échouée: {e}", "err")

    # Reverse lookup
    try:
        rev = socket.gethostbyaddr(unique_ips[0])[0]
        log(f"Reverse → {rev}", "ok")
    except:
        pass

    # nslookup fallback for MX, NS
    try:
        for rtype in ["MX", "NS", "TXT"]:
            if platform.system() == "Windows":
                cmd = ["nslookup", f"-type={rtype}", domain]
            else:
                cmd = ["nslookup", f"-type={rtype}", domain]
            res = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
            lines = [l.strip() for l in res.stdout.splitlines()
                     if l.strip() and not l.startswith("Server") and not l.startswith("Address")]
            if lines:
                log(f"{rtype} records:", "info")
                for l in lines[:5]:
                    if l:
                        print(f"    {C.DIM}{l}{C.RESET}")
    except:
        pass

# ─── MODULE 5: HASH ───────────────────────────────────────
def hash_tool():
    separator("HASH FICHIER / TEXTE")
    choice = prompt("[1] Hasher du texte | [2] Hasher un fichier")

    algos = {"1": "md5", "2": "sha1", "3": "sha256", "4": "sha512"}

    if choice == "1":
        text = prompt("Texte à hasher")
        data = text.encode()
    elif choice == "2":
        path = prompt("Chemin du fichier")
        try:
            with open(path, "rb") as f:
                data = f.read()
        except Exception as e:
            log(f"Erreur: {e}", "err"); return
    else:
        return

    separator("RÉSULTATS")
    for key, algo in algos.items():
        h = hashlib.new(algo, data).hexdigest()
        print(f"  {C.CYAN}{algo.upper():<8}{C.RESET} {h}")

    # Optional: check against known hash
    check = prompt("Comparer avec un hash connu ? (laisser vide pour passer)")
    if check:
        check = check.strip().lower()
        matched = any(hashlib.new(a, data).hexdigest() == check for a in algos.values())
        if matched:
            log("✓ Hash correspondant trouvé !", "ok")
        else:
            log("✗ Aucune correspondance.", "err")

# ─── MODULE 6: BASE64 ─────────────────────────────────────
def base64_tool():
    separator("ENCODAGE / DÉCODAGE BASE64")
    action = prompt("[1] Encoder | [2] Décoder")
    text = prompt("Texte")
    if not text:
        return

    if action == "1":
        result = base64.b64encode(text.encode()).decode()
        log(f"Encodé: {C.GREEN}{result}{C.RESET}", "ok")
    elif action == "2":
        try:
            result = base64.b64decode(text.encode()).decode(errors="replace")
            log(f"Décodé: {C.GREEN}{result}{C.RESET}", "ok")
        except Exception as e:
            log(f"Erreur de décodage: {e}", "err")

# ─── MODULE 7: SSL CHECKER ────────────────────────────────
def ssl_checker():
    separator("VÉRIFICATION SSL/HTTPS")
    host = prompt("Domaine (ex: google.com)")
    if not host:
        return
    port = 443

    try:
        ctx = ssl.create_default_context()
        conn = ctx.wrap_socket(socket.socket(socket.AF_INET), server_hostname=host)
        conn.settimeout(5)
        conn.connect((host, port))
        cert = conn.getpeercert()
        conn.close()

        subject = dict(x[0] for x in cert.get("subject", []))
        issuer  = dict(x[0] for x in cert.get("issuer", []))
        not_before = cert.get("notBefore", "?")
        not_after  = cert.get("notAfter", "?")
        san = cert.get("subjectAltName", [])

        separator("CERTIFICAT SSL")
        print(f"  {C.CYAN}Sujet    {C.RESET} {subject.get('commonName','?')}")
        print(f"  {C.CYAN}Émetteur {C.RESET} {issuer.get('organizationName','?')}")
        print(f"  {C.CYAN}Valide du{C.RESET} {not_before}")
        print(f"  {C.CYAN}Expire le{C.RESET} {not_after}")
        if san:
            names = [v for t, v in san if t == "DNS"][:5]
            print(f"  {C.CYAN}SAN      {C.RESET} {', '.join(names)}")

        # Check expiry
        try:
            exp = datetime.strptime(not_after, "%b %d %H:%M:%S %Y %Z")
            days_left = (exp - datetime.utcnow()).days
            if days_left < 0:
                log(f"Certificat EXPIRÉ depuis {abs(days_left)} jours !", "err")
            elif days_left < 30:
                log(f"Expire dans {days_left} jours — renouvelez bientôt !", "warn")
            else:
                log(f"Certificat valide encore {days_left} jours.", "ok")
        except:
            pass

    except ssl.SSLCertVerificationError as e:
        log(f"Certificat invalide: {e}", "err")
    except Exception as e:
        log(f"Connexion SSL échouée: {e}", "err")

# ─── MODULE 8: SUBNET SCANNER ─────────────────────────────
def subnet_scan():
    separator("SCANNER SOUS-RÉSEAU")
    log("Détection de l'IP locale...", "info")

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
    except:
        local_ip = "192.168.1.1"

    default_net = ".".join(local_ip.split(".")[:3]) + ".0/24"
    log(f"IP locale: {local_ip}", "ok")
    network = prompt(f"Réseau CIDR [{default_net}]") or default_net

    try:
        net = ipaddress.IPv4Network(network, strict=False)
    except ValueError as e:
        log(f"CIDR invalide: {e}", "err"); return

    hosts = list(net.hosts())
    if len(hosts) > 256:
        log("Réseau trop grand (max /24). Réduisez la plage.", "warn"); return

    log(f"Scan de {len(hosts)} hôtes...", "info")
    alive = []
    lock = threading.Lock()

    def check_host(ip):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.3)
            result = s.connect_ex((str(ip), 80))
            s.close()
            if result != 0:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.3)
                result = s.connect_ex((str(ip), 22))
                s.close()
            if result == 0:
                try:
                    name = socket.gethostbyaddr(str(ip))[0]
                except:
                    name = "?"
                with lock:
                    alive.append(str(ip))
                    print(f"  {C.GREEN}[ACTIF]{C.RESET} {str(ip):<18} {C.DIM}{name}{C.RESET}")
        except:
            pass

    threads = []
    for host in hosts:
        t = threading.Thread(target=check_host, args=(host,))
        t.start()
        threads.append(t)
        if len(threads) >= 50:
            for th in threads: th.join()
            threads = []
    for t in threads: t.join()

    separator()
    log(f"{len(alive)} hôte(s) actif(s) sur {len(hosts)}.", "ok" if alive else "warn")

# ─── MODULE 9: SYSTEM INFO ────────────────────────────────
def system_info():
    separator("INFOS SYSTÈME")
    s = platform.system()
    print(f"  {C.CYAN}OS          {C.RESET} {s} {platform.release()} ({platform.machine()})")
    print(f"  {C.CYAN}Python      {C.RESET} {sys.version.split()[0]}")
    print(f"  {C.CYAN}Hostname    {C.RESET} {socket.gethostname()}")

    try:
        local_ip = socket.gethostbyname(socket.gethostname())
        print(f"  {C.CYAN}IP locale   {C.RESET} {local_ip}")
    except:
        pass

    # Network interfaces
    try:
        if s != "Windows":
            result = subprocess.run(["ip", "addr"], capture_output=True, text=True, timeout=3)
            if not result.returncode:
                ifaces = re.findall(r'\d+: (\w+):.*?inet (\d+\.\d+\.\d+\.\d+)', result.stdout, re.DOTALL)
                for iface, ip in ifaces:
                    print(f"  {C.CYAN}Interface   {C.RESET} {iface}: {ip}")
        else:
            result = subprocess.run(["ipconfig"], capture_output=True, text=True, timeout=3)
            ips = re.findall(r'IPv4.*?:\s+([\d.]+)', result.stdout)
            for ip in ips:
                print(f"  {C.CYAN}Interface   {C.RESET} {ip}")
    except:
        pass

    # Open connections count
    try:
        if s != "Windows":
            res = subprocess.run(["ss", "-tuln"], capture_output=True, text=True, timeout=3)
            count = len(res.stdout.strip().splitlines()) - 1
            print(f"  {C.CYAN}Connexions  {C.RESET} {count} ports en écoute")
    except:
        pass

# ─── MODULE 10: BANNER GRABBING ───────────────────────────
def banner_grab():
    separator("BANNIÈRE DE SERVICE")
    host = prompt("Hôte (IP ou domaine)")
    port_str = prompt("Port")
    if not host or not port_str:
        return
    try:
        port = int(port_str)
    except:
        log("Port invalide.", "err"); return

    log(f"Connexion à {host}:{port}...", "info")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((host, port))
        s.send(b"HEAD / HTTP/1.0\r\nHost: " + host.encode() + b"\r\n\r\n")
        banner = s.recv(1024).decode(errors="replace")
        s.close()
        separator("BANNIÈRE REÇUE")
        for line in banner.strip().splitlines()[:20]:
            print(f"  {C.DIM}{line}{C.RESET}")
        log("Bannière récupérée.", "ok")
    except ConnectionRefusedError:
        log("Connexion refusée.", "err")
    except socket.timeout:
        log("Timeout — le port ne répond pas.", "warn")
    except Exception as e:
        log(f"Erreur: {e}", "err")

# ─── MAIN LOOP ────────────────────────────────────────────
def main():
    clear()
    print(BANNER)

    modules = {
        "1": port_scanner,
        "2": ip_info,
        "3": ping_trace,
        "4": dns_lookup,
        "5": hash_tool,
        "6": base64_tool,
        "7": ssl_checker,
        "8": subnet_scan,
        "9": system_info,
        "10": banner_grab,
    }

    while True:
        print(MENU)
        choice = input(f"  {C.BOLD}{C.WHITE}leo-jack{C.RESET}{C.CYAN}#{C.RESET} ").strip()

        if choice == "0":
            print(f"\n{C.CYAN}  Au revoir. Stay ethical.{C.RESET}\n")
            sys.exit(0)
        elif choice in modules:
            try:
                modules[choice]()
            except KeyboardInterrupt:
                log("Opération annulée.", "warn")
        else:
            log("Option invalide.", "warn")

        input(f"\n{C.DIM}  ↩  Appuie sur Entrée pour continuer...{C.RESET}")
        clear()
        print(BANNER)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{C.CYAN}  [leo-jack] Bye.{C.RESET}\n")
        sys.exit(0)
