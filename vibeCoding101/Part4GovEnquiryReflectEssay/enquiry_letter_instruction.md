# Instruction File: Draft the Green@Community Enquiry Letter 

## Input
Read the following materials:
- /workspaces/GCAP3226AIagents/Team5_GreenCommunity/Project_Roadmap_Team5.md
- /workspaces/GCAP3226AIagents/Team5_GreenCommunity/README.md
- /workspaces/GCAP3226AIagents/Topics/GCAP3226-Topic5-GreenCommunity.md

## Process
Follow these steps to compose the enquiry email/letter (modeled after `INSTRUCTION_DraftEnquiry.md`, tailored to Team 5):

1) Establish project context (2–3 sentences)
- Identify yourself as an HKBU undergraduate in GCAP3226.
- State project title: “Green@Community Recycling Network Analysis.”
- Brief purpose: evaluate programme effectiveness and inform resource allocation.

2) Define time window and flexibility
- Default ask: the most recent 3 full calendar years (e.g., 1 Jan 2022 – 31 Dec 2024).
- If unavailable, accept 1–2 years or the closest available period (quarterly/monthly or earlier years).

3) State purpose and use (compliance note)
- Use only for coursework; findings shared in class, final report, and a briefing to a LegCo member.
- Acknowledge EPD and agree to follow any conditions.

4) Request data (be precise; aggregate/anonymized; no PII)
Group requests into decision‑relevant blocks. Use the sub‑headings and bullets below; keep the wording concise and neutral.

A. GREENS Mobile App (GREEN$ ePIS)
- User Base: total registered users; monthly and annual active users (define “active” as earned GREEN$ ≥ once in period).
- User Demographics (counts or percentages; aggregate): age/age‑group; gender; residential district; building type; occupation. For both registered and active users (monthly and annual).
- Participation Intensity (aggregate): annual & monthly total GREEN$; GREEN$ per active user by demographic segments.
- Activity Metrics (aggregate): annual & monthly GREEN$‑earning transaction count; per active user by demographic segment.

B. Green@Community Facility Visitor Volume & Utilization
- Visitor Volume: annual & monthly visitor counts by facility type (recycling stations/stores/spots) and by individual facility.
- Throughput: annual recycled weight by facility type and by facility.
- Contribution to HK Overall Recycling: annual MSW generated; annual total recyclables collected; share handled by Green@Community vs HK total.
- Geographic Utilization: annual, monthly, and daily recycled weight by district, by facility type, and by facility.

C. Operations & Operating Costs
- Operating Costs: annual total; any available breakdowns (staffing, rent, utilities, logistics, maintenance, processing fees, etc.). If detailed prices aren’t available, provide aggregate categories.
- Scale / Inputs: number of facilities by district & type; floor area of stores (total or per store); staffing counts (total, by function, by employment type).
- Unit‑Cost Indicators: e.g., operating cost per recycled tonne.

5) Preferred format & documentation
- Format: CSV/Excel/Open API preferred; PDFs acceptable.
- Include brief definitions/notes (e.g., material categories; fiscal vs calendar year) where relevant.
- Partial aggregates or public references are welcome if full datasets aren’t available.

6) Channels and compliance extras
- Invite EPD to share any application forms, NDA requirements, or designated request channels.
- Reference Code on Access to Information politely (optional but recommended).

7) Professional closing block
- Signature with full name, programme, email.
- Include team members and course instructors’ names/emails.

---

## Research Rationale and Mapping (from my notes)
Use the following to justify why each requested item matters and to keep the letter tightly aligned with Team 5 goals.

Main research questions
1. To what extent is Green@Community effective? (environmental impact + cost‑effectiveness)
- Environmental impact indicators:
  - Participation: visitor volume (stations/stores/spots), GREEN$ ePIS registrations, active users
  - Recyclables collected: total weights, Green@Community’s share of HK recyclables
- Cost‑effectiveness indicators:
  - Cost per tonne; link visitor volumes and weights to operating costs
- Trend & relationship:
  - Annual trends of recycled weight and operating cost (2018–present) to assess whether cost changes are proportionate to impact changes

2. How can overall effectiveness be improved? (factors)
- Impact factors via data analysis:
  - Demographics: age, gender, district, building type, occupation, education, income
  - Engagement modelling: regressions on engagement vs demographics; identify low‑participation groups; infer incentive design needs
- Cost‑effectiveness factors:
  - Cost breakdowns (staffing, rent, logistics, etc.)
  - Facility usage vs demand: per‑facility visitor volume & weights vs district population (C&SD)
  - Facility density and placement: distances vs usage; find under‑used vs overloaded locations
  - Simulation ideas: visualize alternative allocations (e.g., store→spot; more frequent spots; relocate stores to reduce rent; tech helpers to reduce staffing cost)
- Recommendations pathway:
  - Target low‑engagement groups (revise GREEN$ rewards, improve convenience)
  - Optimize network (reduce low‑use stores, add/upgrade overloaded spots/stations)
  - Reduce costs (move from malls to government buildings where viable; consider intelligent helpers)

Mapping to data request blocks
- Participation & demographics → GREEN$ ePIS user base, demographics, activity & intensity metrics
- Utilization & throughput → visitor volume, recycled weight by type/facility/district/time
- Cost & scale → operating totals & breakdowns; facility counts/areas; staffing; unit‑cost indicators
- Trend analysis → annual/monthly series for all above where possible (2018–present if available)

Fallbacks if some data are denied
- Use C&SD district demographics; public MSW/recycling statistics; EPD annual reports
- Shift to higher‑level aggregates; retain ability to run regression/simulation with coarser inputs

---

## Output
Save the composed draft to:
- /workspaces/GCAP3226AIagents/vibeCoding101/Part4GovEnquiryReflectEssay/enquiry_draft_letter.md

---