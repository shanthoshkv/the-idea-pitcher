"""Validate Claude Code plugin manifests, versions, changelog and skill frontmatter."""
import json, pathlib, re, sys

root = pathlib.Path(__file__).resolve().parents[1]
errs = []
plugin = json.loads((root / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
market = json.loads((root / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
entry = market["plugins"][0]
if entry["name"] != plugin["name"]:
    errs.append(f"marketplace plugin name {entry['name']!r} != plugin.json name {plugin['name']!r}")
if entry["version"] != plugin["version"]:
    errs.append(f"marketplace version {entry['version']!r} != plugin.json version {plugin['version']!r}")
log = (root / "CHANGELOG.md").read_text(encoding="utf-8")
if not re.search(rf"^## \[?{re.escape(plugin['version'])}\]?", log, re.M):
    errs.append(f"CHANGELOG.md has no section for {plugin['version']}")
for skill in sorted((root / "skills").glob("*/SKILL.md")):
    m = re.match(r"---\r?\n(.*?)\r?\n---", skill.read_text(encoding="utf-8"), re.S)
    n = re.search(r"^name:\s*(\S+)", m.group(1), re.M) if m else None
    if not n:
        errs.append(f"{skill.relative_to(root)}: missing frontmatter name")
    elif n.group(1) != skill.parent.name:
        errs.append(f"{skill.relative_to(root)}: name {n.group(1)!r} != folder {skill.parent.name!r}")
print("\n".join(errs) or f"OK: {plugin['name']} {plugin['version']}")
sys.exit(1 if errs else 0)
