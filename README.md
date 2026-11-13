# ShopLab — E-commerce Security Lab

> ## ⚠️ WARNING — FOR EDUCATIONAL USE ONLY
>
> - This is a **learning project** about web application security.
> - It will ship in two variants built from the same source code: **Secure** (hardened) and **Vulnerable** (intentionally flawed).
> - **The Vulnerable variant must only run on your own local machine.** Never deploy it to the Internet, and never expose it with ngrok or any other tunnel.
> - Every service port is bound to `127.0.0.1` only (reachable from your machine alone).
> - All data is **fake**. Never enter real personal information or real payment cards.
> - Only attack systems you own. Using the techniques from this lab against other people's systems is **illegal**.

## What is ShopLab?

A small e-commerce website (customers, staff, administrators) used to practice:

1. **Building** a web application the secure way (the **Secure** variant).
2. **Deliberately weakening** one thing at a time to understand how each vulnerability works (the **Vulnerable** variant).
3. **Exploiting** the Vulnerable variant, then proving that the Secure variant blocks the same attack.

| Variant | Purpose | Planned address |
| --- | --- | --- |
| Secure | Reference build with security controls applied | `127.0.0.1:8082` |
| Vulnerable | Same features, with intentional vulnerabilities | `127.0.0.1:8081` |

## Tech stack

Django REST Framework · React (Vite, JavaScript) · PostgreSQL · Docker Compose · VNPay Sandbox · Git + GitHub

## Status

🚧 **Project setup (Phase 0).** There is no application code yet, only the README and repository configuration.
The project is built in small Pull Requests (PRs); each PR is reviewed carefully before it is merged.

## Repository security

This repository is **public**, so:

- Never commit a real `.env` file, passwords, API keys, the VNPay `HashSecret`, or AWS keys.
- Only [`.env.example`](.env.example) is committed. It is a template and **contains no real values**.
- GitHub *Secret scanning* and *Push protection* are enabled to block pushes that contain secrets.

If you find a security problem in this repository, please open an Issue (without including any real secret).
