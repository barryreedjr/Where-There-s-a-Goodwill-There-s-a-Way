
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Find Your Way — Goodwill Gulf Coast", page_icon="🧭", layout="centered")

# --- Theme-y header ---
st.markdown("# 🧭 Find Your Way")
st.caption("A text-based mini‑adventure to match you with Goodwill Gulf Coast programs.")

# --- Program catalog (editable) ---
PROGRAMS = {
    # Employment
    "job_training": {
        "name": "Job Training & Placement Services",
        "areas": ["AL", "FL"],
        "who": "Anyone seeking job skills and help with resumes, applications, and interviews.",
        "link": "https://www.goodwillgulfcoast.org/programs-and-services/employment/",
        "contact": [
            {"label":"AL (Mobile & others)", "phone":"(251) 300-6278", "email":"mcmakenoc@goodwillgc.org"},
            {"label":"AL (Baldwin County)", "phone":"(251) 210-1333", "email":"spanishfortoc@goodwillgc.org"},
            {"label":"FL (Escambia/Santa Rosa)", "phone":"(850) 434-0032", "email":"oliveoc@goodwillgc.org"},
            {"label":"FL (Okaloosa)", "phone":"(850) 243-7118", "email":"fortwaltonoc@goodwillgc.org"},
        ],
    },
    "jobs_at_goodwill": {
        "name": "Jobs at Goodwill",
        "areas": ["AL", "FL"],
        "who": "Apply to work in our stores, e‑commerce, or mission services.",
        "link": "https://www.goodwillgulfcoast.org/programs-and-services/employment/",
        "contact": [],
    },
    "wtc_abilityone": {
        "name": "Work Training Center & AbilityOne (referral)",
        "areas": ["AL"],
        "who": "Individuals with disabilities referred by the Alabama Dept. of Rehabilitation Services.",
        "link": "https://www.goodwillgulfcoast.org/programs-and-services/employment/",
        "contact": [],
    },

    # Education
    "adult_education": {
        "name": "Adult Education / GED Preparation",
        "areas": ["AL"],
        "who": "Adults seeking basic skill remediation, literacy, or GED prep.",
        "link": "https://www.goodwillgulfcoast.org/programs-and-services/education/",
        "contact": [{"label":"General", "link":"https://www.goodwillgulfcoast.org/programs-and-services/registration/"}],
    },
    "ged_testing": {
        "name": "GED Testing (Pearson VUE)",
        "areas": ["AL"],
        "who": "Adults ready to take official GED tests at Goodwill’s testing center in Mobile.",
        "link": "https://www.goodwillgulfcoast.org/programs-and-services/education/",
        "contact": [{"label":"Register", "link":"https://www.goodwillgulfcoast.org/programs-and-services/registration/"}],
    },
    "esl": {
        "name": "English Language Classes",
        "areas": ["AL"],
        "who": "Adults wanting to improve English (Mobile & Baldwin Counties).",
        "link": "https://www.goodwillgulfcoast.org/programs-and-services/education/",
        "contact": [{"label":"ESL contact", "phone":"(251) 300-6274"}],
    },
    "career_pathways": {
        "name": "Career Pathway Certifications",
        "areas": ["AL", "FL"],
        "who": "Forklift (AL, 19+ & driver’s license), Logistics (AL & FL), CNA (FL), Hospitality/Tourism (AL & FL), IT (AL & FL).",
        "link": "https://www.goodwillgulfcoast.org/programs-and-services/education/career-pathway-programs/",
        "contact": [
            {"label":"AL (Mobile & others)", "phone":"(251) 300-6278", "email":"mcmakenoc@goodwillgc.org"},
            {"label":"AL (Baldwin County)", "phone":"(251) 210-1333", "email":"spanishfortoc@goodwillgc.org"},
            {"label":"FL (Escambia/Santa Rosa)", "phone":"(850) 434-0032", "email":"oliveoc@goodwillgc.org"},
            {"label":"FL (Okaloosa)", "phone":"(850) 243-7118", "email":"fortwaltonoc@goodwillgc.org"},
        ],
    },

    # Children & Family
    "early_intervention": {
        "name": "Early Intervention (Birth–3)",
        "areas": ["AL"],
        "who": "Infants/toddlers with developmental delays; family support & therapy.",
        "link": "https://www.goodwillgulfcoast.org/programs-and-services/children-and-family/",
        "contact": [{"label":"Request Info", "link":"https://www.goodwillgulfcoast.org/programs-and-services/registration/"}],
    },
    "hippy_pat": {
        "name": "Home Visitation: HIPPY & Parents as Teachers",
        "areas": ["AL"],
        "who": "Free home‑visitation preschool readiness for ages 0–5; empowers parents.",
        "link": "https://www.goodwillgulfcoast.org/programs-and-services/children-and-family/",
        "contact": [{"label":"Request Info", "link":"https://www.goodwillgulfcoast.org/programs-and-services/registration/"}],
    },
    "autism_eval": {
        "name": "Autism Evaluation Clinic (Ages 2–6)",
        "areas": ["AL", "FL"],
        "who": "Comprehensive ASD assessment & diagnostic services.",
        "link": "https://www.goodwillgulfcoast.org/programs-and-services/children-and-family/",
        "contact": [{"label":"Request Eval", "link":"https://www.goodwillgulfcoast.org/programs-and-services/registration/"}],
    },
    "child_dev_center": {
        "name": "Child Development Center (2.5–5)",
        "areas": ["AL"],
        "who": "Inclusive care & education to prepare children for kindergarten.",
        "link": "https://www.goodwillgulfcoast.org/programs-and-services/children-and-family/",
        "contact": [{"label":"Request Info", "link":"https://www.goodwillgulfcoast.org/programs-and-services/registration/"}],
    },
    "kaleidoscope": {
        "name": "Kaleidoscope Adult Day Program (19+)",
        "areas": ["AL"],
        "who": "Weekday program for adults with disabilities to stay active & engaged.",
        "link": "https://www.goodwillgulfcoast.org/programs-and-services/children-and-family/",
        "contact": [{"label":"Request Info", "link":"https://www.goodwillgulfcoast.org/programs-and-services/registration/"}],
    },
    "military_respite": {
        "name": "Military Respite (Navy families)",
        "areas": ["FL"],
        "who": "Temporary relief for active Navy families caring for a loved one with disabilities/special needs.",
        "link": "https://www.goodwillgulfcoast.org/programs-and-services/children-and-family/",
        "contact": [{"label":"Request Info", "link":"https://www.goodwillgulfcoast.org/programs-and-services/registration/"}],
    },

    # Support Services
    "medical_equipment": {
        "name": "Medical Assistance / Equipment (We Share Project)",
        "areas": ["AL", "FL"],
        "who": "Free adaptive equipment like wheelchairs, walkers, crutches & more (available in stores).",
        "link": "https://www.goodwillgulfcoast.org/programs-and-services/support/",
        "contact": [{"label":"Contact", "phone":"(251) 300-6094", "email":"RHenry@goodwillgc.org"}],
    },
    "vita_financial": {
        "name": "Financial Wellness & FREE Tax Prep (VITA)",
        "areas": ["AL", "FL"],
        "who": "Financial education and IRS‑certified, free tax filing for low/moderate income households.",
        "link": "https://www.goodwillgulfcoast.org/programs-and-services/support/",
        "contact": [{"label":"Request Info", "link":"https://www.goodwillgulfcoast.org/programs-and-services/registration/"}],
    },
    "free_book_program": {
        "name": "Free Book Program",
        "areas": ["AL", "FL"],
        "who": "Free children’s books in stores; also available for schools/daycares.",
        "link": "https://www.goodwillgulfcoast.org/programs-and-services/support/",
        "contact": [{"label":"Books contact", "phone":"(251) 380-7150", "email":"LGaudet@goodwillgc.org"}],
    },

    # Youth
    "youth_career_exploration": {
        "name": "Youth Career Exploration",
        "areas": ["AL"],
        "who": "Career discovery curriculum for teens entering the workforce.",
        "link": "https://www.goodwillgulfcoast.org/programs-and-services/youth/",
        "contact": [{"label":"Request Info", "link":"https://www.goodwillgulfcoast.org/programs-and-services/registration/"}],
    },
    "youth_disabilities": {
        "name": "Youth with Disabilities Program / High School High Tech",
        "areas": ["FL"],
        "who": "Escambia County FL job‑training with hands‑on store experience; HSHT for youth in juvenile justice.",
        "link": "https://www.goodwillgulfcoast.org/programs-and-services/youth/",
        "contact": [{"label":"Request Info", "link":"https://www.goodwillgulfcoast.org/programs-and-services/registration/"}],
    },
}

def pick(*keys):
    return [PROGRAMS[k] for k in keys]

# --- Game state ---
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.answers = {}

def next_step():
    st.session_state.step += 1

def prev_step():
    st.session_state.step = max(0, st.session_state.step - 1)

st.progress(min(st.session_state.step/8.0, 1.0), text="Your journey")

# --- Step 0: Welcome ---
if st.session_state.step == 0:
    st.markdown("### Welcome, traveler!")
    st.write("Answer a few quick questions and we’ll reveal the programs that fit you (or your family).")
    if st.button("Start ▶️"):
        next_step()

# --- Step 1: Where are you located? ---
elif st.session_state.step == 1:
    region = st.radio("Where do you live?", ["Alabama", "Florida", "Other / Prefer not to say"], index=0, help="Some programs are specific to AL or FL.")
    st.session_state.answers["region"] = {"Alabama":"AL","Florida":"FL"}.get(region, "NA")
    cols = st.columns(2)
    if cols[0].button("◀ Back"):
        prev_step()
    if cols[1].button("Next ▶️"):
        next_step()

# --- Step 2: Employment/education interests ---
elif st.session_state.step == 2:
    job_seek = st.checkbox("I'm looking for a job or better job")
    work_at_gw = st.checkbox("I want to apply for a job **at Goodwill**")
    training = st.multiselect("I'm interested in job training/certifications:", ["Forklift", "Logistics", "Healthcare (CNA)", "Hospitality/Tourism", "IT / Google certificates", "Not sure yet"])
    st.session_state.answers.update({"job_seek": job_seek, "work_at_gw": work_at_gw, "training": training})
    cols = st.columns(2)
    if cols[0].button("◀ Back"):
        prev_step()
    if cols[1].button("Next ▶️"):
        next_step()

# --- Step 3: Education basics ---
elif st.session_state.step == 3:
    need_ged = st.checkbox("I want **GED prep** or **adult education**")
    want_esl = st.checkbox("I want **English language classes** (ESL)")
    st.session_state.answers.update({"need_ged": need_ged, "want_esl": want_esl})
    cols = st.columns(2)
    if cols[0].button("◀ Back"):
        prev_step()
    if cols[1].button("Next ▶️"):
        next_step()

# --- Step 4: Family & children ---
elif st.session_state.step == 4:
    has_children = st.checkbox("I have children and want family/child services")
    age0_3 = st.checkbox("Child age **0–3** (Early Intervention, AL)")
    age2_5 = st.checkbox("Child age **2–5** (HIPPY / PAT, AL)")
    age2_6 = st.checkbox("Child age **2–6** (Autism evaluation)")
    age2_5_cdc = st.checkbox("Child age **2.5–5** (Child Development Center, AL)")
    adult19_disab = st.checkbox("Adult **19+** with disabilities (Kaleidoscope, AL)")
    military_florida = st.checkbox("Active Navy family in Florida (Military Respite)")
    st.session_state.answers.update({
        "has_children": has_children, "age0_3": age0_3, "age2_5": age2_5, "age2_6": age2_6,
        "age2_5_cdc": age2_5_cdc, "adult19_disab": adult19_disab, "military_florida": military_florida
    })
    cols = st.columns(2)
    if cols[0].button("◀ Back"):
        prev_step()
    if cols[1].button("Next ▶️"):
        next_step()

# --- Step 5: Support needs ---
elif st.session_state.step == 5:
    need_med = st.checkbox("I need **free medical equipment** (walkers, wheelchairs, etc.)")
    need_tax = st.checkbox("I want **free tax prep** or financial wellness coaching")
    want_books = st.checkbox("I’m interested in **free children’s books**")
    st.session_state.answers.update({"need_med": need_med, "need_tax": need_tax, "want_books": want_books})
    cols = st.columns(2)
    if cols[0].button("◀ Back"):
        prev_step()
    if cols[1].button("Next ▶️"):
        next_step()

# --- Step 6: Youth programs ---
elif st.session_state.step == 6:
    youth_hs = st.checkbox("I’m a **high school student** (or parent/guardian) looking for youth programs")
    youth_disability = st.checkbox("Student has **special needs/disabilities** or is in **juvenile justice**")
    st.session_state.answers.update({"youth_hs": youth_hs, "youth_disability": youth_disability})
    cols = st.columns(2)
    if cols[0].button("◀ Back"):
        prev_step()
    if cols[1].button("See my matches 🎉"):
        next_step()

# --- Step 7: Results ---
else:
    a = st.session_state.answers
    region = a.get("region","NA")
    recs = []

    # Employment
    if a.get("job_seek"):
        recs += pick("job_training")
    if a.get("work_at_gw"):
        recs += pick("jobs_at_goodwill")
    # WTC/AbilityOne hint if AL
    if region == "AL":
        recs += pick("wtc_abilityone")

    # Education
    if a.get("need_ged"):
        recs += pick("adult_education", "ged_testing")
    if a.get("want_esl") and region == "AL":
        recs += pick("esl")
    # Career pathways
    if "Forklift" in a.get("training", []):
        if region == "AL":
            recs += pick("career_pathways")
    if "Logistics" in a.get("training", []):
        recs += pick("career_pathways")
    if "Healthcare (CNA)" in a.get("training", []):
        if region == "FL":
            recs += pick("career_pathways")
    if "Hospitality/Tourism" in a.get("training", []):
        recs += pick("career_pathways")
    if "IT / Google certificates" in a.get("training", []):
        recs += pick("career_pathways")

    # Family & children
    if a.get("age0_3") and region == "AL":
        recs += pick("early_intervention")
    if a.get("age2_5") and region == "AL":
        recs += pick("hippy_pat")
    if a.get("age2_6"):
        recs += pick("autism_eval")
    if a.get("age2_5_cdc") and region == "AL":
        recs += pick("child_dev_center")
    if a.get("adult19_disab") and region == "AL":
        recs += pick("kaleidoscope")
    if a.get("military_florida") and region == "FL":
        recs += pick("military_respite")

    # Support
    if a.get("need_med"):
        recs += pick("medical_equipment")
    if a.get("need_tax"):
        recs += pick("vita_financial")
    if a.get("want_books"):
        recs += pick("free_book_program")

    # Youth
    if a.get("youth_hs"):
        if region == "AL":
            recs += pick("youth_career_exploration")
    if a.get("youth_disability"):
        if region == "FL":
            recs += pick("youth_disabilities")

    # Deduplicate while preserving order
    seen = set()
    unique_recs = []
    for r in recs:
        key = r["name"]
        if key not in seen:
            seen.add(key)
            unique_recs.append(r)

    st.success("🎉 Here are your matches!")
    if not unique_recs:
        st.write("We didn’t find a perfect match yet, but Goodwill can still help. Try contacting the nearest Opportunity Center below.")
    else:
        for prog in unique_recs:
            with st.container(border=True):
                st.markdown(f"### [{prog['name']}]({prog['link']})")
                st.caption(f"Areas: {', '.join(prog['areas'])}")
                st.write(prog["who"])
                if prog["contact"]:
                    st.write("**How to contact:**")
                    for c in prog["contact"]:
                        parts = []
                        if c.get("label"): parts.append(f"*{c['label']}*")
                        if c.get("phone"): parts.append(c["phone"])
                        if c.get("email"): parts.append(c["email"])
                        if c.get("link"): parts.append(f"[Open form]({c['link']})")
                        st.write(" • " + " — ".join(parts))

    st.divider()
    st.markdown("#### General Contacts")
    st.write("- **Request Information form:** https://www.goodwillgulfcoast.org/programs-and-services/registration/")
    st.write("- **Opportunity Centers & locations:** https://www.goodwillgulfcoast.org/locations/opportunity-centers/")

    cols = st.columns(2)
    if cols[0].button("◀ Start over"):
        st.session_state.step = 0
        st.session_state.answers = {}
    if cols[1].button("Go back"):
        prev_step()

st.markdown("<br><small>Note: Program availability/eligibility can vary. This is an informational tool only.</small>", unsafe_allow_html=True)
