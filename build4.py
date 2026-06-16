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

def spectable(headrow, rows):
    th = "".join(['<th>'+h+'</th>' for h in headrow])
    body = ""
    for r in rows:
        cells = "".join(['<td class="mono">'+c+'</td>' if i>0 else '<td>'+c+'</td>' for i, c in enumerate(r)])
        body += '<tr>'+cells+'</tr>'
    return '<div class="table-scroll reveal"><table class="spectable"><thead><tr>'+th+'</tr></thead><tbody>'+body+'</tbody></table></div>'

# ===================== CORIANDER =====================
coriander = phero("Coriander",
    "Rajasthan coriander — the aromatic seed of the desert.",
    "Cool desert nights and dry days concentrate the essential oils into a bold, bright, sweet-citrus seed. Bold Eagle and Single grades, whole or cold-pressed.",
    "images/coriander-hero.jpg", "Bold green coriander seed in close-up",
    [("0.3–0.5%","Volatile oil"),("99%+","Purity"),("Eagle","Premium grade")]) + r'''

<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="split__body reveal">
        <span class="eyebrow leaf">Origin · Rajasthan, Hadoti belt</span>
        <h2>Why the desert makes the better seed.</h2>
        <p>Coriander has moved through Indian kitchens and trade routes for thousands of years — and India today is the world's largest producer and exporter of it. Within India, Rajasthan's Hadoti belt around Ramganj Mandi is the trading heart, home to one of the largest coriander markets anywhere.</p>
        <p>The climate is the secret. Warm, dry days and cool nights slow the plant just enough to pack more essential oil into the seed. The payoff is a bold, plump, green-toned grain with a high volatile-oil content and a clean, sweet, citrus-forward aroma — the difference between coriander that perfumes a dish and coriander that just bulks it out.</p>
        <ul class="checklist">
          <li>''' + I["check"] + r'''<span><b>High volatile oil</b> — aroma you can smell and a lab can measure.</span></li>
          <li>''' + I["check"] + r'''<span><b>Bold, bright seed</b> — Eagle and Single grades, machine-cleaned.</span></li>
          <li>''' + I["check"] + r'''<span><b>Whole or cold-pressed powder</b> — green-toned and fragrant.</span></li>
        </ul>
      </div>
      <div class="split__media reveal d1">''' + img("images/coriander-field.jpg", "Coriander crop flowering in a Rajasthan field", "", "ph--tall") + r'''</div>
    </div>
  </div>
</section>

<section class="section paper-2">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow">Why demand keeps climbing</span><h2>The world's most-used seed spice.</h2><p>Coriander sits in spice blends, pickles, sausage and brewing recipes, snack seasonings and ground masalas across every continent — and the demand for clean, high-aroma seed only grows.</p></div>
    <div class="grid g-3">
      <div class="card reveal"><div class="card__ico">''' + I["chefhat"] + r'''</div><h4>Blends &amp; masalas</h4><p>A backbone of curry powders and ground blends — its citrus-sweet note rounds out heat and earth.</p></div>
      <div class="card reveal d1"><div class="card__ico">''' + I["box"] + r'''</div><h4>Pickling &amp; processing</h4><p>Whole seed for pickles, brines, sausage and charcuterie, and brewing applications.</p></div>
      <div class="card reveal d2"><div class="card__ico">''' + I["drop"] + r'''</div><h4>Extraction</h4><p>High essential-oil seed favoured for oil and oleoresin where aroma yield matters.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow">Specifications</span><h2>Coriander grades &amp; typical specs.</h2><p>Indicative ranges — exact figures are set per order and confirmed by lab report.</p></div>
    ''' + spectable(
        ["Grade / form","Volatile oil","Purity","Moisture","Best for"],
        [
          ["Eagle (bold, single)","0.35–0.50%","99%+","≤9%","Premium whole seed, retail &amp; export"],
          ["Single / scooter","0.30–0.45%","99%+","≤9%","General culinary &amp; processing"],
          ["Split coriander","0.25–0.40%","99%+","≤9%","Grinding &amp; blends"],
          ["Cold-pressed powder","retains aroma","milled to spec","≤9%","Masalas, seasonings, retail"],
        ]) + r'''
  </div>
</section>

<section class="section roast">
  <div class="wrap" data-tabs>
    <div class="section-head reveal"><span class="eyebrow cream">Forms</span><h2>Whole seed or cold-pressed powder.</h2></div>
    <div class="tabs reveal" style="margin-bottom:30px;background:rgba(247,241,230,.06);border-color:var(--line-light)">
      <button class="tab active" data-tab="cseed">Whole seed</button>
      <button class="tab" data-tab="cpowder">Cold-pressed powder</button>
    </div>
    <div class="tabpanel active" data-panel="cseed">
      <div class="split"><div class="split__media reveal">''' + img("images/coriander-seed-macro.jpg", "Macro of whole coriander seeds", "", "ph--wide") + r'''</div>
      <div class="split__body reveal d1"><h3 style="font-size:1.6rem;margin-bottom:.5em;color:var(--paper)">Whole coriander seed</h3><p>Machine-cleaned to ≥99% purity, sorted for bold, uniform, green-toned grains with low admixture and controlled moisture.</p><ul class="checklist"><li>''' + I["check"] + r'''<span>Eagle &amp; Single grades</span></li><li>''' + I["check"] + r'''<span>Low admixture, ≥99% purity</span></li><li>''' + I["check"] + r'''<span>Jute or PP export packing</span></li></ul></div></div>
    </div>
    <div class="tabpanel" data-panel="cpowder">
      <div class="split"><div class="split__media reveal">''' + img("images/coriander-powder.jpg", "Green-toned cold-pressed coriander powder", "", "ph--wide") + r'''</div>
      <div class="split__body reveal d1"><h3 style="font-size:1.6rem;margin-bottom:.5em;color:var(--paper)">Cold-pressed coriander powder</h3><p>Low-RPM milled so the powder keeps its fresh green colour and sweet-citrus aroma instead of turning dull and flat. Ground to your mesh.</p><ul class="checklist"><li>''' + I["check"] + r'''<span>Aroma &amp; colour preserved</span></li><li>''' + I["check"] + r'''<span>Mesh ground to order</span></li><li>''' + I["check"] + r'''<span>No fillers or additives</span></li></ul></div></div>
    </div>
  </div>
</section>

<section class="section roast ctaband">
  <div class="wrap"><div class="ctaband__inner reveal">
    <h2>Sample our Rajasthan coriander.</h2>
    <p>Tell us grade, form and volume — we'll send documented samples with volatile-oil and purity figures.</p>
    <div class="btn-row"><a class="btn btn--primary" href="contact.html">Request coriander samples ''' + I["arrow"] + r'''</a><a class="btn btn--light" href="harvest-calendar.html">Coriander season</a></div>
  </div></div>
</section>
'''
page("coriander.html", "Rajasthan Coriander Exporter — High Volatile-Oil Seed | Ace7 Spices",
     "Single-origin Rajasthan coriander from Ace7 Spices: bold Eagle & Single grades, high volatile oil, ≥99% purity, whole seed or cold-pressed powder. Lab-verified, export-ready.",
     coriander, "Products")

# ===================== TURMERIC =====================
turmeric = phero("Turmeric",
    "Sangli &amp; Salem turmeric — India's golden standard.",
    "Hard, bright fingers from two of the country's most prized turmeric belts — graded by curcumin and screened lead-chromate-free for safe, honest colour.",
    "images/turmeric-hero.jpg", "Bright golden turmeric fingers and powder",
    [("2–5%","Curcumin"),("Pb-free","Screened"),("2 belts","Sourced")]) + r'''

<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="split__body reveal">
        <span class="eyebrow turmeric">Origin · Sangli, MH &amp; Salem, TN</span>
        <h2>The sacred spice, measured in curcumin.</h2>
        <p>Turmeric has been India's golden spice for more than four thousand years — sacred in ritual, central in the kitchen, and now one of the most sought-after ingredients in the global wellness and food-colour industries. Where modern buyers used to ask "how bright?", they now ask "how much curcumin?".</p>
        <p>We answer from two belts that lead on exactly that. Sangli, in Maharashtra, is one of Asia's largest turmeric trading hubs, famed for hard, lustrous fingers. Salem and the Erode belt in Tamil Nadu are prized for high-curcumin turmeric — the benchmark for food, colour and nutraceutical buyers. We grade by curcumin and colour, and we screen every lot lead-chromate-free.</p>
        <ul class="checklist">
          <li>''' + I["check"] + r'''<span><b>Curcumin-graded</b> — typically 2–5%, set to your requirement.</span></li>
          <li>''' + I["check"] + r'''<span><b>Hard, bright fingers</b> — boiled, dried and polished.</span></li>
          <li>''' + I["check"] + r'''<span><b>Lead-chromate screened</b> — honest colour, safe to eat.</span></li>
        </ul>
      </div>
      <div class="split__media reveal d1">''' + img("images/turmeric-field.jpg", "Turmeric crop being harvested in a field", "", "ph--tall") + r'''</div>
    </div>
  </div>
</section>

<section class="section paper-2">
  <div class="wrap">
    <div class="split split--rev">
      <div class="split__media reveal">''' + img("images/turmeric-curing.jpg", "Turmeric rhizomes being boiled and dried during curing", "", "ph--tall") + r'''</div>
      <div class="split__body reveal d1">
        <span class="eyebrow turmeric">The lead-chromate problem</span>
        <h2>Bright shouldn't mean dangerous.</h2>
        <p class="lead">Some turmeric on the world market is brightened with lead-chromate — a toxic industrial pigment used to fake a richer yellow. It's one of the most serious adulteration risks in the spice trade.</p>
        <p>We treat it as a hard line. Our turmeric gets its colour from curcumin and curing, not from a pigment, and every lot is explicitly screened for lead-chromate before it ships. The number you see on the spec sheet is real, and so is its safety.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow">Specifications</span><h2>Turmeric grades &amp; typical specs.</h2><p>Indicative ranges — exact curcumin and colour are set per order and confirmed by lab report.</p></div>
    ''' + spectable(
        ["Grade / form","Curcumin","Moisture","Screening","Best for"],
        [
          ["Salem high-curcumin finger","3.0–5.0%","≤10%","Pb-chromate: not detected","Nutraceutical, colour, premium"],
          ["Sangli bright finger","2.0–3.5%","≤10%","Pb-chromate: not detected","Culinary, retail, export"],
          ["Bulb / round","1.5–2.5%","≤10%","Pb-chromate: not detected","Grinding &amp; processing"],
          ["Cold-pressed powder","to spec","≤10%","Pb-chromate: not detected","Masalas, food colour, retail"],
        ]) + r'''
  </div>
</section>

<section class="section roast">
  <div class="wrap" data-tabs>
    <div class="section-head reveal"><span class="eyebrow cream">Forms</span><h2>Fingers or cold-pressed powder.</h2></div>
    <div class="tabs reveal" style="margin-bottom:30px;background:rgba(247,241,230,.06);border-color:var(--line-light)">
      <button class="tab active" data-tab="tfinger">Whole fingers</button>
      <button class="tab" data-tab="tpowder">Cold-pressed powder</button>
    </div>
    <div class="tabpanel active" data-panel="tfinger">
      <div class="split"><div class="split__media reveal">''' + img("images/turmeric-fingers.jpg", "Bright polished turmeric fingers", "", "ph--wide") + r'''</div>
      <div class="split__body reveal d1"><h3 style="font-size:1.6rem;margin-bottom:.5em;color:var(--paper)">Whole turmeric fingers</h3><p>Boiled, sun-dried and polished fingers, graded by belt and curcumin. Hard, bright and clean — ready for grinding or whole-spice use.</p><ul class="checklist"><li>''' + I["check"] + r'''<span>Sangli &amp; Salem grades</span></li><li>''' + I["check"] + r'''<span>Curcumin-graded</span></li><li>''' + I["check"] + r'''<span>Lead-chromate screened</span></li></ul></div></div>
    </div>
    <div class="tabpanel" data-panel="tpowder">
      <div class="split"><div class="split__media reveal">''' + img("images/turmeric-powder.jpg", "Vivid golden cold-pressed turmeric powder", "", "ph--wide") + r'''</div>
      <div class="split__body reveal d1"><h3 style="font-size:1.6rem;margin-bottom:.5em;color:var(--paper)">Cold-pressed turmeric powder</h3><p>Low-RPM milled to protect colour and curcumin, ground to your mesh. Deep, even gold with the curcumin figure confirmed by lab report.</p><ul class="checklist"><li>''' + I["check"] + r'''<span>Curcumin verified per lot</span></li><li>''' + I["check"] + r'''<span>No added colour — ever</span></li><li>''' + I["check"] + r'''<span>Mesh ground to order</span></li></ul></div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow">Where it goes</span><h2>From the kitchen to the capsule.</h2></div>
    <div class="grid g-4">
      <div class="card reveal"><div class="card__ico">''' + I["chefhat"] + r'''</div><h4>Culinary &amp; HORECA</h4><p>Even colour and warm, earthy flavour for curries, rice and ready meals.</p></div>
      <div class="card reveal d1"><div class="card__ico">''' + I["drop"] + r'''</div><h4>Natural food colour</h4><p>Honest, curcumin-driven yellow for sauces, snacks and dairy.</p></div>
      <div class="card reveal d2"><div class="card__ico">''' + I["flask"] + r'''</div><h4>Nutraceutical</h4><p>High-curcumin lots for supplements, extracts and wellness products.</p></div>
      <div class="card reveal d3"><div class="card__ico">''' + I["globe"] + r'''</div><h4>Retail &amp; private label</h4><p>Whole and powdered turmeric packed under your own brand.</p></div>
    </div>
  </div>
</section>

<section class="section roast ctaband">
  <div class="wrap"><div class="ctaband__inner reveal">
    <h2>Specify your curcumin. We'll match it.</h2>
    <p>Tell us the curcumin level, form and volume — we'll send documented, lead-chromate-screened samples.</p>
    <div class="btn-row"><a class="btn btn--primary" href="contact.html">Request turmeric samples ''' + I["arrow"] + r'''</a><a class="btn btn--light" href="harvest-calendar.html">Turmeric season</a></div>
  </div></div>
</section>
'''
page("turmeric.html", "Sangli & Salem Turmeric Exporter — High Curcumin, Lead-Chromate-Free | Ace7 Spices",
     "Single-origin turmeric from Ace7 Spices: hard, bright Sangli & high-curcumin Salem fingers and cold-pressed powder, graded by curcumin (2–5%) and screened lead-chromate-free. Lab-verified.",
     turmeric, "Products")

# ===================== CUSTOM BLENDS =====================
blends = phero("Custom blends",
    "Your formulation, our single-origin spice.",
    "Beyond straight chilli, coriander and turmeric, we build to order — custom blends, set SHU and ASTA, bespoke mesh, and full private-label and white-label programmes.",
    "images/custom-blends-hero.jpg", "Custom spice blend being prepared with measured ingredients",
    [("To-spec","SHU · ASTA · mesh"),("OEM","Private label"),("Bulk","Or your packs")]) + r'''

<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="split__body reveal">
        <span class="eyebrow">Built to order</span>
        <h2>Send us the brief. We'll build the spice.</h2>
        <p>Every market and kitchen wants something slightly different — a specific heat, a particular red, a mesh that runs cleanly on your line, a recipe blend that's yours alone. Because we control sourcing and milling, we can build to that brief instead of asking you to settle for an off-the-shelf grade.</p>
        <p>Give us a target — a SHU figure, an ASTA value, a curcumin level, a sample of a blend you already use, or just the dish you're trying to nail — and we'll formulate, mill and document it as its own traceable, lab-released lot.</p>
        <ul class="checklist">
          <li>''' + I["check"] + r'''<span><b>Set SHU &amp; ASTA</b> for chilli, set curcumin for turmeric.</span></li>
          <li>''' + I["check"] + r'''<span><b>Custom mesh</b> milled to your line's requirement.</span></li>
          <li>''' + I["check"] + r'''<span><b>Recipe blends</b> matched from your sample or spec.</span></li>
        </ul>
      </div>
      <div class="split__media reveal d1">''' + img("images/blend-bowls.jpg", "Bowls of spice components being weighed for a custom blend", "", "ph--tall") + r'''</div>
    </div>
  </div>
</section>

<section class="section paper-2">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow">How a custom order works</span><h2>From brief to documented lot.</h2></div>
    <div class="steps">
      <div class="step reveal"><span class="card__num">01</span><h3 style="margin-top:8px">Share your brief</h3><p>Send target specs, a reference sample, your destination market and volume. The more detail, the closer the first sample.</p></div>
      <div class="step reveal d1"><span class="card__num">02</span><h3 style="margin-top:8px">Sample &amp; refine</h3><p>We formulate and mill a documented sample with its lab report. You taste, test and tell us what to adjust.</p></div>
      <div class="step reveal d2"><span class="card__num">03</span><h3 style="margin-top:8px">Lock &amp; produce</h3><p>Once approved, the spec becomes a repeatable, lot-coded standard — produced, packed and shipped to schedule.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split split--rev">
      <div class="split__media reveal">''' + img("images/private-label-packs.jpg", "Private-label spice packaging mockups with blank branding", "", "ph--tall") + r'''</div>
      <div class="split__body reveal d1">
        <span class="eyebrow">Private &amp; white label</span>
        <h2>Our spice. Your brand on the bag.</h2>
        <p class="lead">Run a retail line, a HORECA brand or a distribution label without operating a spice plant. We supply the product; you supply the brand — and the pack carries your identity, not ours.</p>
        <ul class="checklist">
          <li>''' + I["check"] + r'''<span><b>White-label supply</b> — unbranded, ready for your packaging.</span></li>
          <li>''' + I["check"] + r'''<span><b>Private-label packing</b> — filled and sealed in your packs.</span></li>
          <li>''' + I["check"] + r'''<span><b>Format flexibility</b> — retail pouches to bulk bags.</span></li>
          <li>''' + I["check"] + r'''<span><b>Consistent, traceable lots</b> — the quality behind your name.</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section roast ctaband">
  <div class="wrap"><div class="ctaband__inner reveal">
    <h2>Have a spec or a sample in mind?</h2>
    <p>Send it over. We'll formulate a documented sample and quote production volumes.</p>
    <div class="btn-row"><a class="btn btn--primary" href="contact.html">Start a custom order ''' + I["arrow"] + r'''</a><a class="btn btn--light" href="products.html">See the base range</a></div>
  </div></div>
</section>
'''
page("custom-blends.html", "Custom Blends, Private Label & White Label Spices | Ace7 Spices",
     "Ace7 Spices builds to your brief: custom spice blends, set SHU/ASTA and curcumin, bespoke mesh, and full private-label & white-label programmes — single-origin, lab-tested, traceable.",
     blends, "Products")
