# Builder for chunk-10.json (surgery-t37..t42). No external API used.
import json

def N(t, c=None, d=None):
    node = {"title": t}
    if d is not None:
        node["detail"] = d
    if c:
        node["children"] = c
    return node

t37 = {"id": "surgery-t37", "title": "3. Chapter 47: Plastic & Reconstructive Surgery (Remaining Topics)", "children": [
  N("Tissue Expansion", [
    N("Principle", d="A deflated silicone balloon expander is placed subcutaneously adjacent to a defect and serially inflated weekly with normal saline via a filling port."),
    N("How overlying skin expands", [
      N("Mechanical creep", d="Collagen fibre realignment and expulsion of interstitial water."),
      N("Biological creep / stress relaxation", d="Mitotic epidermal proliferation and dermal angiogenesis."),
      N("Surrounded by a vascular fibrous capsule", d="The expander becomes surrounded by a vascular fibrous capsule."),
    ]),
    N("Advantages & Indications", [
      N("Sensate skin of identical colour, texture, and hair-bearing quality", d="Provides sensate skin of identical colour, texture, and hair-bearing quality without a distant donor defect."),
      N("Ideal for scalp reconstruction", d="The only way to create new hair-bearing scalp."),
      N("Giant congenital melanocytic naevi"),
      N("Burn scar contractures"),
      N("Two-stage breast reconstruction"),
    ]),
  ]),
  N("Autologous Lipotransfer (Coleman Fat Grafting)", [
    N("Step 1 — Harvest", d="Low-pressure tumescent liposuction harvest (from abdomen/thigh)."),
    N("Step 2 — Centrifugation", d="Centrifugation (3000 rpm for 3 minutes) to separate oil and blood from viable adipocytes and adipose-derived stromal stem cells."),
    N("Step 3 — Reinjection", d="Micro-droplet reinjection via blunt cannulae into multiple tissue planes."),
    N("Uses", [
      N("Breast reconstruction contour defects"),
      N("Irradiated scars"),
      N("Parry–Romberg syndrome"),
    ]),
    N("~20–50% of grafted fat resorbs"),
    N("Rare risk: intravascular fat embolism"),
  ]),
  N("Microsurgery, Free Flap Monitoring & Medicinal Leech Therapy", [
    N("Free Flap Monitoring", [
      N("Keep the patient \"Warm, Wet and Comfortable\"", d="Warm, Wet (hyperdynamic normovolaemia), and Comfortable (pain-free to prevent catecholamine-induced vasospasm)."),
      N("Monitor hourly in the first 48 hours", d="Monitor colour, temperature, turgor, capillary refill, handheld/implantable Doppler signal, and pinprick bleeding."),
      N("Arterial Thrombosis (1/3 of failures)", d="Flap is pale/white, cool, flaccid/empty, absent capillary refill, and no bleeding on pinprick."),
      N("Venous Thrombosis/Congestion (2/3 of failures)", d="Flap is dark purple/dusky blue, tense/swollen, very brisk capillary refill (<1 s), and rapid dark venous oozing on pinprick."),
      N("Action", d="Release tight dressings/sutures at bedside and return immediately to theatre for microvascular exploration and revision anastomosis (>60% salvage rate if explored early)."),
    ]),
    N("Medicinal Leech Therapy (Hirudo medicinalis)", [
      N("Indication", d="Salvage of venously congested flaps or distal digital/ear replants where venous outflow is insufficient or no suitable vein exists for microvascular anastomosis."),
      N("Never used for", d="Arterial insufficiency or main-pedicle venous thrombosis that can be surgically revised."),
      N("Mechanism", d="Leech saliva contains hirudin (potent direct thrombin inhibitor), hyaluronidase, and histamine-like vasodilators; each leech ingests 5 mL of blood and the bite oozes up to 50–150 mL over several hours while neovascular venous channels grow in (takes 7–14 days)."),
      N("Mandatory Prophylaxis", d="The leech gut harbours the symbiotic Gram-negative bacterium Aeromonas hydrophila, which causes severe flap infection/necrosis; all patients must receive prophylactic Ciprofloxacin (quinolone) or Co-trimoxazole during leech therapy and regular haemoglobin monitoring."),
    ]),
  ]),
]}

t38 = {"id": "surgery-t38", "title": "4. Chapter 53: Oral Cavity Cancer (Remaining Topics)", "children": [
  N("Sentinel Lymph Node Biopsy (SLNB) in Early Oral Cancer", [
    N("Used in cT1–T2 N0 oral cavity SCC", d="Used as an alternative to upfront elective neck dissection."),
    N("Technique", d="Peritumoral injection of (99m)Tc-nanocolloid + ICG/blue dye identifies the first draining node(s), including unexpected contralateral drainage."),
    N("If positive", d="If positive on step-serial sectioning and immunohistochemistry, completion neck dissection is performed."),
  ]),
  N("Access Procedures for Oral Cancer Resection", [
    N("Transoral Resection", d="For anterior T1/T2 lesions."),
    N("Lip-Split Mandibulotomy", d="Paramedian stepped osteotomy in front of the mental foramen (preserving the inferior alveolar nerve) to swing the hemimandible laterally for posterior tongue/oropharyngeal tumours."),
    N("Visor Flap / Mandibular Lingual Release (\"Drop-down\" approach)", d="Subplatysmal apron incision releasing floor-of-mouth muscles from the inner mandible to drop the tongue into the neck without splitting the lip or bone."),
    N("Weber–Fergusson Incision", d="Divides upper lip philtrum, curves around the ala and lateral nasal wall, and extends infraorbitally to expose the maxilla for Maxillectomy."),
  ]),
  N("Virtual Surgical Planning (VSP), Zygomatic Implants & Immunotherapy", [
    N("VSP", d="Preoperative 3D CT CAD/CAM stereolithographic models and custom 3D-printed cutting guides for precise mandibular resection and fibula/scapula osteotomies."),
    N("ZIP (Zygomatic Implant Perforator) Flap", d="Immediate placement of long zygomatic dental implants perforating through a radial forearm/ALT soft-tissue free flap to provide immediate fixed dental rehabilitation after maxillectomy without needing a bony free flap."),
    N("Immunotherapy in Recurrent/Metastatic HNSCC", d="Anti-PD-1 immune checkpoint inhibitors (Pembrolizumab, Nivolumab) prolong overall survival in platinum-refractory or PD-L1-positive recurrent/metastatic oral SCC."),
  ]),
]}
