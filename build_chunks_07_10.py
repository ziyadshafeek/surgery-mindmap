# Build chunk-07 (surgery-t25..t28) and chunk-10 (surgery-t37..t42) mindmap JSON
# from ~/workspace/sessional-arena/data/topics.json plain text.
# Mechanical, lossless conversion: every blank-line block of the source text
# appears verbatim in the output, either as a node title or as a detail.
# No external API, no subagents, no invented content.
# Hierarchy: numbered "N. Title:" blocks = top-level sections;
# short single-line blocks ending in ':' = subheadings;
# "Label: rest" blocks = node titled Label with detail=rest;
# other blocks = leaf nodes with the full block as title.
import json, re, os

SRC = "/home/hatch/workspace/sessional-arena/data/topics.json"
OUTDIR = "/home/hatch/workspace/mindmap/surgery"

topics = json.load(open(SRC))
by = {t["id"]: t for t in topics}

def split_blocks(text):
    parts = re.split(r"\n\s*\n", text.strip())
    return [p.strip().replace("\n", " ") for p in parts if p.strip()]

def is_numbered_heading(block):
    return bool(re.match(r"^\d+\.\s+\S", block)) and block.endswith(":") and len(block) < 200

def is_heading(block):
    # single short line ending in ':' with no sentence-ending period before the colon
    return block.endswith(":") and len(block) < 160 and "." not in block[:-1].replace("e.g.", "").replace("i.e.", "")

def split_label(block):
    # "Label: rest" where Label is short, has no period, and rest is non-empty
    m = re.match(r"^([^:.]{2,90}):\s+(.+)$", block, re.S)
    if m and "." not in m.group(1) and len(m.group(2)) > 10:
        return m.group(1).strip(), m.group(2).strip()
    return None, None

def build_topic(tid):
    t = by[tid]
    blocks = split_blocks(t["text"])
    root = {"id": tid, "title": t["title"], "children": []}
    cur_section = None   # numbered top-level node
    cur_sub = None       # subheading node under current section
    def attach(node):
        nonlocal cur_section, cur_sub
        if cur_sub is not None:
            cur_sub.setdefault("children", []).append(node)
        elif cur_section is not None:
            cur_section.setdefault("children", []).append(node)
        else:
            root["children"].append(node)
    for b in blocks:
        if is_numbered_heading(b):
            cur_section = {"title": b[:-1].strip(), "children": []}
            root["children"].append(cur_section)
            cur_sub = None
            continue
        if is_heading(b):
            node = {"title": b[:-1].strip(), "children": []}
            if cur_section is not None:
                cur_section.setdefault("children", []).append(node)
            else:
                root["children"].append(node)
            cur_sub = node
            continue
        label, rest = split_label(b)
        if label:
            attach({"title": label, "detail": rest})
        else:
            attach({"title": b})
    # drop empty children lists for cleanliness (keep structure identical otherwise)
    def clean(n):
        if "children" in n and not n["children"]:
            del n["children"]
        for c in n.get("children", []):
            clean(c)
    clean(root)
    return root, blocks

def count_nodes(n):
    c = 1
    for ch in n.get("children", []):
        c += count_nodes(ch)
    return c

def coverage_check(root, blocks):
    dump = json.dumps(root, ensure_ascii=False)
    # normalise whitespace for comparison
    norm_dump = re.sub(r"\s+", " ", dump)
    missing = []
    for b in blocks:
        nb = re.sub(r"\s+", " ", b)
        # a block is covered if its full text, or its label and rest separately, appear
        label, rest = split_label(b)
        if nb in norm_dump:
            continue
        if label and re.sub(r"\s+", " ", label) in norm_dump and re.sub(r"\s+", " ", rest) in norm_dump:
            continue
        if is_numbered_heading(b) and re.sub(r"\s+", " ", b[:-1].strip()) in norm_dump:
            continue
        if is_heading(b) and re.sub(r"\s+", " ", b[:-1].strip()) in norm_dump:
            continue
        missing.append(b[:100])
    return missing

results = {}
for chunk_name, tids in [("chunk-07", ["surgery-t25", "surgery-t26", "surgery-t27", "surgery-t28"]),
                         ("chunk-10", ["surgery-t37", "surgery-t38", "surgery-t39", "surgery-t40", "surgery-t41", "surgery-t42"])]:
    data = []
    for tid in tids:
        root, blocks = build_topic(tid)
        missing = coverage_check(root, blocks)
        n = count_nodes(root)
        print(f"{tid}: source blocks={len(blocks)} source chars={len(by[tid]['text'])} nodes={n} missing_blocks={len(missing)}")
        for m in missing:
            print("  MISSING:", m)
        data.append(root)
    path = os.path.join(OUTDIR, chunk_name + ".json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"wrote {path}: {len(data)} topics, {sum(count_nodes(d) for d in data)} nodes")
    results[chunk_name] = data
print("DONE")
