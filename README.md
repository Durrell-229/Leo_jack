# 🔐 leo-jack — Cybersecurity Toolkit

```
  ██╗     ███████╗ ██████╗       ██╗ █████╗  ██████╗██╗  ██╗
  ██║     ██╔════╝██╔═══██╗      ██║██╔══██╗██╔════╝██║ ██╔╝
  ██║     █████╗  ██║   ██║      ██║███████║██║     █████╔╝ 
  ██║     ██╔══╝  ██║   ██║ ██   ██║██╔══██║██║     ██╔═██╗ 
  ███████╗███████╗╚██████╔╝ ╚█████╔╝██║  ██║╚██████╗██║  ██╗
  ╚══════╝╚══════╝ ╚═════╝   ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
```

> ⚠️ **Usage éthique et légal uniquement.** Cet outil est destiné à la formation, aux tests sur vos propres systèmes, et à la cybersécurité défensive.

---

## ✅ Prérequis

- **Python 3.6+** (aucune dépendance externe)
- Fonctionne sur **Linux**, **Windows**, **macOS**, **Termux (Android)**, **GitHub Codespaces**

---

## 🚀 Installation & Lancement

### Linux / macOS / GitHub Codespaces
```bash
git clone https://github.com/TON_USERNAME/leo-jack.git
cd leo-jack
python3 leo_jack.py
```

### Windows
```cmd
git clone https://github.com/TON_USERNAME/leo-jack.git
cd leo-jack
python leo_jack.py
```

### Termux (Android)
```bash
pkg update && pkg install python git
git clone https://github.com/TON_USERNAME/leo-jack.git
cd leo-jack
python leo_jack.py
```

---

## 🛠️ Modules disponibles

| # | Module | Description |
|---|--------|-------------|
| 1 | **Scanner de ports** | Scan rapide, standard (1-1024) ou personnalisé avec multi-threading |
| 2 | **Info IP / Géolocalisation** | Pays, FAI, organisation, détection proxy/VPN via ip-api.com |
| 3 | **Ping & Traceroute** | Test de connectivité et trace de route |
| 4 | **Analyse DNS** | Résolution A/AAAA, reverse lookup, MX, NS, TXT |
| 5 | **Hash fichier/texte** | MD5, SHA1, SHA256, SHA512 avec vérification |
| 6 | **Encodage Base64** | Encodage et décodage |
| 7 | **Vérification SSL** | Validité du certificat, émetteur, date d'expiration |
| 8 | **Scanner sous-réseau** | Découverte d'hôtes actifs sur un réseau CIDR |
| 9 | **Infos système** | OS, interfaces réseau, connexions actives |
| 10 | **Banner grabbing** | Récupération de la bannière d'un service |

---

## 📁 Structure

```
leo-jack/
├── leo_jack.py     # Script principal (tout-en-un)
└── README.md
```

---

## 🔒 Éthique

Cet outil est conçu pour :
- Auditer **vos propres** systèmes et réseaux
- Apprendre les bases de la cybersécurité
- Effectuer des tests en environnement contrôlé

**Ne l'utilisez jamais sur des systèmes sans autorisation explicite.**

---

## 📝 Licence

MIT — libre d'utilisation et de modification.
