# 🔐 leo-jack — Cybersecurity Toolkit

```
  ██╗     ███████╗ ██████╗       ██╗ █████╗  ██████╗██╗  ██╗
  ██║     ██╔════╝██╔═══██╗      ██║██╔══██╗██╔════╝██║ ██╔╝
  ██║     █████╗  ██║   ██║      ██║███████║██║     █████╔╝ 
  ██║     ██╔══╝  ██║   ██║ ██   ██║██╔══██║██║     ██╔═██╗ 
  ███████╗███████╗╚██████╔╝ ╚█████╔╝██║  ██║╚██████╗██║  ██╗
  ╚══════╝╚══════╝ ╚═════╝   ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
```

> ⚠️ **Usage éthique et légal uniquement.** Cet outil est destiné à la formation,
> aux tests sur vos propres systèmes, et à la cybersécurité défensive.

---

## 📦 Dépôt

```
https://github.com/Durrell-229/Leo_jack.git
```

---

## ✅ Prérequis

- **Python 3.6+** — aucune dépendance externe, bibliothèque standard uniquement
- Compatible **Linux**, **Windows**, **macOS**, **Termux (Android)**, **GitHub Codespaces**

---

## 🚀 Installation & Lancement

### 🐧 Linux / macOS / GitHub Codespaces
```bash
git clone https://github.com/Durrell-229/Leo_jack.git
cd Leo_jack
python3 leo_jack.py
```

### 🪟 Windows
```cmd
git clone https://github.com/Durrell-229/Leo_jack.git
cd Leo_jack
python leo_jack.py
```

### 📱 Termux (Android)
```bash
pkg update && pkg install python git
git clone https://github.com/Durrell-229/Leo_jack.git
cd Leo_jack
python leo_jack.py
```

### ⚡ Raccourci Termux (optionnel)
```bash
echo "alias leojack='python ~/Leo_jack/leo_jack.py'" >> ~/.bashrc
source ~/.bashrc
# Lancer depuis n'importe où :
leojack
```

---

## 🛠️ Modules disponibles

| # | Module | Description | Termux |
|---|--------|-------------|--------|
| 1 | **Scanner de ports** | Scan rapide (top 20), standard (1-1024) ou personnalisé — multi-threadé | ✅ |
| 2 | **Info IP / Géolocalisation** | Pays, FAI, organisation, détection proxy/VPN | ✅ |
| 3 | **Ping & Traceroute** | Test de connectivité et trace de route | ⚠️ `pkg install traceroute` |
| 4 | **Analyse DNS** | Résolution A/AAAA, reverse lookup, MX, NS, TXT | ✅ |
| 5 | **Hash fichier/texte** | MD5, SHA1, SHA256, SHA512 avec vérification | ✅ |
| 6 | **Encodage Base64** | Encodage et décodage | ✅ |
| 7 | **Vérification SSL** | Validité du certificat, émetteur, jours restants | ✅ |
| 8 | **Scanner sous-réseau** | Découverte d'hôtes actifs sur un réseau CIDR /24 | ✅ Wi-Fi |
| 9 | **Infos système** | OS, interfaces réseau, connexions actives | ✅ |
| 10 | **Banner grabbing** | Récupération de la bannière d'un service réseau | ✅ |

---

## 🔄 Mise à jour

```bash
cd Leo_jack
git pull
```

---

## 📤 Contribuer / Pousser des modifications

```bash
cd Leo_jack
git add .
git commit -m "mise à jour leo-jack"
git push
```

> 💡 Pour `git push`, utilise un **token d'accès personnel** GitHub (pas ton mot de passe).
> GitHub → Settings → Developer settings → Personal access tokens → Generate new token

---

## 📁 Structure du projet

```
Leo_jack/
├── leo_jack.py     # Script principal tout-en-un
└── README.md       # Ce fichier
```

---

## 🔒 Avertissement éthique

Cet outil est conçu pour :
- Auditer **vos propres** systèmes et réseaux
- Apprendre les bases de la cybersécurité
- Effectuer des tests en environnement contrôlé (CTF, lab, etc.)

**Ne l'utilisez jamais sur des systèmes sans autorisation explicite.**
Tout usage non autorisé est illégal et contraire à l'éthique.

---

## 📝 Licence

MIT — libre d'utilisation, de modification et de distribution.

---

*Made with 🖤 by Durrell-229 — leo-jack v1.0*
