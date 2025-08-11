# Find Your Way — Goodwill Gulf Coast (Text Adventure)

A simple Streamlit app that asks a few questions and recommends Goodwill Gulf Coast programs, with links and contact info.

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud
1. Push these three files to a GitHub repo.
2. Create a new Streamlit app pointing to `app.py` on your `main` branch.
3. Done!

## Customize
Open `app.py` and edit the `PROGRAMS` dictionary:
- Update blurbs, phone numbers, and links.
- Add/remove programs as needed.
- The matching rules live at the bottom (Step 7).

---
**Note:** This tool is informational; programs can have eligibility limits and may change over time.
