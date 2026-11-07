# Build chunk-06 mindmap JSON for surgery-t21..t24 from topics.json text.
# Transcribed verbatim from source; no external LLM used.
import json, os

def N(title, children):
    return {"title": title, "children": children}

def L(title, detail=None):
    d = {"title": title}
    if detail:
        d["detail"] = detail
    return d

t21 = {
    "id": "surgery-t21",
    "title": "Q6.6: Thyroiditis & Lingual Thyroid",
    "children": [
        L("Covers: KU 22, TU"),
        N("1. Thyroiditis (Classification & Features)", [
            N("Hashimoto\u2019s Thyroiditis (Chronic Lymphocytic / Autoimmune Thyroiditis)", [
                L("Commonest cause of hypothyroidism in iodine-sufficient areas",
                  "Commonest cause of hypothyroidism in iodine-sufficient areas; Female:Male = 10\u201315:1 (ages 30\u201350)."),
                L("Pathology",
                  "Diffuse Hurthle/Askanazy cell metaplasia, lymphoid follicles with germinal centres, acinar destruction, and fibrosis."),
                L("Clinical Features",
                  "Firm, rubbery, diffusely enlarged, bosselated goitre; initially may have transient \u201cHashitoxicosis\u201d followed by permanent hypothyroidism (myxoedema). Predisposes to Primary Thyroid MALT Lymphoma and PTC."),
                L("Diagnosis",
                  "High titres of Anti-TPO (>90%) and Anti-Thyroglobulin antibodies, elevated TSH, and lymphocytic thyroiditis on FNAC."),
                L("Treatment",
                  "Lifelong Levothyroxine replacement (surgery only for compressive symptoms or suspected malignancy)."),
            ]),
            N("De Quervain\u2019s Thyroiditis (Subacute Granulomatous / Viral Thyroiditis)", [
                L("Follows an upper respiratory viral infection in young women."),
                L("Presents with",
                  "Acute painful, tender thyroid swelling radiating to the jaw/ears, fever, malaise, markedly raised ESR, absent thyroid antibodies, and very low radioiodine uptake despite transient hyperthyroidism (due to release of preformed hormone from disrupted follicles)."),
                L("Self-limiting; treated with NSAIDs or Prednisolone (10\u201320 mg/day tapered over 4 weeks)."),
            ]),
            N("Riedel\u2019s Thyroiditis (Invasive Fibrous Thyroiditis)", [
                L("Rare IgG4-related fibroinflammatory disorder",
                  "Dense woody fibrous tissue replaces the thyroid and invades through the capsule into strap muscles, carotid sheath, RLN, parathyroids, and trachea (associated with retroperitoneal and mediastinal fibrosis)."),
                L("Mimics anaplastic carcinoma (stony hard, fixed goitre with stridor)."),
                L("Treatment",
                  "Core biopsy/wedge isthmusectomy to decompress the trachea, high-dose corticosteroids, Tamoxifen, and levothyroxine."),
            ]),
        ]),
        N("2. Lingual Thyroid", [
            L("Complete failure of descent of the median thyroid anlage",
              "Leaves a rounded, reddish-blue mass at the base of the tongue (foramen caecum); in 70% of cases, it is the only functioning thyroid tissue present."),
            L("Causes dysphagia, dysphonia, bleeding, or airway obstruction (enlarges during puberty/pregnancy)."),
            L("Confirmed by (99m)Tc / \u00b9\u00b2\u00b3I scan."),
            L("Treated with suppressive Levothyroxine (or \u00b9\u00b3\u00b9I ablation / transoral excision if obstructive)."),
        ]),
    ],
}

t22 = {
    "id": "surgery-t22",
    "title": "Q7.1: Primary Hyperparathyroidism (Parathyroid Adenoma), Sestamibi Scan & Hypocalcaemia",
    "children": [
        L("Covers: TU, RGU"),
        N("1. Surgical Anatomy & Physiology", [
            L("Four glands (30 mg each, \u201cPortland brick\u201d yellow-brown colour); all four are supplied by the Inferior Thyroid Artery."),
            L("Superior Parathyroids",
              "Develop from the 4th pharyngeal pouch; constant position (80% lie within a 2 cm circle centred 1 cm above the intersection of the inferior thyroid artery and RLN at the cricothyroid junction)."),
            L("Inferior Parathyroids",
              "Develop from the 3rd pharyngeal pouch along with the thymus (longer descent = more variable position; >50% lie near the lower pole of the thyroid or within the thyrothymic tract)."),
            N("PTH Action: Increases serum Ca\u00b2\u207a and decreases serum PO\u2084\u00b3\u207b by:", [
                L("(i) stimulating osteoclast bone resorption"),
                L("(ii) increasing distal renal tubular Ca\u00b2\u207a reabsorption and proximal tubular phosphate excretion"),
                L("(iii) activating renal 1\u03b1-hydroxylase to convert 25(OH)D \u2192 1,25(OH)\u2082D\u2083 (increasing intestinal Ca\u00b2\u207a absorption)"),
            ]),
        ]),
        N("2. Etiology & Pathology of Primary Hyperparathyroidism (PHPT)", [
            L("Single Parathyroid Adenoma: 80\u201385% (double adenoma in 2\u20134%)."),
            L("Four-Gland Hyperplasia: 15% (associated with MEN 1, MEN 2A, MEN 4, and chronic Lithium therapy)."),
            L("Parathyroid Carcinoma: 1%",
              "Associated with HRPT2/CDC73 gene mutation [loss of parafibromin staining] and Hyperparathyroidism\u2013Jaw Tumour [HPT-JT] syndrome; presents with palpable neck mass and severe hypercalcaemia >3.5 mmol/L."),
        ]),
        N("3. Clinical Features", [
            L("Asymptomatic Hypercalcaemia (70\u201380% in modern practice)",
              "Detected incidentally on routine biochemistry or DEXA scan."),
            N("Classical Symptomatic Pentad: \u201cBones, Stones, Abdominal Groans, Psychic Moans, and Fatigue Overtones\u201d", [
                L("Skeletal",
                  "Osteopenia/osteoporosis (preferentially affecting cortical bone of the distal third of the radius), subperiosteal bone resorption of phalanges, tapering of distal clavicles, \u201csalt and pepper\u201d skull, and Osteitis fibrosa cystica (Brown tumours)."),
                L("Renal (commonest symptomatic manifestation \u2014 15\u201320%)",
                  "Recurrent calcium oxalate/phosphate renal calculi, nephrocalcinosis, polyuria/polydipsia."),
                L("Gastrointestinal",
                  "Peptic ulceration (calcium stimulates gastrin release), acute/chronic pancreatitis, constipation, cholelithiasis."),
                L("Neuropsychiatric & Cardiovascular",
                  "Depression, lethargy, confusion, proximal muscle weakness, hypertension, shortened QT interval, and band keratopathy of the cornea."),
            ]),
        ]),
        N("4. Diagnosis & Localisation Studies", [
            N("1. Biochemical Diagnosis (Mandatory First Step \u2014 \u201cImaging never diagnoses PHPT\u201d)", [
                L("Elevated total and ionised serum Calcium + inappropriately elevated or unsuppressed intact PTH."),
                L("Low serum Phosphate, elevated serum alkaline phosphatase, normal vitamin D, and 24-hour urinary calcium >400 mg/day",
                  "24-hour urinary calcium >400 mg/day (with urinary calcium:creatinine clearance ratio >0.02; a ratio <0.01 indicates Familial Hypocalciuric Hypercalcaemia [FHH], where surgery is contraindicated)."),
            ]),
            N("2. Preoperative Localisation Studies (To guide Minimally Invasive Parathyroidectomy)", [
                N("Technetium-99m Sestamibi ((99m)Tc-MIBI) Scintigraphy with SPECT (Short Note [TU])", [
                    L("Principle",
                      "Sestamibi is a lipophilic cationic radiotracer that concentrates in mitochondria-rich oxyphil cells of hyperfunctioning parathyroid adenomas. On dual-phase imaging (15 min and 2 hours post-injection), normal thyroid tissue washes out the tracer rapidly, whereas a parathyroid adenoma shows delayed retention/persistent hot spot (Sensitivity 79%, PPV 91%)."),
                ]),
                L("High-Resolution Neck Ultrasonography",
                  "Identifies oval hypoechoic adenomas posterior to the thyroid and evaluates coexisting thyroid nodules (Sensitivity 76%, PPV 93%)."),
                L("Four-Dimensional Computed Tomography (4D-CT)",
                  "Uses non-contrast, arterial, and delayed venous phases (4th dimension = time/perfusion); parathyroid adenomas show rapid arterial enhancement and rapid washout compared with lymph nodes or thyroid. Ideal when USG and Sestamibi are discordant or negative."),
            ]),
        ]),
        N("5. Management", [
            N("Indications for Surgery: All symptomatic patients, and Asymptomatic patients meeting any of the NIH/Fourth International Workshop Criteria (Table 56.2)", [
                L("Serum calcium >0.25 mmol/L (>1.0 mg/dL) above the upper limit of normal."),
                L("Skeletal: DEXA T-score \u2264 -2.5 at lumbar spine, hip, or distal 1/3 radius, or vertebral fracture."),
                L("Renal: eGFR <60 mL/min, 24-hour urinary calcium >400 mg/day, or nephrolithiasis/nephrocalcinosis on imaging."),
                L("Age <50 years."),
            ]),
            N("Surgical Approaches", [
                L("Concordant USG + Sestamibi (Single Adenoma)",
                  "Minimally Invasive (Focused) Parathyroidectomy (MIP) through a <3 cm incision. Intraoperative PTH (ioPTH) monitoring using the Miami Criteria (a >50% drop in plasma PTH from the highest pre-excision value at 10 minutes post-excision into the normal range confirms cure, as PTH half-life is 3\u20135 minutes)."),
                L("Discordant/Negative Imaging or Familial/Multigland Disease (MEN 1/2A)",
                  "Bilateral Four-Gland Neck Exploration with either Subtotal (3(1/2)-gland) Parathyroidectomy (leaving half of the most normal inferior gland marked with a non-absorbable clip/suture) or Total Parathyroidectomy with Forearm Autotransplantation (into brachioradialis pockets) + Cervical Thymectomy."),
            ]),
            N("Medical Management (for unfit patients or Hypercalcaemic Crisis [Ca\u00b2\u207a >3.5 mmol/L])", [
                L("Acute Crisis",
                  "Aggressive IV 0.9% Normal Saline hydration (200\u2013500 mL/h) + loop diuretic (Furosemide after volume restoration) + IV Bisphosphonates (Zoledronic acid/Pamidronate) + Calcitonin."),
                L("Chronic Medical Therapy",
                  "Cinacalcet (calcimimetic that increases sensitivity of the parathyroid Calcium-Sensing Receptor [CaSR]), Bisphosphonates, or Denosumab."),
            ]),
        ]),
        N("6. Trousseau\u2019s Sign & Hypocalcaemia [RGU, TU]", [
            L("Trousseau\u2019s Sign of Latent Tetany",
              "Inflating a sphygmomanometer cuff on the upper arm 20 mmHg above systolic blood pressure for 3 minutes induces ischaemia of the ulnar/median nerves, provoking carpopedal spasm (\u201cobstetrician\u2019s hand\u201d / main d\u2019accoucheur): flexion at the wrist and metacarpophalangeal joints, extension of the interphalangeal joints, and adduction of the thumb (94% sensitive and 99% specific for hypocalcaemia)."),
        ]),
    ],
}

t23 = {
    "id": "surgery-t23",
    "title": "Q7.2: Phaeochromocytoma, Neuroblastoma & Multiple Endocrine Neoplasia (MEN) Syndromes",
    "children": [
        L("Covers: KU 24, 15, RGU, TU \u2014 Short Answers"),
        N("1. Phaeochromocytoma & Paraganglioma (PPGL) [KU 24, 15, TU]", [
            L("Definition",
              "Neuroectodermal catecholamine-secreting tumours arising from chromaffin cells of the adrenal medulla (Phaeochromocytoma \u2014 PCC) or extra-adrenal autonomic ganglia (Paraganglioma \u2014 PGL, commonest at the Organ of Zuckerkandl near the inferior mesenteric artery origin)."),
            L("Traditional \u201cRule of 10s\u201d (and Modern Genetics)",
              "~10% extra-adrenal, 10% bilateral, 10% malignant, 10% in children. Today, 25\u201330% are hereditary: MEN 2A/2B (RET gene), Von Hippel\u2013Lindau (VHL) disease, Neurofibromatosis type 1 (NF-1), and Hereditary PGL Syndromes (SDHB, SDHD succinate dehydrogenase mutations \u2014 SDHB carries a 34\u201397% risk of malignancy)."),
            L("Clinical Features",
              "Classic paroxysmal triad of episodic throbbing headache, profuse sweating, and palpitations (90% specific in the presence of an adrenal mass), with sustained or paroxysmal hypertension, pallor, anxiety, tremor, and hyperglycaemia. Precipitated by exercise, abdominal palpation, anaesthetic induction, or unopposed \u03b2-blockers."),
            N("Stepwise Diagnosis & Management", [
                L("Biochemical Confirmation First",
                  "Elevated Plasma Free Metanephrines (99% sensitive) and/or 24-hour Urinary Fractionated Metanephrines (97% sensitive). (Biopsy of a suspected PCC is strictly contraindicated)."),
                L("Anatomical & Functional Localisation",
                  "Contrast CT or MRI abdomen (shows a vascular adrenal mass with central necrosis, bright \u201clight-bulb\u201d T2 hyperintensity on MRI, >10 HU on non-contrast CT)."),
                L("Functional imaging with \u00b9\u00b2\u00b3I-MIBG (meta-iodobenzylguanidine) scintigraphy, \u2076\u2078Ga-DOTATATE PET-CT, or \u00b9\u2078F-FDOPA PET for extra-adrenal, bilateral, or metastatic disease."),
                N("Mandatory Preoperative Pharmacological Preparation (Reduces mortality from 45% to <3%)", [
                    L("Step 1 \u2014 \u03b1-Adrenergic Blockade",
                      "Start non-competitive irreversible \u03b1-blocker Phenoxybenzamine (10 mg BD, increased by 10\u201320 mg/day up to 100\u2013160 mg/day for 10\u201314 days) or selective \u03b1\u2081-blocker Doxazosin alongside high oral salt and fluid intake to expand contracted intravascular volume until orthostatic hypotension and nasal stuffiness are achieved."),
                    L("Step 2 \u2014 \u03b2-Adrenergic Blockade (Propranolol / Atenolol)",
                      "Added ONLY AFTER adequate \u03b1-blockade is established to control reflex tachycardia/arrhythmias. (Giving a \u03b2-blocker first abolishes \u03b2\u2082-mediated skeletal muscle vasodilation, leaving unopposed \u03b1\u2081-vasoconstriction \u2192 fatal hypertensive crisis and pulmonary oedema)."),
                ]),
                L("Surgical Treatment",
                  "Laparoscopic Adrenalectomy (transperitoneal or posterior retroperitoneoscopic approach) with early ligation of the adrenal vein and minimal tumour manipulation (Open resection for tumours >8\u201310 cm or locally invasive malignant PCC). Watch for sudden hypotension and hypoglycaemia after adrenal vein ligation."),
            ]),
        ]),
        N("2. Multiple Endocrine Neoplasia (MEN) Syndromes [KU 24, RGU, TU] (Table surgery-tbl-004)", [
            N("MEN Type 1 (Wermer\u2019s Syndrome)", [
                L("Inheritance & Gene",
                  "Autosomal Dominant; MEN1 tumour suppressor gene (Chromosome 11q13) encoding Menin."),
                N("Components \u2014 \u201cThe 3 P\u2019s\u201d", [
                    L("Parathyroid Hyperplasia (95%) \u2014 earliest & commonest."),
                    L("Pancreatic/Duodenal Islet Cell NETs (30\u201380%)",
                      "Non-functioning P-NETs, Gastrinoma (ZES), Insulinoma, VIPoma, Glucagonoma."),
                    L("Pituitary Adenomas (15\u201350%)",
                      "Prolactinoma (60%), GH (acromegaly), ACTH."),
                    L("Others: Adrenocortical tumours, foregut carcinoids, lipomas, facial angiofibromas."),
                ]),
            ]),
            N("MEN Type 2A (Sipple\u2019s Syndrome)", [
                L("Inheritance & Gene",
                  "Autosomal Dominant; RET proto-oncogene (Chromosome 10q11) encoding a transmembrane tyrosine kinase receptor (Codon 634 commonest)."),
                N("Components", [
                    L("Medullary Thyroid Carcinoma (90\u2013100%) \u2014 main determinant of survival."),
                    L("Phaeochromocytoma (10\u201370%) \u2014 often bilateral."),
                    L("Parathyroid Hyperplasia (20\u201330%) \u2014 mild/asymptomatic."),
                    L("Variants: Familial MTC (FMTC), MEN 2A with cutaneous lichen amyloidosis or Hirschsprung\u2019s disease."),
                ]),
            ]),
            N("MEN Type 2B", [
                L("Inheritance & Gene",
                  "Autosomal Dominant (50% de novo); RET proto-oncogene (Codon 918 commonest)."),
                N("Components", [
                    L("Medullary Thyroid Carcinoma (100%) \u2014 very aggressive, infancy onset."),
                    L("Phaeochromocytoma (50\u201360%)."),
                    L("Mucosal Neuromas (100%) of lips, tongue, eyelids & Intestinal Ganglioneuromatosis."),
                    L("Marfanoid Habitus."),
                    L("Note: Does NOT develop hyperparathyroidism."),
                ]),
            ]),
        ]),
        N("3. Neuroblastoma [TU]", [
            L("Commonest extracranial solid malignancy of infancy/childhood (75% present <2 years of age)",
              "Arises from neural crest neuroblasts in the adrenal medulla (40%) or sympathetic chain."),
            L("Clinical Features",
              "Large irregular abdominal mass that crosses the midline (unlike Wilms\u2019 tumour), weight loss, periorbital ecchymoses (\u201craccoon eyes\u201d from orbital metastases), bone pain, Pepper syndrome (massive liver metastases), Hutchinson syndrome (skull/bone metastases), or opsoclonus\u2013myoclonus."),
            L("Diagnosis & Prognosis",
              "Elevated 24-hour urinary VMA / HVA / metanephrines; CT/MRI + \u00b9\u00b2\u00b3I-MIBG scan; bone marrow aspirate and biopsy (small round blue cells with Homer-Wright rosettes). MYCN oncogene amplification (present in 25%), age >18 months, and 1p/11q deletion predict poor prognosis. Treated by risk-stratified surgery \u00b1 multiagent chemotherapy."),
        ]),
    ],
}

t24 = {
    "id": "surgery-t24",
    "title": "Q8.1: Triple Assessment, BI-RADS, Benign Breast Diseases (ANDI, Mastalgia, Fibroadenoma, Phyllodes Tumour, Breast Abscess & Nipple Discharge)",
    "children": [
        L("Covers: KU 24, 23, 22, 21, 20, 19, 17, 16, RGU, TU \u2014 Short Essays & Short Answers"),
        N("1. Triple Assessment of a Breast Lump [KU 24, 23, 22, 21, 19]", [
            L("Every patient presenting with a breast symptom/lump is evaluated systematically by combining three modalities (Diagnostic accuracy and Positive Predictive Value >99.9% when concordant)."),
            L("Clinical Assessment",
              "Detailed history (duration, pain, nipple discharge, menstrual/obstetric history, family history) + systematic bimanual Clinical Breast Examination (inspection in 4 postures + palpation of all four quadrants, subareolar region, axillary tail, and regional lymph nodes using the flat pads of the fingers)."),
            N("Radiological Imaging", [
                L("Ultrasonography (First-line in women <35\u201340 years with dense breasts)",
                  "Distinguishes cystic from solid lesions and evaluates axillary lymph nodes."),
                L("Mammography (First-line in women \u2265 35\u201340 years)",
                  "Two views (Craniocaudal [CC] and Mediolateral Oblique [MLO]) using low-voltage, high-amperage X-rays (~ 1 mGy radiation). Mammographic signs of malignancy: irregular spiculated mass, clustered pleomorphic/branching microcalcifications, and architectural distortion."),
            ]),
            L("Pathological Tissue Sampling",
              "Image-guided Large-Diameter Core Needle Biopsy (14G Tru-Cut needle) under local anaesthesia (preferred over FNAC as it distinguishes in situ from invasive cancer and allows ER, PR, HER2/neu, and Ki-67 immunohistochemistry)."),
        ]),
        N("2. BI-RADS (Breast Imaging Reporting and Data System) Grading (Table 58.1) [KU 17]", [
            L("BI-RADS 0: Incomplete assessment \u2192 Requires additional imaging."),
            L("BI-RADS 1: Negative / Normal (0% malignancy) \u2192 Routine screening."),
            L("BI-RADS 2: Benign finding (e.g., simple cyst, calcified fibroadenoma; 0% malignancy) \u2192 Routine screening."),
            L("BI-RADS 3: Probably benign (e.g., typical fibroadenoma; \u2264 2% malignancy) \u2192 Short-interval (6-month) imaging follow-up."),
            L("BI-RADS 4: Suspicious abnormality (4a: Low 2\u201310%; 4b: Moderate 10\u201350%; 4c: High 50\u201395% malignancy) \u2192 Core needle biopsy indicated."),
            L("BI-RADS 5: Highly suggestive of malignancy (\u2265 95% probability) \u2192 Biopsy mandatory."),
            L("BI-RADS 6: Known biopsy-proven malignancy prior to definitive therapy."),
        ]),
        N("3. ANDI (Aberrations of Normal Development and Involution) Concept [KU 22, RGU, TU]", [
            L("Formulated by Hughes, Mansel & Webster (Cardiff Breast Clinic) to replace confusing historical terms like \u201cfibroadenosis\u201d or \u201cfibrocystic disease\u201d.",
              "Most benign breast conditions arise from physiological responses of the Terminal Ductal Lobular Unit (TDLU) to cyclical hormones across three reproductive phases (Table surgery-tbl-005)."),
            N("1. Early Reproductive / Lobular Development (15\u201325 years)", [
                L("Normal Physiological Process: Stromal and lobular development; nipple eversion."),
                L("Benign Aberration (ANDI): Fibroadenoma, Adolescent hypertrophy, Nipple inversion."),
                L("Progression to Disease State: Giant fibroadenoma (>5 cm), Gigantomastia, Subareolar abscess / Mammary duct fistula."),
            ]),
            N("2. Mature Reproductive / Cyclical Change (25\u201340 years)", [
                L("Normal Physiological Process: Cyclical hormonal proliferation and secretion."),
                L("Benign Aberration (ANDI): Cyclical Mastalgia and diffuse Benign Nodularity (formerly \u201cfibroadenosis\u201d)."),
                L("Progression to Disease State: Incapacitating mastalgia."),
            ]),
            N("3. Involution (35\u201355 years)", [
                L("Normal Physiological Process: Lobular involution, stromal replacement, ductal dilation, epithelial turnover."),
                L("Benign Aberration (ANDI): Macrocysts, Sclerosing adenosis, Duct ectasia, Simple epithelial hyperplasia."),
                L("Progression to Disease State: Periductal mastitis, Intracystic papilloma, Epithelial hyperplasia with atypia (ADH / ALH \u2014 RR for cancer 4\u20135x)."),
            ]),
        ]),
        N("4. Mastalgia (Breast Pain) (Table 58.2) [KU 22, TU]", [
            N("Classification", [
                L("Cyclical Mastalgia (2/3 of cases)",
                  "Bilateral diffuse heaviness/pain (worst in upper outer quadrants) starting at ovulation (day 14), peaking premenstrually, and relieved by menses."),
                L("Non-Cyclical Mastalgia",
                  "Unilateral, well-localised (\u201ctrigger spot\u201d) pain unrelated to menses, occurring pre- or postmenopausally (due to duct ectasia, periductal mastitis, cysts, or sclerosing adenosis)."),
                L("Extramammary (Referred) Pain",
                  "Tietze\u2019s syndrome (painful costochondral junction), lateral chest wall muscular pain, angina, or cervical radiculopathy."),
            ]),
            N("Management", [
                L("Perform Triple Assessment to exclude cancer \u2192 Firm Reassurance (resolves symptoms in 85% of women) + record a Daily Visual Analogue Scale (VAS) Breast Pain Chart for 1 month."),
                L("First-Line Conservative Measures",
                  "Well-fitting supportive sports brassiere, dietary Flaxseed (30 g/day) or Evening Primrose Oil, and Topical NSAID gel (Diclofenac / Piroxicam QDS)."),
                N("Second-Line Systemic Therapy (for severe pain VAS >3/10)", [
                    L("Ormeloxifene (Centchroman) 30 mg twice weekly for 3\u20136 months (selective oestrogen receptor modulator widely used in India for mastalgia and benign nodularity/fibroadenoma)."),
                    L("Low-dose Tamoxifen (10 mg daily for 3\u20136 months)."),
                    L("Danazol (100\u2013200 mg daily) or LHRH agonists (Goserelin) for refractory cases."),
                ]),
            ]),
        ]),
        N("5. Fibroadenoma (\u201cBreast Mouse\u201d) [RGU, TU]", [
            L("Arises from hyperplasia of a single lobule (TDLU) in women aged 15\u201325 years.",
              "Firm, smooth, well-circumscribed, painless lump (1\u20133 cm) that slips readily beneath the examining fingers (\u201cbreast mouse\u201d)."),
            L("Pathology: Benign proliferation of both stromal fibrous tissue and epithelial ducts (pericanalicular vs intracanalicular types)."),
            L("Management",
              "In women <25 years with typical clinical/USG features (BI-RADS 3), conservative observation or medical therapy with Ormeloxifene is safe. Indications for Surgical Excision (Enucleation): Age >30 years, size >5 cm (Giant fibroadenoma \u2014 excised via a submammary Gaillard Thomas incision), rapid growth, suspicious USG features, complex histology, or patient anxiety."),
        ]),
        N("6. Phyllodes Tumour (Serocystic Disease of Brodie / formerly Cystosarcoma Phyllodes) [KU 24, 23, 20, RGU, TU]", [
            N("Pathology", [
                L("A fibroepithelial tumour with leaf-like (Greek: phyllon = leaf) clefts lined by epithelium and a hypercellular mesenchymal spindle-cell stroma. Classified by stromal atypia, margins, and mitotic count into:"),
                L("Benign (<4 mitoses/10 HPF)."),
                L("Borderline (4\u20139 mitoses/10 HPF)."),
                L("Malignant (\u2265 10 mitoses/10 HPF, sarcomatous stromal overgrowth, infiltrative margins)."),
            ]),
            N("Clinical Features", [
                L("Occurs in women aged 35\u201355 years (10\u201320 years older than fibroadenoma)."),
                L("Presents as a rapidly growing, large, painless, bosselated mass with stretched, shiny overlying skin and prominent engorged subcutaneous veins."),
                L("Despite massive size and occasional pressure necrosis/ulceration of the skin, it remains mobile over the chest wall, does not cause nipple retraction/peau d\u2019orange, and rarely metastasises to axillary lymph nodes (malignant phyllodes spreads haematogenously to the lungs)."),
            ]),
            N("Management", [
                L("Wide Local Excision with a 1\u20132 cm margin of normal breast tissue (simple enucleation is strictly contraindicated due to high local recurrence)."),
                L("Simple Mastectomy (without axillary lymph node dissection) is indicated for massive tumours (unfavourable tumour-to-breast ratio), recurrent tumours, or malignant phyllodes tumours, followed by adjuvant radiotherapy for malignant/recurrent cases."),
            ]),
        ]),
        N("7. Breast Abscess & Antibioma [KU 19, RGU, TU]", [
            N("Lactational Breast Abscess", [
                L("Caused by Staphylococcus aureus entering via a cracked nipple or milk stasis (peaks in the first month of primiparous lactation and at weaning)."),
                L("Management",
                  "Support the breast, continue 2-hourly breastfeeding/expression, give anti-staphylococcal antibiotics (Flucloxacillin / Co-amoxiclav / Erythromycin), and perform Ultrasound-Guided Needle Aspiration (for abscesses <3 cm) or Ultrasound-Guided Percutaneous Suction Catheter Drainage (for abscesses >3 cm or >30 mL pus) with saline irrigation."),
                L("(Open incision and drainage is avoided unless skin is necrotic, as it causes ugly scars and milk fistulae)."),
            ]),
            L("Non-Lactational (Subareolar) Abscess",
              "Occurs in young female smokers due to Periductal Mastitis and squamous metaplasia of major lactiferous ducts; ruptures at the areolar margin to form a Mammary Duct Fistula with transverse slit-like nipple retraction. Treated with antibiotics + metronidazole, smoking cessation, and Hadfield\u2019s Major Duct Excision once acute sepsis settles."),
            N("Antibioma (Short Note [KU 19])", [
                L("When a formed breast abscess is inappropriately treated with prolonged courses of antibiotics without draining the pus, the pus becomes sterile and inspissated, surrounded by a thick, dense, fibrous reactive wall."),
                L("Clinically, it forms a painless, hard, fixed breast lump with skin tethering that closely mimics breast carcinoma. Diagnosed by USG and core biopsy; treated by evacuation or surgical excision."),
            ]),
        ]),
        N("8. Evaluation & Management of Abnormal Nipple Discharge [KU 16, RGU, TU]", [
            L("Pathological Discharge (\u201cThe 4 S\u2019s\u201d)",
              "Single-duct, Spontaneous, Serous (clear/straw-coloured) or Sanguineous (bloodstained) discharge (Summary Box 58.2)."),
            N("Causes by Character of Discharge", [
                L("Bloodstained or Serous (Single Duct)",
                  "Solitary Intraductal Papilloma (commonest cause \u2014 located within 5 cm of the nipple), Ductal Carcinoma in situ (DCIS) / Invasive Ductal Carcinoma, or Duct ectasia."),
                L("Thick, Multicoloured (Green, Black, Muddy, or Cheesy from Multiple Ducts)",
                  "Duct Ectasia (benign disorder of involution; dilated subareolar ducts >3 mm filled with inspissated debris)."),
                L("Purulent Discharge: Periductal Mastitis."),
                L("Bilateral Milky Discharge (Galactorrhoea)",
                  "Hyperprolactinaemia (prolactinoma, hypothyroidism, or dopamine-antagonist drugs like metoclopramide, haloperidol, chlorpromazine)."),
                L("Surface Serosanguineous Exudate: Paget\u2019s Disease of the Nipple or eczema."),
            ]),
            N("Evaluation & Management", [
                L("Triple Assessment",
                  "Clinical examination (locate the \u201ctrigger point\u201d quadrant that expresses discharge on radial pressure), High-Resolution Subareolar Ultrasonography (85% accuracy in visualising intraductal papillomas or dilated ducts) + Mammography, and core biopsy if any mass is present. (Nipple discharge cytology has poor sensitivity and is largely abandoned)."),
                N("Surgical Treatment (Indicated for persistent single-duct bloody/serous discharge, especially in women >40 years)", [
                    L("Single-Duct Discharge: Microdochectomy",
                      "Cannulate the offending duct orifice with a lacrimal probe or nylon suture \u2192 circumareolar incision \u2192 excise a 2\u20135 cm length of the single terminal lactiferous duct for histology."),
                    L("Multiduct Discharge / Severe Duct Ectasia: Hadfield\u2019s Operation (Radical Subareolar Major Mammary Duct Excision)",
                      "Excision of the entire cone of major lactiferous ducts beneath the nipple\u2013areola complex."),
                ]),
            ]),
        ]),
        N("9. Gynaecomastia [KU 17, RGU, TU]", [
            L("Definition",
              "Benign proliferation of glandular ductal and stromal tissue of the male breast (forming a firm, rubbery, mobile subareolar disc >2 cm), resulting from an increased Oestrogen-to-Androgen ratio. Must be differentiated from pseudogynaecomastia (fatty deposition in obesity without a palpable subareolar fibrous disc) and male breast cancer (eccentric, painless, hard, fixed mass with nipple retraction/ulceration)."),
            N("Etiology", [
                L("Physiological (Trimodal peaks)",
                  "Neonatal (transplacental maternal oestrogens), Pubertal (ages 12\u201315; regresses spontaneously within 1\u20132 years in 90%), and Senescent (>60 years due to falling free testosterone and peripheral aromatisation of androgens in adipose tissue)."),
                N("Pathological", [
                    L("Drugs (\u201cDISCO\u201d)",
                      "Digoxin, Isoniazid, Spironolactone (commonest), Cimetidine, Oestrogens/anti-androgens (Finasteride, Flutamide, Ketoconazole, Calcium channel blockers, Marijuana, Anabolic steroids)."),
                    L("Liver Cirrhosis (impaired hepatic metabolism of oestrogens)."),
                    L("Chronic Renal Failure & Thyrotoxicosis."),
                    L("Testicular Deficiency (Hypogonadism)",
                      "Klinefelter\u2019s syndrome (47,XXY) (carries a 20\u201350-fold increased risk of male breast cancer), mumps orchitis, cryptorchidism."),
                    L("Hormone-Secreting Tumours",
                      "Leydig/Sertoli cell testicular tumours, hCG-secreting germ cell tumours, adrenocortical feminising tumours."),
                ]),
            ]),
            L("Simon\u2019s Classification",
              "Grade I: Minor enlargement, no skin excess; Grade IIa: Moderate enlargement, no skin excess; Grade IIb: Moderate enlargement with minor skin excess; Grade III: Gross enlargement with marked ptosis and skin excess (resembling a female breast)."),
            N("Management", [
                L("Exclude testicular tumour (palpate testes + scrotal USG), check LFTs, RFTs, TFTs, serum Testosterone, Oestradiol, LH, FSH, \u03b2-hCG, and Prolactin, and perform breast USG/mammogram (+ core biopsy if suspicious of cancer)."),
                L("Medical: Withdraw offending drugs; reassure in pubertal cases; trial of Tamoxifen (10\u201320 mg daily for 3\u20136 months) or Danazol gives relief in painful, recent-onset florid gynaecomastia."),
                L("Surgical (for longstanding fibrotic gynaecomastia >12 months or cosmetic distress)",
                  "Subcutaneous Mastectomy (Webster\u2019s intra-areolar incision) preserving a 5 mm subareolar button to prevent \u201csaucer deformity\u201d, combined with Liposuction (or concentric skin reduction for Grade III)."),
            ]),
        ]),
    ],
}

data = [t21, t22, t23, t24]

def count_nodes(node):
    n = 1
    for c in node.get("children", []):
        n += count_nodes(c)
    return n

total = sum(count_nodes(t) for t in data)
per_topic = {t["id"]: count_nodes(t) for t in data}

os.makedirs("/home/hatch/workspace/mindmap/surgery", exist_ok=True)
with open("/home/hatch/workspace/mindmap/surgery/chunk-06.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("topics:", [t["id"] for t in data])
print("nodes per topic:", per_topic)
print("total nodes:", total)
