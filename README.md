# GhostTrace

> Outil OSINT modulaire en ligne de commande — reconnaissance de domaines, profils et infrastructure

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-En%20développement-orange)

---

## Présentation

GhostTrace est un outil OSINT (*Open Source Intelligence*) développé from scratch en Python. Il permet de collecter des informations publiques sur une cible — domaine, username ou adresse IP — depuis un seul point d'entrée en ligne de commande.

Le projet est conçu avec une architecture modulaire : chaque type de reconnaissance est isolé dans un module indépendant, testable et extensible.

> ⚠️ **Usage légal uniquement.** Cet outil est destiné à des fins éducatives et à des audits sur des systèmes pour lesquels vous avez une autorisation explicite.

---

## Fonctionnalités

### `ghosttrace web <domain>`
Analyse complète d'un domaine :
- Résolution DNS multi-records (A, MX, NS, TXT)
- Lookup WHOIS (registrar, dates d'enregistrement et d'expiration, name servers)
- Analyse des headers HTTP (serveur, stack technique, protections en place)
- Détection automatique HTTP / HTTPS

### `ghosttrace person <username>` *(en cours)*
Recherche de présence en ligne sur 15+ plateformes :
- GitHub, GitLab, Bitbucket, StackOverflow, HackerOne
- Steam, Telegram, DeviantArt, Keybase, Fiverr
- Gravatar, Linktree, AboutMe, Pinterest, et plus
- Gestion des soft 404 par plateforme (keyword, taille de réponse)

### `ghosttrace infra <ip>` *(à venir)*
Analyse d'infrastructure :
- Scan de ports ouverts
- Récupération de banners
- GeoIP
- Intégration Shodan

---

## Architecture

```
ghosttrace/
├── cli.py                  ← Entry point Click (CLI)
├── core/
│   └── session.py          ← SessionManager (dual-lib httpx / requests)
├── modules/
│   ├── web.py              ← Recon domaine
│   ├── person.py           ← Recon username
│   └── infra.py            ← Recon infrastructure (à venir)
└── output/
    └── display.py          ← Affichage Rich (tableaux, couleurs)
```

---

## Stack technique

| Composant | Technologie |
|---|---|
| Langage | Python 3.13 |
| CLI | Click |
| HTTP | httpx + requests (dual-lib) |
| DNS | dnspython |
| WHOIS | python-whois |
| Affichage terminal | Rich |
| Build system | Hatchling |
| Tests | pytest *(à venir)* |

---

## Installation

```bash
git clone https://github.com/<username>/ghosttrace.git
cd ghosttrace
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

---

## Utilisation

```bash
# Analyse d'un domaine
ghosttrace web example.com

# Recherche d'un username
ghosttrace person torvalds

# Version
ghosttrace version
```

---

## Choix techniques notables

**Dual-lib HTTP (httpx + requests)**
Certaines plateformes (notamment Reddit) bloquent les requêtes `httpx` au niveau du fingerprint TLS. Le `SessionManager` gère les deux clients de façon transparente — `httpx.Client` par défaut, `requests.Session` avec connection pooling pour les plateformes qui l'exigent.

**Gestion des soft 404**
Plusieurs plateformes retournent un code HTTP 200 même quand un profil n'existe pas. GhostTrace gère trois stratégies de détection par plateforme : status code HTTP, présence d'un keyword dans le HTML, et taille de la réponse.

**Architecture modulaire**
Chaque module est indépendant et testable isolément. Le core engine gère les sessions, les headers et la réutilisation des connexions de façon centralisée.

---

## Roadmap

- [x] Module Web (DNS, WHOIS, HTTP headers)
- [x] Affichage Rich
- [x] SessionManager dual-lib
- [ ] Module Person complet (breach lookup HaveIBeenPwned)
- [ ] Module Infra (ports, GeoIP, Shodan)
- [ ] Export JSON / CSV
- [ ] Rapport HTML (Jinja2)
- [ ] Tests unitaires (pytest)
- [ ] CI GitHub Actions

---
*Projet développé dans le cadre d'un apprentissage de la cybersécurité offensive.*
