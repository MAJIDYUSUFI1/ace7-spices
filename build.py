# -*- coding: utf-8 -*-
import os
from partials import head, header, footer, lotstrip_track, ICONS, PHONE, PHONE_DISP, EMAIL

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

# ===================== HOME =====================
home = r'''
<section class="hero">
  <div class="hero__media">''' + img("images/hero-spice-harvest.jpg", "Red chillies drying in the sun at a Guntur farm at golden hour", "", "ph--wide") + r'''</div>
  <div class="hero__grain"></div>
  <div class="hero__inner">
    <div class="hero__grid">
      <div class="reveal in">
        <span class="eyebrow cream">Single-origin · Cold-pressed · Lab-verified</span>
        <h1 class="display" style="margin-top:18px">The real flavours of India, <em>sealed at the source.</em></h1>
        <p class="hero__sub">We export single-origin red chilli, coriander and turmeric — cold-press milled at low RPM so the aroma survives the journey, batch-tested before every shipment, and traceable to the farm.</p>
        <div class="hero__cta">
          <a class="btn btn--primary" href="contact.html">Request a quote ''' + I["arrow"] + r'''</a>
          <a class="btn btn--ghost" href="products.html">View the range</a>
        </div>
        <div class="hero__stats">
          <div class="hstat"><b>3</b><span>Single-origin crops</span></div>
          <div class="hstat"><b>4</b><span>Markets served</span></div>
          <div class="hstat"><b>100%</b><span>Batch lab-tested</span></div>
        </div>
      </div>
      <div class="hero__card reveal in d1">
        <h4>Specimen lot · ships with every order</h4>
        <div class="specrow"><span>Lot code</span><b>AC7-RC-2406</b></div>
        <div class="specrow"><span>Origin</span><b>Guntur, Andhra Pradesh</b></div>
        <div class="specrow"><span>Pungency</span><b>35,000 SHU</b></div>
        <div class="specrow"><span>Colour (ASTA)</span><b>160</b></div>
        <div class="specrow"><span>Moisture</span><b>9.2%</b></div>
        <div class="specrow"><span>Lab report</span><b class="verified">''' + I["check"] + r''' Verified</b></div>
      </div>
    </div>
  </div>
  <div class="marquee"><div class="marquee__track">''' + lotstrip_track() + r'''</div></div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="uspstrip reveal">
      <div class="usp"><div class="usp__ico">''' + I["grind"] + r'''</div><h4>Cold-press, low-RPM milling</h4><p>Friction-free grinding keeps the volatile oils — and the aroma — intact in every powder.</p></div>
      <div class="usp"><div class="usp__ico">''' + I["shield"] + r'''</div><h4>Zero adulteration</h4><p>No added colours, no starch, no preservatives, no chemicals. Spice, and only spice.</p></div>
      <div class="usp"><div class="usp__ico">''' + I["flask"] + r'''</div><h4>Batch lab-tested</h4><p>Every lot is screened for pungency, colour, pesticide, microbiology and aflatoxin before dispatch.</p></div>
      <div class="usp"><div class="usp__ico">''' + I["qr"] + r'''</div><h4>Fully traceable</h4><p>Each pack carries a lot code linking back to the farm-belt, the season and its lab report.</p></div>
    </div>
  </div>
</section>

<section class="section paper-2">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">Three crops · three heartlands</span>
      <h2>We don't sell "Indian spices." We sell one crop, from one belt, picked at one season.</h2>
      <p>Single-origin means traceable flavour you can specify and repeat — never a blended-down commodity.</p>
    </div>
    <div class="grid g-3">
      <a class="origincard reveal" href="red-chilli.html">
        <div class="origincard__media">''' + img("images/red-chilli-guntur.jpg", "Glossy red Guntur chillies", "", "ph--tall") + r'''</div>
        <span class="tag">16 varieties</span>
        <div class="origincard__body">
          <span class="origincard__kick">Guntur · Andhra Pradesh</span>
          <h3>Red Chilli</h3>
          <p>Heat and colour, measured. We match SHU and ASTA to your formulation — Teja for fire, Sannam for balance, Byadgi for deep colour.</p>
          <div class="origincard__spec">
            <div><span>SHU range</span><b>8k–100k</b></div>
            <div><span>ASTA</span><b>32–160</b></div>
            <div><span>Form</span><b>Whole · Powder</b></div>
          </div>
          <span class="txtlink">Explore red chilli ''' + I["arrow"] + r'''</span>
        </div>
      </a>
      <a class="origincard reveal d1" href="coriander.html">
        <div class="origincard__media">''' + img("images/coriander-rajasthan.jpg", "Bold green-toned coriander seed", "", "ph--tall") + r'''</div>
        <span class="tag">High volatile oil</span>
        <div class="origincard__body">
          <span class="origincard__kick">Rajasthan · Hadoti belt</span>
          <h3>Coriander</h3>
          <p>The aromatic seed of the desert. Cool nights and dry days concentrate the essential oils into a bold, bright, sweet-citrus seed.</p>
          <div class="origincard__spec">
            <div><span>Volatile oil</span><b>0.3–0.5%</b></div>
            <div><span>Purity</span><b>99%+</b></div>
            <div><span>Form</span><b>Whole · Powder</b></div>
          </div>
          <span class="txtlink">Explore coriander ''' + I["arrow"] + r'''</span>
        </div>
      </a>
      <a class="origincard reveal d2" href="turmeric.html">
        <div class="origincard__media">''' + img("images/turmeric-sangli-salem.jpg", "Bright golden turmeric fingers and powder", "", "ph--tall") + r'''</div>
        <span class="tag">Graded by curcumin</span>
        <div class="origincard__body">
          <span class="origincard__kick">Sangli, MH · Salem, TN</span>
          <h3>Turmeric</h3>
          <p>India's golden standard, measured in curcumin. Hard, bright fingers from two of the country's most prized turmeric belts.</p>
          <div class="origincard__spec">
            <div><span>Curcumin</span><b>2–5%</b></div>
            <div><span>Screened</span><b>Pb-free</b></div>
            <div><span>Form</span><b>Whole · Powder</b></div>
          </div>
          <span class="txtlink">Explore turmeric ''' + I["arrow"] + r'''</span>
        </div>
      </a>
    </div>
  </div>
</section>

<section class="section roast">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow cream">Why we're called Ace7</span>
      <h2>The Ace7 Standard — seven marks every lot must earn.</h2>
      <p>The "7" isn't decoration. It's the seven-point protocol a batch passes through before it carries our name — from the farm gate to the sealed export bag.</p>
    </div>
    <div class="marks reveal">
      <div class="mark"><div class="mark__no"></div><div class="mark__body"><h3>Single-origin sourcing</h3><p>One crop, one farm-belt, one season. We never blend regions or seasons down to hit a price — origin is the whole point.</p></div></div>
      <div class="mark"><div class="mark__no"></div><div class="mark__body"><h3>Hand-sorting &amp; grading</h3><p>Every lot is sorted for colour, size and defects before it goes near a mill. The best form in, the best result out.</p></div></div>
      <div class="mark"><div class="mark__no"></div><div class="mark__body"><h3>Cold-press, low-RPM milling</h3><p>Low-speed grinding generates almost no heat, so the volatile oils that carry aroma and pungency stay locked in the powder.</p></div></div>
      <div class="mark"><div class="mark__no"></div><div class="mark__body"><h3>Zero adulteration</h3><p>No colour additives, no starch fillers, no preservatives, no anti-caking chemistry. What's on the spec sheet is what's in the bag.</p></div></div>
      <div class="mark"><div class="mark__no"></div><div class="mark__body"><h3>Batch lab-testing</h3><p>Pungency, colour, curcumin, moisture, pesticide residue, microbiology and aflatoxin — tested lot by lot, before anything ships.</p></div></div>
      <div class="mark"><div class="mark__no"></div><div class="mark__body"><h3>End-to-end traceability</h3><p>A lot code on every pack ties the product back to its farm-belt, harvest season and its own lab report. Open a recall in seconds, not weeks.</p></div></div>
      <div class="mark"><div class="mark__no"></div><div class="mark__body"><h3>Climate-aware packaging</h3><p>Food-grade, moisture-barrier packing in export formats — so the spice that leaves our floor is the spice that reaches your kitchen.</p></div></div>
    </div>
    <div class="btn-row reveal" style="margin-top:40px">
      <a class="btn btn--light" href="about.html">Read our story ''' + I["arrow"] + r'''</a>
      <a class="btn btn--ghost" href="quality.html">See how we test</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow center">From soil to sealed</span>
      <h2>Source. Sort. Process.</h2>
      <p>A short, deliberately simple supply chain — because every hand a spice passes through is a chance for it to lose flavour or pick up something it shouldn't.</p>
    </div>
    <div class="steps">
      <div class="step reveal">
        <div class="step__media"><span class="step__no">1</span>''' + img("images/process-sourcing.jpg", "Farmer in a field handing over freshly harvested crop", "", "ph--wide") + r'''</div>
        <h3><small>Source</small>Straight from the farm-belt</h3>
        <p>We buy from the growing regions each crop is famous for — Guntur, Rajasthan's Hadoti, Sangli and Salem — close to the farmers who raise them.</p>
      </div>
      <div class="step reveal d1">
        <div class="step__media"><span class="step__no">2</span>''' + img("images/process-sorting.jpg", "Workers hand-sorting red chillies for colour and quality", "", "ph--wide") + r'''</div>
        <h3><small>Sort</small>Graded to the best form</h3>
        <p>Lots are cleaned, colour- and size-sorted, and defect-checked by hand and machine — so only the best material moves forward.</p>
      </div>
      <div class="step reveal d2">
        <div class="step__media"><span class="step__no">3</span>''' + img("images/process-coldpress.jpg", "Cold-press low-RPM spice grinding machine", "", "ph--wide") + r'''</div>
        <h3><small>Process</small>Cold-pressed &amp; lab-released</h3>
        <p>Cold-press milled to your spec, then lab-tested and lot-coded before it's packed in export-ready, moisture-barrier formats.</p>
      </div>
    </div>
    <div class="center reveal" style="margin-top:40px"><a class="btn btn--ghost" href="process.html">Walk through the full process ''' + I["arrow"] + r'''</a></div>
  </div>
</section>

<section class="section roast">
  <div class="wrap">
    <div class="split">
      <div class="split__media reveal">''' + img("images/harvest-field.jpg", "Seasonal spice field showing crop life cycle", "", "ph--tall") + r'''</div>
      <div class="split__body reveal d1">
        <span class="eyebrow cream">Buy at peak freshness</span>
        <h2>Know exactly when each crop is at its best.</h2>
        <p class="lead">Spices are seasonal. Our interactive harvest calendar maps the sowing, growth, harvest and processing windows for all three crops — so you can plan contracts around peak-freshness lots instead of guessing.</p>
        <ul class="checklist">
          <li>''' + I["check"] + r'''<span><b>Red chilli</b> — red-ripe harvest Dec–Mar, peaking Feb–Mar at the Guntur yard.</span></li>
          <li>''' + I["check"] + r'''<span><b>Coriander</b> — a rabi crop, harvested Feb–Mar across Rajasthan.</span></li>
          <li>''' + I["check"] + r'''<span><b>Turmeric</b> — an 8–9 month crop, dug and cured Jan–Mar.</span></li>
        </ul>
        <div class="btn-row" style="margin-top:28px"><a class="btn btn--light" href="harvest-calendar.html">Open the harvest calendar ''' + I["arrow"] + r'''</a></div>
      </div>
    </div>
  </div>
</section>

<section class="section paper-2">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">Who we ship to</span>
      <h2>Built for buyers who answer to a spec sheet.</h2>
      <p>From hotel and restaurant kitchens to import houses and food manufacturers — across four markets that demand consistency, documentation and food safety.</p>
    </div>
    <div class="markets reveal">
      <div class="market"><div class="market__code">HORECA</div><h4>Hotels, restaurants &amp; catering</h4><p>Consistent heat, colour and aroma that chefs can build a menu on, batch after batch.</p></div>
      <div class="market"><div class="market__code">GCC</div><h4>Gulf import &amp; distribution</h4><p>Export documentation, Halal-friendly handling and the deep colour the Gulf market prefers.</p></div>
      <div class="market"><div class="market__code">EU</div><h4>European food industry</h4><p>Pesticide, aflatoxin and microbiology screening aligned to strict European thresholds.</p></div>
      <div class="market"><div class="market__code">IND</div><h4>Indian manufacturers &amp; HORECA</h4><p>Reliable domestic supply of single-origin, single-spice lots in bulk formats.</p></div>
    </div>
    <p class="muted reveal" style="margin-top:26px;text-align:center">Need a recipe blend, a specific SHU, or your own private label? <a class="txtlink" href="custom-blends.html" style="display:inline-flex">We build to your formulation ''' + I["arrow"] + r'''</a></p>
  </div>
</section>

<section class="section">
  <div class="wrap center">
    <div class="reveal" style="max-width:24ch;margin-inline:auto">
      <p class="quote quote--center">"Real flavour isn't a tagline. It's a spec sheet you can verify."</p>
      <p class="cite">— The Ace7 promise</p>
    </div>
  </div>
</section>

<section class="section roast ctaband">
  <div class="wrap"><div class="ctaband__inner reveal">
    <span class="eyebrow cream" style="justify-content:center">Let's talk volumes</span>
    <h2>Tell us your spec. We'll send samples and a quote.</h2>
    <p>Share the crop, the grade, the SHU or curcumin you need and your destination market — we'll match a single-origin lot and get documented samples moving.</p>
    <div class="btn-row"><a class="btn btn--primary" href="contact.html">Request a quote ''' + I["arrow"] + r'''</a><a class="btn btn--light" href="tel:''' + PHONE + r'''">Call ''' + PHONE_DISP + r'''</a></div>
  </div></div>
</section>
'''
page("index.html", "Ace7 Spices — Single-Origin Indian Red Chilli, Coriander & Turmeric Exporter",
     "Ace7 Spices exports single-origin, cold-press milled, lab-tested red chilli (Guntur), coriander (Rajasthan) and turmeric (Sangli & Salem) to HORECA, GCC, Europe and India. Whole & powdered, fully traceable.",
     home, "Home")

# ===================== ABOUT =====================
about = r'''
<section class="phero">
  <div class="phero__media">''' + img("images/about-mandi.jpg", "Indian spice market with sacks of red chilli and turmeric", "", "ph--wide") + r'''</div>
  <div class="phero__inner reveal in">
    <p class="crumbs"><a href="index.html">Home</a> / <span>Our story</span></p>
    <h1 class="display">Spices that taste the way they do at the farm gate.</h1>
    <p>Ace7 Spices was built on a simple frustration: by the time most "Indian spices" reach a kitchen abroad, they've been blended down, colour-corrected and milled half to death. We set out to ship the other kind.</p>
    <div class="phero__meta">
      <div class="m"><b>3</b><span>Single-origin crops</span></div>
      <div class="m"><b>4</b><span>Markets served</span></div>
      <div class="m"><b>7</b><span>Quality marks per lot</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="split__body reveal">
        <span class="eyebrow">The origin story</span>
        <h2>It started in the mandi, not the boardroom.</h2>
        <p>The people behind Ace7 grew up around India's spice trade — in the colour and noise of the mandis, among the drying yards of the chilli belts and the boiling pits where turmeric is cured. We knew what a freshly milled spice was supposed to smell like.</p>
        <p>So it was hard to ignore what was arriving overseas under the name "Indian spice": powders cut with starch, chillies dyed for colour, turmeric brightened with things that don't belong in food, aroma ground out by hot, high-speed mills. Buyers were paying for India and receiving a commodity.</p>
        <p>We started Ace7 to close that gap — to take the best material from the regions each crop is actually famous for, process it gently and honestly, prove it in a lab, and ship it with its papers. Nothing exotic. Just the real thing, done properly.</p>
      </div>
      <div class="split__media reveal d1">''' + img("images/about-drying-yard.jpg", "Red chillies spread across a traditional drying yard in India", "", "ph--tall") + r'''</div>
    </div>
  </div>
</section>

<section class="section roast">
  <div class="wrap">
    <div class="split split--rev">
      <div class="split__media reveal">''' + img("images/about-seven-marks.jpg", "Close-up of a lab-tested spice batch with a lot label", "", "ph--tall") + r'''</div>
      <div class="split__body reveal d1">
        <span class="eyebrow cream">What the "7" means</span>
        <h2>Seven marks, or it doesn't carry our name.</h2>
        <p class="lead">Ace7 is named for the seven-point standard every lot has to earn. It's the shortest honest answer to the question buyers really ask: how do I know this is what you say it is?</p>
        <ul class="checklist">
          <li>''' + I["check"] + r'''<span><b>01 · Single-origin</b> — one crop, one belt, one season.</span></li>
          <li>''' + I["check"] + r'''<span><b>02 · Hand-sorted &amp; graded</b> — best form in, best result out.</span></li>
          <li>''' + I["check"] + r'''<span><b>03 · Cold-press, low-RPM milled</b> — aroma kept intact.</span></li>
          <li>''' + I["check"] + r'''<span><b>04 · Zero adulteration</b> — no colour, starch or chemicals.</span></li>
          <li>''' + I["check"] + r'''<span><b>05 · Batch lab-tested</b> — proven before it ships.</span></li>
          <li>''' + I["check"] + r'''<span><b>06 · End-to-end traceability</b> — a lot code on every pack.</span></li>
          <li>''' + I["check"] + r'''<span><b>07 · Climate-aware packaging</b> — flavour that survives the trip.</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section paper-2">
  <div class="wrap">
    <div class="grid g-3">
      <div class="card reveal"><div class="card__ico">''' + I["sprout"] + r'''</div><h3>Our mission</h3><p>To put genuinely single-origin, unadulterated Indian spice into the hands of professional buyers — and to make its quality something they can verify, not just trust.</p></div>
      <div class="card reveal d1"><div class="card__ico">''' + I["globe"] + r'''</div><h3>Our vision</h3><p>To be the name a serious buyer reaches for when "from India" has to mean a specific belt, a specific season and a specific, repeatable spec.</p></div>
      <div class="card reveal d2"><div class="card__ico">''' + I["handshake"] + r'''</div><h3>How we work</h3><p>Close to the farms at one end and to your spec sheet at the other, with the shortest possible supply chain in between and a lab report at every gate.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow">The values behind every lot</span><h2>What we refuse to compromise.</h2></div>
    <div class="grid g-2">
      <div class="card reveal"><span class="card__num">01</span><h4>Honesty over appearance</h4><p>We'd rather ship a chilli that's a shade less uniform than one that's been dyed to look the part. Colour comes from the crop, never from a bottle.</p></div>
      <div class="card reveal d1"><span class="card__num">02</span><h4>Aroma over throughput</h4><p>Low-RPM milling is slower and costlier than hammer mills. We accept that, because heat is what kills the aroma you're paying for.</p></div>
      <div class="card reveal"><span class="card__num">03</span><h4>Proof over promises</h4><p>Every claim on our spec sheets is something a lab can measure and a lot code can trace. Trust should be checkable.</p></div>
      <div class="card reveal d1"><span class="card__num">04</span><h4>Fairness at the source</h4><p>A clean supply chain starts with the people who grow the crop. We build durable relationships in the belts we buy from.</p></div>
    </div>
  </div>
</section>

<section class="section roast">
  <div class="wrap center">
    <div class="reveal" style="max-width:60ch;margin-inline:auto">
      <span class="eyebrow cream" style="justify-content:center">The company behind the brand</span>
      <h2 style="font-size:clamp(1.8rem,3.6vw,2.8rem);margin:.5em 0">Ace7 Spices™ is a brand of Ace Adam International LLP.</h2>
      <p class="lead">Ace Adam International LLP is the parent company that owns and operates the Ace7 Spices brand, our sourcing relationships and our export operations — giving buyers a single, accountable legal entity to contract with across every market we serve.</p>
      <div class="btn-row" style="justify-content:center;margin-top:30px"><a class="btn btn--primary" href="contact.html">Start a conversation ''' + I["arrow"] + r'''</a><a class="btn btn--ghost" href="process.html">See how we operate</a></div>
    </div>
  </div>
</section>
'''
page("about.html", "Our Story — Ace7 Spices | A Brand of Ace Adam International LLP",
     "The origin story behind Ace7 Spices: single-origin Indian spice, the seven-mark Ace7 Standard, and our mission to make spice quality verifiable. A brand of Ace Adam International LLP.",
     about, "About")
