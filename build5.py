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

def phero(crumb, title, sub, img_src, img_alt, metas):
    m = "".join(['<div class="m"><b>'+a+'</b><span>'+b+'</span></div>' for a, b in metas])
    return (r'''
<section class="phero">
  <div class="phero__media">''' + img(img_src, img_alt, "", "ph--wide") + r'''</div>
  <div class="phero__inner reveal in">
    <p class="crumbs"><a href="index.html">Home</a> / <span>''' + crumb + r'''</span></p>
    <h1 class="display">''' + title + r'''</h1>
    <p>''' + sub + r'''</p>
    <div class="phero__meta">''' + m + r'''</div>
  </div>
</section>''')

# ===================== HARVEST CALENDAR =====================
calendar = phero("Harvest calendar",
    "Know exactly when each crop is at its best.",
    "Spices are seasonal — and freshness is flavour. This interactive calendar maps the sowing, growth, harvest and processing windows for all three crops, with the specs that matter at each stage.",
    "images/harvest-hero.jpg", "Seasonal Indian spice landscape across the year",
    [("12","Months mapped"),("4","Crop phases"),("3","Crops")]) + r'''

<section class="section">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow">Interactive · tap any month</span><h2>The Ace7 harvest year.</h2><p>Each crop runs on its own clock. Tap a coloured cell to see what's happening on the farm that month — and what we test for when it reaches processing. Peak-harvest months are outlined.</p></div>
    <div class="calendar reveal" data-calendar>
      <div class="cal__legend">
        <span><i class="lg-sow"></i> Sowing / planting</span>
        <span><i class="lg-grow"></i> Growth &amp; flowering</span>
        <span><i class="lg-harvest"></i> Harvest <small style="opacity:.7">(outlined = peak)</small></span>
        <span><i class="lg-process"></i> Processing &amp; lab release</span>
      </div>
      <div class="cal-wrap"><div class="cal__grid"></div></div>
      <div class="cal__detail"></div>
      <p class="cal__hint">Tip: use the arrow / enter keys to step through months when focused. Windows are typical seasonal ranges and shift slightly year to year.</p>
    </div>
  </div>
</section>

<section class="section paper-2">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow">At a glance</span><h2>Crop calendars &amp; freshness windows.</h2></div>
    <div class="grid g-3">
      <div class="card reveal"><span class="card__num" style="color:var(--chilli)">RED CHILLI · GUNTUR</span><div class="card__ico">''' + I["fire"] + r'''</div><h4>Red chilli</h4><p><b>Sow</b> Jun–Jul · <b>Grow</b> Aug–Nov · <b>Harvest</b> Dec–Mar (peak Feb–Mar) · <b>Process</b> Feb–Apr.</p><p style="margin-top:10px;font-size:.86rem">A Kharif/irrigated crop; red-ripe pods are hand-picked in rounds and arrive at the Guntur yard through late winter.</p></div>
      <div class="card reveal d1"><span class="card__num" style="color:#8FA31E">CORIANDER · RAJASTHAN</span><div class="card__ico" style="background:rgba(143,163,30,.14);color:#6f8a16">''' + I["sprout"] + r'''</div><h4>Coriander</h4><p><b>Sow</b> Oct–Nov · <b>Grow</b> Dec–Jan · <b>Harvest</b> Feb–Mar (peak Mar) · <b>Process</b> Mar–Apr.</p><p style="margin-top:10px;font-size:.86rem">A rabi/winter crop; the cool season concentrates essential oils before the spring harvest and mandi arrivals.</p></div>
      <div class="card reveal d2"><span class="card__num" style="color:#b3730a">TURMERIC · SANGLI &amp; SALEM</span><div class="card__ico" style="background:rgba(217,142,4,.14);color:#b3730a">''' + I["drop"] + r'''</div><h4>Turmeric</h4><p><b>Plant</b> May–Jul · <b>Grow</b> Aug–Dec · <b>Harvest</b> Jan–Mar (peak Feb–Mar) · <b>Process</b> Feb–Apr.</p><p style="margin-top:10px;font-size:.86rem">A long, 8–9 month crop; rhizomes are dug, boiled, dried and polished before curcumin testing.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="split__body reveal">
        <span class="eyebrow">Why it matters to your contract</span>
        <h2>Buy fresh-season lots, not last year's stock.</h2>
        <p>Knowing the calendar lets you time orders to the freshest material — and lets us reserve peak-harvest lots for buyers who plan ahead. It also means honest answers: if a crop is between seasons, we'll tell you, and we'll show you the lot's harvest date in its traceability record.</p>
        <ul class="checklist">
          <li>''' + I["check"] + r'''<span><b>Plan ahead</b> — reserve peak-season lots before they're gone.</span></li>
          <li>''' + I["check"] + r'''<span><b>Verify freshness</b> — every lot code carries its harvest season.</span></li>
          <li>''' + I["check"] + r'''<span><b>Smooth supply</b> — we hold properly-stored stock between harvests.</span></li>
        </ul>
        <div class="btn-row" style="margin-top:26px"><a class="btn btn--primary" href="contact.html">Plan a seasonal order ''' + I["arrow"] + r'''</a></div>
      </div>
      <div class="split__media reveal d1">''' + img("images/harvest-planning.jpg", "Spice lots in controlled storage between harvest seasons", "", "ph--tall") + r'''</div>
    </div>
  </div>
</section>
'''
page("harvest-calendar.html", "Harvest Calendar — Spice Crop Seasons & Freshness | Ace7 Spices",
     "Interactive harvest calendar for Ace7 Spices: sowing, growth, harvest and processing windows for Guntur red chilli, Rajasthan coriander and Sangli/Salem turmeric, with stage specifications.",
     calendar, "Quality")

# ===================== INDUSTRIES & MARKETS =====================
industries = phero("Markets &amp; industries",
    "Four markets. One standard of proof.",
    "Whether a lot lands in a Gulf import house, a European factory, an Indian kitchen or a hotel group, it ships with the same single-origin sourcing, lab testing and documentation.",
    "images/markets-hero.jpg", "Export containers and a world map representing global spice trade",
    [("HORECA","· GCC · EU · IND"),("Bulk","& private label"),("Docs","with every lot")]) + r'''

<section class="section">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow">Markets we serve</span><h2>Built around what each buyer needs.</h2></div>
    <div class="grid g-2">
      <div class="card reveal"><div class="card__ico">''' + I["chefhat"] + r'''</div><h3>HORECA</h3><p>Hotels, restaurants, catering and cloud kitchens need flavour that doesn't drift between deliveries. Our spec-locked, lab-verified lots give chefs the same heat, colour and aroma every time — so the dish a guest loved last month tastes identical today.</p></div>
      <div class="card reveal d1"><div class="card__ico">''' + I["globe"] + r'''</div><h3>GCC &amp; the Gulf</h3><p>The Gulf market knows its spice and prefers deep, rich colour. We supply high-ASTA chilli and bright turmeric with Halal-friendly handling, full export documentation and packaging suited to the climate and the trade.</p></div>
      <div class="card reveal"><div class="card__ico">''' + I["shield"] + r'''</div><h3>Europe</h3><p>European food businesses work to some of the strictest residue and contaminant limits in the world. We screen pesticide, aflatoxin and microbiology against those thresholds and ship the Certificates of Analysis your QA team needs on file.</p></div>
      <div class="card reveal d1"><div class="card__ico">''' + I["box"] + r'''</div><h3>India</h3><p>For Indian manufacturers, HORECA groups and packers, we offer dependable domestic supply of single-origin, single-spice lots in bulk formats — FSSAI-compliant and traceable, without the commodity-grade variability.</p></div>
    </div>
  </div>
</section>

<section class="section roast">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow cream">Who buys from us</span><h2>The buyers we're built for.</h2></div>
    <div class="grid g-4">
      <div class="card card--roast reveal"><div class="card__ico">''' + I["box"] + r'''</div><h4>Importers &amp; distributors</h4><p>Reliable, documented lots to land, clear and move on.</p></div>
      <div class="card card--roast reveal d1"><div class="card__ico">''' + I["grind"] + r'''</div><h4>Food manufacturers</h4><p>Spec-locked spice for blends, sauces, snacks and ready meals.</p></div>
      <div class="card card--roast reveal d2"><div class="card__ico">''' + I["chefhat"] + r'''</div><h4>HORECA groups</h4><p>Consistent kitchen-grade spice across many sites.</p></div>
      <div class="card card--roast reveal d3"><div class="card__ico">''' + I["tag"] + r'''</div><h4>Private-label brands</h4><p>Retail and food-service lines packed under your name.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="split__body reveal">
        <span class="eyebrow">Export &amp; logistics</span>
        <h2>Documented, packed and on schedule.</h2>
        <p>Exporting spice is as much about paperwork and packing as it is about the product. We coordinate the documents, formats and loading so your lot clears customs and reaches you without surprises.</p>
        <ul class="checklist">
          <li>''' + I["check"] + r'''<span><b>Export documentation</b> — invoice, packing list, certificate of origin, phytosanitary and CoA as required.</span></li>
          <li>''' + I["check"] + r'''<span><b>Market-fit packaging</b> — jute, PP and laminated formats around 10/25/50 kg or to spec.</span></li>
          <li>''' + I["check"] + r'''<span><b>Container loading</b> — coordinated dispatch with lot codes on every bag.</span></li>
          <li>''' + I["check"] + r'''<span><b>Documented samples first</b> — verify before you commit to volume.</span></li>
        </ul>
      </div>
      <div class="split__media reveal d1">''' + img("images/export-logistics.jpg", "Sealed spice bags being loaded into a shipping container", "", "ph--tall") + r'''</div>
    </div>
    <div class="divider"></div>
    <div class="statsband reveal" style="background:var(--roast)">
      <div class="bigstat"><b>3</b><span>Single-origin crops</span></div>
      <div class="bigstat"><b>16+</b><span>Chilli varieties</span></div>
      <div class="bigstat"><b>4</b><span>Markets served</span></div>
      <div class="bigstat"><b>100%</b><span>Lots lab-tested</span></div>
    </div>
  </div>
</section>

<section class="section roast ctaband">
  <div class="wrap"><div class="ctaband__inner reveal">
    <h2>Tell us your market. We'll ship to its standard.</h2>
    <p>Share your destination, the grade you need and your volume — we'll handle the spec, the testing and the documents.</p>
    <div class="btn-row"><a class="btn btn--primary" href="contact.html">Request a quote ''' + I["arrow"] + r'''</a><a class="btn btn--light" href="quality.html">See our testing</a></div>
  </div></div>
</section>
'''
page("industries.html", "Markets & Industries — HORECA, GCC, Europe & India | Ace7 Spices",
     "Ace7 Spices serves HORECA, GCC, European and Indian buyers — importers, food manufacturers, hotel groups and private-label brands — with single-origin, lab-tested, fully documented spice exports.",
     industries, "Markets")

# ===================== CONTACT =====================
contact = r'''
<section class="phero" style="padding-bottom:clamp(48px,6vw,72px)">
  <div class="phero__media">''' + img("images/contact-hero.jpg", "Spice samples laid out for a buyer inquiry", "", "ph--wide") + r'''</div>
  <div class="phero__inner reveal in">
    <p class="crumbs"><a href="index.html">Home</a> / <span>Contact</span></p>
    <h1 class="display">Tell us your spec. We'll send samples and a quote.</h1>
    <p>Share the crop, grade, SHU or curcumin you need and your destination market. We'll match a single-origin lot, send documented samples and quote your volume.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split" style="align-items:start;gap:clamp(30px,5vw,64px)">
      <div class="reveal">
        <span class="eyebrow">Request a quote</span>
        <h2 style="font-size:clamp(1.6rem,3vw,2.2rem);margin:.4em 0 1em">Trade inquiry</h2>
        <div class="formcard">
          <form data-inquiry novalidate>
            <div class="field-row">
              <div class="field"><label for="name">Your name <span class="req">*</span></label><input id="name" name="name" type="text" required autocomplete="name"></div>
              <div class="field"><label for="company">Company <span class="req">*</span></label><input id="company" name="company" type="text" required autocomplete="organization"></div>
            </div>
            <div class="field-row">
              <div class="field"><label for="email">Work email <span class="req">*</span></label><input id="email" name="email" type="email" required autocomplete="email"></div>
              <div class="field"><label for="phone">Phone / WhatsApp</label><input id="phone" name="phone" type="tel" autocomplete="tel"></div>
            </div>
            <div class="field-row">
              <div class="field"><label for="country">Country</label><input id="country" name="country" type="text" autocomplete="country-name"></div>
              <div class="field"><label for="market">Market</label>
                <select id="market" name="market"><option value="">Select…</option><option>HORECA</option><option>GCC / Gulf</option><option>Europe</option><option>India</option><option>Other</option></select>
              </div>
            </div>
            <div class="field">
              <label>Products of interest</label>
              <div class="checkgroup">
                <label class="checkitem"><input type="checkbox" value="Red chilli"> Red chilli</label>
                <label class="checkitem"><input type="checkbox" value="Coriander"> Coriander</label>
                <label class="checkitem"><input type="checkbox" value="Turmeric"> Turmeric</label>
                <label class="checkitem"><input type="checkbox" value="Custom blend / private label"> Custom / private label</label>
              </div>
            </div>
            <div class="field-row">
              <div class="field"><label for="form">Form</label>
                <select id="form" name="form"><option value="">Select…</option><option>Whole</option><option>Powder</option><option>Both</option><option>Crushed / flakes</option></select>
              </div>
              <div class="field"><label for="grade">Target spec (SHU / ASTA / curcumin)</label><input id="grade" name="grade" type="text" placeholder="e.g. 35,000 SHU · ASTA 160"></div>
            </div>
            <div class="field"><label for="volume">Estimated volume</label><input id="volume" name="volume" type="text" placeholder="e.g. 5,000 kg / month or a trial order"></div>
            <div class="field"><label for="message">Message</label><textarea id="message" name="message" placeholder="Tell us about your requirement, packaging, timelines or anything else."></textarea></div>
            <button class="btn btn--primary" type="submit" style="width:100%;justify-content:center">Send inquiry ''' + I["arrow"] + r'''</button>
            <p class="form-note">By sending, you agree to be contacted about your inquiry. We don't share your details. See our <a href="privacy-policy.html" style="color:var(--chilli)">privacy policy</a>.</p>
          </form>
          <div class="form-success">''' + I["check"] + r'''
            <h4>Thanks — your inquiry is ready to send.</h4>
            <p>To make sure it reaches us, tap below to open it in your email app. We typically reply within one business day.</p>
            <a class="btn btn--primary" data-mailto href="mailto:''' + EMAIL + r'''" style="margin-top:16px">Open in email ''' + I["arrow"] + r'''</a>
          </div>
        </div>
      </div>

      <div class="reveal d1">
        <span class="eyebrow">Direct channels</span>
        <h2 style="font-size:clamp(1.6rem,3vw,2.2rem);margin:.4em 0 1em">Reach us</h2>
        <div class="infocard"><div class="infocard__ico">''' + I["mail"] + r'''</div><div><h4>Email</h4><a href="mailto:''' + EMAIL + r'''">''' + EMAIL + r'''</a></div></div>
        <div class="infocard"><div class="infocard__ico">''' + I["phone"] + r'''</div><div><h4>Phone</h4><a href="tel:''' + PHONE + r'''">''' + PHONE_DISP + r'''</a></div></div>
        <div class="infocard"><div class="infocard__ico">''' + I["wa"] + r'''</div><div><h4>WhatsApp</h4><a href="https://wa.me/917415032994">''' + PHONE_DISP + r'''</a></div></div>
        <div class="infocard"><div class="infocard__ico">''' + I["globe"] + r'''</div><div><h4>Website</h4><a href="https://ace7spices.com">ace7spices.com</a></div></div>
        <div class="infocard"><div class="infocard__ico">''' + I["shield"] + r'''</div><div><h4>Registered entity</h4><p>Ace Adam International LLP<br><span class="muted" style="font-size:.92rem;font-weight:400">Parent company of Ace7 Spices™ · India</span></p></div></div>

        <div class="card card--roast" style="margin-top:28px;background:var(--roast)">
          <div class="card__num" style="color:var(--turmeric-2)">FAST TRACK</div>
          <h4 style="color:var(--paper)">Already know your spec?</h4>
          <p>Email us the crop, grade, SHU/curcumin, form and volume and we'll come straight back with sample availability and a quote.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section paper-2">
  <div class="wrap">
    <div class="section-head center reveal"><span class="eyebrow center">Before you ask</span><h2>Common questions.</h2></div>
    <div class="accordion reveal" style="max-width:820px;margin-inline:auto">
      <div class="acc"><button class="acc__q" aria-expanded="false">Do you provide samples?<span class="acc__ico"></span></button><div class="acc__a"><div class="acc__a-inner">Yes. We send documented samples with a lab report so you can verify the spec before committing to a volume order. Tell us the crop, grade and form you'd like to evaluate.</div></div></div>
      <div class="acc"><button class="acc__q" aria-expanded="false">Can you match a specific SHU, ASTA or curcumin level?<span class="acc__ico"></span></button><div class="acc__a"><div class="acc__a-inner">That's the core of how we work. For chilli we set pungency (SHU) and colour (ASTA); for turmeric we grade by curcumin. Share your target and we'll match a single-origin lot and confirm it by lab report.</div></div></div>
      <div class="acc"><button class="acc__q" aria-expanded="false">What are your minimum order quantities?<span class="acc__ico"></span></button><div class="acc__a"><div class="acc__a-inner">MOQs depend on the crop, grade and destination. We handle trial orders through to regular bulk contracts — tell us your volume and market and we'll advise what works.</div></div></div>
      <div class="acc"><button class="acc__q" aria-expanded="false">Do you offer private label?<span class="acc__ico"></span></button><div class="acc__a"><div class="acc__a-inner">Yes — both white-label (unbranded, ready for your packaging) and private-label (filled and sealed in your packs). See our custom blends &amp; private label page for details.</div></div></div>
      <div class="acc"><button class="acc__q" aria-expanded="false">Which documents ship with an order?<span class="acc__ico"></span></button><div class="acc__a"><div class="acc__a-inner">Export-grade lots travel with a Certificate of Analysis, specification sheet, commercial invoice, packing list, certificate of origin and phytosanitary documentation as your market requires.</div></div></div>
    </div>
  </div>
</section>
'''
page("contact.html", "Contact & Request a Quote | Ace7 Spices",
     "Request samples and a quote from Ace7 Spices. Tell us the crop, grade, SHU/curcumin, form and volume. Email support@ace7spices.com or call +91 74150 32994. A brand of Ace Adam International LLP.",
     contact, "Contact")

# ===================== PRIVACY =====================
privacy = r'''
<section class="phero" style="padding-bottom:clamp(40px,5vw,60px)">
  <div class="phero__inner reveal in" style="position:relative;z-index:2">
    <p class="crumbs"><a href="index.html">Home</a> / <span>Privacy policy</span></p>
    <h1 class="display" style="font-size:clamp(2.2rem,5vw,3.6rem)">Privacy policy</h1>
    <p>How Ace Adam International LLP handles the information you share with us through ace7spices.com.</p>
  </div>
  <div class="phero__media" style="opacity:.5"><div class="ph"></div></div>
</section>
<section class="section"><div class="wrap"><div class="prose reveal">
  <p class="updated">Last updated: ''' + "January 2025" + r'''</p>
  <p>This privacy policy explains how <strong>Ace Adam International LLP</strong> ("Ace7 Spices", "we", "us") collects and uses information when you visit <a href="https://ace7spices.com">ace7spices.com</a> or contact us about our products. We keep this simple: we only collect what we need to respond to you and run our business.</p>

  <h2>Information we collect</h2>
  <ul>
    <li><strong>Information you give us</strong> — such as your name, company, email, phone number, country, product interests and the details of your inquiry when you submit our contact form or email us.</li>
    <li><strong>Technical information</strong> — basic, non-identifying data your browser shares automatically (such as device and browser type) and aggregate usage analytics, where enabled.</li>
  </ul>

  <h2>How we use it</h2>
  <ul>
    <li>To respond to your inquiry, send samples, prepare quotes and manage our trading relationship.</li>
    <li>To improve our website and understand, in aggregate, how it is used.</li>
    <li>To comply with legal, accounting and export-documentation obligations.</li>
  </ul>

  <h2>Sharing</h2>
  <p>We do not sell your personal information. We share it only with service providers who help us operate (for example, email, hosting or logistics partners), and only as needed, or where required by law.</p>

  <h2>Data retention</h2>
  <p>We keep inquiry and trading records for as long as needed to serve you and to meet our legal and accounting obligations, after which we delete or anonymise them.</p>

  <h2>Your choices</h2>
  <p>You can ask us to access, correct or delete the personal information we hold about you, or to stop contacting you, by emailing <a href="mailto:''' + EMAIL + r'''">''' + EMAIL + r'''</a>. You can also decline non-essential cookies in your browser.</p>

  <h2>Cookies</h2>
  <p>We use only the cookies needed to run the site and, where enabled, privacy-respecting analytics to understand aggregate usage. We do not use them to build advertising profiles.</p>

  <h2>Contact</h2>
  <p>Questions about this policy can be sent to <a href="mailto:''' + EMAIL + r'''">''' + EMAIL + r'''</a> or by post to Ace Adam International LLP, India.</p>

  <p style="font-size:.86rem;color:var(--ink-faint);margin-top:2em">This document is provided as general information and should be reviewed by your legal adviser before publication to ensure it meets the requirements of the jurisdictions in which you operate.</p>
</div></div></section>
'''
page("privacy-policy.html", "Privacy Policy | Ace7 Spices",
     "How Ace Adam International LLP, the parent company of Ace7 Spices, collects and uses information shared via ace7spices.com.",
     privacy, "")

# ===================== TERMS =====================
terms = r'''
<section class="phero" style="padding-bottom:clamp(40px,5vw,60px)">
  <div class="phero__inner reveal in" style="position:relative;z-index:2">
    <p class="crumbs"><a href="index.html">Home</a> / <span>Terms &amp; conditions</span></p>
    <h1 class="display" style="font-size:clamp(2.2rem,5vw,3.6rem)">Terms &amp; conditions</h1>
    <p>The terms on which Ace Adam International LLP operates ace7spices.com and engages with buyers.</p>
  </div>
  <div class="phero__media" style="opacity:.5"><div class="ph"></div></div>
</section>
<section class="section"><div class="wrap"><div class="prose reveal">
  <p class="updated">Last updated: January 2025</p>
  <p>These terms govern your use of <a href="https://ace7spices.com">ace7spices.com</a> (the "site"), operated by <strong>Ace Adam International LLP</strong> under the brand <strong>Ace7 Spices™</strong>. By using the site you accept these terms.</p>

  <h2>About the site</h2>
  <p>The site provides information about our products and is an invitation for buyers to make inquiries. It is not an offer to sell, and nothing on it forms a binding contract on its own.</p>

  <h2>Product information &amp; specifications</h2>
  <p>Specifications, including SHU, ASTA, curcumin, volatile oil, purity and moisture, are presented as typical or indicative ranges. Exact values are set per order and confirmed for each lot by laboratory report. Crop characteristics vary naturally by season and harvest. Images are illustrative.</p>

  <h2>Orders &amp; quotations</h2>
  <p>Any order, price, sample or quotation is subject to a separate written agreement (such as a proforma invoice or sales contract) that sets out the binding specification, quantity, price, packaging, delivery terms and payment terms for that transaction.</p>

  <h2>Intellectual property</h2>
  <p>The Ace7 Spices name, logo, site content and design are owned by Ace Adam International LLP and may not be copied or reused without permission.</p>

  <h2>Acceptable use</h2>
  <p>You agree not to misuse the site, attempt to disrupt it, or use it for unlawful purposes.</p>

  <h2>Limitation of liability</h2>
  <p>The site is provided "as is". To the extent permitted by law, we are not liable for losses arising from reliance on general site information rather than the agreed specification and documentation for your specific order.</p>

  <h2>Governing law</h2>
  <p>These terms are governed by the laws of India, and the courts of India shall have jurisdiction, unless otherwise agreed in writing for a specific transaction.</p>

  <h2>Contact</h2>
  <p>Questions about these terms can be sent to <a href="mailto:''' + EMAIL + r'''">''' + EMAIL + r'''</a>.</p>

  <p style="font-size:.86rem;color:var(--ink-faint);margin-top:2em">This document is provided as general information and should be reviewed by your legal adviser before publication to ensure it meets the requirements of the jurisdictions in which you operate.</p>
</div></div></section>
'''
page("terms.html", "Terms & Conditions | Ace7 Spices",
     "Terms and conditions for ace7spices.com, operated by Ace Adam International LLP under the Ace7 Spices brand.",
     terms, "")
