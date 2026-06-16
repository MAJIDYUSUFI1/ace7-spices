# -*- coding: utf-8 -*-
import os
from partials import head, header, footer, ICONS, PHONE, PHONE_DISP, EMAIL

OUT = os.path.dirname(os.path.abspath(__file__))
I = ICONS

def img(src, alt, cls="", phcls=""):
    return ('<img src="' + src + '" alt="' + alt + '" loading="lazy" '
            'data-ph="' + alt + '" data-ph-class="' + phcls + '" class="' + cls + '">')

def page(name, title, desc, body, active, rel=""):
    html = head(title, desc, rel) + header(active, rel) + '<main id="main">' + body + '</main>' + footer(rel)
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", name, "(%d kb)" % (len(html)//1024))

def phero(crumb_parent, crumb, title, sub, img_src, img_alt, metas):
    m = "".join(['<div class="m"><b>'+a+'</b><span>'+b+'</span></div>' for a, b in metas])
    return (r'''
<section class="phero">
  <div class="phero__media">''' + img(img_src, img_alt, "", "ph--wide") + r'''</div>
  <div class="phero__inner reveal in">
    <p class="crumbs"><a href="index.html">Home</a> / ''' + crumb_parent + r'''<span>''' + crumb + r'''</span></p>
    <h1 class="display">''' + title + r'''</h1>
    <p>''' + sub + r'''</p>
    <div class="phero__meta">''' + m + r'''</div>
  </div>
</section>''')

# ===================== PROCESS =====================
process = phero("", "Our process",
    "A short supply chain, watched at every gate.",
    "The journey from a farmer's field to a sealed, lab-released export bag — with no unnecessary hands in between.",
    "images/process-coldpress.jpg", "Cold-press low-RPM spice milling at the Ace7 facility",
    [("4","Controlled stages"),("0","Adulterants added"),("100%","Lab-released")]) + r'''

<section class="section">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow">Stage by stage</span><h2>Source &rarr; sort &rarr; process &rarr; pack.</h2><p>Each crop follows the same disciplined path. The shorter and cleaner the chain, the more of the farm-gate flavour survives to your kitchen.</p></div>
    <div class="steps">
      <div class="step reveal"><div class="step__media"><span class="step__no">1</span>''' + img("images/process-sourcing.jpg", "Farmer handing over freshly harvested spice crop", "", "ph--wide") + r'''</div><h3><small>Source</small>From the right belt</h3><p>We buy in the regions each crop is famous for, working close to growers to select lots by variety, season and quality — not by whoever is cheapest that week.</p></div>
      <div class="step reveal d1"><div class="step__media"><span class="step__no">2</span>''' + img("images/process-sorting.jpg", "Workers hand-sorting chillies for colour and defects", "", "ph--wide") + r'''</div><h3><small>Sort</small>Cleaned &amp; graded</h3><p>Lots are de-stoned, winnowed and cleaned, then colour-, size- and defect-sorted by hand and machine so only premium material moves on.</p></div>
      <div class="step reveal d2"><div class="step__media"><span class="step__no">3</span>''' + img("images/process-coldpress.jpg", "Cold-press low-RPM grinder producing aromatic spice powder", "", "ph--wide") + r'''</div><h3><small>Process</small>Cold-pressed to spec</h3><p>Whole spice is shipped as-is; powders are cold-press milled at low RPM to your target mesh, keeping temperatures — and the volatile oils — under control.</p></div>
      <div class="step reveal d3"><div class="step__media"><span class="step__no">4</span>''' + img("images/process-packing.jpg", "Export-ready spice packing in food-grade bags", "", "ph--wide") + r'''</div><h3><small>Pack</small>Sealed, coded &amp; released</h3><p>After a passing lab report, every lot is given a traceable code and packed in food-grade, moisture-barrier export formats ready for the container.</p></div>
    </div>
  </div>
</section>

<section class="section roast">
  <div class="wrap">
    <div class="split">
      <div class="split__media reveal">''' + img("images/coldpress-detail.jpg", "Detail of low-RPM cold-press grinding stones", "", "ph--tall") + r'''</div>
      <div class="split__body reveal d1">
        <span class="eyebrow cream">The differentiator</span>
        <h2>Why we grind cold and slow.</h2>
        <p class="lead">Aroma and pungency live in a spice's volatile oils. Conventional high-speed hammer mills spin so fast they heat the spice — and that heat boils those oils off as you grind.</p>
        <p>Our cold-press, low-RPM mills run slowly enough that the spice barely warms. The result is a powder that still smells of the whole spice it came from: brighter coriander, redder chilli, deeper turmeric — with the essential-oil content the lab can actually measure.</p>
        <ul class="checklist">
          <li>''' + I["check"] + r'''<span><b>Low heat</b> — protects volatile oils, colour and pungency.</span></li>
          <li>''' + I["check"] + r'''<span><b>Mesh to order</b> — milled to the particle size your line needs.</span></li>
          <li>''' + I["check"] + r'''<span><b>Dedicated runs</b> — no cross-contamination between crops or lots.</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow">Infrastructure</span><h2>The facility behind the spec sheet.</h2><p>A clean, controlled environment from intake to dispatch — built so quality is the default outcome, not a lucky one.</p></div>
    <div class="grid g-3">
      <div class="card reveal"><div class="card__ico">''' + I["box"] + r'''</div><h4>Intake &amp; storage</h4><p>Incoming lots are inspected, documented and stored in dry, ventilated conditions that protect moisture and colour before processing.</p></div>
      <div class="card reveal d1"><div class="card__ico">''' + I["grind"] + r'''</div><h4>Cold-press milling hall</h4><p>Low-RPM mills with crop-dedicated lines, sieving and metal detection to keep every powder clean and consistent.</p></div>
      <div class="card reveal d2"><div class="card__ico">''' + I["flask"] + r'''</div><h4>In-line QC &amp; lab</h4><p>Sampling and testing at intake and pre-dispatch, with third-party lab confirmation for export-grade lots.</p></div>
      <div class="card reveal"><div class="card__ico">''' + I["shield"] + r'''</div><h4>Hygienic handling</h4><p>Food-grade contact surfaces, controlled access and documented cleaning between runs.</p></div>
      <div class="card reveal d1"><div class="card__ico">''' + I["tag"] + r'''</div><h4>Packing &amp; coding</h4><p>Export bags filled, weighed, sealed and lot-coded — with packaging matched to each destination market.</p></div>
      <div class="card reveal d2"><div class="card__ico">''' + I["globe"] + r'''</div><h4>Dispatch &amp; logistics</h4><p>Container loading and export documentation coordinated so lots leave on schedule with their papers in order.</p></div>
    </div>
    <div class="reveal" style="margin-top:44px">''' + img("images/facility-loading.jpg", "Workers loading sealed spice bags into an export container truck", "", "ph--wide") + r'''</div>
  </div>
</section>

<section class="section roast ctaband">
  <div class="wrap"><div class="ctaband__inner reveal">
    <h2>Want to see a lot run to your spec?</h2>
    <p>Send us your target grade, mesh and volume — we'll process a documented sample and share its lab report.</p>
    <div class="btn-row"><a class="btn btn--primary" href="contact.html">Request a sample ''' + I["arrow"] + r'''</a><a class="btn btn--light" href="quality.html">See our testing</a></div>
  </div></div>
</section>
'''
page("process.html", "Our Process — Source, Sort, Cold-Press & Ship | Ace7 Spices",
     "How Ace7 Spices turns farm-belt crops into export-grade spice: hand-sorting, cold-press low-RPM milling that preserves aroma, in-line QC and lab-released, lot-coded packing.",
     process, "About")

# ===================== QUALITY & TRACEABILITY =====================
quality = phero("", "Quality &amp; traceability",
    "Every claim we make, a lab can measure.",
    "We test each lot before it ships and code it so it can be traced back to the farm-belt, the season and its own report. Trust, made checkable.",
    "images/lab-testing.jpg", "Lab technician testing a spice sample in a quality control lab",
    [("100%","Lots tested"),("7","Test parameters"),("1","Lot code per pack")]) + r'''

<section class="section">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow">What we test</span><h2>Seven things we check before a lot earns a code.</h2><p>Pungency and colour tell you what you're buying. The safety panel tells you it's safe to put in food. We run both, lot by lot.</p></div>
    <div class="grid g-4">
      <div class="card reveal"><div class="card__ico">''' + I["fire"] + r'''</div><h4>Pungency (SHU)</h4><p>Scoville heat measured so red chilli matches your formulation, lot after lot.</p></div>
      <div class="card reveal d1"><div class="card__ico">''' + I["drop"] + r'''</div><h4>Colour (ASTA / curcumin)</h4><p>ASTA colour value for chilli and curcumin % for turmeric — the numbers buyers price on.</p></div>
      <div class="card reveal d2"><div class="card__ico">''' + I["scale"] + r'''</div><h4>Moisture</h4><p>Kept within export limits to protect shelf life and prevent caking and mould.</p></div>
      <div class="card reveal d3"><div class="card__ico">''' + I["leaf"] + r'''</div><h4>Pesticide residue</h4><p>Screened against destination-market thresholds, including strict EU limits.</p></div>
      <div class="card reveal"><div class="card__ico">''' + I["shield"] + r'''</div><h4>Aflatoxin</h4><p>Tested to keep mycotoxins below regulated limits for safe human consumption.</p></div>
      <div class="card reveal d1"><div class="card__ico">''' + I["flask"] + r'''</div><h4>Microbiology</h4><p>Total plate count, yeast &amp; mould and pathogen screening for food-safe lots.</p></div>
      <div class="card reveal d2"><div class="card__ico">''' + I["drop"] + r'''</div><h4>Lead-chromate (turmeric)</h4><p>Turmeric is explicitly screened for lead-chromate adulteration — a known risk we will not carry.</p></div>
      <div class="card reveal d3"><div class="card__ico">''' + I["tag"] + r'''</div><h4>Purity &amp; admixture</h4><p>Foreign matter and admixture checked so what's in the bag is the spice on the label.</p></div>
    </div>
  </div>
</section>

<section class="section roast">
  <div class="wrap">
    <div class="split split--rev">
      <div class="split__media reveal">''' + img("images/traceability-qr.jpg", "Spice export bag with a lot-code label and QR tag", "", "ph--tall") + r'''</div>
      <div class="split__body reveal d1">
        <span class="eyebrow cream">Traceability</span>
        <h2>One code that tells the whole story.</h2>
        <p class="lead">Every pack we ship carries a lot code. That code is the thread back through our records to where and when the spice was grown, how it was processed, and what its lab report said.</p>
        <p>If a question ever comes up on your side, you don't open an investigation — you quote a code, and we can pull the lot's full history in minutes.</p>
        <div class="hero__card" style="background:rgba(247,241,230,.05);margin-top:24px">
          <h4>Anatomy of a lot code</h4>
          <div class="specrow"><span>AC7</span><b>Ace7 Spices</b></div>
          <div class="specrow"><span>RC / CN / TM</span><b>Chilli · Coriander · Turmeric</b></div>
          <div class="specrow"><span>24</span><b>Harvest year</b></div>
          <div class="specrow"><span>06</span><b>Batch of the season</b></div>
          <div class="specrow"><span>Links to</span><b class="verified">''' + I["check"] + r''' Farm-belt · season · lab report</b></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow">With every shipment</span><h2>The documents that travel with your spice.</h2><p>Export-grade lots ship with the paperwork your customs, QA and procurement teams need — no chasing required.</p></div>
    <div class="grid g-3">
      <div class="card reveal"><div class="card__ico">''' + I["doc"] + r'''</div><h4>Certificate of Analysis</h4><p>Lot-specific lab results for the spec and safety parameters relevant to your market.</p></div>
      <div class="card reveal d1"><div class="card__ico">''' + I["doc"] + r'''</div><h4>Specification sheet</h4><p>Variety, origin, grade, mesh, SHU/ASTA or curcumin, moisture and packaging detail.</p></div>
      <div class="card reveal d2"><div class="card__ico">''' + I["globe"] + r'''</div><h4>Export &amp; origin docs</h4><p>Commercial invoice, packing list, certificate of origin and phytosanitary paperwork as required.</p></div>
    </div>
    <div class="divider"></div>
    <div class="center reveal">
      <span class="eyebrow center">Standards we work to</span>
      <h3 style="font-size:clamp(1.4rem,2.6vw,2rem);margin:.5em 0 1em">Aligned to global food-safety expectations</h3>
      <p class="muted" style="max-width:62ch;margin:0 auto 8px">Our handling, hygiene and testing are built around recognised food-safety and export frameworks — including FSSAI compliance for Indian food businesses, Halal-friendly handling for the Gulf, and pesticide/aflatoxin limits aligned to EU thresholds.</p>
      <p class="form-note" style="max-width:62ch;margin:0 auto">Specific certifications can be confirmed for your market on request — tell us your destination and we'll share what applies to your lot.</p>
    </div>
  </div>
</section>

<section class="section roast ctaband">
  <div class="wrap"><div class="ctaband__inner reveal">
    <h2>Need a sample with its lab report?</h2>
    <p>Tell us the crop, grade and market. We'll send documented samples you can verify before you commit.</p>
    <div class="btn-row"><a class="btn btn--primary" href="contact.html">Request documented samples ''' + I["arrow"] + r'''</a><a class="btn btn--light" href="harvest-calendar.html">Check crop freshness</a></div>
  </div></div>
</section>
'''
page("quality.html", "Quality & Traceability — Lab-Tested, Lot-Coded Spices | Ace7 Spices",
     "Ace7 Spices batch-tests every lot for pungency, colour, curcumin, moisture, pesticide, aflatoxin, microbiology and adulteration — then lot-codes it for full farm-to-export traceability.",
     quality, "Quality")

# ===================== SUSTAINABILITY =====================
sustain = phero("", "Sustainability",
    "Clean spice starts with the soil and the farmer.",
    "Single-origin sourcing is only as good as the relationships behind it. We invest in the farm-belts we buy from — because flavour, fairness and continuity travel together.",
    "images/farmers-field.jpg", "Indian spice farmers standing in a cultivated field",
    [("4","Farm-belts sourced"),("0","Middle-man markups hidden"),("Long","-term grower ties")]) + r'''

<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="split__body reveal">
        <span class="eyebrow leaf">Our philosophy</span>
        <h2>Give back to the source.</h2>
        <p>A spice can only be as good as the season and the soil it came from — and a supply chain can only be as clean as the people in it are treated fairly. So we treat sourcing as a relationship, not a transaction.</p>
        <p>Working close to the growing regions lets us reward quality directly, keep the chain short, and build the kind of repeat relationships that produce consistent crops year after year. Good for the farmer, good for the lot, good for you.</p>
      </div>
      <div class="split__media reveal d1">''' + img("images/farmer-portrait.jpg", "Portrait of an Indian spice farmer holding fresh produce", "", "ph--tall") + r'''</div>
    </div>
  </div>
</section>

<section class="section paper-2">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow leaf">How we put it into practice</span><h2>Commitments we're building on.</h2></div>
    <div class="grid g-3">
      <div class="card reveal"><div class="card__ico">''' + I["handshake"] + r'''</div><h4>Fair, direct sourcing</h4><p>Buying close to source means growers are rewarded for quality, and the value of a good crop reaches the people who raised it.</p></div>
      <div class="card reveal d1"><div class="card__ico">''' + I["sprout"] + r'''</div><h4>Quality-led farming</h4><p>We favour growers and practices that protect soil and crop health — the foundation of high essential-oil, high-curcumin, deep-colour spice.</p></div>
      <div class="card reveal d2"><div class="card__ico">''' + I["leaf"] + r'''</div><h4>Less waste, less harm</h4><p>Sorting and processing are run to minimise waste, and we avoid the chemical shortcuts that pollute both the product and the environment.</p></div>
      <div class="card reveal"><div class="card__ico">''' + I["globe"] + r'''</div><h4>Continuity of supply</h4><p>Durable grower relationships smooth out seasonal swings, so buyers get dependable volumes of the same quality year on year.</p></div>
      <div class="card reveal d1"><div class="card__ico">''' + I["box"] + r'''</div><h4>Responsible packaging</h4><p>We choose packaging that protects the spice while keeping material use sensible and fit for the destination market.</p></div>
      <div class="card reveal d2"><div class="card__ico">''' + I["shield"] + r'''</div><h4>Transparency</h4><p>Traceability isn't just a safety feature — it's a record of where value goes and how each lot was made.</p></div>
    </div>
  </div>
</section>

<section class="section roast">
  <div class="wrap center">
    <div class="reveal" style="max-width:26ch;margin-inline:auto">
      <p class="quote quote--center">"Replenish, nurture, and keep the chain short. The flavour follows."</p>
      <p class="cite">— How we think about sourcing</p>
    </div>
  </div>
</section>

<section class="section ctaband roast">
  <div class="wrap"><div class="ctaband__inner reveal">
    <h2>Source spice you can stand behind.</h2>
    <p>Talk to us about single-origin lots backed by fair sourcing and full traceability.</p>
    <div class="btn-row"><a class="btn btn--primary" href="contact.html">Get in touch ''' + I["arrow"] + r'''</a><a class="btn btn--light" href="about.html">Read our story</a></div>
  </div></div>
</section>
'''
page("sustainability.html", "Sustainability & Fair Sourcing — Ace7 Spices",
     "Ace7 Spices invests in the farm-belts it sources from — fair, direct sourcing, quality-led farming, responsible packaging and full traceability behind every single-origin lot.",
     sustain, "About")
