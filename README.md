# Adversary Emulation Plan Builder (AEPB)

Generate lab-ready adversary emulation plans from MITRE ATT&CK.
![CI](https://github.com/sahilrahman378-hub/adversary-emulation-plan-builder/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Why

Writing an emulation plan by hand from MITRE ATT&CK is slow and error-prone.
AEPB pulls a threat group's techniques directly from the ATT&CK STIX dataset
and produces a kill-chain-ordered markdown checklist you can run in a lab.

## Features

- MITRE ATT&CK STIX native — no hardcoded tables
- Kill-chain ordered output (recon → impact)
- Per-technique checklist for emulation + detection verification
- Zero runtime dependencies (Python stdlib only)

## Install

```bash
git clone https://github.com/sahilrahman378-hub/adversary-emulation-plan-builder.git
cd adversary-emulation-plan-builder
curl -L -o enterprise-attack.json https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack.json