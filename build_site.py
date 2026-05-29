# -*- coding: utf-8 -*-
"""
Generator for the Lorenzani course mastery website.
Authored from the verbatim lecture slides (Class 1-4), the seminar notes,
the course outline / reading list, the assigned readings and the
Comprehensive Exam Preparation Guide. Produces a single self-contained
index.html (HTML + embedded CSS + JS, no external dependencies).
"""
import json, html

# =============================================================================
#  CONTENT MODEL
#  Block types used in reading mode:
#    text | def (definition) | ex (example) | principle (key principle)
#    | warn (exam tip / warning) | quote | list (items[])
# =============================================================================

def T(s): return {"k": "text", "t": s}
def DEF(s): return {"k": "def", "t": s}
def EX(s): return {"k": "ex", "t": s}
def PR(s): return {"k": "principle", "t": s}
def WARN(s): return {"k": "warn", "t": s}
def Q(s): return {"k": "quote", "t": s}
def LST(items, lead=None): return {"k": "list", "lead": lead, "items": items}

def mcq(q, options, answer, source, concept):
    return {"type": "mcq", "q": q, "options": options, "answer": answer,
            "source": source, "concept": concept}

def blank(q, accept, source, concept, display=None):
    if isinstance(accept, str): accept = [accept]
    return {"type": "blank", "q": q, "accept": accept, "answer": display or accept[0],
            "source": source, "concept": concept}

MODULES = [
    ("intro", "Course Foundations & Digital Glossary"),
    ("m1", "Module 1 — Foresight as a Beacon of the New EU Industrial Strategy"),
    ("m2", "Module 2 — Digital Industrial Strategy & Open Strategic Autonomy"),
    ("m3", "Module 3 — The EU as a Digital Normative Superpower"),
    ("m4", "Module 4 — Dynamic Coherence with the Green & Fair Transition"),
    ("seminar", "Seminar — DSA & DMA (the 'Digital Sisters')"),
    ("readings", "Key Readings & Course Documents"),
    ("synthesis", "Thematic Synthesis, Timeline & Exam Preparation"),
]

SECTIONS = []
def S(id, module, title, blocks, terms=None, quiz=None):
    SECTIONS.append({"id": id, "module": module, "title": title,
                     "blocks": blocks, "terms": terms or [], "quiz": quiz or []})

# -----------------------------------------------------------------------------
# INTRO
# -----------------------------------------------------------------------------
S("intro-overview", "intro", "Course Overview & the Central Argument", [
    T("Course title: <b>‘Foresight, industrial strategy and digital policies: a new consistent trio in the EU’</b> — European Political and Governance Studies, Academic Year 2025-2026. Professor: <b>Dimitri LORENZANI</b>; Academic Assistant: <b>Marco NICOLICH</b>. It is an <b>optional course</b> (25h of teaching)."),
    PR("The central claim of the course: digitalisation is not merely a sectoral agenda — it has become a <b>foundation</b> for competitiveness, open strategic autonomy, economic security, regulation, the green transition and the fair transition."),
    Q("“Industrial strategies today – as seen in the US and China – combine multiple policies, ranging from fiscal policies to encourage domestic production, to trade policies to penalise anti-competitive behaviour, to foreign economic policies to secure supply chains. In the EU context, linking policies in this way requires […] a new industrial strategy for Europe.” — Mario Draghi, ‘The Future of European Competitiveness’, September 2024"),
    DEF("<b>Dynamic policy coherence</b>: the capacity to exploit synergies and assuage trade-offs with other policies over an inter-temporal setting — for instance ensuring that the pursued digital transition also interacts with the green and fair transitions as well as with the overarching goal of achieving Europe’s open strategic autonomy in an increasingly contested global arena."),
    PR("The <b>key takeaway</b> of the course: Europe’s new industrial strategy, strategic foresight and digital laws/policies can be regarded as a new — and crucial — <b>‘consistent trio’</b> in EU policymaking."),
    LST([
        "Strategic foresight is the <b>analytical lens</b> (it anticipates risks, opportunities and dependencies).",
        "Industrial strategy is the <b>capacity-building agenda</b> (it selects priorities).",
        "Digital policy is both the <b>object and the instrument</b> of transformation (it supplies the regulatory and technological tools).",
    ], lead="The trio, in one line:"),
    T("The course consists of <b>4 modules</b>: (1) strategic foresight as a beacon of the EU’s new industrial strategy; (2) digitalisation and advanced technologies as a leg of Europe’s new industrial strategy and open strategic autonomy; (3) the EU as a digital normative superpower (regulatory); (4) dynamic coherence of the digital transition with the green/fair transition."),
], terms=[
    {"t":"Consistent trio","d":"Foresight + industrial strategy + digital policy as a new, crucial trio in EU policymaking."},
    {"t":"Dynamic policy coherence","d":"The capacity to exploit synergies and manage trade-offs between policies over time, especially between digital, green, fair and security objectives."},
], quiz=[
    mcq("What is the course's 'consistent trio'?",
        ["Foresight, industrial strategy and digital policy",
         "Competition, trade and fiscal policy",
         "Green, digital and defence policy",
         "AI Act, DSA and DMA"],
        0, "Europe’s new industrial strategy, strategic foresight and digital laws and policies can be regarded as a new – and crucial – ‘consistent trio’ in EU policymaking.", "Consistent trio"),
    blank("Complete Draghi (Sept 2024): 'In the EU context, linking policies in this way requires […] a new ______ strategy for Europe.'",
          ["industrial"], "“…linking policies in this way requires […] a new industrial strategy for Europe”. — Mario Draghi, ‘The Future of European Competitiveness’, September 2024", "Draghi Report"),
    blank("The capacity to exploit synergies and assuage trade-offs with other policies over an inter-temporal setting is called dynamic policy ______.",
          ["coherence"], "digital regulations benefit from so-called dynamic policy coherence (the capacity to exploit synergies and assuage trade-offs with other policies over an inter-temporal setting).", "Dynamic policy coherence"),
    mcq("In the trio, strategic foresight functions primarily as the…",
        ["analytical lens", "capacity-building agenda", "enforcement mechanism", "funding instrument"],
        0, "Foresight is the analytical lens; industrial strategy is the capacity-building agenda; digital policy is both the object and instrument of transformation.", "Consistent trio"),
    mcq("How many teaching modules make up the course?",
        ["4", "3", "5", "2"], 0, "The course will consist of 4 modules (accounting for 25 hours of teaching overall).", "Course structure"),
])

S("intro-marking", "intro", "Marking & Assessment of the Course", [
    LST([
        "<b>Participation (15%)</b>: physical presence, active engagement, and the result of a <b>mid-term quiz</b>.",
        "<b>Oral presentations (30%)</b>: 5 students assigned to each of 5 groups; presenting with a slideshow for <b>30 minutes max</b>, followed by ca. 30 minutes of debate. A <b>written outline (max 2 pages excl. bibliography)</b> sent at least <b>48 hours</b> before the presentation to the Academic Assistant; analytical part with policy conclusions and personal recommendations. Mark = average of a common group mark (incl. outline) + an individual mark for delivery.",
        "<b>Final exam (55%)</b>: a <b>2-hour written exam — closed-book (no internet)</b>; <b>1–2 essay questions (1000 words max) = 50% of the grade</b>; <b>a few short questions = 50% of the grade</b>. Penalties apply (see outline).",
    ], lead="The grade is built from three components:"),
    WARN("Exam-format facts are frequently tested as short questions. Memorise: 55% weight, 2 hours, closed-book, ≤1000-word essays. Oral = 30%, participation = 15%."),
    T("Teaching method: the course is interactive; students are expected to actively participate in all classes. AI tools (for checking, reference-style management or information searches) remain permitted by default for course work and the Master’s thesis, but students bear full responsibility for content and must comply with College regulations on academic integrity (Articles 39a, 39b and 40 of the Academic Regulations)."),
], terms=[
    {"t":"Final exam (55%)","d":"A 2-hour closed-book written exam: 1–2 essays (1000 words max, 50%) plus a few short questions (50%)."},
], quiz=[
    mcq("What share of the final grade does the final exam represent?",
        ["55%", "50%", "30%", "15%"], 0, "Final exam (55%): 2-hour written exam – closed-book.", "Assessment"),
    mcq("The final exam is…",
        ["2-hour, closed-book (no internet)", "3-hour, open-book", "take-home over 48 hours", "oral only"],
        0, "2-hour written exam – closed-book (no internet).", "Assessment"),
    blank("Essay questions in the final exam are capped at ______ words max.",
          ["1000","1,000"], "1-2 essay questions (1000 words max) – 50% of the grade.", "Assessment"),
    mcq("Oral presentations are worth what share of the grade?",
        ["30%", "15%", "55%", "25%"], 0, "Oral presentations (30%).", "Assessment"),
    blank("The written outline for the oral presentation must be sent at least ______ hours in advance.",
          ["48"], "Written outline (max 2 pages excl. bibliography) to be sent at least 48 hours before the oral presentation to Academic Assistant.", "Assessment"),
])

S("intro-schedule", "intro", "Schedule & Module Map", [
    T("The course develops around 4 teaching modules. An optional tutorial ‘Digital Policy 101’ with the Academic Assistant is possible."),
    LST([
        "Fri 09/01/2026 — General introduction + MODULE 1 (foresight as a beacon of the new EU industrial strategy)",
        "Sat 10/01/2026 — MODULE 1 + MODULE 2 (Open Strategic Autonomy)",
        "Fri 30/01/2026 — MODULE 2 (Open Strategic Autonomy)",
        "Sat 31/01/2026 — MODULE 2 + Presentation Group 1 + MODULE 3 (Regulatory)",
        "Fri 20/03/2026 — MODULE 3 (Regulatory) + SEMINAR by M. HAVRDA",
        "Sat 21/03/2026 — MODULE 3 + Presentations Group 2 & 3 + MODULE 4 (Twinning green-digital)",
        "Fri 17/04/2026 — MODULE 4 (Twinning green-digital) + SEMINAR by F. CHIRICO",
        "Sat 18/04/2026 — MODULE 4 + Presentations Group 4 & 5",
    ], lead="Overall schedule:"),
    LST([
        "Module 1: Introduction — strategic foresight as a beacon of the EU’s new industrial strategy.",
        "Module 2: Digitalisation and advanced technologies as a leg of Europe’s new industrial strategy and open strategic autonomy.",
        "Module 3: The EU as a digital normative superpower (regulatory).",
        "Module 4: Dynamic coherence of the digital transition with the green/fair transition (twinning).",
    ], lead="The four modules:"),
    EX("Two seminars complement the modules: <b>M. HAVRDA</b> (with Module 3) and <b>F. CHIRICO</b> (with Module 4, on the DSA and DMA)."),
], terms=[], quiz=[
    mcq("Which seminar accompanies Module 4 and covers the DSA and DMA?",
        ["F. Chirico", "M. Havrda", "A. Renda", "M. Szapiro"], 0,
        "MODULE 4 (Twinning green-digital) + SEMINAR by F. CHIRICO.", "Seminars"),
    mcq("Module 4 is about…",
        ["Twinning of the digital transition with the green/fair transition",
         "Open strategic autonomy", "EU digital regulation", "Strategic foresight tools"],
        0, "MODULE 4 (Twinning green-digital).", "Course structure"),
])

S("intro-readinglist", "intro", "Reading List (Compulsory Readings by Module)", [
    LST([
        "A ‘Geopolitical Commission’: Reaching a Point of Inflexion?, Lorenzani D. and M. Szapiro, 2023 (in O. Costa & S. Van Hecke eds., “The EU Political System After the 2019 European Elections”).",
        "Strategic foresight as a beacon for the new EU industrial policy, Lorenzani D., 2024, European Law Journal (vol. 30, no. 3, Sept 2024, pp. 422-433).",
        "Competitiveness Compass Communication, European Commission, 2025.",
        "2020 Strategic Foresight Report, European Commission, 2020.",
        "2025 Strategic Foresight Report, European Commission, 2025.",
    ], lead="Module 1:"),
    LST([
        "Draghi Report, 2024 — part B chapters ‘Digitalisation & Advanced Tech’ (p 67), ‘Accelerating Innovation’ (p 228) and ‘Strengthening Governance’ (p 307).",
        "2021 Strategic Foresight Report, European Commission, 2021.",
        "New measures to secure raw materials and strengthen the EU’s economic security, 2025; and New EU economic security doctrine (European Parliament briefing, 2025).",
        "2025 Report on the state of the Digital Decade, European Commission, 2025.",
        "Revised Cybersecurity Act, European Commission, 2026.",
    ], lead="Module 2:"),
    LST([
        "2023 Strategic Foresight Report, European Commission, 2023.",
        "Anu Bradford: the race to become the next technology superpower, McKinsey Global Publishing, November 2023.",
        "Artificial Intelligence and the Great Divergence, White House, 2026.",
        "Draghi Report, 2024, chapter ‘Strengthening governance’ (p 307 and following).",
        "Digital issues in the EU-US Trade and Technology Council, Commission documents.",
    ], lead="Module 3:"),
    LST([
        "What ‘North Star’ for future EU industrial policy?, Andrea Renda, 2024.",
        "The Technology/Jobs Puzzle: A European Perspective, Andrea Renda, Pierre Alexandre Balland and Lucia Bosoer, February 28, 2023.",
        "The future of jobs is green, JRC, Publications Office of the European Union, 2021.",
        "IoT4SDGs, CEPS publications, Andrea Renda and Moritz Laurer, 2020.",
        "2022 Strategic Foresight Report, European Commission, 2022.",
    ], lead="Module 4:"),
    WARN("The compulsory core: the <b>Draghi Report</b> (Part A + digital and governance chapters in Part B), the <b>Competitiveness Compass</b>, and the <b>Strategic Foresight Reports 2020-2021-2022-2023-2025</b>."),
], terms=[], quiz=[
    mcq("Which author wrote 'The Technology/Jobs Puzzle: A European Perspective' (with Balland and Bosoer)?",
        ["Andrea Renda", "Mario Draghi", "Anu Bradford", "Dimitri Lorenzani"], 0,
        "The Technology/Jobs Puzzle: A European Perspective, Andrea Renda, Pierre Alexandre Balland and Lucia Bosoer, 2023.", "Renda"),
    mcq("Which Strategic Foresight Reports are listed as compulsory?",
        ["2020, 2021, 2022, 2023 and 2025", "Only 2024", "2019 and 2020", "2022 and 2026"], 0,
        "The European Commission’s Strategic Foresight Reports 2020-2021-2022-2023-2025.", "Reading list"),
    mcq("Which McKinsey reading concerns 'the race to become the next technology superpower'?",
        ["Anu Bradford (2023)", "Andrea Renda (2024)", "Federico Fabbrini (2025)", "Mario Draghi (2024)"], 0,
        "Anu Bradford: the race to become the next technology superpower, McKinsey Global Publishing, November 2023.", "Reading list"),
])

S("intro-glossary1", "intro", "Digital Glossary (I): AI, Connectivity & Computing", [
    DEF("<b>Artificial intelligence (AI)</b>: the ability of a computer or computer-controlled robot to perform tasks associated with intelligent beings — reasoning, discovering meaning, generalizing, learning from past experience. It combines computer science and data analytics and encompasses <b>machine learning</b> and <b>deep learning</b> (AI algorithms that create expert systems to make predictions or classifications based on input data)."),
    DEF("<b>5G/6G</b>: fifth- and sixth-generation technology for wireless communications over cellular data networks; operating on higher radio frequencies than 4G, providing more bandwidth and lower latency at microsecond speeds. Wireless generations are standardized by the <b>International Telecommunication Union</b>."),
    DEF("<b>Edge (computing)</b>: a distributed computing paradigm/architecture that brings computation and data storage closer to the sources of data, in order to improve response times and save bandwidth."),
    DEF("<b>Supercomputing</b>: a type of high-performance computing (HPC) using computers with high computational capabilities (supercomputers) to process complex calculations and large volumes of data."),
    DEF("<b>Quantum (computing)</b>: the use of quantum (physics) phenomena like superposition and entanglement to perform computation exponentially faster than classic (electrodynamics) computers, including HPCs."),
    DEF("<b>Internet of Things (IoT)</b>: devices with sensors, processing ability, software and other technologies that connect and exchange data with other devices and systems over the Internet or other communications networks."),
    DEF("<b>Cloud</b>: networked computing facilities providing remote data storage and processing services via the internet."),
], terms=[
    {"t":"Artificial intelligence (AI)","d":"The ability of a computer/robot to perform tasks of intelligent beings; combines computer science and data analytics; encompasses machine learning and deep learning."},
    {"t":"5G/6G","d":"Fifth-/sixth-generation wireless tech; higher frequencies than 4G; more bandwidth, lower (microsecond) latency; standardised by the ITU."},
    {"t":"Edge computing","d":"Distributed architecture bringing computation/storage closer to data sources to improve response times and save bandwidth."},
    {"t":"Quantum computing","d":"Uses superposition and entanglement to compute exponentially faster than classical computers."},
    {"t":"IoT","d":"Devices with sensors/software that connect and exchange data over the internet or other networks."},
], quiz=[
    blank("AI encompasses machine learning and ______ learning (algorithms that create expert systems to make predictions or classifications).",
          ["deep"], "It combines computer science, data analytics and encompasses machine learning and deep learning.", "AI"),
    mcq("Which two quantum-physics phenomena let quantum computers compute exponentially faster?",
        ["Superposition and entanglement", "Reflection and refraction", "Induction and conduction", "Fission and fusion"],
        0, "Quantum: use of quantum phenomena like superposition and entanglement to perform computation exponentially faster than classic computers.", "Quantum"),
    mcq("Wireless generations (5G/6G) are standardized by the…",
        ["International Telecommunication Union (ITU)", "European Commission", "ISO", "NATO"], 0,
        "Wireless generations are standardized by International Telecommunication Union.", "5G/6G"),
    blank("______ computing brings computation and data storage closer to the sources of data to improve response times and save bandwidth.",
          ["Edge"], "Edge (computing): distributed computing paradigm that brings computation and data storage closer to the sources of data.", "Edge computing"),
])

S("intro-glossary2", "intro", "Digital Glossary (II): Exascale, Twins, Data Centres & AI Models", [
    DEF("<b>Exascale</b>: a measure of supercomputer performance — computing systems capable of calculating at least “10¹⁸ IEEE 754 Double Precision (64-bit) operations (multiplications and/or additions) per second (exaFLOPS)”."),
    DEF("<b>Digital twins</b>: a digital model of an intended or actual real-world physical product, system or process (the ‘physical twin’) that serves as its indistinguishable digital counterpart for practical purposes: simulation, integration, testing, monitoring, maintenance."),
    DEF("<b>Data Centres</b>: a centralized facility where an organization’s IT operations and equipment are concentrated, serving critical functions related to storing, processing and disseminating data and applications. <b>Enterprise on-premise</b> data centres are hosted in the organization’s own facilities (e.g. for greater control over security and regulatory compliance). <b>Cloud computing</b> data centres house IT infrastructure resources for shared use by multiple customers via the Internet. Cloud providers sometimes maintain smaller <b>edge data centers</b> closer to customers for lower latency or data-intensive workloads like big-data analytics."),
    DEF("<b>Edge cloud (or fog)</b>: cloud computing that occurs at the network edge (the point where data is exchanged between devices — computers, smartphones, sensors, IoT devices — and cloud services) instead of sending data back to a central data center or private cloud. Advantages: reducing data latency; maintaining high availability by processing data closer to the source (if one edge location fails, another nearby can take over); and reducing the risk of unauthorized access to sensitive data via public networks."),
    DEF("<b>AI model</b>: a program trained on a set of data to perform specific tasks like recognizing certain patterns or making certain decisions. It uses algorithms to learn from data and apply that learning to achieve pre-defined objectives, and can make predictions when provided with the necessary information. An <b>AI language model</b> is a program that can recognize and generate text based on the preceding words."),
], terms=[
    {"t":"Exascale","d":"Supercomputer performance of at least 10^18 double-precision operations per second (exaFLOPS)."},
    {"t":"Digital twins","d":"A digital counterpart of a real-world physical product/system/process used for simulation, testing, monitoring, maintenance."},
    {"t":"Data Centres","d":"Centralized facilities concentrating IT operations for storing, processing and disseminating data; can be on-premise, cloud or edge."},
    {"t":"Edge cloud (fog)","d":"Cloud computing at the network edge; reduces latency, raises availability, reduces unauthorized-access risk."},
], quiz=[
    mcq("'Exascale' refers to a system capable of at least how many double-precision operations per second?",
        ["10¹⁸ (exaFLOPS)", "10⁹ (gigaFLOPS)", "10¹² (teraFLOPS)", "10¹⁵ (petaFLOPS)"], 0,
        "Exascale: computing systems capable of calculating at least 10^18 IEEE 754 Double Precision operations per second (exaFLOPS).", "Exascale"),
    blank("A digital ______ is the indistinguishable digital counterpart of a real-world physical product, system or process.",
          ["twin","twins"], "Digital twins: digital model of intended or actual real-world physical product, system, or process (physical twin).", "Digital twins"),
    mcq("Edge cloud (fog) is best described as…",
        ["cloud computing that occurs at the network edge",
         "a centralized enterprise data centre",
         "a quantum computer", "a 6G base station"], 0,
        "Edge cloud (or fog): cloud computing that occurs at the network edge instead of sending data back to a central data center.", "Edge cloud"),
])

# -----------------------------------------------------------------------------
# MODULE 1
# -----------------------------------------------------------------------------
S("m1-trio", "m1", "A New ‘Consistent Trio’ — the Industrial-Policy Turn", [
    PR("The <b>Von der Leyen I Commission</b> was a <b>swinging moment</b> in EU industrial policies — shifting between <b>vertical vs horizontal</b> approaches towards <b>competitiveness, resilience and (open) strategic autonomy</b>."),
    T("Module 1 asks: foresight as a beacon of the EU’s new industrial strategy for Europe — <b>why is it linked?</b>"),
    Q("“Industrial strategies today – as seen in the US and China – combine multiple policies, ranging from fiscal policies to encourage domestic production, to trade policies to penalise anti-competitive behaviour, to foreign economic policies to secure supply chains. In the EU context, linking policies in this way requires […] a new industrial strategy for Europe.” — Mario Draghi, ‘The Future of European Competitiveness’, September 2024 ('Soul searching for a new industrial strategy')."),
    EX("The slide pairs the US and China as examples of countries that already <b>combine</b> fiscal, trade and foreign-economic policies into an industrial strategy — the model the EU is urged to emulate."),
], terms=[
    {"t":"Von der Leyen I Commission","d":"Identified in the course as a 'swinging moment' in EU industrial policy (vertical vs horizontal) towards competitiveness, resilience and open strategic autonomy."},
    {"t":"Vertical vs horizontal industrial policy","d":"Vertical = sector/technology-targeted support; horizontal = economy-wide framework conditions. The VdL I Commission swung between them."},
], quiz=[
    mcq("The course calls the Von der Leyen I Commission a 'swinging moment' between which two industrial-policy approaches?",
        ["Vertical vs horizontal", "Fiscal vs monetary", "Open vs closed", "National vs supranational"], 0,
        "Von der Leyen I Commission as a swinging moment in EU industrial policies (vertical vs horizontal) towards competitiveness, resilience and (open) strategic autonomy.", "Industrial policy turn"),
    mcq("Draghi notes that US and Chinese industrial strategies combine fiscal policies, trade policies and…",
        ["foreign economic policies to secure supply chains", "monetary easing", "carbon taxes", "data-protection rules"], 0,
        "…to foreign economic policies to secure supply chains.", "Draghi Report"),
])

S("m1-compass", "m1", "The Competitiveness Compass — Europe’s ‘North Star’", [
    DEF("<b>Competitiveness Compass</b>: a Commission framework (2025), presented as a <b>‘North Star’</b>, to orient Europe towards <b>productivity, innovation, decarbonisation and security</b>."),
    T("Related slides build the theme: ‘A Competitiveness Compass for Europe’, ‘Competitiveness as Europe’s North Star’, ‘A new Competitiveness Compass for Europe’, and ‘Digital innovation-based productivity’."),
    EX("A <b>Competitiveness Coordination Tool (CCT)</b> is presented as part of the Compass machinery."),
    PR("The Compass connects <b>competitiveness</b> to <b>digital innovation-based productivity</b> — i.e. digital technologies are framed as the engine of Europe’s productivity and competitiveness."),
], terms=[
    {"t":"Competitiveness Compass","d":"A 2025 Commission framework, presented as a 'North Star', orienting Europe towards productivity, innovation, decarbonisation and security."},
    {"t":"Competitiveness Coordination Tool (CCT)","d":"A coordination instrument presented as part of the Competitiveness Compass machinery."},
], quiz=[
    blank("The Competitiveness Compass is presented as Europe’s ‘______ Star’.",
          ["North"], "Competitiveness as Europe’s ‘North Star’.", "Competitiveness Compass"),
    mcq("The Competitiveness Compass orients Europe towards which four objectives?",
        ["Productivity, innovation, decarbonisation and security",
         "Trade, defence, agriculture and migration",
         "Tax, spending, debt and deficit",
         "Privacy, transparency, fairness and openness"], 0,
        "Competitiveness Compass: a Commission framework to orient Europe towards productivity, innovation, decarbonisation and security.", "Competitiveness Compass"),
])

S("m1-lens", "m1", "Foresight as a ‘Strategic Lens’", [
    DEF("<b>Foresight</b> is “the discipline of exploring, anticipating and shaping the future”. It is a set of qualitative and quantitative tools and methods to build a <b>safe space to ask disruptive questions</b> and use <b>collective intelligence</b> in a structured way to prepare for future developments/crises (Strategic Foresight Report, 2020)."),
    DEF("<b>Strategic foresight</b> is a <b>foresight-based political narrative</b>, informing today’s policies/decision-making through: analysis of long-term (mega)trends, and short-term horizon scanning."),
    Q("“You are not doing a good job if you are not attracting some incoming fire.” — Hillary Clinton (cited to convey that good foresight challenges the status quo)."),
    T("The slide closes with a ‘Post Scriptum: What foresight is <i>not</i>’ — a reminder that foresight is not prediction/fortune-telling but structured preparation."),
], terms=[
    {"t":"Strategic foresight","d":"A policy discipline of exploring, anticipating and shaping future developments so EU strategies are resilient and future-proof; a foresight-based political narrative informing today's decisions."},
    {"t":"Collective intelligence","d":"Structured pooling of diverse expertise used in foresight to prepare for future developments/crises."},
], quiz=[
    blank("Foresight is defined as 'the discipline of exploring, anticipating and ______ the future'.",
          ["shaping"], "Foresight is “the discipline of exploring, anticipating and shaping the future”.", "Strategic foresight"),
    mcq("According to the 2020 SFR, foresight builds a 'safe space' to…",
        ["ask disruptive questions and use collective intelligence",
         "lobby for national interests", "predict exact future events", "replace democratic debate"], 0,
        "A set of tools and methods to build a safe space to ask disruptive questions and use collective intelligence in a structured way.", "Strategic foresight"),
    mcq("Strategic foresight informs today's policies through long-term (mega)trend analysis and…",
        ["short-term horizon scanning", "annual budget votes", "treaty revision", "comitology"], 0,
        "Strategic foresight: analysis of long-term (mega)trends; short-term horizon scanning.", "Strategic foresight"),
])

S("m1-orga", "m1", "Organisation of Foresight within the EU", [
    LST([
        "A <b>Commissioner in charge of strategic foresight</b> — leading political efforts to embed it into EU policymaking.",
        "Member States’ foresight capabilities supported by an <b>EU Foresight Network of ‘Ministers of the Future’</b>.",
        "The Commission’s <b>Secretariat-General & Joint Research Centre (JRC)</b> are the lead services for implementing this mandate.",
        "<b>9 EU institutions</b> participate in the inter-institutional foresight network <b>ESPAS (European Strategy and Policy Analysis System)</b>.",
    ], lead="Foresight is institutionally embedded across the EU:"),
], terms=[
    {"t":"ESPAS","d":"European Strategy and Policy Analysis System — the inter-institutional foresight network in which 9 EU institutions participate."},
    {"t":"Ministers of the Future","d":"An EU Foresight Network of Member-State ministers supporting national foresight capabilities."},
    {"t":"Joint Research Centre (JRC)","d":"The Commission's science service; with the Secretariat-General it is a lead service implementing the foresight mandate and produces the foresight studies underpinning the SFRs."},
], quiz=[
    blank("The inter-institutional foresight network in which 9 EU institutions participate is called ______ (acronym).",
          ["ESPAS"], "9 EU institutions participate in the inter-institutional foresight network ESPAS (European Strategy and Policy Analysis System).", "ESPAS"),
    mcq("Which two Commission services are the lead services for implementing the foresight mandate?",
        ["Secretariat-General & Joint Research Centre", "DG COMP & DG TRADE", "ECB & EIB", "EEAS & ENISA"], 0,
        "Commission’s Secretariat-General & Joint Research Centre lead services for implementing this mandate.", "ESPAS"),
    mcq("The EU Foresight Network of Member-State ministers is nicknamed the…",
        ["Ministers of the Future", "Council of Elders", "Digital Decade Board", "Foresight College"], 0,
        "Member States’ foresight capabilities supported by an EU Foresight Network of Ministers of the Future.", "Ministers of the Future"),
])

S("m1-commissioner", "m1", "The Foresight Commissioner & Open Strategic Autonomy", [
    Q("“We want to keep Europe at the forefront of the sustainability transition, leveraging our unique social market economy and global trade power. This will help strengthen Europe’s leadership in the world, and our ability to stand on our own while building strong partnerships with others: this is what we call Europe’s open strategic autonomy.” — Maroš Šefčovič, Executive Vice-President for the European Green Deal, Interinstitutional Relations and Foresight."),
    DEF("<b>Open strategic autonomy (OSA)</b>: the EU objective of reducing harmful dependencies while remaining outward-looking and cooperative where possible — being ‘as open as possible, as autonomous as necessary’ (and, more recently, increasingly the other way round)."),
    PR("OSA is the <b>geopolitical dimension of resilience</b>: the freedom and capacity to act in the world in an increasingly contested and multipolar global order."),
], terms=[
    {"t":"Open strategic autonomy (OSA)","d":"Reducing harmful dependencies while staying outward-looking; 'as open as possible, as autonomous as necessary'; the geopolitical dimension of resilience."},
], quiz=[
    blank("OSA is summarised as being 'as open as possible, as ______ as necessary'.",
          ["autonomous"], "OSA is the geopolitical dimension of resilience: being as open as possible, as autonomous as necessary… or, more recently, increasingly the other way round.", "Open strategic autonomy"),
    mcq("Which Commissioner is quoted defining Europe’s open strategic autonomy?",
        ["Maroš Šefčovič", "Ursula von der Leyen", "Mario Draghi", "Thierry Breton"], 0,
        "Maroš Šefčovič, Executive Vice-President for the European Green Deal, Interinstitutional Relations and Foresight.", "Open strategic autonomy"),
])

S("m1-toolbox", "m1", "The Foresight Toolbox", [
    LST([
        "<b>Scenarios</b>: the JRC offers an online <b>Scenario Building and Exploration System</b> to simulate possible future paths on any topic (e.g. ‘what if quantum broke current encryption systems?’).",
        "<b>Megatrends monitoring and implications assessment</b>.",
        "<b>Horizon scanning</b>.",
        "<b>Others</b>: personas, Delphi, vision building, etc.",
        "<b>Tech foresight</b> (e.g. <b>FUTURINNOV</b> to inform the EIC and link with the MFF 2028-2034 via a new <b>Observatory for Emerging Technologies</b>).",
    ], lead="Foresight methods/tools:"),
], terms=[
    {"t":"FUTURINNOV","d":"A tech-foresight initiative to inform the EIC and link with the MFF 2028-2034 via a new Observatory for Emerging Technologies."},
    {"t":"Scenario Building and Exploration System","d":"A JRC online tool to simulate possible future paths on any topic."},
], quiz=[
    mcq("Which is NOT listed as a foresight tool/method in the toolbox?",
        ["Quantitative easing", "Scenarios", "Horizon scanning", "Delphi"], 0,
        "Toolbox: Scenarios; Megatrends monitoring; Horizon scanning; Others: personas, Delphi, vision building; Tech foresight.", "Foresight toolbox"),
    mcq("FUTURINNOV is a tech-foresight initiative designed to inform the EIC and link with…",
        ["the MFF 2028-2034 via a new Observatory for Emerging Technologies",
         "NATO planning", "the ECB's monetary policy", "the AI Act sandboxes"], 0,
        "Tech foresight (e.g. FUTURINNOV to inform the EIC and link with MFF 2028-2034 via a new Observatory for Emerging Technologies).", "FUTURINNOV"),
])

S("m1-megatrends", "m1", "Megatrends & Horizon Scanning", [
    T("The Commission’s <b>Megatrends Hub</b> analyses <b>14 global megatrends</b> from an EU perspective — a crucial methodology underlying the Commission’s Strategic Foresight Reports."),
    DEF("<b>Megatrends</b>: large-scale, long-term driving forces that are observable now and could have significant influence on the future, impacting most human activities, processes and perceptions."),
    DEF("<b>Horizon scanning</b>: the Commission keeps an eye on the horizon to anticipate future developments — especially in areas of disruptive change/innovation like digital. Horizon scanners from <b>ESPAS</b> identify <b>‘signs of change’</b>, then validated as <b>‘weak signals’</b> and explored in terms of their future impact via <b>‘sense-making sessions’</b>. Output: <b>quarterly horizon scanning newsletters</b> presented to the College."),
    EX("Examples cited: the Horizon Scanning bulletins of Dec 2023 and Nov 2025 (HorizonScanning_ESPAS_06.pdf)."),
], terms=[
    {"t":"Megatrends","d":"Large-scale, long-term driving forces observable now that could significantly influence the future across most human activities."},
    {"t":"Horizon scanning","d":"Anticipating future developments by spotting 'signs of change', validating them as 'weak signals', and exploring impact in 'sense-making sessions'; output = quarterly newsletters to the College."},
], quiz=[
    blank("The Commission’s Megatrends Hub analyses ______ global megatrends from an EU perspective.",
          ["14"], "Commission’s Megatrends Hub analyses 14 global megatrends from EU perspective.", "Megatrends"),
    mcq("In horizon scanning, 'signs of change' are first validated as ______ before their impact is explored.",
        ["'weak signals'", "'megatrends'", "'black swans'", "'scenarios'"], 0,
        "Horizon scanners from ESPAS identify ‘signs of change’ then validated as ‘weak signals’ and explored via ‘sense-making sessions’.", "Horizon scanning"),
    mcq("The output of horizon scanning is…",
        ["quarterly horizon scanning newsletters presented to the College",
         "annual budget reports", "binding regulations", "treaty amendments"], 0,
        "Output: quarterly horizon scanning newsletters presented to the College.", "Horizon scanning"),
])

S("m1-sfr", "m1", "The Strategic Foresight Report (SFR)", [
    DEF("<b>Strategic Foresight Report (SFR)</b>: an <b>annual Commission Communication</b>, underpinned by a JRC Foresight study. It addresses cross-cutting strategic issues, proposes increasingly concrete policy recommendations (‘areas for action’), builds the case for future EU or national initiatives, and mainstreams ideas via the Foresight Networks’ inclusive participatory process."),
    EX("Each SFR pairs a <b>Science for Policy Report</b> (JRC) with a <b>Commission Communication</b>."),
], terms=[
    {"t":"Strategic Foresight Report (SFR)","d":"Annual Commission Communication, underpinned by a JRC foresight study; proposes 'areas for action' and builds the case for future initiatives."},
], quiz=[
    mcq("The Strategic Foresight Report is best described as…",
        ["an annual Commission Communication underpinned by a JRC foresight study",
         "a binding regulation", "a treaty protocol", "a one-off Draghi report"], 0,
        "Annual Commission Communication, underpinned by JRC’s Foresight study.", "SFR"),
    blank("The SFR proposes increasingly concrete policy recommendations called ‘areas for ______’.",
          ["action"], "Proposing increasingly concrete policy recommendations (“areas for action”).", "SFR"),
])

S("m1-mainstreaming", "m1", "Mainstreaming Resilience, OSA & Sustainable Competitiveness", [
    Q("“[…] investing in our European tech sovereignty, we want to create links and not dependencies […]” — Commission President Ursula von der Leyen, State of the Union Speech, 15 September 2021."),
    EX("<b>Spain</b> put open strategic autonomy as the <i>fil rouge</i> of its <b>2023 Presidency</b>: the foresight study “Resilient EU 2030” on reinforcing the EU’s OSA and global leadership, with the Commission and a cluster of Member States; an informal European Council on 6 October 2023 discussed this and issued a Leaders’ Declaration."),
    T("<b>Mainstreaming resilience</b> in the European Semester via <b>Resilience Dashboards</b>. The <b>2021 Annual Sustainable Growth Survey</b> (Nov 2020) mentioned resilience 69 times, defined along the lines of the 2020 SFR."),
    LST([
        "The <b>2022 SFR</b> studied forward-looking interplays between the green and digital transitions to maximise synergies and assuage trade-offs across <b>5 critical sectors towards 2050</b>.",
        "A <b>2023 JRC Foresight Study</b> set out <b>4 scenarios</b> for a sustainable EU in 2050.",
        "Key idea of <b>dynamic policy coherence</b> underlying the 2023 SFR: digitalisation can help assuage the <b>‘North Star trilemma’</b> between competitiveness, decarbonisation and security (Module 4).",
    ], lead="Mainstreaming sustainable competitiveness:"),
    EX("Update of the new EU industrial strategy (May 2021) aimed to “respond to the lessons learned from the crisis to enhance the EU's open strategic autonomy” and “strengthen the resilience of the Single Market”, with a new focus on the <b>mitigation of excessive dependencies</b>."),
], terms=[
    {"t":"North Star trilemma","d":"The tension between competitiveness, decarbonisation and security that digitalisation can help assuage (underpins the 2023 SFR)."},
    {"t":"Resilience Dashboards","d":"Tools mainstreaming resilience in the European Semester."},
    {"t":"Resilient EU 2030","d":"A foresight study (Spain's 2023 Presidency, with the Commission and Member States) to reinforce the EU's OSA and global leadership."},
], quiz=[
    mcq("Which Member State made open strategic autonomy the 'fil rouge' of its 2023 Presidency?",
        ["Spain", "France", "Germany", "Italy"], 0,
        "Spain put open strategic autonomy as the fil rouge of its Presidency in 2023.", "OSA mainstreaming"),
    mcq("The 'North Star trilemma' that digitalisation can help assuage is between…",
        ["competitiveness, decarbonisation and security",
         "openness, autonomy and partnership",
         "AI, chips and cloud",
         "trade, fiscal and monetary policy"], 0,
        "Digitalization can help assuage the ‘North Star trilemma’ between competitiveness, decarbonization, and security.", "North Star trilemma"),
    blank("The 2022 SFR examined green-digital interplays across 5 critical sectors towards the year ______.",
          ["2050"], "2022 SFR on forward-looking interplays between the green and digital transitions… across 5 critical sectors towards 2050.", "2022 SFR"),
    mcq("Whose 2021 State of the Union line is 'we want to create links and not dependencies'?",
        ["Ursula von der Leyen", "Maroš Šefčovič", "Mario Draghi", "Hillary Clinton"], 0,
        "Commission President Ursula von der Leyen, State of the Union Speech, 15 September 2021.", "OSA mainstreaming"),
])

S("m1-linking", "m1", "Linking Foresight & the New EU Industrial Strategy", [
    Q("EU industrial policy is an example of the point of inflection towards a ‘geopolitical Commission’ due to “increased awareness of the need for more assertiveness and coherence between domestic and external policy agendas and across time horizons” (Lorenzani D. and M. Szapiro, 2023)."),
    PR("The SFRs have contributed to mainstreaming <b>resilience, open strategic autonomy and sustainable competitiveness</b> as pillars of a new industrial policy (Lorenzani D., 2024)."),
    DEF("<b>Mitigation of excessive dependencies</b>: based on JRC foresight input, the EU mapped (excessive) dependencies across <b>11 sensitive industrial ecosystems</b> — i.e. (over)reliance on a limited number of actors for the supply of goods, services, data, infrastructures, skills and technologies, with limited capacity for internal production to substitute imports critical to the Union’s and Member States’ strategic interests."),
], terms=[
    {"t":"Geopolitical Commission","d":"Lorenzani & Szapiro (2023): a point of inflection towards more assertiveness and coherence between domestic and external agendas across time horizons."},
    {"t":"11 sensitive industrial ecosystems","d":"The ecosystems across which the EU mapped excessive dependencies (over-reliance on limited actors for goods, services, data, infrastructures, skills, technologies)."},
], quiz=[
    blank("The EU mapped excessive dependencies across ______ sensitive industrial ecosystems.",
          ["11"], "(Excessive) dependencies across 11 sensitive industrial ecosystems.", "Mitigation of dependencies"),
    mcq("Lorenzani & Szapiro (2023) describe the EU industrial-policy turn as a point of inflection towards a…",
        ["'geopolitical Commission'", "'digital single market'", "'fiscal union'", "'defence union'"], 0,
        "EU industrial policy as example of the point of inflection towards a ‘geopolitical Commission’ (Lorenzani & Szapiro, 2023).", "Geopolitical Commission"),
    mcq("Per Lorenzani (2024), the SFRs mainstreamed which three pillars of a new industrial policy?",
        ["Resilience, open strategic autonomy and sustainable competitiveness",
         "Tax, trade and defence",
         "AI, chips and cloud",
         "DSA, DMA and AI Act"], 0,
        "The SFRs have contributed to mainstream resilience, open strategic autonomy, and sustainable competitiveness as pillars of a new industrial policy.", "Linking foresight"),
])

S("m1-takeaways", "m1", "Module 1 — Key Takeaways", [
    LST([
        "Strategic foresight is the <b>analytical lens</b> of this course.",
        "The Strategic Foresight Reports and other foresight input guided the Commission’s <b>geopolitical awakening</b> via more policy coherence around the concepts of <b>resilience, open strategic autonomy and sustainable competitiveness</b>.",
        "The EU’s <b>industrial strategy</b> is the area most affected by this shift, through a new focus on sustainable competitiveness and <b>mitigation of excessive strategic dependencies</b>, as shown by the new Competitiveness Compass for Europe.",
        "The rest of the course investigates how specific pieces of EU (digital) laws and policies fit this framework — with a focus on <b>innovation and security (Module 2)</b>, <b>regulatory superpower (Module 3)</b> and <b>dynamic coherence vis-à-vis green and social aspects (Module 4)</b>.",
    ], lead="The four key takeaways of Module 1:"),
], terms=[], quiz=[
    mcq("Module 1's takeaway names strategic foresight as the course's…",
        ["analytical lens", "funding tool", "enforcement body", "trade instrument"], 0,
        "Strategic foresight is the analytical lens of this course.", "Module 1 takeaways"),
    mcq("Module 2, 3 and 4 focus respectively on…",
        ["innovation & security; regulatory superpower; dynamic green/social coherence",
         "trade; defence; agriculture",
         "AI; chips; cloud",
         "DSA; DMA; AI Act"], 0,
        "…innovation and security (module 2), regulatory superpower (module 3), and dynamic coherence vis-à-vis green and social aspects (module 4).", "Module 1 takeaways"),
])

# -----------------------------------------------------------------------------
# MODULE 2
# -----------------------------------------------------------------------------
S("m2-intro", "m2", "Module 2 — A New EU Digital Industrial Strategy", [
    T("Module 2: a new EU digital industrial strategy and its <b>geopolitical/geoeconomic relevance</b>. Focus: the <b>build-up and diffusion of advanced technologies</b>."),
    LST([
        "<b>More tech foresight & security of supply</b> (identify high-potential techs to invest in or secure supply chains). <i>Example: Chips Act + Economic Security Doctrine.</i>",
        "<b>State-of-the-art enablers</b>: fast and secure connectivity infrastructure, HPC, spectrum, etc. <i>Example: AI Gigafactories + Cybersecurity Act.</i>",
        "<b>Forward-looking approach to diffuse AI and general-purpose techs</b> across industrial sectors of strength (‘vertical AI use cases’). <i>Example: Apply AI + Cloud & AI Development Act.</i>",
    ], lead="The three pillars of the new digital industrial strategy:"),
], terms=[
    {"t":"Vertical AI use cases","d":"Diffusion of AI and general-purpose technologies across industrial sectors of strength (e.g. Apply AI strategy)."},
], quiz=[
    mcq("Which is one of the three pillars of the new EU digital industrial strategy?",
        ["State-of-the-art enablers (connectivity, HPC, spectrum)",
         "A single EU corporate tax", "A common EU army", "A federal budget"], 0,
        "Pillars: tech foresight & security of supply; state-of-the-art enablers; vertical AI use cases.", "Module 2 pillars"),
    mcq("The example paired with 'tech foresight & security of supply' is…",
        ["Chips Act + Economic Security Doctrine",
         "AI Gigafactories + Cybersecurity Act",
         "Apply AI + Cloud & AI Development Act",
         "DSA + DMA"], 0,
        "More tech foresight & security of supply… Example: Chips Act + Economic Security Doctrine.", "Module 2 pillars"),
])

S("m2-mtt", "m2", "The EU’s ‘Middle Technology Trap’", [
    DEF("<b>Middle technology trap</b>: the EU specialises in mid-tech, mature industries (notably automotive) rather than the frontier digital/software sectors where the US (and increasingly others) lead — leaving Europe stuck in the middle of the value/technology ladder."),
    EX("Top firms by market value illustrate the gap. <b>US (2003 → 2012 → 2022)</b>: Ford/Pfizer/GM → Microsoft/Intel/Merck → <b>Google, Meta, Microsoft (all software)</b>. <b>EU (2003 → 2012 → 2022)</b>: Mercedes/Siemens/VW → VW/Mercedes/Bosch → <b>VW, Mercedes, Bosch (all auto)</b> (Science, research and innovation performance of the EU, 2024)."),
    EX("Evidence base: the <b>European Innovation Scoreboard 2024</b>."),
], terms=[
    {"t":"Middle technology trap","d":"The EU's over-specialisation in mid-tech, mature sectors (e.g. automotive) instead of frontier digital/software, leaving it lagging at the technology frontier."},
    {"t":"European Innovation Scoreboard","d":"Annual EU benchmark of innovation performance (2024 edition cited)."},
], quiz=[
    mcq("The 'middle technology trap' describes the EU being stuck in…",
        ["mid-tech, mature sectors (e.g. automotive) rather than frontier software/digital",
         "low-tech agriculture only", "frontier quantum computing", "defence manufacturing"], 0,
        "The EU’s middle technology trap: EU top firms remained auto (VW, Mercedes, Bosch) while US shifted to software (Google, Meta, Microsoft).", "Middle technology trap"),
    mcq("By 2022 the EU's most valuable companies were dominated by which sector?",
        ["Automotive (VW, Mercedes, Bosch)", "Software", "Pharma", "Hardware"], 0,
        "EU 2022: VW (auto), Mercedes (auto), Bosch (auto).", "Middle technology trap"),
])

S("m2-rilifecycle", "m2", "The Research & Innovation Lifecycle: Capital, Knowledge, Scale", [
    PR("The R&I lifecycle is presented along three needs: <b>CAPITAL</b>, <b>KNOWLEDGE</b> and <b>SCALE</b> — to escape the middle technology trap, the EU must connect funding, research excellence and scale-up capacity."),
    EX("On <b>CAPITAL</b>, the slide details <b>Horizon Europe</b> by pillar (figures in € bn): Pillar 1 ‘Excellent Science’ (25) incl. ERC (16), MSCA (6.6), Research infrastructures (2.4); Pillar 2 ‘Global Challenges’ (53.5) incl. Cluster 4 ‘Digital, Industry and Space’ (15.3) and Cluster 5 ‘Climate, Energy and Mobility’ (15.1); Pillar 3 ‘Innovative Europe’ (13.6) incl. EIC (10.1)."),
    T("SCALE is highlighted as the EU’s persistent weakness: European innovators struggle to scale up to global size."),
], terms=[
    {"t":"R&I lifecycle (CAPITAL/KNOWLEDGE/SCALE)","d":"The three needs of the research & innovation lifecycle the EU must connect to exit the middle technology trap."},
    {"t":"Horizon Europe","d":"The EU R&I framework programme, structured in 3 pillars (Excellent Science; Global Challenges; Innovative Europe incl. the EIC)."},
    {"t":"European Innovation Council (EIC)","d":"Part of Horizon Europe Pillar 3 (Innovative Europe), ~€10.1bn, supporting breakthrough/scale-up innovation."},
], quiz=[
    mcq("The Research & Innovation lifecycle is presented along which three needs?",
        ["Capital, Knowledge and Scale", "Promote, Protect, Partner", "Reduce, Reuse, Recycle", "People, Planet, Profit"], 0,
        "Research & innovation lifecycle: CAPITAL / KNOWLEDGE / SCALE.", "R&I lifecycle"),
    mcq("Within Horizon Europe, the European Innovation Council (EIC) sits in which pillar?",
        ["Pillar 3 – Innovative Europe", "Pillar 1 – Excellent Science", "Pillar 2 – Global Challenges", "It is not in Horizon Europe"], 0,
        "PILLAR 3: Innovative Europe, 13.6 — EIC, 10.1.", "Horizon Europe"),
])

S("m2-chipsact", "m2", "The EU Chips Act — Three Pillars", [
    DEF("<b>EU Chips Act</b>: an EU Regulation that entered into force in <b>September 2023</b> — the leitmotiv of the President’s State of the Union address — providing a framework to raise the EU’s production share to <b>20% by 2030</b>."),
    LST([
        "<b>Pillar 1 — ‘Chips for Europe’ initiative</b>: pilot lines for testing advanced chips (incl. quantum); a cloud-based electronic-design-automation (EDA) platform; chips competence centres in MS to boost skills; a <b>Chips Fund</b> (3.3 bn EUR from Horizon Europe & Digital Europe Programme, blended under InvestEU & EIC) to catalyse <b>43 bn EUR</b> public/private investment by 2030.",
        "<b>Pillar 2 — Security of supply and resilience</b>: FOAK (first-of-a-kind) integrated production facilities (IPF) & open EU foundries (OEF) ‘of public interest’ can access financial aid and admin support (e.g. fast construction permits); Design Centres of Excellence.",
        "<b>Pillar 3 — Monitoring and crisis response</b>: a <b>European Semiconductor Board (ESB)</b> supports the Commission in strategic mapping and monitoring (incl. preventive measures if national authorities alert COM); an <b>emergency toolbox</b> (QMV in Council) if serious disruptions affect a critical sector: (1) information gathering from firms (enforced with fines); (2) priority-rated orders (last resort, after consulting ESB); (3) common purchasing of crisis-related products.",
    ], lead="The three pillars:"),
], terms=[
    {"t":"EU Chips Act","d":"EU Regulation (in force Sept 2023) to raise the EU chip production share to 20% by 2030; 3 pillars: Chips for Europe; security of supply; monitoring/crisis response."},
    {"t":"European Semiconductor Board (ESB)","d":"Supports the Commission in strategic mapping/monitoring of chips and is consulted before priority-rated orders."},
    {"t":"FOAK","d":"First-of-a-kind facilities (integrated production facilities/open EU foundries) eligible for aid and fast permits under the Chips Act."},
], quiz=[
    blank("The EU Chips Act aims to raise the EU’s chip production share to ______% by 2030.",
          ["20"], "Framework to raise production share to 20% by 2030.", "EU Chips Act"),
    mcq("When did the EU Chips Act Regulation enter into force?",
        ["September 2023", "January 2020", "December 2025", "2018"], 0,
        "EU Regulation entered into force in Sep 2023.", "EU Chips Act"),
    blank("The Chips Fund provides 3.3 bn EUR aiming to catalyse ______ bn EUR of public/private investment by 2030.",
          ["43"], "Chips Fund: 3.3 bn EUR… to catalyse 43 bn EUR public/private investment by 2030.", "EU Chips Act"),
    mcq("The Chips Act emergency toolbox (Pillar 3) includes all EXCEPT:",
        ["Nationalising foreign foundries",
         "Information gathering from firms (enforced with fines)",
         "Priority-rated orders (last resort)",
         "Common purchasing of crisis-related products"], 0,
        "Emergency toolbox: 1) information gathering (fines); 2) priority-rated orders; 3) common purchasing.", "EU Chips Act"),
])

S("m2-stateaid", "m2", "Bespoke State Aid & the ‘Chips Subsidies Race’", [
    T("EU state-aid rules allow targeted support for chips <b>R&D</b> but not <b>manufacturing</b>; moreover, <b>IPCEIs</b> are complex and lengthy (up to 3 years) — e.g. the 2nd IPCEI on Microelectronics and Communication Technologies (June 2023)."),
    Q("The Chips Act introduced a bespoke State aid approach for chips manufacturing: “Commission recognizes the need for a case-by-case assessment, where public support includes State aid that does not fall under existing guidelines […] may be justified […] up to 100% of a proven funding gap, if such facilities would otherwise not exist in Europe.”"),
    LST([
        "Criteria: <b>FOAK; cross-border impact; supply security; funding-gap analysis</b>.",
        "Scale of the global race (announced/subsidy programmes): <b>EU ~EUR 100 bn announced</b>; <b>US CHIPS and Science Act $53 bn</b> (tax incentives, state grants); <b>China $150–200 bn</b>; <b>Japan $5 bn</b>.",
        "Direction of travel: towards a <b>Chips Act 2.0 in 2026</b>.",
    ], lead="Key facts:"),
], terms=[
    {"t":"IPCEI","d":"Important Projects of Common European Interest — complex, lengthy (up to 3 years) state-aid vehicles; e.g. 2nd IPCEI on Microelectronics (June 2023)."},
    {"t":"Bespoke State aid (chips)","d":"A case-by-case Chips Act approach allowing aid up to 100% of a proven funding gap for FOAK facilities that would otherwise not exist in Europe."},
], quiz=[
    blank("Under the Chips Act bespoke State aid approach, support may cover up to ______% of a proven funding gap.",
          ["100"], "…may be justified […] up to 100% of a proven funding gap, if such facilities would otherwise not exist in Europe.", "State aid"),
    mcq("The US CHIPS and Science Act is cited at roughly…",
        ["$53 bn", "$5 bn", "$150–200 bn", "€100 bn"], 0,
        "US CHIPS and Science Act ($53 bn, tax incentives, state grants).", "Chips subsidies race"),
    mcq("EU state-aid rules traditionally allow targeted support for chips R&D but NOT for…",
        ["manufacturing", "research", "training", "design"], 0,
        "EU state aid rules allow targeted support for chips R&D but not manufacturing.", "State aid"),
])

S("m2-chipswar", "m2", "Security Dimension — the ‘Chips War’", [
    PR("The EU Chips Act is an example of efforts towards a new EU industrial policy for <b>critical tech inputs</b> like semiconductors (more domestic capacities & more secure supply from third countries)."),
    DEF("<b>Battle of narratives, offers and models</b> (2023 SFR): EU tech sovereignty helps fight a battle on the global stage and is key for security & defence (a stronger Europe in the world) and EU values (a Europe that protects), vis-à-vis: third countries’ propaganda amplified by social media/AI; and third countries’ alternative offers to the EU <b>Global Gateway</b> or the <b>Partnership for Global Infrastructure & Investment</b> (e.g. China’s <b>Belt and Road Initiative</b> and <b>Digital Silk Road</b>)."),
    PR("Securing critical digital infrastructure matters for global influence and for the <b>‘battle of models’</b> between democratic and authoritarian regimes."),
], terms=[
    {"t":"Battle of narratives, offers and models","d":"The global contest (2023 SFR) in which EU tech sovereignty competes with third-country propaganda and alternative offers (e.g. Belt and Road)."},
    {"t":"Global Gateway","d":"The EU's connectivity-investment offer, rivalled by China's Belt and Road / Digital Silk Road."},
], quiz=[
    mcq("The 2023 SFR frames EU tech sovereignty as fighting a 'battle of narratives, offers and…'",
        ["models", "armies", "currencies", "tariffs"], 0,
        "EU tech sovereignty contributes to fighting a battle of narratives, of offers and of models on the global stage (2023 SFR).", "Chips War"),
    mcq("Which Chinese initiatives are cited as alternatives to the EU Global Gateway?",
        ["Belt and Road Initiative and Digital Silk Road",
         "CHIPS and Science Act", "Made in China 2025 and AI Act", "BRICS and SCO"], 0,
        "…third countries’ alternative offers to the EU Global Gateway… (e.g. Belt and Road Initiative and Digital Silk Road).", "Global Gateway"),
])

S("m2-econsec", "m2", "Economic Security Strategy — the 3 P’s", [
    DEF("<b>Economic Security Strategy</b> (2023 Communication): a new comprehensive (country-agnostic?) approach to <b>risk management</b> built on the <b>3 P’s — promoting</b> competitiveness, <b>protecting</b> economic security, <b>partnering</b> with like-minded countries (…and Preparing?) — to jointly assess and minimise risks related to: supply-chain resilience; physical and cyber security of critical infrastructure; technology security and leakage; and the weaponisation of dependencies and economic coercion."),
    EX("Tool-testing & evidence-building (2023-2025): a recommendation lists <b>10 critical technologies</b> for risk mitigation and flags <b>4 high-risk areas</b> (<b>advanced chips, AI, quantum, biotech</b>) for immediate joint risk assessment and evaluation of the need for restrictive measures or support (under <b>STEP</b>). Complemented by pilots on FDI screening, export controls and outbound investments."),
], terms=[
    {"t":"Economic Security Strategy (3 P's)","d":"2023 risk-management approach: Promoting competitiveness, Protecting economic security, Partnering with like-minded countries (…and Preparing?)."},
    {"t":"4 high-risk areas","d":"Advanced chips, AI, quantum and biotech — flagged for immediate joint risk assessment."},
    {"t":"STEP","d":"Strategic Technologies for Europe Platform — vehicle under which support/restrictive measures for critical tech are evaluated."},
], quiz=[
    mcq("The Economic Security Strategy's '3 P's' are…",
        ["Promoting, Protecting, Partnering", "People, Planet, Profit", "Predict, Prevent, Prepare", "Price, Product, Place"], 0,
        "3 P’s: promoting competitiveness, protecting economic security, partnering with like-minded countries… and Preparing?", "Economic Security Strategy"),
    blank("The Economic Security Strategy flags 4 high-risk areas: advanced chips, AI, quantum and ______.",
          ["biotech","biotechnology"], "…flags 4 high-risk areas (advanced chips, AI, quantum, biotech).", "Economic Security Strategy"),
    blank("A recommendation lists ______ critical technologies for risk mitigation.",
          ["10","ten"], "recommendation lists 10 critical technologies for risk mitigation.", "Economic Security Strategy"),
])

S("m2-doctrine", "m2", "The Economic Security Doctrine (Dec 2025)", [
    LST([
        "<b>Tighter FDI Screening</b>: a 2024 Regulation to create conformity in inbound investment screening (minimum sectoral scope, extended targets, all MS with a screening regime).",
        "<b>Coordination among MS’ export controls</b>, against unilateral measures and based on common EU lists (2024 White Paper).",
        "<b>Outbound Investments screening</b>: a 2025 Recommendation to avoid circumvention of export controls and leakage.",
        "<b>Scale up dual-use / advanced-tech R&D and prevent technology leakage</b>: tailoring cross-sector EU programmes to finance it (linking the EU Chips Act with Horizon) and boosting research security vis-à-vis third countries (including a new EU Centre).",
    ], lead="Operationalisation with the December 2025 Economic Security Doctrine:"),
    PR("The Doctrine makes these standard components of an EU economic-security governance, classified in <b>6 high-risk areas</b>, tied to risk thresholds, and thus normalised and scalable."),
], terms=[
    {"t":"Economic Security Doctrine (Dec 2025)","d":"Operationalises economic security via FDI screening, export-control coordination, outbound-investment screening and dual-use R&D; 6 high-risk areas tied to risk thresholds."},
], quiz=[
    mcq("The December 2025 Economic Security Doctrine classifies risks into how many high-risk areas?",
        ["6", "4", "10", "3"], 0,
        "The Doctrine makes these standard components… classified in 6 high-risk area, tied to risk thresholds.", "Economic Security Doctrine"),
    mcq("Which is a pillar of the Economic Security Doctrine?",
        ["Outbound investment screening (2025 Recommendation)",
         "A single EU defence budget", "A carbon border tax", "A digital euro"], 0,
        "Outbound Investments screening: 2025 Recommendation to avoid circumvention of export controls and leakage.", "Economic Security Doctrine"),
])

S("m2-infra", "m2", "State-of-the-Art Enablers — Digital Infrastructure", [
    DEF("<b>Digital Decade Policy Programme (DDPP)</b>: a governance framework with <b>targets for 2030</b> and a monitoring system with annual reports based on <b>DESI</b> (Digital Economy and Society Index). Member States produce <b>2-yearly Digital Decade Roadmaps</b> towards the 2030 targets."),
    LST([
        "Support to multi-country projects via <b>EU Digital Infrastructure Consortia (EDICs)</b>, combining investment from the EU, MS and the private sector (3 set up in 2024).",
        "<b>Digital Rights & Principles</b> (see Module 4).",
        "The draft <b>Digital Networks Act (DNA — 21/1/26)</b> aims to achieve the 2030 Digital Decade targets for digital infrastructure.",
    ], lead="Key instruments:"),
], terms=[
    {"t":"Digital Decade Policy Programme (DDPP)","d":"Governance framework with 2030 targets and DESI-based monitoring; MS produce 2-yearly Digital Decade Roadmaps."},
    {"t":"DESI","d":"Digital Economy and Society Index — the basis for Digital Decade annual monitoring reports."},
    {"t":"EDICs","d":"EU Digital Infrastructure Consortia — vehicles for multi-country projects combining EU, MS and private investment (3 set up in 2024)."},
], quiz=[
    mcq("The Digital Decade Policy Programme's annual monitoring reports are based on which index?",
        ["DESI", "DMA", "DSA", "MFF"], 0,
        "DDPP: monitoring system with annual reports based on DESI.", "DDPP"),
    blank("Multi-country digital projects are supported via EU Digital Infrastructure Consortia, known by the acronym ______.",
          ["EDICs","EDIC"], "EU Digital Infrastructure Consortia (EDICs).", "EDICs"),
])

S("m2-cyber", "m2", "The EU Cybersecurity Acquis", [
    LST([
        "<b>NIS2 Directive</b>",
        "<b>Cybersecurity Act</b>",
        "<b>Cyber Resilience Act</b> (+ sectoral acts and a cyber-diplomacy toolbox)",
    ], lead="Three pillars of the cybersecurity acquis:"),
    DEF("<b>NIS2</b>: a mechanism of EU-wide cooperation on the cyber-security of critical infrastructure (network and information systems for essential and important entities) with harmonised requirements (e.g. cyber-risk management, business continuity, reporting to national authorities) and <b>fines up to 2% of turnover</b> otherwise. <b>Essential entities</b> include energy, healthcare, public sector, banking, transport, digital infrastructure (and submarine cables under certain conditions). <b>Important entities</b> include digital service providers, food production and waste management — a whole-of-supply-chain/systemic approach."),
    DEF("<b>Cyber Resilience Act (CRA)</b>: a regulation introducing mandatory cybersecurity requirements for manufacturers throughout the product lifecycle. Compliance (acknowledged via <b>CE marking</b>) is required for EU market access (from <b>2027</b>) and enforced with fines up to <b>EUR 15 mn or 2.5% of turnover</b>."),
    DEF("<b>EU Cybersecurity Act</b>: a regulation on a <b>voluntary</b> EU cybersecurity certification for products, services and processes. Certificates are recognised in all MS and encourage <b>security-by-design</b>, making cross-border trade easier — cybersecurity becomes a competitive advantage for EU industry. It gives a <b>permanent mandate to ENISA</b> and creates a new <b>EU Cybersecurity Competence Centre (ECCC) in Bucharest</b> to ensure MS synergies."),
], terms=[
    {"t":"NIS2 Directive","d":"EU-wide cooperation on cybersecurity of critical infrastructure; harmonised requirements for essential and important entities; fines up to 2% of turnover."},
    {"t":"Cyber Resilience Act (CRA)","d":"Mandatory lifecycle cybersecurity requirements for manufacturers; CE marking; EU market access from 2027; fines up to €15mn or 2.5% turnover."},
    {"t":"EU Cybersecurity Act","d":"Voluntary EU cybersecurity certification scheme; security-by-design; permanent ENISA mandate; ECCC in Bucharest."},
    {"t":"ENISA","d":"The EU Agency for Cybersecurity, given a permanent mandate by the Cybersecurity Act."},
], quiz=[
    mcq("The three pillars of the EU cybersecurity acquis are…",
        ["NIS2 Directive, Cybersecurity Act, Cyber Resilience Act",
         "DSA, DMA, AI Act", "GDPR, ePrivacy, NIS1", "Chips Act, STEP, EDICs"], 0,
        "Pillars: (1) NIS2 Directive; (2) Cybersecurity Act; (3) Cyber Resilience Act.", "Cybersecurity acquis"),
    mcq("The Cyber Resilience Act is enforced with fines up to…",
        ["EUR 15 mn or 2.5% of turnover", "EUR 35 mn or 7% of turnover", "2% of turnover", "EUR 5 mn flat"], 0,
        "Cyber Resilience Act… enforced with fines up to EUR 15 mn or 2.5% of turnover.", "Cyber Resilience Act"),
    mcq("The EU Cybersecurity Act sets up a certification scheme that is…",
        ["voluntary", "mandatory for all products", "limited to defence", "only for banks"], 0,
        "EU Cybersecurity Act: Regulation on a voluntary EU cybersecurity certification for products, services, and processes.", "EU Cybersecurity Act"),
    blank("The new EU Cybersecurity Competence Centre (ECCC) is located in ______.",
          ["Bucharest"], "new EU Cybersecurity Competence Centre (ECCC) in Bucharest to ensure MS’ synergies.", "ECCC"),
    mcq("Under NIS2, which is an 'essential entity'?",
        ["Energy", "Food production", "Waste management", "Generic digital service providers"], 0,
        "Essential entities (e.g., energy, healthcare, public sector, banking, transport, and digital infrastructure).", "NIS2"),
])

S("m2-cables", "m2", "State-of-the-Art Enablers — Submarine Cables", [
    PR("The EU’s technological sovereignty is challenged by the <b>weaponisation of interdependence</b> by third countries, relevant for critical digital infrastructure."),
    EX("China’s <b>HMN</b> constructed and upgraded undersea cables connecting Member States and Indo-Pacific areas with NATO military bases."),
    EX("The US <b>banned Huawei’s equipment</b> and prohibited <b>TikTok on government devices</b>. In the EU: <b>14 MS have no restrictions</b> on high-risk suppliers; only EU institutions and a few MS banned TikTok on government devices."),
], terms=[
    {"t":"Weaponisation of interdependence","d":"The use of supply/infrastructure dependencies (e.g. submarine cables) as leverage by third countries; a challenge to EU tech sovereignty."},
], quiz=[
    mcq("Which company is named as constructing/upgrading undersea cables linking MS and Indo-Pacific areas with NATO bases?",
        ["China's HMN", "Huawei", "TikTok", "Gaia-X"], 0,
        "China’s HMN constructed and upgraded undersea cables connecting MS and Indo-Pacific areas with NATO military bases.", "Submarine cables"),
    blank("On high-risk suppliers, ______ EU Member States have no restrictions.",
          ["14"], "In the EU: 14 MS have no restrictions on high-risk suppliers.", "Submarine cables"),
])

S("m2-hpc", "m2", "AI Vertical Use Cases — Computing Power (HPC)", [
    EX("The EU has a strong position in <b>high-performance computing (HPC)</b> thanks to the <b>EuroHPC Joint Undertaking</b>: <b>4 EU supercomputers are in the top 10 worldwide</b>."),
    DEF("<b>AI Factories Initiative</b>: opens up HPCs to innovative startups to train trustworthy AI models. The EuroHPC Regulation is amended to create <b>AI factories (19 operational across 16 MS)</b> and soon the first <b>4–5 AI Gigafactories</b> in Europe. EuroHPC acquires and operates HPCs to train large <b>GPAI</b> models; facilitates access to public and private users (SMEs); and offers open-source software for innovators in LLMs/algorithms. EU funding, VC & equity (via EIC/InvestEU) for genAI; reskilling & upskilling; and common <b>Data Spaces</b> for AI and novel industrial use cases."),
    T("The <b>AI Office</b> coordinates EU policies on AI and implements the AI Act."),
], terms=[
    {"t":"EuroHPC Joint Undertaking","d":"The EU body for high-performance computing; 4 EU supercomputers are in the global top 10; amended to create AI factories."},
    {"t":"AI Factories / AI Gigafactories","d":"AI factories (19 across 16 MS) open HPCs to startups to train trustworthy AI; the first 4–5 AI Gigafactories are planned for Europe."},
    {"t":"AI Office","d":"Coordinates EU AI policies and implements the AI Act."},
], quiz=[
    blank("Thanks to EuroHPC, ______ EU supercomputers are in the global top 10.",
          ["4","four"], "4 EU supercomputers are in the top 10 worldwide.", "EuroHPC"),
    mcq("How many AI factories are described as operational, and across how many MS?",
        ["19 across 16 MS", "4 across 4 MS", "27 across 27 MS", "10 across 5 MS"], 0,
        "AI factories (19 operational across 16 MS) and soon the first 4-5 AI Gigafactories in Europe.", "AI Factories"),
    mcq("Which body coordinates EU AI policies and implements the AI Act?",
        ["The AI Office", "ENISA", "the ECCC", "the European Semiconductor Board"], 0,
        "AI office coordinates EU policies on AI & implements AI Act.", "AI Office"),
])

S("m2-quantum", "m2", "AI Vertical Use Cases — Quantum Computing", [
    PR("Quantum computing will be the <b>next disruptive technological development</b> and a <b>test for the EU’s OSA</b>."),
    WARN("Security implications: quantum may <b>break the digital encryption systems</b> underpinning security & defence."),
    EX("<b>China appears at the forefront</b>. The EU is far from having <b>3 quantum computers by 2030</b> (a Digital Decade target) but has key strengths: large public capital, excellent skills and a vibrant ecosystem of RTOs/start-ups."),
], terms=[
    {"t":"Quantum (OSA test)","d":"The next disruptive technology and a test for EU open strategic autonomy; could break current encryption; China leads, EU lags the 2030 target of 3 quantum computers."},
], quiz=[
    mcq("Why is quantum computing a security concern in the course?",
        ["It may break the digital encryption systems underpinning security & defence",
         "It causes blackouts", "It is radioactive", "It violates the AI Act"], 0,
        "Security implications: it may break digital encryption systems underpinning security & Defence.", "Quantum"),
    blank("The Digital Decade target is to have ______ quantum computers by 2030 — a goal the EU is far from.",
          ["3","three"], "EU is far from having 3 quantum computers by 2030 (DD target).", "Quantum"),
])

S("m2-cloud", "m2", "AI Vertical Use Cases — Cloud", [
    DEF("<b>IKEA cloud paradox</b>: the EU has <b>lost the cloud market to US hyperscalers</b>, against which direct competition is unrealistic. Past initiatives for a European ‘LEGO cloud’ infrastructure (e.g. <b>Gaia-X</b>) have disappointed."),
    PR("Governments can create space (e.g. via <b>public procurement</b>) for EU ‘<b>sovereign cloud</b>’ solutions, and developing local <b>edge nodes</b> reduces dependence on hyperscalers and ensures data stays in the EU."),
    EX("EU <b>data value loss</b> is estimated at up to <b>90%</b>."),
], terms=[
    {"t":"IKEA cloud paradox","d":"The EU has lost the cloud market to US hyperscalers; competing head-on is unrealistic; a 'LEGO cloud' (e.g. Gaia-X) disappointed."},
    {"t":"Sovereign cloud / edge nodes","d":"EU solutions (supported via public procurement) and local edge nodes that reduce hyperscaler dependence and keep data in the EU."},
    {"t":"Gaia-X","d":"A European 'LEGO cloud' infrastructure initiative cited as having disappointed."},
], quiz=[
    mcq("The 'IKEA cloud paradox' refers to…",
        ["the EU having lost the cloud market to US hyperscalers (head-on competition unrealistic)",
         "cheap Swedish data centres", "modular open-source software", "a quantum encryption flaw"], 0,
        "EU has lost the cloud market to US hyperscalers against which competition is unrealistic (‘IKEA cloud paradox’).", "Cloud"),
    blank("EU data value loss is estimated at up to ______%.",
          ["90"], "EU data value loss estimated at up to 90%.", "Cloud"),
    mcq("Which initiative for a European 'LEGO cloud' is said to have disappointed?",
        ["Gaia-X", "EuroHPC", "STEP", "Global Gateway"], 0,
        "Past initiatives for a European ‘LEGO cloud’ infrastructure (e.g. Gaia-X) have disappointed.", "Cloud"),
])

S("m2-takeaways", "m2", "Module 2 — Key Takeaways", [
    LST([
        "The EU needs a new <b>digital industrial policy focused on open strategic autonomy</b>, combining R&I and industrial policies to exit its <b>middle technology trap</b>.",
        "A new digital industrial policy should leverage at the same time <b>investments and regulation</b>, with three pillars: (i) <b>technology horizon scanning & economic security</b>; (ii) <b>cyber-secure digital infrastructure</b>; and (iii) <b>vertical AI use cases</b>.",
        "This strategy has clear <b>geopolitical and security implications</b> — contributing to a ‘battle of narratives, offers and models’ on the global stage.",
        "Regulatory milestones include: (i) the <b>EU Chips Act and Economic Security Strategy</b>; (ii) the <b>EU cyber-security framework</b>; and (iii) the inter-linked components of the <b>AI Continent Strategy</b> (e.g. AI Gigafactories initiative and steps towards an EU cloud/edge).",
    ], lead="The four key takeaways of Module 2:"),
], terms=[
    {"t":"AI Continent Strategy","d":"The umbrella linking AI Gigafactories, EU cloud/edge steps and related initiatives as part of the new digital industrial policy."},
], quiz=[
    mcq("Module 2's three pillars of a new digital industrial policy are tech horizon scanning & economic security, cyber-secure digital infrastructure and…",
        ["vertical AI use cases", "a federal budget", "a common army", "a digital euro"], 0,
        "Pillars: (i) technology horizon scanning & economic security; (ii) cyber-secure digital infrastructure; and (iii) vertical AI use cases.", "Module 2 takeaways"),
])

# -----------------------------------------------------------------------------
# MODULE 3
# -----------------------------------------------------------------------------
S("m3-intro", "m3", "Module 3 — The EU as a Digital Normative Superpower?", [
    DEF("<b>Normative power / normative superpower</b>: influence based on rules, values and standards rather than military or purely economic coercion. The EU can project power through law by setting binding standards."),
    DEF("<b>Brussels effect</b>: the EU’s capacity to shape global markets through regulation, because firms adapt to EU rules and sometimes diffuse those standards beyond Europe."),
    LST([
        "<b>2021 SFR</b>: ensuring a first-mover position in standard setting.",
        "<b>2022 SFR</b>: a strategic approach to influencing international standardisation, e.g. in batteries.",
        "<b>2023 SFR</b>: a transatlantic marketplace, also in digital standards.",
    ], lead="The SFRs build the standard-setting case:"),
    EX("Digital: pioneering regulations (e.g. the AI Act) for a more human-centric digital transition “have influenced the evolution of the global regulatory framework”. In a global battle of narratives, offers and models, other geo-blocks take assertive standard-setting actions (e.g. <b>China Standards 2035</b>), and ‘Digital Empires’ governance models are evolving or fighting for influence."),
], terms=[
    {"t":"Normative (super)power","d":"Influence via rules, values and standards rather than military/economic coercion."},
    {"t":"Brussels effect","d":"The EU shapes global markets through regulation because firms adapt to EU rules and diffuse them beyond Europe."},
    {"t":"China Standards 2035","d":"China's assertive standard-setting strategy cited as a rival in the global 'battle of models'."},
], quiz=[
    mcq("The 'Brussels effect' means…",
        ["firms adapt to EU rules, diffusing EU standards globally",
         "the EU copies US regulation", "Brussels' weather affects markets", "the EU bans non-EU firms"], 0,
        "Brussels effect: the EU’s capacity to shape global markets through regulation because firms adapt to EU rules and sometimes diffuse those standards beyond Europe.", "Brussels effect"),
    mcq("Which is China's assertive standard-setting strategy cited in the course?",
        ["China Standards 2035", "Made in China 2025", "Belt and Road 2049", "Digital Silk Road 2030"], 0,
        "other geo-blocks are taking assertive standard-setting actions (e.g. China Standards 2035).", "Standardisation"),
])

S("m3-empires", "m3", "Digital Empires & the Battles for Influence", [
    DEF("<b>Digital Empires (Anu Bradford)</b>: a ‘horizontal battle’ for influence (‘<b>regulatory un-peace</b>’) between three governance models. (1) <b>US market-driven model</b>: regulation handed over to tech companies to maximise innovation. (2) <b>China’s state-driven model</b>: authoritarian control enabled by tech-based tools but open to economic interdependence. (3) <b>EU rights-driven model</b>: boosted by economic size."),
    PR("There is also a <b>‘vertical battle’</b> for influence: <b>governments vs tech giants</b>."),
    T("Intersections: acquiescence for economic interest; the need for international techno-democratic regulatory cooperation to meet public opinion’s shift away from trust in market self-regulation; and the question of whether the EU is the only credible techno-democratic alternative offer to China’s."),
], terms=[
    {"t":"Digital Empires","d":"Anu Bradford's framing of three rival digital-governance models (US market-driven, China state-driven, EU rights-driven)."},
    {"t":"Regulatory un-peace","d":"The horizontal battle for influence between geo-blocks over digital governance."},
    {"t":"Horizontal vs vertical battle","d":"Horizontal = between geo-blocks (US/China/EU models); vertical = governments vs tech giants."},
], quiz=[
    mcq("In Bradford's 'Digital Empires', the US model is best described as…",
        ["market-driven (regulation handed to tech companies to maximise innovation)",
         "rights-driven", "state-driven authoritarian control", "foresight-driven"], 0,
        "US market-driven model: regulation handed over to tech companies to maximize innovation.", "Digital Empires"),
    mcq("The EU's governance model in 'Digital Empires' is…",
        ["rights-driven, boosted by economic size",
         "market-driven", "state-driven", "defence-driven"], 0,
        "EU rights-driven model: boosted by economic size.", "Digital Empires"),
    mcq("The 'vertical battle' for influence is between…",
        ["governments vs tech giants", "US vs China", "EU vs UK", "regulators vs courts"], 0,
        "‘Vertical battle’ for influence governments vs. tech giants.", "Digital Empires"),
])

S("m3-ttc", "m3", "EU-US Techno-Democratic Regulatory Alliance? (TTC)", [
    DEF("<b>EU-US Trade and Technology Council (TTC)</b>: one of multiplying policy actions to move towards a ‘<b>transatlantic marketplace</b>’ — including for digital/tech (half of its working groups)."),
    LST([
        "Coordination on the availability of <b>CRMs (critical raw materials)</b> for chips under a joint ‘early warning mechanism’.",
        "Use of digital trade tools to reduce red tape for firms and strengthen common approaches to investment screening and export controls.",
        "Common principles for <b>trustworthy AI</b>.",
    ], lead="TTC digital/tech work includes:"),
    T("Despite current uncertainties, there is a case for more transatlantic regulatory compatibility: EITHER as a <b>veneer</b> motivated by economic interest (e.g. transatlantic personal data flows); OR as <b>true co-regulatory convergence</b> in digital standardisation (as a ‘functional superpower’)."),
], terms=[
    {"t":"EU-US TTC","d":"Trade and Technology Council moving towards a 'transatlantic marketplace'; ~half its working groups are digital/tech."},
    {"t":"Functional superpower","d":"The EU achieving influence through true co-regulatory convergence in digital standardisation."},
], quiz=[
    mcq("The EU-US TTC works towards a…",
        ["'transatlantic marketplace'", "'common army'", "'digital euro'", "'single Atlantic state'"], 0,
        "EU-US TTC as one of multiplying policy actions to move towards a “transatlantic marketplace”.", "TTC"),
    mcq("Which is one of the TTC's digital/tech work areas?",
        ["Common principles for trustworthy AI", "A common corporate tax", "A shared central bank", "Joint nuclear deterrent"], 0,
        "Common principles for trustworthy AI.", "TTC"),
])

S("m3-tools", "m3", "Linking Foresight & Regulation — Agile Regulatory Tools", [
    DEF("Andrea Renda maps regulatory tools by phase of the ‘<b>policy cycle</b>’ (with maturity, government-capacity requirements and innovation impact)."),
    LST([
        "<b>Agenda-setting</b>: crowdsourcing priorities; horizon scanning & strategic foresight; transition pathways and backcasting.",
        "<b>Regulatory</b>: self- and co-regulation & outcome-based regulation; <b>regulatory sandboxes</b> (+ testbeds, policy experiments, innovation deals/hubs); tech sprints and regulatory hackathons.",
        "<b>Implementation/enforcement</b>: regulatory guidance to support compliance; <b>RegTech and SupTech</b>, predictive analytics; innovation hubs.",
    ], lead="Tools by policy-cycle phase (Renda, CEPS):"),
    DEF("<b>Regulatory sandbox</b>: a controlled scheme (under an ‘experimentation clause’) where applicants are screened and tested; results are evaluated for suitability, scalability, representativeness and reliability before deployment/authorisation (or the sandbox ‘fails’)."),
], terms=[
    {"t":"Regulatory sandbox","d":"A controlled testing scheme under an experimentation clause; screens applicants, evaluates results before authorisation."},
    {"t":"RegTech / SupTech","d":"Technology for regulatory compliance (RegTech) and supervision (SupTech), used in implementation/enforcement."},
    {"t":"Backcasting","d":"An agenda-setting foresight tool working backwards from a desired future via transition pathways."},
], quiz=[
    mcq("Regulatory sandboxes, tech sprints and co-regulation belong to which policy-cycle phase?",
        ["Regulatory", "Agenda-setting", "Implementation/enforcement", "Adjudication"], 0,
        "Regulatory: self- and co-regulation; regulatory sandboxes; tech sprints and regulatory hackathons.", "Agile regulation"),
    mcq("Which author maps the regulatory tools by phase of the policy cycle?",
        ["Andrea Renda (CEPS)", "Anu Bradford", "Mario Draghi", "Federico Fabbrini"], 0,
        "Source: Andrea Renda, CEPS (forthcoming).", "Agile regulation"),
])

S("m3-banking", "m3", "Example of a Regulatory Sandbox — Open Banking", [
    EX("The <b>UK’s sandbox for open banking</b> was launched in <b>2016 by the Financial Conduct Authority (FCA)</b> — one of the first of its kind globally."),
    EX("Many tested solutions went to market (e.g. Open Banking apps) and other jurisdictions adopted a similar model based on the UK (and the EU’s <b>PSD2</b>) experience."),
    T("Process flow: an experimentation clause → sandbox screening of applicants → evaluation (suitability, scalability, representativeness, reliability) → if results are sufficiently robust and positive and residual risks are managed with real-world safeguards, the firm exits to authorisation/deployment; otherwise the application is rejected or the sandbox ‘failed’."),
], terms=[
    {"t":"Open banking sandbox","d":"The UK FCA's 2016 sandbox (one of the first globally); influenced other jurisdictions alongside the EU's PSD2."},
    {"t":"PSD2","d":"The EU's revised Payment Services Directive, part of the open-banking experience referenced in the sandbox example."},
], quiz=[
    blank("The UK open-banking sandbox was launched in 2016 by the Financial Conduct Authority (acronym ______).",
          ["FCA"], "UK’s sandbox for open banking launched in 2016 by the Financial Conduct Authority (FCA).", "Open banking sandbox"),
    mcq("The open-banking model spread based on the UK experience and the EU's…",
        ["PSD2", "GDPR", "AI Act", "DMA"], 0,
        "other jurisdictions adopted a similar model based on the UK (and the EU’s PSD2) experience.", "Open banking sandbox"),
])

S("m3-aiact1", "m3", "The AI Act — Normative Superpower in Digital?", [
    DEF("<b>AI Act</b>: the world’s <b>first horizontal regulation on AI</b> — a common binding framework for the use & supply of AI systems in the EU; <b>Regulation (EU) 2024/1689</b>. A clear example of a <b>rights-based normative superpower</b> (with echoes in the US, China, UK and beyond)."),
    PR("It is largely a <b>risk-based and precautionary</b> approach, but offers good examples of <b>agile / experimental / adaptive regulation</b>: co-regulation, compulsory regulatory sandboxes, and guidance for compliance."),
    EX("The <b>AI Pact</b> seeks industry’s voluntary pledges to anticipate AI Act provisions (<b>over 100 in Sep 2024</b>; <b>over 230 in Jan 2026</b>); voluntary codes of conduct for non-high-risk AI systems; EU harmonised standards for presumption of conformity; and pilot sandboxes in the MS since <b>2022 (ES — Spain)</b>."),
], terms=[
    {"t":"AI Act","d":"World's first horizontal AI regulation, Regulation (EU) 2024/1689; rights-based, risk-based, with agile tools (sandboxes, codes, guidance)."},
    {"t":"AI Pact","d":"Voluntary industry pledges to anticipate AI Act provisions (100+ in Sep 2024, 230+ in Jan 2026)."},
], quiz=[
    mcq("The AI Act is notable as…",
        ["the world's first horizontal regulation on AI",
         "a voluntary code only", "a US federal law", "a sectoral medical-device rule"], 0,
        "World’s first horizontal regulation on AI: common binding framework for use & supply of AI systems in EU.", "AI Act"),
    blank("The AI Act's official citation is Regulation (EU) 2024/______.",
          ["1689"], "Artificial Intelligence Act, Regulation (EU) 2024/1689.", "AI Act"),
    mcq("Pilot AI regulatory sandboxes have run in Member States since 2022, starting in…",
        ["Spain (ES)", "France", "Germany", "Italy"], 0,
        "pilot sandboxes in the MS since 2022 (ES).", "AI Act"),
])

S("m3-aiact2", "m3", "The AI Act — Risk-Based Architecture", [
    PR("The AI Act applies to all providers placing AI systems and GPAI models on the EU market (with exceptions such as military)."),
    DEF("<b>Risk-based approach</b>: a <b>ban for 8 unacceptable-risk</b> systems; strong requirements (e.g. <b>conformity assessment</b>) on <b>high-risk</b> ones; <b>transparency obligations</b> on <b>low-risk</b> ones; and <b>minimal obligations</b> otherwise."),
    T("Enforcement is <b>phased</b>, with an attempt to move it forward via the AI Pact with firms. There are special provisions for <b>GPAI models</b> (presumption of conformity via standards), and <b>regulatory sandboxes are mandated at MS level</b> to test innovative solutions."),
], terms=[
    {"t":"AI Act risk tiers","d":"Unacceptable (8 banned), high-risk (conformity assessment), low-risk (transparency), minimal (minimal obligations)."},
    {"t":"Conformity assessment","d":"The strong compliance requirement imposed on high-risk AI systems."},
], quiz=[
    blank("The AI Act bans how many 'unacceptable-risk' AI practices? ______",
          ["8","eight"], "Risk-based approach: ban for 8 unacceptable-risk ones.", "AI Act"),
    mcq("High-risk AI systems under the AI Act face mainly…",
        ["strong requirements such as conformity assessment",
         "an outright ban", "only transparency obligations", "no obligations"], 0,
        "strong requirements (e.g. conformity assessment) on high-risk ones.", "AI Act"),
    mcq("Low-risk AI systems are subject mainly to…",
        ["transparency obligations", "a ban", "conformity assessment", "fines of 7%"], 0,
        "transparency obligations on low-risk ones; minimal obligations otherwise.", "AI Act"),
])

S("m3-aiact3", "m3", "The AI Act — GPAI, Sandboxing & Governance", [
    LST([
        "Vast <b>transparency requirements for all GPAI models</b>.",
        "Special provisions for GPAI models with <b>high-impact capabilities</b> (presumption of posing <b>systemic risks</b>): notification, risk assessment and mitigation.",
        "<b>Codes of practice</b> by the Commission and presumption of conformity for compliance with EU harmonised standards (agile regulation).",
    ], lead="General-purpose AI (GPAI) models:"),
    LST([
        "National authorities must establish <b>at least one regulatory sandbox</b> at national level to facilitate development and testing of innovative AI systems.",
        "Prospective providers of high-risk AI systems may test them in advance in <b>real-world conditions</b> if they respect guarantees (e.g. asking for consent).",
    ], lead="Sandboxing:"),
    DEF("<b>Governance & fines</b>: MS must designate at least a <b>market surveillance authority</b> and a <b>notifying authority</b>. Fines up to <b>EUR 35 million or 7% of total worldwide annual turnover</b> (whichever is higher) for infringements on prohibited practices or non-compliance on data (lower fines for smaller companies). EU-level actors: the Commission (implementing/delegated acts, oversight of standardisation), the <b>AI Board</b>, the <b>AI Office</b> and EU standardisation bodies."),
    WARN("The <b>2025 Digital Omnibus</b> (under negotiation) extends compliance deadlines: currently <b>02/12/27</b> for listed high-risk AI systems (e.g. employment, law enforcement, education) and <b>02/12/28</b> for AI systems embedded in regulated products (e.g. medical devices, machinery)."),
], terms=[
    {"t":"GPAI models","d":"General-purpose AI models; all face transparency requirements; high-impact ones presumed to pose systemic risks (notification, risk assessment, mitigation)."},
    {"t":"AI Act fines","d":"Up to EUR 35 million or 7% of total worldwide annual turnover (whichever higher) for the gravest infringements."},
    {"t":"Digital Omnibus (2025)","d":"Under negotiation; extends AI Act compliance deadlines (02/12/27 for listed high-risk; 02/12/28 for AI in regulated products)."},
], quiz=[
    mcq("The maximum AI Act fine for the gravest infringements is…",
        ["EUR 35 million or 7% of worldwide annual turnover",
         "EUR 15 million or 2.5% of turnover", "2% of turnover", "EUR 20 million flat"], 0,
        "Imposition of fines up to EUR 35 million or 7% of total worldwide annual turnover (whichever the higher).", "AI Act fines"),
    mcq("Under the AI Act, national authorities must establish at least one…",
        ["regulatory sandbox", "AI ministry", "data centre", "supercomputer"], 0,
        "National authorities must establish at least one regulatory sandbox at national level.", "AI Act"),
    mcq("GPAI models with high-impact capabilities are presumed to pose…",
        ["systemic risks", "no risk", "unacceptable risk (banned)", "only transparency risk"], 0,
        "Special provisions for GPAI models with high-impact capabilities (presumption of posing system risks).", "GPAI"),
    mcq("Which two authorities must each MS designate to enforce the AI Act?",
        ["A market surveillance authority and a notifying authority",
         "A central bank and a court", "A data protection authority and a tax office", "An AI Office and an AI Board"], 0,
        "MS must designate at least a market surveillance authority and a notifying authority to ensure enforcement.", "AI Act governance"),
])

S("m3-takeaways", "m3", "Module 3 — Key Takeaways", [
    LST([
        "Key digital regulation across the ‘pillars’ of the <b>Digital Single Market</b> (AI Act, DMA, DSA, etc.) is an area where the EU can still claim a <b>‘normative superpower’</b> status — e.g. via standardisation practices contributing to ‘<b>functional</b>’ sovereignty (and thus OSA) within the Digital Empires’ horizontal and vertical battles for influence.",
        "Despite large and persistent regulatory divergences, moving towards a ‘<b>digital transatlantic marketplace</b>’ via more EU-US (and beyond) regulatory compatibility and cooperation would respond to such geo-economic interests.",
        "<b>Agile regulatory tools</b> — including strategic foresight and private-sector involvement (co-regulation, standardisation, regulatory sandboxes) — also contribute to these strategic goals and are part of a new digital industrial policy.",
    ], lead="The key takeaways of Module 3:"),
], terms=[
    {"t":"Digital Single Market","d":"The EU project of integrating digital markets, reducing fragmentation and creating common rules for online services and digital business."},
], quiz=[
    mcq("Module 3 argues the EU can claim 'normative superpower' status especially through…",
        ["standardisation practices contributing to functional sovereignty",
         "military build-up", "currency devaluation", "withdrawing from global trade"], 0,
        "…via standardization practices contributing to a “functional” sovereignty and thus open strategic autonomy.", "Module 3 takeaways"),
])

# -----------------------------------------------------------------------------
# MODULE 4
# -----------------------------------------------------------------------------
S("m4-intro", "m4", "Module 4 — Dynamic Coherence of the Digital with the Green/Fair Transition", [
    T("Module 4: the <b>dynamic coherence</b> of the digital transition with the green/fair transition — pairing, as in the SFRs, a JRC ‘Science for Policy Report’ with a Commission Communication."),
    PR("Core question: can the digital transition <b>reinforce</b> the green and fair transitions rather than undermine them? Dynamic coherence asks whether policy can manage these interdependencies <b>over time</b>."),
], terms=[
    {"t":"Twinning (green-digital)","d":"The combined green and digital transition; managing synergies and trade-offs between them over time."},
], quiz=[
    mcq("Module 4's central concept for managing green-digital interdependencies over time is…",
        ["dynamic (policy) coherence", "the Brussels effect", "the middle technology trap", "the 3 P's"], 0,
        "Dynamic coherence asks whether policy can manage these interdependencies over time.", "Module 4"),
])

S("m4-trilemma", "m4", "Solving the EU’s Industrial-Policy Trilemma", [
    DEF("<b>Industrial-policy trilemma</b> (Renda, 2024): the tension between <b>competitiveness, decarbonisation and economic security</b> — and, adding <b>fairness</b>, a <b>quadrilemma</b> — that industrial policy must manage."),
    PR("Digitalisation can help <b>solve / assuage</b> the trilemma/quadrilemma by exploiting synergies and reducing trade-offs across these overlapping (and sometimes competing) goals."),
], terms=[
    {"t":"Industrial-policy trilemma/quadrilemma","d":"The tension between competitiveness, decarbonisation, economic security (trilemma) plus fairness (quadrilemma) that industrial policy must manage (Renda, 2024)."},
], quiz=[
    mcq("The industrial-policy trilemma (Renda) is between competitiveness, decarbonisation and…",
        ["economic security", "migration", "monetary policy", "agriculture"], 0,
        "Solving the EU’s industrial policy trilemma… competitiveness and decarbonization (Source: Andrea Renda, 2024).", "Trilemma"),
    blank("Adding fairness turns the industrial-policy trilemma into a ______.",
          ["quadrilemma"], "industrial policy trilemma / quadrilemma between economic security, competitiveness and decarbonization, plus fairness.", "Quadrilemma"),
])

S("m4-2022sfr", "m4", "2022 SFR — Tech Factors to Assuage Trade-offs", [
    EX("The 2022 SFR identifies digital technology factors to assuage green-digital trade-offs, including: <b>digital technologies for sustainable farming</b>; environmental monitoring systems; reduced demand for space; building design and redesign; self-organised <b>microgrids</b> & grid-based governance of the e-system; <b>energy-as-a-service</b>; materials optimisation (via AI); materials and wastes tracing; <b>Mobility as a Service (MaaS)/Transport as a Service (TaaS)</b>; and <b>digital twins</b>."),
], terms=[
    {"t":"Mobility/Transport as a Service (MaaS/TaaS)","d":"Digital-enabled mobility models identified by the 2022 SFR to assuage green-digital trade-offs."},
], quiz=[
    mcq("Which is a 2022 SFR tech factor to assuage green-digital trade-offs?",
        ["Mobility as a Service (MaaS)", "Quantitative easing", "Carbon border tax", "A common EU army"], 0,
        "2022 SFR: tech factors… Mobility as a Service (MaaS)/Transport as a Service (TaaS); digital twins; energy-as-a-service.", "2022 SFR"),
])

S("m4-twinning2050", "m4", "Twinning by 2050 — a Scenario-Based Approach", [
    PR("Understanding forward-looking interplays between the digital and green/fair transition can <b>reduce trade-offs</b> and <b>maximise synergies</b>."),
    EX("Key figures: <b>ICT is responsible for 7%–9% of global electricity use</b> (a trade-off); <b>AI-based systems could reduce global emissions by 4%</b> (a synergy)."),
    DEF("The <b>JRC built 4 scenarios of a sustainable Europe in 2050</b> along <b>2 axes</b>: <b>societal behaviour</b> (individualistic vs collaborative) and <b>policy mix</b> (less vs more supportive of sustainability)."),
    EX("Equity dimension: the analysis covers green and social factors — e.g. the <b>richest decile emits 3 times more per capita</b> than all other citizens."),
], terms=[
    {"t":"4 scenarios for 2050","d":"JRC scenarios of a sustainable Europe in 2050 along two axes: societal behaviour (individualistic vs collaborative) and policy mix (less vs more supportive of sustainability)."},
], quiz=[
    blank("ICT is responsible for ______ of global electricity use (a trade-off the SFR highlights).",
          ["7%-9%","7-9%","7%–9%","7 to 9%","7%‑9%"], "ICT responsible of 7%-9% of global electricity use.", "Twinning by 2050",
          display="7%–9%"),
    blank("AI-based systems could reduce global emissions by ______ (a synergy).",
          ["4%","4"], "AI-based systems could reduce global emissions by 4%.", "Twinning by 2050", display="4%"),
    mcq("The JRC's 4 scenarios for 2050 vary along which two axes?",
        ["Societal behaviour (individualistic vs collaborative) and policy mix (less vs more supportive of sustainability)",
         "Rich vs poor and old vs young",
         "Digital vs analogue and urban vs rural",
         "Openness vs autonomy and risk vs reward"], 0,
        "JRC built 4 scenarios… along 2 axis: societal behavior (individualistic vs. collaborative) and policy mix (less vs. more supportive of sustainability).", "Twinning by 2050"),
    blank("On equity, the richest decile emits ______ times more per capita than all other citizens.",
          ["3","three"], "the richest decile emits 3 times more per capita than all other citizens.", "Twinning by 2050"),
])

S("m4-pathways", "m4", "From Scenarios to Policy Pathways", [
    DEF("<b>Green business boom</b>: change is primarily driven by the market and by innovation. As resource costs surge, corporations decouple profits from resource consumption — engaging in the circular economy, renewable energies and sustainable bio-economy. Innovation accelerates market opportunities for sustainable business models (enabled by new digital techs), so the economy promotes sustainable behaviour while generating added value. This movement is global, as geopolitical conflicts in the 2020s generated a strong pushback."),
    DEF("<b>Glocal eco-world</b>: policymakers failed to respond effectively to the major havoc brought by climate change, forcing people to adapt to more difficult circumstances. Society shifts to a new paradigm: people (re)discover the value of human relationships, connections, community help and the possibility of a dignified life with lower levels of material prosperity."),
], terms=[
    {"t":"Green business boom","d":"A 2050 scenario where market + innovation decouple profits from resource use (circular economy, renewables, bio-economy)."},
    {"t":"Glocal eco-world","d":"A 2050 scenario where, after failed policy responses to climate havoc, society adapts with lower material prosperity but stronger human relationships and community."},
], quiz=[
    mcq("In the 'Green business boom' scenario, change is primarily driven by…",
        ["the market and by innovation", "the state and regulation", "community self-help", "international treaties"], 0,
        "Green business boom: change is primarily driven by the market and by innovation.", "Scenarios"),
    mcq("The 'Glocal eco-world' scenario arises because…",
        ["policymakers failed to respond effectively to climate change",
         "innovation decoupled profits from resources", "the EU achieved full autonomy", "AI reduced emissions by 4%"], 0,
        "Glocal eco-world: policymakers failed to respond effectively to the major havoc brought by climate change.", "Scenarios"),
])

S("m4-industry5", "m4", "Industry 5.0 & Society 5.0", [
    DEF("<b>Industry 5.0</b>: an approach that links industrial transformation with <b>human-centricity, sustainability and resilience</b> — (digital) technologies for the SDGs."),
    DEF("<b>Society 5.0</b>: a ‘super-smart industrial transformation and society’ combining broad societal goals like the <b>SDGs</b> with new technologies. Innovation is useful as it enables addressing global societal challenges."),
], terms=[
    {"t":"Industry 5.0","d":"Links industrial transformation with human-centricity, sustainability and resilience."},
    {"t":"Society 5.0","d":"A 'super-smart' society combining societal goals (SDGs) with new technologies."},
], quiz=[
    mcq("Industry 5.0 links industrial transformation with…",
        ["human-centricity, sustainability and resilience",
         "automation, profit and scale", "defence, security and autonomy", "tax, trade and fiscal policy"], 0,
        "Industry 5.0: An approach that links industrial transformation with human-centricity, sustainability and resilience.", "Industry 5.0"),
    mcq("'Society 5.0' is defined as a super-smart transformation combining new technologies with…",
        ["broad societal goals like the SDGs", "military objectives", "monetary union", "the Brussels effect"], 0,
        "Society 5.0: ‘super smart industrial transformation and society’ combining broad societal goals like SDGs with new technologies.", "Society 5.0"),
])

S("m4-health", "m4", "Example — AI in Healthcare", [
    EX("AI has a key ‘vertical’ application to healthcare throughout the lifecycle of medicinal products: (1) speeding up (efficiency gains) the discovery of novel compounds with potential medicinal applications; (2) rapidly identifying patients for phase III clinical trials; (3) personalising therapies & optimising treatment plans."),
    EX("Key use case for COVID-19 vaccines: the EU-funded project <b>Exscalate</b> used HPC to screen molecules."),
    LST([
        "More effective patent protection (and a larger market).",
        "Large cost savings (up to <b>50%</b>) with some pass-through.",
    ], lead="Advantages of HPC & AI to accelerate drug discovery (down from the current 9.1 years for clinical development):"),
], terms=[
    {"t":"Exscalate","d":"EU-funded project that used HPC to screen molecules — a key AI/HPC use case for COVID-19 vaccines."},
], quiz=[
    mcq("Which EU-funded project used HPC to screen molecules for COVID-19 vaccines?",
        ["Exscalate", "EuroHPC", "Gaia-X", "FUTURINNOV"], 0,
        "Key use case for COVID-19 vaccines (EU-funded project Exscalate used HPC to screen molecules).", "AI in healthcare"),
    blank("HPC & AI can deliver large cost savings of up to ______% in drug discovery.",
          ["50"], "Large cost savings (up to 50%) with some pass-through.", "AI in healthcare"),
    blank("Current clinical development takes about ______ years, which AI/HPC aim to shorten.",
          ["9.1"], "(down from current 9.1 years for clinical development).", "AI in healthcare"),
])

S("m4-jobs", "m4", "The Technology/Jobs Puzzle", [
    DEF("<b>Technology/jobs puzzle</b>: the AI revolution will transform the job market — but will it lead to job loss? Productivity growth and job expansion could be another outcome (example: preventive medicine), but how to achieve it? The issue is <b>not only numerical</b>: policymakers should create ‘<b>good jobs</b>’ in ‘<b>good sectors</b>’."),
    PR("<b>Skills foresight</b> across key industrial ecosystems can empower workers along the digital transition and boost innovation — e.g. <b>Industry 5.0, the Pact for Skills, the Alliance for Apprenticeships, the New Innovation Agenda, Deep Tech Talent Initiatives, Net-Zero Academies</b>."),
    LST([
        "Industrial policy meets (skills) foresight to veer towards the creation of needed skills in sectors deemed strategic.",
        "A common space for skills as part of a digital transatlantic (or transpacific) marketplace.",
    ], lead="Recommendations:"),
], terms=[
    {"t":"Technology/jobs puzzle","d":"Whether the AI revolution causes job loss or job expansion; the goal is 'good jobs' in 'good sectors' via skills foresight (Renda, Balland, Bosoer 2023)."},
    {"t":"Skills foresight","d":"Anticipating skills needs across industrial ecosystems to empower workers and boost innovation."},
], quiz=[
    mcq("The technology/jobs puzzle stresses creating…",
        ["'good jobs' in 'good sectors'", "more low-wage jobs", "fewer regulations", "a universal basic income"], 0,
        "policymakers should tackle the technology / jobs puzzle and create ‘good jobs’ in ‘good sectors’.", "Technology/jobs puzzle"),
    mcq("Which is cited as a skills-foresight instrument?",
        ["Pact for Skills", "Chips Act", "DMA", "Global Gateway"], 0,
        "…(e.g. Industry 5.0, Pact for Skills, Alliance for Apprenticeships, New Innovation Agenda, Deep Tech Talent Initiatives, Net-Zero Academies).", "Skills foresight"),
])

S("m4-skills", "m4", "Digital Skills — the Digital Decade Targets", [
    EX("<b>42-44% of Europeans do not have basic digital skills</b> (particularly older people and rural areas), hampering everyday tasks and access to online services — this means <b>less than 70%</b>, against the <b>2030 target of 80%</b>."),
    PR("The skills gap (by age, gender, education, urbanisation) is large and varies across Member States."),
    EX("<b>ICT specialists</b> in the EU (<b>81% of which are male</b>) increased by <b>57.8% in 2012-2022</b> but are still flagged as insufficient by <b>85% of EU firms</b>. The status quo would mean just <b>12 million ICT specialists by 2030</b> — well below the <b>20 million</b> Digital Decade target."),
], terms=[
    {"t":"Digital Decade skills targets","d":"80% of people with basic digital skills and 20 million ICT specialists by 2030; the EU currently lags both."},
], quiz=[
    blank("The Digital Decade target is for ______% of people to have basic digital skills by 2030.",
          ["80"], "less than 70% of the 2030 target of 80%.", "Digital skills"),
    blank("The Digital Decade target is ______ million ICT specialists by 2030.",
          ["20","20 million","twenty"], "well below the 20 million DD target.", "Digital skills"),
    mcq("What share of Europeans lack basic digital skills?",
        ["42-44%", "12%", "80%", "57.8%"], 0,
        "42-44% of Europeans do not have basic digital skills.", "Digital skills"),
])

S("m4-gig", "m4", "A New EU Social Contract — Gig Workers", [
    EX("The gig economy and platform work are rising: <b>28 mn gig workers in 2022</b>, <b>43 mn in 2025</b>."),
    WARN("Issue: <b>93% (26 mn)</b> of workers are classified as <b>self-employed</b>, not entitled to the same rights & protection as employees. Around <b>5 million (19%)</b> are likely to be incorrectly classified."),
    DEF("The EU is the <b>1st legislator in the world to regulate platform work</b>: the Council adopted the <b>Platform Work Directive in October 2024</b>. Member States have <b>2 years to transpose</b> it. It (1) helps determine the correct employment status & social protection (self-employed vs employees); and (2) establishes rules on the use of <b>algorithms in the workplace</b> and related transparency safeguards."),
], terms=[
    {"t":"Platform Work Directive","d":"Adopted by the Council in October 2024; the EU is the first legislator worldwide to regulate platform work; MS have 2 years to transpose."},
], quiz=[
    blank("Gig workers rose from 28 mn in 2022 to ______ mn in 2025.",
          ["43"], "28 mn gig workers in 2022, 43 mn in 2025.", "Gig workers"),
    blank("______% of gig workers (26 mn) are classified as self-employed.",
          ["93"], "93% (26 mn) of workers are classified as self-employed.", "Gig workers"),
    mcq("The Platform Work Directive was adopted by the Council in…",
        ["October 2024", "September 2021", "December 2025", "January 2020"], 0,
        "the Council adopted the Platform Work Directive in October 2024.", "Platform Work Directive"),
    mcq("How long do Member States have to transpose the Platform Work Directive?",
        ["2 years", "6 months", "5 years", "immediately"], 0,
        "Member States have 2 years to transpose this Directive into national law.", "Platform Work Directive"),
])

S("m4-gig2", "m4", "Platform Work Directive — Mechanisms", [
    LST([
        "A <b>rebuttable legal presumption of employment relationship</b> based on control/direction elements in national law or collective agreement in force, with modalities set out by each Member State.",
        "<b>Use of algorithms in the workplace</b>: workers to be informed about automated monitoring & decision-making; personal data protected; <b>human oversight at least for significant decisions</b>.",
        "<b>Enforcement of transparency & traceability</b>: platforms to declare work to national authorities (including cross-border).",
    ], lead="The Directive's mechanisms:"),
    WARN("The debate on <b>control triggers</b> is complex: sometimes platforms’ rate control is to the workers’ advantage or to users’ benefit (certainty)."),
], terms=[
    {"t":"Rebuttable presumption of employment","d":"The Platform Work Directive's mechanism: workers presumed employees based on control/direction elements, unless rebutted; modalities set by each MS."},
], quiz=[
    mcq("The Platform Work Directive introduces a 'rebuttable legal presumption' of…",
        ["an employment relationship (based on control/direction)",
         "self-employment", "tax residence", "data ownership"], 0,
        "Rebuttable legal presumption of employment relationship based on control / direction elements.", "Platform Work Directive"),
    mcq("On workplace algorithms, the Directive requires human oversight…",
        ["at least for significant decisions", "for no decisions", "for all decisions without exception", "only on weekends"], 0,
        "human oversight at least for significant decision.", "Platform Work Directive"),
])

S("m4-takeaways", "m4", "Module 4 — Key Takeaways", [
    LST([
        "Digitalisation can help <b>solve the industrial-policy trilemma/quadrilemma</b> between economic security, competitiveness and decarbonisation, <b>plus fairness</b>, as overlapping (and sometimes competing) goals.",
        "<b>Twinning mainstreaming</b> is evident across EU policymaking — from the Digital Decade’s focus on <b>climate-neutral data centres and low-energy semiconductors</b> to the <b>Critical Raw Materials Act</b>.",
        "<b>Skills foresight</b> across key industrial ecosystems can assuage the technology/jobs puzzle, helping move towards ‘good jobs’ in ‘good (strategic) sectors’. Skills foresight and a focus on digital skills are part of the <b>2025 Union of Skills strategy</b>.",
        "A new (digital) industrial strategy for Europe also calls for a <b>new EU social contract</b>, including adequate workers’ protection in the digital world (the <b>Platform Work Directive</b>).",
    ], lead="The four key takeaways of Module 4:"),
], terms=[
    {"t":"Critical Raw Materials Act","d":"Cited as evidence of twinning mainstreaming across EU policymaking."},
    {"t":"Union of Skills strategy (2025)","d":"The 2025 strategy of which skills foresight and digital skills are a part."},
], quiz=[
    mcq("Twinning mainstreaming is illustrated by the Digital Decade's focus on climate-neutral data centres and…",
        ["low-energy semiconductors", "high-frequency trading", "nuclear submarines", "carbon credits"], 0,
        "from the Digital Decade’s focus on climate-neutral data centres and low-energy semiconductors, to the Critical Raw Materials Act.", "Module 4 takeaways"),
    mcq("Skills foresight and digital skills are framed as part of the 2025…",
        ["Union of Skills strategy", "Competitiveness Compass", "Chips Act 2.0", "Digital Omnibus"], 0,
        "Skills foresight and a focus on digital skills are part of the 2025 Union of Skills strategy.", "Module 4 takeaways"),
])

# -----------------------------------------------------------------------------
# SEMINAR DSA / DMA
# -----------------------------------------------------------------------------
S("sem-sisters", "seminar", "The DSA & DMA — the ‘Digital (not twin) Sisters’", [
    DEF("The <b>DSA and DMA</b> are recent Regulations. The <b>DSA</b> ensures a <b>safer digital space</b> where average users’ <b>fundamental rights</b> are protected (especially vis-à-vis <b>VLOPs</b> — very large online platforms). The <b>DMA</b> ensures a <b>level playing field for businesses</b> (e.g. SMEs, start-ups) and a fair choice for business users marketing products/services online, vis-à-vis <b>gatekeepers</b>."),
    PR("Digital technologies create new ways to exercise and infringe fundamental rights and freedoms (the ‘battle of models’) — e.g. trade of illegal content online, disinformation, and private rule-makers in digital markets. The DSA/DMA mark the start of a long, collaborative process to change the status quo."),
], terms=[
    {"t":"DSA (Digital Services Act)","d":"Regulation (EU) 2022/2065 on online intermediary services: due-diligence obligations, systemic risks and platform accountability; protects users' fundamental rights, esp. vis-à-vis VLOPs."},
    {"t":"DMA (Digital Markets Act)","d":"Regulation imposing obligations on gatekeeper platforms to promote contestability and fairness; protects a level playing field for business users."},
    {"t":"VLOPs","d":"Very Large Online Platforms — the focus of the DSA's strongest obligations."},
    {"t":"Gatekeepers","d":"Large platforms subject to DMA obligations to ensure contestability and fairness."},
], quiz=[
    mcq("The DSA primarily protects…",
        ["users' fundamental rights and a safer digital space (esp. vs VLOPs)",
         "a level playing field for businesses vs gatekeepers",
         "chip supply chains", "AI model providers"], 0,
        "safer digital space where average users’ fundamental rights are protected (DSA) especially vis-à-vis VLOPs.", "DSA/DMA"),
    mcq("The DMA primarily targets…",
        ["gatekeepers, to ensure contestability and a level playing field",
         "VLOPs and illegal content", "submarine cables", "quantum encryption"], 0,
        "a level playing field for businesses… vis-à-vis gatekeepers online (DMA).", "DSA/DMA"),
])

S("sem-origins", "seminar", "Origins, Due Diligence & Gatekeeper Obligations", [
    DEF("Origins in <b>e-commerce law</b>: the <b>2000 E-commerce Directive</b> is the origin point for EU intermediary-liability and digital-services rules; the regulatory landscape also includes the <b>2018 Audiovisual Media Services Directive</b> update."),
    DEF("<b>DSA — asymmetric due diligence</b>: obligations scale with the size and systemic role of the service. The DSA imposes <b>due-diligence obligations</b>, addresses <b>systemic risks</b> and establishes <b>platform accountability</b>, with the heaviest duties on the largest platforms (VLOPs)."),
    DEF("<b>DMA — gatekeeper obligations</b>: the DMA imposes <i>ex ante</i> obligations on gatekeeper platforms to promote <b>contestability and fairness</b> (e.g. against self-preferencing and unfair conditions for business users)."),
    EX("Official citations from the reading list: <b>Digital Services Act, Regulation (EU) 2022/2065</b>; the DSA/DMA are presented in depth in the <b>Filomena Chirico seminar</b>."),
], terms=[
    {"t":"E-commerce Directive (2000)","d":"The origin point for EU intermediary-liability and digital-services rules."},
    {"t":"Asymmetric due diligence (DSA)","d":"DSA obligations scale with the size and systemic role of the service; heaviest on VLOPs."},
], quiz=[
    mcq("EU intermediary-liability and digital-services rules originate in which instrument?",
        ["The 2000 E-commerce Directive", "The 2018 AVMSD", "GDPR", "The AI Act"], 0,
        "2000: E-commerce Directive: origin point for EU intermediary-liability and digital-services rules.", "DSA origins"),
    mcq("The DSA's due-diligence model is described as…",
        ["asymmetric (scaling with platform size/systemic role)",
         "identical for all firms", "voluntary", "limited to gatekeepers"], 0,
        "DSA asymmetric due diligence… heaviest duties on the largest platforms (VLOPs).", "DSA"),
    blank("The Digital Services Act is Regulation (EU) 2022/______.",
          ["2065"], "Digital Services Act, Regulation (EU) 2022/2065.", "DSA"),
])

# -----------------------------------------------------------------------------
# READINGS
# -----------------------------------------------------------------------------
S("read-draghi", "readings", "The Draghi Report (2024)", [
    DEF("<b>Draghi Report</b>: Mario Draghi’s 2024 report ‘The Future of European Competitiveness’ — used in the course as the central diagnosis of EU industrial-policy needs. Compulsory: Part A + the digital and governance chapters in Part B (‘Digitalisation & Advanced Tech’ p 67; ‘Accelerating Innovation’ p 228; ‘Strengthening Governance’ p 307)."),
    Q("“Industrial strategies today – as seen in the US and China – combine multiple policies… In the EU context, linking policies in this way requires […] a new industrial strategy for Europe.” — Mario Draghi, September 2024."),
], terms=[
    {"t":"Draghi Report","d":"Mario Draghi's 2024 report on the future of European competitiveness; the course's central diagnosis of EU industrial-policy needs."},
], quiz=[
    mcq("The Draghi Report is titled…",
        ["'The Future of European Competitiveness'", "'Digital Empires'", "'A Shield for Europe'", "'The North Star'"], 0,
        "Mario Draghi, ‘The Future of European Competitiveness’, September 2024.", "Draghi Report"),
])

S("read-renda", "readings", "Andrea Renda — North Star & the Technology/Jobs Puzzle", [
    DEF("Andrea Renda (2024), ‘What North Star for future EU industrial policy?’, frames the <b>industrial-policy trilemma/quadrilemma</b> (competitiveness, decarbonisation, economic security + fairness) and maps <b>agile regulatory tools</b> by policy-cycle phase."),
    DEF("Renda, Balland & Bosoer (2023), ‘The Technology/Jobs Puzzle: A European Perspective’, frames whether AI causes job loss or job expansion and argues for ‘good jobs in good sectors’ via skills foresight."),
    EX("Also by Renda: ‘IoT4SDGs’ (CEPS, with Moritz Laurer, 2020)."),
], terms=[
    {"t":"Andrea Renda","d":"CEPS author of the 'North Star' industrial-policy paper, the Technology/Jobs Puzzle, the regulatory-tools policy-cycle map and IoT4SDGs."},
], quiz=[
    mcq("Which Renda paper frames whether AI leads to job loss or job expansion?",
        ["The Technology/Jobs Puzzle (2023)", "What North Star for future EU industrial policy? (2024)", "IoT4SDGs (2020)", "Digital Empires (2023)"], 0,
        "The Technology/Jobs Puzzle: A European Perspective, Andrea Renda, Pierre Alexandre Balland and Lucia Bosoer, 2023.", "Renda"),
])

S("read-shield", "readings", "A Shield for Europe — Reviving the European Defence Community", [
    DEF("‘<b>A Shield for Europe: Reviving the European Defence Community</b>’ (Federico Fabbrini, Survival, 2025, 67:1, 55-60). A defence-policy reading on European security, OSA and the potential revival of an EDC-like framework."),
    EX("Context: a major conventional inter-state war returned to Europe (Russia’s aggression against Ukraine); EU leaders called it a ‘<b>tectonic shift in European history</b>’ in the <b>Versailles Declaration of March 2022</b>; Trump’s re-election compounds the challenge. If the US withheld support, the EU would become, by default, the main instrument of European defence solidarity."),
    DEF("<b>European Defence Community (EDC)</b>: in 1951 six countries — Belgium, France, Italy, Luxembourg, the Netherlands and West Germany — founded the <b>ECSC</b> with the 1951 <b>Treaty of Paris</b>; in 1952 they established the EDC, explicitly focused on defending Western Europe (France also saw it as a way to deal with the remilitarisation of Germany)."),
    PR("Fabbrini argues that since the four states that ratified it never rescinded their ratification, if <b>France and Italy</b> approved the treaty today, the EDC would become operational; the EDC would be interconnected with NATO (allaying decoupling fears), open to any EU state (with a veto on uncooperative partners), and would build a bridge with the UK."),
], terms=[
    {"t":"European Defence Community (EDC)","d":"A 1950s supranational defence framework (est. 1952), revisited by Fabbrini (2025) as a possible model for European defence solidarity."},
    {"t":"Versailles Declaration (March 2022)","d":"EU leaders called Russia's war a 'tectonic shift in European history'."},
    {"t":"Treaty of Paris (1951)","d":"Founded the European Coal and Steel Community (ECSC) by six countries."},
], quiz=[
    mcq("Who wrote 'A Shield for Europe: Reviving the European Defence Community' (2025)?",
        ["Federico Fabbrini", "Andrea Renda", "Anu Bradford", "Dimitri Lorenzani"], 0,
        "Federico Fabbrini (2025) A Shield for Europe: Reviving the European Defence Community, Survival.", "EDC"),
    mcq("The 2022 Versailles Declaration described Russia's war as a…",
        ["'tectonic shift in European history'", "'point of inflection'", "'North Star'", "'battle of models'"], 0,
        "the war, they stated, ‘constitutes a tectonic shift in European history’.", "EDC"),
    blank("The EDC was established in the year ______, after the ECSC's 1951 Treaty of Paris.",
          ["1952"], "in 1952 they established the EDC, a new organisation explicitly focused on defending Western Europe.", "EDC"),
    mcq("Per Fabbrini, the EDC could become operational today if which two states approved the treaty?",
        ["France and Italy", "Germany and Poland", "Spain and Portugal", "Belgium and the Netherlands"], 0,
        "if France and Italy approved the treaty today, the EDC would become operational.", "EDC"),
])

S("read-orals", "readings", "Oral Presentation Themes (the Five Debates)", [
    LST([
        "<b>Group 1</b>: the links (synergies and trade-offs) between European <b>industrial policy and competition policy</b> — with a focus on the digital field; present at least 2 recent examples of EU digital legislation where this tension is most relevant.",
        "<b>Group 2</b>: the pros and cons of <b>tech export controls and preference clauses</b> in trade/public procurement — are they necessary for economic security or the end of Europe’s openness?",
        "<b>Group 3</b>: the pros and cons of Europe’s <b>(over)regulating the digital world</b> — the balance between the <b>principle of precaution and innovation</b>; present 2 recent examples and compare with the AI Act.",
        "<b>Group 4</b>: the pros and cons of alternative strategies to make the <b>digital transition greener</b> (innovation-led vs de-growth strategies towards decarbonisation; best achieving the twinning).",
        "<b>Group 5</b>: the new ‘<b>socio-economic models</b>’ imposed by digitalisation (labour market, skills, inequalities) — ‘How can digitalisation be part of the solution rather than of the problem?’",
    ], lead="The course treats five policy debates as central:"),
], terms=[], quiz=[
    mcq("Which oral-presentation debate asks whether export controls are 'necessary for economic security or the end of Europe’s openness'?",
        ["Group 2", "Group 1", "Group 3", "Group 5"], 0,
        "Group 2: pros and cons of tech export controls and preference clauses… are they necessary for economic security or the end of Europe’s openness?", "Oral themes"),
    mcq("Which debate centres on the balance between the precautionary principle and innovation, compared with the AI Act?",
        ["Group 3", "Group 1", "Group 4", "Group 5"], 0,
        "Group 3: pros and cons of Europe’s (over)regulating the digital world… balance between principle of precaution and innovation… compare them with the AI Act.", "Oral themes"),
])

# -----------------------------------------------------------------------------
# SYNTHESIS / TIMELINE / EXAM PREP
# -----------------------------------------------------------------------------
S("syn-themes", "synthesis", "Thematic Synthesis — Five Cross-Cutting Themes", [
    DEF("<b>1. The consistent trio</b>: digital policy must be embedded in a broader industrial and foresight strategy. Foresight identifies long-term risks and scenarios; industrial strategy selects capacity-building priorities; digital policy supplies the regulatory and technological instruments."),
    DEF("<b>2. Open strategic autonomy & economic security</b>: building capacity and reducing excessive dependencies without simply closing the EU economy; reframing supply chains, critical technologies, cybersecurity and infrastructure as risk-management fields."),
    DEF("<b>3. The EU as digital normative superpower</b>: projecting power through law by setting binding standards (AI, platforms, services, gatekeepers); linked to the Brussels effect and global regulatory competition."),
    DEF("<b>4. Dynamic policy coherence & the twin/fair transition</b>: digitalisation creates both opportunities and trade-offs for decarbonisation and social fairness; coherence manages these interdependencies over time."),
    DEF("<b>5. Competitiveness, productivity & the innovation lifecycle</b>: competitiveness is connected to digital innovation, scale-up capacity, R&I, skills and industrial ecosystems; the EU must escape a middle-technology trap."),
], terms=[], quiz=[
    mcq("Which theme links the EU's power to the Brussels effect and global regulatory competition?",
        ["The EU as digital normative superpower",
         "The consistent trio", "Dynamic policy coherence", "The innovation lifecycle"], 0,
        "The EU as digital normative superpower: projecting power through law… linked to the Brussels effect and to global regulatory competition.", "Synthesis"),
])

S("syn-timeline", "synthesis", "Course Timeline (Memorise the Dates)", [
    LST([
        "<b>1950s</b>: European Defence Community project (supranational defence reference).",
        "<b>2000</b>: E-commerce Directive — origin of EU intermediary-liability and digital-services rules.",
        "<b>2018</b>: Audiovisual Media Services Directive update.",
        "<b>2020</b>: Strategic Foresight Report cycle and the digital-strategy policy turn begin to feature centrally.",
        "<b>2022</b>: Versailles Declaration & Russia’s war against Ukraine reinforce the strategic-autonomy agenda; 2022 SFR focuses on green-digital twinning.",
        "<b>2023</b>: Economic Security Strategy; 2023 SFR; Spain’s Presidency foregrounds OSA; EU Chips Act enters into force (Sep).",
        "<b>2024</b>: Draghi Report and the European competitiveness agenda; Platform Work Directive adopted (Oct); AI Act = Regulation (EU) 2024/1689.",
        "<b>2025</b>: Competitiveness Compass and SFR 2025; Fabbrini article on reviving the EDC; Economic Security Doctrine (Dec).",
        "<b>2026</b>: Course and exam year; final exam is a closed-book 2-hour written exam.",
    ], lead="Key dates:"),
], terms=[], quiz=[
    mcq("In which year did the EU Chips Act Regulation enter into force?",
        ["2023", "2020", "2025", "2018"], 0, "2023: …EU Chips Act enters into force (Sep).", "Timeline"),
    mcq("The 2000 milestone in the timeline is the…",
        ["E-commerce Directive", "AI Act", "Versailles Declaration", "Competitiveness Compass"], 0,
        "2000: E-commerce Directive: origin point for EU intermediary-liability and digital-services rules.", "Timeline"),
])

S("syn-exam", "synthesis", "Exam Preparation — Topics, Pitfalls & Model Plans", [
    LST([
        "The consistent trio as the EU’s new policy paradigm.",
        "Open strategic autonomy in digital technologies.",
        "EU digital regulation as normative power: AI Act, DSA and DMA.",
        "The EU competitiveness problem and the role of digital industrial policy.",
        "Digitalisation, decarbonisation and fairness: solving the industrial-policy trilemma.",
    ], lead="Likely essay topics:"),
    LST([
        "Define strategic foresight; define open strategic autonomy; define the Brussels effect.",
        "What is the difference between the DSA and DMA? What are gatekeepers (DMA) and systemic risks (DSA)?",
        "What is the EU Chips Act designed to address? What is dynamic policy coherence?",
        "How does the AI Act structure regulation by risk? What is the technology/jobs puzzle?",
    ], lead="Possible short questions:"),
    WARN("Common mistakes to avoid: treating digital policy as only market regulation (ignoring industrial capacity); using OSA as a synonym for protectionism; describing the AI Act/DSA/DMA without explaining their different regulatory logics; listing instruments without linking them to competitiveness/autonomy/coherence; ignoring trade-offs (innovation vs regulation; openness vs security; digitalisation vs jobs; green transition vs industrial cost)."),
    PR("High-value arguments: foresight is the analytical lens, industrial strategy the capacity-building agenda, digital policy both object and instrument; the EU’s regulatory strength must be connected to innovation and scale-up; OSA is about managing dependencies, not withdrawing; green and digital transitions are not automatically coherent — policy must create synergies; structure answers as concept → policy example → trade-off → conclusion."),
], terms=[], quiz=[
    mcq("A recommended structure for exam answers is…",
        ["concept → policy example → trade-off → conclusion",
         "opinion → anecdote → opinion", "definition only", "list of dates"], 0,
        "Exam answers should move from concept to policy example to trade-off to conclusion.", "Exam technique"),
    mcq("Which is a 'common mistake to avoid'?",
        ["Using open strategic autonomy as a synonym for protectionism",
         "Linking instruments to competitiveness", "Discussing trade-offs", "Using course terminology"], 0,
        "Common mistakes: Using open strategic autonomy as a synonym for protectionism.", "Exam technique"),
])

# =============================================================================
#  GLOSSARY (auto-compiled from section terms + dedicated entries)
# =============================================================================
GLOSSARY_EXTRA = [
    {"t":"Machine learning / deep learning","d":"AI algorithms that create expert systems to make predictions or classifications based on input data (encompassed within AI)."},
    {"t":"Supercomputing (HPC)","d":"High-performance computing using supercomputers to process complex calculations and large data volumes."},
    {"t":"Cloud","d":"Networked computing facilities providing remote data storage and processing services via the internet."},
    {"t":"AI model","d":"A program trained on data to recognise patterns or make decisions; an AI language model generates text from preceding words."},
    {"t":"Platform work","d":"Labour mediated by digital platforms, raising questions about employment status, social protection and fairness."},
    {"t":"Twin transition","d":"The combined green and digital transition, emphasising synergies and trade-offs."},
    {"t":"Industrial policy trilemma","d":"The tension between competitiveness, decarbonisation and economic security/fairness that industrial policy must manage."},
]

# =============================================================================
#  FLASHCARDS — auto-built from every term + curated key-fact cards
# =============================================================================
FLASHCARDS = []
def card(front, back, concept):
    FLASHCARDS.append({"front": front, "back": back, "concept": concept})

# curated high-yield fact cards (beyond plain term->definition)
CURATED_CARDS = [
    ("State the course's 'consistent trio'.", "Strategic foresight + industrial strategy + digital policy — a new, crucial trio in EU policymaking.", "Consistent trio"),
    ("Weighting of the final exam, and its format?", "55% of the grade; a 2-hour closed-book written exam (1–2 essays ≤1000 words = 50%; a few short questions = 50%).", "Assessment"),
    ("Define foresight (2020 SFR).", "“The discipline of exploring, anticipating and shaping the future” — tools/methods to create a safe space for disruptive questions using collective intelligence to prepare for the future.", "Strategic foresight"),
    ("What does ESPAS stand for and how many institutions take part?", "European Strategy and Policy Analysis System; 9 EU institutions participate.", "ESPAS"),
    ("How many global megatrends does the Megatrends Hub analyse?", "14.", "Megatrends"),
    ("Horizon scanning: name the three steps and the output.", "Spot 'signs of change' → validate as 'weak signals' → explore impact in 'sense-making sessions'; output = quarterly newsletters to the College.", "Horizon scanning"),
    ("OSA in one phrase?", "'As open as possible, as autonomous as necessary' — the geopolitical dimension of resilience.", "Open strategic autonomy"),
    ("Across how many sensitive industrial ecosystems did the EU map excessive dependencies?", "11.", "Mitigation of dependencies"),
    ("Chips Act: production target and entry into force?", "Raise EU production share to 20% by 2030; entered into force September 2023.", "EU Chips Act"),
    ("Chips Fund figures?", "3.3 bn EUR (Horizon Europe & Digital Europe, blended under InvestEU & EIC) to catalyse 43 bn EUR by 2030.", "EU Chips Act"),
    ("Chips bespoke state aid: how much of a funding gap can be covered?", "Up to 100% of a proven funding gap for FOAK facilities that would otherwise not exist in Europe.", "State aid"),
    ("Global chip subsidy figures (US/China/Japan/EU)?", "US CHIPS Act $53bn; China $150–200bn; Japan $5bn; EU ~€100bn announced.", "Chips subsidies race"),
    ("The Economic Security Strategy's 3 P's?", "Promoting (competitiveness), Protecting (economic security), Partnering (with like-minded countries) — and Preparing?", "Economic Security Strategy"),
    ("The 4 high-risk areas flagged by the Economic Security Strategy?", "Advanced chips, AI, quantum, biotech.", "Economic Security Strategy"),
    ("Three pillars of the cybersecurity acquis?", "NIS2 Directive; Cybersecurity Act; Cyber Resilience Act (+ sectoral acts & cyber-diplomacy toolbox).", "Cybersecurity acquis"),
    ("NIS2 fines vs Cyber Resilience Act fines?", "NIS2: up to 2% of turnover. CRA: up to €15mn or 2.5% of turnover (EU market access from 2027, via CE marking).", "Cybersecurity acquis"),
    ("Where is the EU Cybersecurity Competence Centre (ECCC)?", "Bucharest.", "ECCC"),
    ("EuroHPC: EU supercomputers in the global top 10?", "4.", "EuroHPC"),
    ("AI factories — how many and across how many MS? Plus Gigafactories?", "19 AI factories across 16 MS; plus the first 4–5 AI Gigafactories planned.", "AI Factories"),
    ("Digital Decade quantum-computer target by 2030?", "3 quantum computers (the EU is far from it; China leads).", "Quantum"),
    ("What is the 'IKEA cloud paradox' and the data-value-loss figure?", "The EU lost the cloud market to US hyperscalers; head-on competition is unrealistic. EU data value loss is up to 90%.", "Cloud"),
    ("Define the Brussels effect.", "The EU shapes global markets through regulation because firms adapt to EU rules and diffuse them beyond Europe.", "Brussels effect"),
    ("Bradford's three Digital Empires models?", "US market-driven; China state-driven; EU rights-driven.", "Digital Empires"),
    ("AI Act: what is it, and its citation?", "World's first horizontal AI regulation; Regulation (EU) 2024/1689; rights-based and risk-based.", "AI Act"),
    ("AI Act risk tiers?", "8 banned (unacceptable); high-risk (conformity assessment); low-risk (transparency); minimal (minimal obligations).", "AI Act"),
    ("AI Act maximum fines?", "Up to €35 million or 7% of total worldwide annual turnover (whichever higher).", "AI Act fines"),
    ("AI Pact pledges: Sep 2024 vs Jan 2026?", "Over 100 (Sep 2024); over 230 (Jan 2026).", "AI Pact"),
    ("Digital Omnibus (2025) extended AI Act deadlines?", "02/12/27 for listed high-risk AI; 02/12/28 for AI embedded in regulated products (e.g. medical devices, machinery).", "Digital Omnibus"),
    ("DSA vs DMA in one line each?", "DSA: safer digital space, protects users' fundamental rights (esp. vs VLOPs). DMA: level playing field, obligations on gatekeepers for contestability & fairness.", "DSA/DMA"),
    ("Origin of EU intermediary-liability/digital-services rules?", "The 2000 E-commerce Directive.", "DSA origins"),
    ("DSA citation?", "Regulation (EU) 2022/2065.", "DSA"),
    ("UK open-banking sandbox: who and when?", "Launched 2016 by the Financial Conduct Authority (FCA); model spread alongside the EU's PSD2.", "Open banking sandbox"),
    ("ICT share of global electricity vs AI emissions reduction potential?", "ICT = 7%–9% of global electricity use (trade-off); AI could cut global emissions by 4% (synergy).", "Twinning by 2050"),
    ("JRC 2050 scenarios: the two axes?", "Societal behaviour (individualistic vs collaborative) and policy mix (less vs more supportive of sustainability) — 4 scenarios.", "Twinning by 2050"),
    ("Name the two scenario pathways described.", "'Green business boom' (market/innovation-driven) and 'Glocal eco-world' (adaptation after failed policy response).", "Scenarios"),
    ("AI in healthcare: project and savings?", "EU-funded Exscalate used HPC to screen molecules (COVID-19 vaccines); up to 50% cost savings; cuts the ~9.1-year clinical-development time.", "AI in healthcare"),
    ("Digital Decade skills targets by 2030?", "80% with basic digital skills and 20 million ICT specialists (EU lags both; 42-44% currently lack basic skills).", "Digital skills"),
    ("Gig workers 2022 vs 2025, and % self-employed?", "28 mn (2022) → 43 mn (2025); 93% (26 mn) classified self-employed; ~5 mn (19%) likely misclassified.", "Gig workers"),
    ("Platform Work Directive: when adopted, transposition, key mechanism?", "Council adopted Oct 2024; 2 years to transpose; rebuttable presumption of employment + rules on workplace algorithms.", "Platform Work Directive"),
    ("Industrial-policy trilemma vs quadrilemma (Renda)?", "Trilemma: competitiveness, decarbonisation, economic security. Quadrilemma adds fairness.", "Trilemma"),
    ("Draghi Report title and year?", "'The Future of European Competitiveness', September 2024.", "Draghi Report"),
    ("EDC: founding years and the 'two states' point?", "ECSC via 1951 Treaty of Paris (6 states); EDC established 1952. Fabbrini (2025): if France and Italy approved today, the EDC would become operational.", "EDC"),
    ("Von der Leyen I Commission — described how?", "A 'swinging moment' in EU industrial policy (vertical vs horizontal) towards competitiveness, resilience and (open) strategic autonomy.", "Industrial policy turn"),
    ("Competitiveness Compass: what and four aims?", "A 2025 Commission framework / 'North Star' orienting Europe towards productivity, innovation, decarbonisation and security.", "Competitiveness Compass"),
]
for f,b,c in CURATED_CARDS:
    card(f,b,c)

# term-based cards from each section
_seen = set()
for sec in SECTIONS:
    for t in sec["terms"]:
        key = t["t"].lower()
        if key in _seen: continue
        _seen.add(key)
        card("Define: <b>%s</b>" % t["t"], t["d"], t["t"])

# =============================================================================
#  Build glossary list (terms + extras), with backlinks to sections
# =============================================================================
GLOSSARY = []
_gseen = {}
for sec in SECTIONS:
    for t in sec["terms"]:
        k = t["t"].lower()
        if k not in _gseen:
            _gseen[k] = {"term": t["t"], "def": t["d"], "sec": sec["id"], "secTitle": sec["title"]}
for e in GLOSSARY_EXTRA:
    k = e["t"].lower()
    if k not in _gseen:
        _gseen[k] = {"term": e["t"], "def": e["d"], "sec": None, "secTitle": None}
GLOSSARY = sorted(_gseen.values(), key=lambda x: x["term"].lower())

# =============================================================================
#  Assemble data payload
# =============================================================================
DATA = {
    "modules": [{"id": m[0], "title": m[1]} for m in MODULES],
    "sections": SECTIONS,
    "glossary": GLOSSARY,
    "flashcards": FLASHCARDS,
}

total_quiz = sum(len(s["quiz"]) for s in SECTIONS)
print("Sections:", len(SECTIONS))
print("Flashcards:", len(FLASHCARDS))
print("Quiz questions:", total_quiz)
print("Glossary entries:", len(GLOSSARY))

data_json = json.dumps(DATA, ensure_ascii=False).replace("</", "<\\/")

# write data to a temp file used by the HTML assembler
with open("site_data.json", "w", encoding="utf-8") as f:
    f.write(data_json)
print("wrote site_data.json")
