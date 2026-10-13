#!/usr/bin/env python3
"""Adversary Emulation Plan Builder (AEPB) — MVP

Generate lab-ready adversary emulation plans from MITRE ATT&CK.

Authorized lab use only. This tool generates plans; it does not execute
any technique against any system.
"""
import argparse
import json
import re
from pathlib import Path
from datetime import date

STIX_FILE = Path("enterprise-attack.json")

TACTIC_ORDER = [
    "reconnaissance",
    "resource-development",
    "initial-access",
    "execution",
    "persistence",
    "privilege-escalation",
    "stealth",
    "defense-evasion",
    "defense-impairment",
    "credential-access",
    "discovery",
    "lateral-movement",
    "collection",
    "command-and-control",
    "exfiltration",
    "impact",
]


def safe_filename(name):
    """Convert a group name into a safe filename."""
    return re.sub(r"[^A-Za-z0-9._-]+", "_", name).strip("_")


def load_stix(path):
    with path.open(encoding="utf-8") as f:
        return json.load(f)["objects"]


def find_group(objects, name):
    name_l = name.lower()
    for o in objects:
        if o.get("type") == "intrusion-set":
            aliases = [a.lower() for a in o.get("aliases", [])]
            if o.get("name", "").lower() == name_l or name_l in aliases:
                return o
    return None


def group_techniques(objects, group_id):
    """Return list of technique STIX ids used by the group."""
    tech_ids = []
    for o in objects:
        if o.get("type") != "relationship":
            continue
        if o.get("relationship_type") != "uses":
            continue
        if not o.get("source_ref", "").endswith(group_id):
            continue
        target = o.get("target_ref", "")
        if "attack-pattern--" in target:
            tech_ids.append(target)
    return list(set(tech_ids))


def technique_info(objects, tech_id):
    for o in objects:
        if o.get("id") == tech_id:
            tactics = [
                p["phase_name"]
                for p in o.get("kill_chain_phases", [])
                if p.get("kill_chain_name") == "mitre-attack"
            ]
            ext = o.get("external_references", [{}])
            ext_id = "?"
            for r in ext:
                if r.get("source_name") == "mitre-attack":
                    ext_id = r.get("external_id", "?")
                    break
            return {
                "id": ext_id,
                "name": o.get("name", "?"),
                "description": (o.get("description") or "").split("\n")[0][:300],
                "tactics": tactics or ["unknown"],
            }
    return None


def sort_by_tactic(techniques):
    def key(t):
        tactic = t["tactics"][0]
        try:
            return TACTIC_ORDER.index(tactic)
        except ValueError:
            return len(TACTIC_ORDER)

    return sorted(techniques, key=key)


def build_plan(group_name, stix_path):
    objects = load_stix(stix_path)
    group = find_group(objects, group_name)
    if not group:
        raise SystemExit(f"Group not found: {group_name}")

    tech_ids = group_techniques(objects, group["id"])
    techs = [technique_info(objects, tid) for tid in tech_ids]
    techs = [t for t in techs if t]
    techs = sort_by_tactic(techs)

    aliases = ", ".join(group.get("aliases", []) or [])
    lines = [
        f"# Adversary Emulation Plan: {group['name']}",
        "",
        f"**Generated:** {date.today().isoformat()}  ",
        f"**Aliases:** {aliases or 'N/A'}  ",
        f"**Techniques:** {len(techs)}",
        "",
        "> **Authorized lab use only.** Run only in an isolated environment you own.",
        "",
        "## Execution Plan",
        "",
    ]

    for i, t in enumerate(techs, 1):
        lines.append(f"### {i}. {t['id']} — {t['name']}")
        lines.append(f"**Tactic:** {', '.join(t['tactics'])}  ")
        lines.append("")
        lines.append(t["description"] or "_No description._")
        lines.append("")
        lines.append("- [ ] Emulate in lab")
        lines.append("- [ ] Verify telemetry / detection")
        lines.append("")

    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser(
        description="Adversary Emulation Plan Builder (authorized lab use only)"
    )
    p.add_argument("--group", required=True, help="e.g. APT29, FIN7, Lazarus Group")
    p.add_argument("--stix", default=str(STIX_FILE), help="Path to enterprise-attack.json")
    p.add_argument("-o", "--output", default=None, help="Output markdown path")
    args = p.parse_args()

    plan = build_plan(args.group, Path(args.stix))

    if args.output:
        out = Path(args.output)
    else:
        out = Path(f"{safe_filename(args.group)}_plan.md")

    out.write_text(plan, encoding="utf-8")
    print(f"[+] Wrote {out} ({len(plan.splitlines())} lines)")


if __name__ == "__main__":
    main()