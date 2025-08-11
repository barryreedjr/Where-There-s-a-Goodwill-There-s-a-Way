import streamlit as st

# ---------------- Setup & Theme ----------------
st.set_page_config(
    page_title="Where There’s a Goodwill, There’s a Way — Finder",
    page_icon="🧭",
    layout="centered"
)

PRIMARY = "#0033A0"  # Goodwill deep blue-ish

CUSTOM_CSS = f"""
<style>
html, body, [class*="block-container"] {{
  font-family: Inter, system-ui, -apple-system, Segoe UI, Roboto, "Helvetica Neue", Arial, "Noto Sans";
}}
.header-box {{
  background: linear-gradient(135deg, {PRIMARY} 0%, #2C58FF 60%);
  color: white;
  padding: 1.2rem 1rem;
  border-radius: 18px;
  box-shadow: 0 10px 30px rgba(0,0,0,.12);
  text-align: center;
}}
.header-box h1 {{
  font-weight: 800;
  letter-spacing: 0.2px;
  margin: 0 0 .25rem 0;
}}
.header-box .tagline {{
  opacity: .95;
  font-size: 0.95rem;
}}
.card {{
  border: 1px solid rgba(0,0,0,.08);
  border-radius: 16px;
  padding: 1rem 1rem .6rem;
  background: white;
  box-shadow: 0 6px 18px rgba(0,0,0,.06);
  margin-bottom: .75rem;
}}
.reason {{
  background:#F1F5F9;
  border-radius: 10px;
  padding:.5rem .8rem;
  margin-top:.35rem;
  font-size:.92rem;
}}
.footer {{
  opacity:.85;
  font-size:.9rem;
}}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ---------------- Program Catalog (links/blurbs from goodwillgulfcoast.org) ----------------
PROGRAMS = {
    # Employment
    "job_training": {
        "name": "Job Training & Placement Services",
        "areas": ["AL","FL"],
        "who": "Help with resumes, interviews, applications, and job search; training to build workplace skills.",
        "link": "https://www.goodwillgulfcoast.org/programs-and-services/employment/job-training/",
        "why_keys": ["job_seek","returning_to_work","first_job","career_change"],
    },
    "jobs_at_goodwill": {
        "name": "Jobs at Goodwill",
        "areas": ["AL","FL"],
        "who": "Apply to work in stores, e-commerce, or mission services.",
        "link": "https://www.goodwillgulfcoast.org/jobs/",
        "why_keys": ["work_at_goodwill"],
    },
    "wtc_abilityone": {
        "name": "Work Training Center & AbilityOne (by referral)",
        "areas": ["AL"],
        "who": "Hands-on experience + coaching for individuals with disabilities (referral via Alabama Dept. of Rehab Services).",
        "link": "https://www.goodwillgulfcoast.org/programs-and-services/employment/work-training-center-and-ability-one/",
        "why_keys": ["disability_support","region_AL"],
    },

    # Education
    "adult_education": {
        "name": "Adult Education & GED Preparation",
        "areas": ["AL"],
        "who": "Morning/afternoon/evening classes; GED prep and basic skills.",
        "link": "https://www.goodwillgulfcoast.org/programs-and-services/education/adult-education/",
        "why_keys": ["no_hs","education_goal"],
    },
    "ged_testing": {
        "name": "GED Testing (Pearson VUE)",
        "areas": ["AL"],
        "who": "Official GED testing at Goodwill (Mobile).",
        "link": "https://www.goodwillgulfcoast.org/programs-and-services/education/",
        "why_keys": ["ged_ready"],
    },
    "esl": {
        "name": "English Language Classes",
        "areas": ["AL"],
        "who": "English classes in Mobile & Baldwin counties.",
        "link": "https://www.goodwillgulfcoast.org/programs-and-services/education/english-classes/",
        "why_keys": ["improve_english"],
    },
    "career_pathways": {
        "name": "Career Pathway Certifications",
        "areas": ["AL","FL"],
        "who": "Certifications in logistics, hospitality/tourism, IT; forklift (AL, 19+ w/ driver’s license); CNA (FL).",
        "link": "https://www.goodwillgulfcoast.org/programs-and-services/education/career-pathway-programs/",
        "why_keys": ["hands_on","digital_skills","hospitality","logistics","forklift_ok","healthcare_FL"],
    },

    # Children & Family
    "early_intervention": {
        "name": "Early Intervention (Birth–3)",
        "areas": ["AL"],
        "who": "Support for infants/toddlers with developmental delays; parent coaching & therapies.",
        "link": "https://www.goodwillgulfcoast.org/programs-and-services/children-and-family/early-intervention/",
        "why_keys": ["child_age_0_3","region_AL"],
    },
    "hippy_pat": {
        "name": "Home Visitation: HIPPY & Parents as Teachers",
        "areas": ["AL"],
        "who": "Free home-visitation preschool-readiness (0–5); empowers parents as first teachers.",
        "link": "https://www.goodwillgulfcoast.org/programs-and-services/children-and-family/home-visitation/",
        "why_keys": ["child_age_0_5","parent_coaching","region_AL"],
    },
    "autism_eval": {
        "name": "Autism Evaluation Clinic (Ages 2–6)",
        "areas": ["AL","FL"],
        "who": "Comprehensive ASD assessments for young children.",
        "link": "https://www.goodwillgulfcoast.org/programs-and-services/children-and-family/autism-evaluation-clinic/",
        "why_keys": ["autism_question"],
    },
    "child_dev_center": {
        "name": "Child Development Center (2.5–5)",
        "areas": ["AL"],
        "who": "Inclusive care & kindergarten readiness in partnership with MCPSS.",
        "link": "https://www.goodwillgulfcoast.org/programs-and-services/children-and-family/child-development-center/",
        "why_keys": ["child_age_2_5","region_AL"],
    },
    "kaleidoscope": {
        "name": "Kaleidoscope Adult Day Program (19+)",
        "areas": ["AL"],
        "who": "Weekday program for adults with disabilities to stay active & engaged.",
        "link": "https://www.goodwillgulfcoast.org/programs-and-services/children-and-family/kaleidoscope-adult-day-program/",
        "why_keys": ["adult_19_plus_disability","region_AL"],
    },
    "military_respite": {
        "name": "Military Respite (Navy families)",
        "areas": ["FL"],
        "who": "Temporary relief for active Navy families caring for a loved one with disabilities/special needs.",
        "link": "https://www.goodwillgulfcoast.org/programs-and-services/children-and-family/military-respite-program/",
        "why_keys": ["navy_family_FL"],
    },

    # Support
    "medical_equipment": {
        "name": "Medical Assistance / Equipment (We Share Project)",
        "areas": ["AL","FL"],
        "who": "Free adaptive equipment like wheelchairs, walkers, bath benches, and more (subject to availability).",
        "link": "https://www.goodwillgulfcoast.org/programs-and-services/support/medical-assistance/",
        "why_keys": ["assistive_needs"],
    },
    "vita_financial": {
        "name": "Financial Wellness & FREE Tax Prep (VITA)",
        "areas": ["AL","FL"],
        "who": "Financial education and free, IRS-certified tax filing for low/moderate-income households.",
        "link": "https://www.goodwillgulfcoast.org/programs-and-services/support/",
        "why_keys": ["tax_help"],
    },
    "free_book_program": {
        "name": "Free Book Program",
        "areas": ["AL","FL"],
        "who": "Free children’s books in stores; also available for schools/daycares.",
        "link": "https://www.goodwillgulfcoast.org/programs-and-services/support/",
        "why_keys": ["free_books"],
    },

    # Youth
    "youth_career_exploration": {
        "name": "Youth Career Exploration (AL)",
        "areas": ["AL"],
        "who": "Career discovery curriculum for teens entering the workforce.",
        "link": "https://www.goodwillgulfcoast.org/programs-and-services/youth/",
        "why_keys": ["youth_hs_AL"],
    },
    "youth_disabilities": {
        "name": "Youth with Disabilities / HSHT (FL)",
        "areas": ["FL"],
        "who": "Escambia County FL job-training + HSHT for youth in juvenile justice (referral).",
        "link": "https://www.goodwillgulfcoast.org/programs-and-services/youth/",
        "why_keys": ["youth_disability_FL"],
    },
}

REQ_INFO = "https://www.goodwillgulfcoast.org/programs-and-services/registration/"
OPPORTUNITY_CENTERS = "https://www.goodwillgulfcoast.org/locations/opportunity-centers/"
JOBS_LINK = "https://www.goodwillgulfcoast.org/jobs/"

# ---------------- Header ----------------
st.markdown("""
<div class="header-box">
  <h1>Where There’s a Goodwill, There’s a Way</h1>
  <div class="tagline">Answer a few story-style questions and we’ll suggest Goodwill Gulf Coast programs that fit you (or your family).</div>
</div>
""", unsafe_allow_html=True)
st.write("")

# ---------------- State ----------------
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.a = {}

def next_step(): st.session_state.step += 1
def back(): st.session_state.step = max(0, st.session_state.step-1)

st.progress(min(st.session_state.step/8.0, 1.0), text="Your journey")

# ---------------- Story-style questions (infers needs) ----------------
if st.session_state.step == 0:
    st.markdown("### Ready to find your way?")
    st.write("Pick what describes you best — there are no wrong answers.")
    if st.button("Start ▶️"):
        next_step()

elif st.session_state.step == 1:
    st.markdown("#### First, where do you spend most of your time?")
    region = st.selectbox("Region", ["Alabama", "Florida", "Other / Prefer not to say"], index=0)
    st.session_state.a["region"] = {"Alabama":"AL","Florida":"FL"}.get(region, "NA")
    c1, c2 = st.columns(2)
    if c1.button("◀ Back"): back()
    if c2.button("Next ▶️"): next_step()

elif st.session_state.step == 2:
    st.markdown("#### About your work journey")
    work_mood = st.radio(
        "Which sounds most like you right now?",
        [
            "I’m gearing up for my **first job** or starting fresh",
            "I’m **returning to work** or switching paths",
            "I’m working now but want **better pay** or a promotion",
            "I want to **work at Goodwill**",
            "Skip for now",
        ],
        index=0
    )
    a = st.session_state.a
    a["first_job"] = ("first job" in work_mood.lower())
    a["returning_to_work"] = ("returning" in work_mood.lower() or "switching" in work_mood.lower())
    a["career_change"] = ("switching" in work_mood.lower() or "better" in work_mood.lower())
    a["job_seek"] = work_mood != "Skip for now"
    a["work_at_goodwill"] = ("goodwill" in work_mood.lower())

    c1, c2 = st.columns(2)
    if c1.button("◀ Back"): back()
    if c2.button("Next ▶️"): next_step()

elif st.session_state.step == 3:
    st.markdown("#### Skills & certifications — what are you curious about? (choose any)")
    picks = st.multiselect(
        "Think about the next season of your career:",
        [
            "Hands-on roles around **warehouses/equipment**",
            "Customer-facing **hospitality or retail**",
            "**Digital/IT** skills & certificates",
            "Healthcare, like **CNA** (Florida)",
            "Supply chain/**logistics**",
            "None of these match me",
        ],
    )
    a = st.session_state.a
    a["hands_on"] = any("warehouses" in p for p in picks)
    a["hospitality"] = any("hospitality" in p for p in picks)
    a["digital_skills"] = any("Digital/IT" in p for p in picks)
    a["healthcare_FL"] = any("CNA" in p for p in picks)
    a["logistics"] = any("logistics" in p for p in picks)

    st.markdown("##### Quick check for hands-on paths (optional):")
    age_band = st.selectbox("Your age group", ["Under 18", "19–24", "25–54", "55+"], index=2)
    has_license = st.checkbox("I have a valid driver’s license")
    a["age19plus"] = age_band != "Under 18"
    a["forklift_ok"] = a.get("hands_on") and a.get("age19plus") and has_license

    c1, c2 = st.columns(2)
    if c1.button("◀ Back"): back()
    if c2.button("Next ▶️"): next_step()

elif st.session_state.step == 4:
    st.markdown("#### Learning & language")
    school_feel = st.radio(
        "Your school story sounds like:",
        [
            "I **finished high school** (or equivalent)",
            "I’m still working toward finishing high school/GED",
            "Prefer not to say",
        ],
        index=0,
    )
    a = st.session_state.a
    a["no_hs"] = ("working" in school_feel.lower() or "ged" in school_feel.lower())
    a["education_goal"] = a["no_hs"]

    english = st.radio(
        "How comfortable are you communicating in English at work/school?",
        ["Very comfortable", "I get by but I’d like structured classes", "Prefer not to say"], index=0
    )
    a["improve_english"] = ("structured" in english.lower()) and (a.get("region")=="AL")

    a["ged_ready"] = st.checkbox("I feel **ready to schedule** official GED testing (Mobile area)")

    c1, c2 = st.columns(2)
    if c1.button("◀ Back"): back()
    if c2.button("Next ▶️"): next_step()

elif st.session_state.step == 5:
    st.markdown("#### Family & caregiving")
    with st.expander("Tell us about your family (optional)"):
        has_children = st.checkbox("I’m a parent/guardian")
        child_ages = st.multiselect("Children’s ages (select any)", ["0–3", "2–5", "2–6", "K-12", "18+"])
        want_parent_coach = st.checkbox("I’m interested in **home-based parent coaching** and school readiness")
        adult_disab = st.checkbox("An adult (19+) in my household might benefit from a **weekday program** for people with disabilities")
        autism_check = st.checkbox("I’d like to **learn about a developmental/autism evaluation** for a young child")
        navy_FL = st.checkbox("We’re an **active-duty Navy** household in Florida caring for someone with special needs")

    a = st.session_state.a
    a["has_children"] = has_children
    a["child_age_0_3"] = ("0–3" in child_ages) and a.get("region")=="AL"
    a["child_age_2_5"] = ("2–5" in child_ages) and a.get("region")=="AL"
    a["child_age_2_6"] = ("2–6" in child_ages)
    a["parent_coaching"] = want_parent_coach and a.get("region")=="AL"
    a["adult_19_plus_disability"] = adult_disab and a.get("region")=="AL"
    a["autism_question"] = autism_check
    a["navy_family_FL"] = navy_FL and a.get("region")=="FL"

    c1, c2 = st.columns(2)
    if c1.button("◀ Back"): back()
    if c2.button("Next ▶️"): next_step()

elif st.session_state.step == 6:
    st.markdown("#### Day-to-day supports")
    taxes = st.radio("When tax season hits, my plan is:",
                     ["Use a paid preparer", "Do it myself", "I’d love **free, in-person help**", "Skip"], index=3)
    mobility = st.radio("Getting around the house:",
                        ["All good", "Could use assistive items (walker, bath bench, etc.)", "Skip"], index=2)
    books = st.checkbox("I’m interested in free **children’s books** from local Goodwill stores")
    a = st.session_state.a
    a["tax_help"] = ("free" in taxes.lower())
    a["assistive_needs"] = ("assistive" in mobility.lower())
    a["free_books"] = books

    c1, c2 = st.columns(2)
    if c1.button("◀ Back"): back()
    if c2.button("See my matches 🎉"): next_step()

# ---------------- Results ----------------
else:
    a = st.session_state.a
    region = a.get("region","NA")
    a["region_AL"] = region == "AL"
    a["region_FL"] = region == "FL"

    scores = {key:0 for key in PROGRAMS.keys()}
    reason_map = {key:[] for key in PROGRAMS.keys()}

    def add_for(prog_key, weight=1):
        for k in PROGRAMS[prog_key]["why_keys"]:
            if a.get(k):
                scores[prog_key] += weight
                reason_map[prog_key].append(k)

    for pk in PROGRAMS:
        add_for(pk, 1)

    if a.get("work_at_goodwill"):
        scores["jobs_at_goodwill"] += 2  # small boost if they explicitly want this

    def fits_region(prog):
        areas = PROGRAMS[prog]["areas"]
        if "AL" in areas and region=="AL": return True
        if "FL" in areas and region=="FL": return True
        if "AL" in areas and "FL" in areas: return region in ("AL","FL")
        return "AL" in areas and "FL" in areas  # for NA, show multi-region supports

    ranked = sorted([p for p in PROGRAMS if fits_region(p)],
                    key=lambda k: (-scores[k], PROGRAMS[k]["name"]))

    st.success("🎉 Here are your matches!")
    shown = 0
    for pk in ranked:
        if scores[pk] <= 0: continue
        pr = PROGRAMS[pk]

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown(f"### [{pr['name']}]({pr['link']})")
        st.caption(f"Areas: {', '.join(pr['areas'])}")
        st.write(pr["who"])

        if reason_map[pk]:
            readable = {
                "job_seek":"You’re exploring new or better work",
                "first_job":"You mentioned starting your first job",
                "returning_to_work":"You’re returning or switching paths",
                "career_change":"You’re seeking a new direction",
                "work_at_goodwill":"You want to apply at Goodwill",
                "disability_support":"You or a family member could use disability-related supports",
                "region_AL":"You’re in Alabama",
                "region_FL":"You’re in Florida",
                "no_hs":"You’re still working toward a diploma/GED",
                "education_goal":"You set an education goal",
                "ged_ready":"You feel ready to schedule GED testing",
                "improve_english":"You’d like structured English classes",
                "hands_on":"You’re into hands-on/equipment roles",
                "hospitality":"Hospitality/retail interests",
                "digital_skills":"You’re exploring IT/digital certificates",
                "logistics":"You’re curious about logistics",
                "forklift_ok":"You’re 19+ with a driver’s license and like equipment",
                "healthcare_FL":"Healthcare/CNA interest (FL)",
                "child_age_0_3":"You have a child age 0–3",
                "child_age_2_5":"You have a child age 2–5",
                "child_age_2_6":"You have a child age 2–6",
                "parent_coaching":"You want home-based parent coaching",
                "adult_19_plus_disability":"You asked about a weekday program for adults with disabilities",
                "autism_question":"You’re curious about an autism/development evaluation",
                "navy_family_FL":"You’re an active-duty Navy family in FL",
                "assistive_needs":"You mentioned needing assistive equipment",
                "tax_help":"You’d like free, in-person tax help",
                "free_books":"You’re interested in free children’s books",
                "youth_hs_AL":"You’re a high school student (AL)",
                "youth_disability_FL":"Youth disability/justice (FL)",
            }
            whys = [readable.get(k,k) for k in dict.fromkeys(reason_map[pk]).keys()]
            st.markdown("**Why this matched you**")
            st.markdown("<div class='reason'>• " + "<br>• ".join(whys) + "</div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)
        shown += 1

    if shown == 0:
        st.info("We didn’t find a perfect match yet, but Goodwill can still help. Try contacting the nearest Opportunity Center below.")

    st.divider()
    st.markdown("#### Next steps")
    st.write(f"• **Request Information form:** {REQ_INFO}")
    st.write(f"• **Opportunity Centers & locations:** {OPPORTUNITY_CENTERS}")
    st.write(f"• **Jobs at Goodwill:** {JOBS_LINK}")

    c1, c2 = st.columns(2)
    if c1.button("◀ Start over"):
        st.session_state.step = 0
        st.session_state.a = {}
    if c2.button("Go back"):
        back()

st.markdown("<br><div class='footer'>This tool is informational only; programs/eligibility may change.</div>", unsafe_allow_html=True)
