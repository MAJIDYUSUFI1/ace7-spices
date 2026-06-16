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

# ===================== PRODUCTS OVERVIEW =====================
products = phero("Products",
    "Three crops. Whole or powdered. Always single-origin.",
    "A focused range, on purpose. We'd rather be the best at three spices than average at thirty — each one sourced from the belt it's famous for and milled to your spec.",
    "images/products-flatlay.jpg", "Flat lay of red chilli, coriander and turmeric whole and powdered",
    [("3","Core crops"),("16+","Chilli varieties"),("2","Forms each")]) + r'''

<section class="section">
  <div class="wrap">
    <div class="grid g-3">
      <a class="origincard reveal" href="red-chilli.html">
        <div class="origincard__media">''' + img("images/red-chilli-guntur.jpg", "Glossy red Guntur chillies", "", "ph--tall") + r'''</div>
        <span class="tag">16 varieties</span>
        <div class="origincard__body"><span class="origincard__kick">Guntur · Andhra Pradesh</span><h3>Red Chilli</h3><p>Whole, crushed, flakes and powder. Teja, Sannam and Byadgi families — SHU and ASTA set to your formulation.</p><span class="txtlink">View red chilli ''' + I["arrow"] + r'''</span></div>
      </a>
      <a class="origincard reveal d1" href="coriander.html">
        <div class="origincard__media">''' + img("images/coriander-rajasthan.jpg", "Bold green coriander seed", "", "ph--tall") + r'''</div>
        <span class="tag">High volatile oil</span>
        <div class="origincard__body"><span class="origincard__kick">Rajasthan · Hadoti belt</span><h3>Coriander</h3><p>Bold Eagle &amp; Single seed and cold-pressed powder — bright, sweet-citrus aroma and ≥99% purity.</p><span class="txtlink">View coriander ''' + I["arrow"] + r'''</span></div>
      </a>
      <a class="origincard reveal d2" href="turmeric.html">
        <div class="origincard__media">''' + img("images/turmeric-sangli-salem.jpg", "Golden turmeric fingers and powder", "", "ph--tall") + r'''</div>
        <span class="tag">Graded by curcumin</span>
        <div class="origincard__body"><span class="origincard__kick">Sangli, MH · Salem, TN</span><h3>Turmeric</h3><p>Hard, bright fingers and high-curcumin powder — screened lead-chromate-free for safe, honest colour.</p><span class="txtlink">View turmeric ''' + I["arrow"] + r'''</span></div>
      </a>
    </div>
  </div>
</section>

<section class="section paper-2">
  <div class="wrap">
    <div class="split">
      <div class="split__body reveal">
        <span class="eyebrow">Whole &amp; powdered</span>
        <h2>Same crop, two forms — both cold-handled.</h2>
        <p>Whole spices ship as cleaned, graded, sun-dried material with their flavour locked in the seed or pod. When you need powder, we cold-press mill it at low RPM so it reaches you smelling like the whole spice it came from — not like something that's been heat-stripped on the way.</p>
        <ul class="checklist">
          <li>''' + I["check"] + r'''<span><b>Whole</b> — chilli pods, coriander seed, turmeric fingers; sorted &amp; graded.</span></li>
          <li>''' + I["check"] + r'''<span><b>Powder</b> — milled to your mesh, aroma and colour intact.</span></li>
          <li>''' + I["check"] + r'''<span><b>Specialty cuts</b> — crushed, seedless and flakes for chilli.</span></li>
        </ul>
      </div>
      <div class="split__media reveal d1">''' + img("images/whole-vs-powder.jpg", "Comparison of whole spices beside their cold-pressed powders", "", "ph--tall") + r'''</div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap center">
    <div class="section-head center reveal"><span class="eyebrow center">Packaging &amp; volumes</span><h2>Export-ready, in the format you order in.</h2><p>Food-grade, moisture-barrier packing built for the container and the climate it's crossing.</p></div>
    <div class="grid g-4 reveal">
      <div class="card"><div class="card__ico">''' + I["box"] + r'''</div><h4>Jute / gunny bags</h4><p>Breathable bags for whole spice in classic export weights.</p></div>
      <div class="card"><div class="card__ico">''' + I["box"] + r'''</div><h4>PP / laminated bags</h4><p>Moisture-barrier packing for powders and longer transits.</p></div>
      <div class="card"><div class="card__ico">''' + I["box"] + r'''</div><h4>Bulk &amp; custom</h4><p>Common formats around 10, 25 and 50 kg — or to your requirement.</p></div>
      <div class="card"><div class="card__ico">''' + I["tag"] + r'''</div><h4>Private label</h4><p>Your brand, your pack, our spice. See custom &amp; private label.</p></div>
    </div>
    <div class="center reveal" style="margin-top:36px"><a class="btn btn--primary" href="contact.html">Request the full spec &amp; price list ''' + I["arrow"] + r'''</a></div>
  </div>
</section>

<section class="section roast ctaband">
  <div class="wrap"><div class="ctaband__inner reveal">
    <h2>Not sure which grade fits your market?</h2>
    <p>Tell us the dish, the heat or colour you're after, and the destination — we'll recommend a variety and send samples.</p>
    <div class="btn-row"><a class="btn btn--primary" href="contact.html">Ask our team ''' + I["arrow"] + r'''</a><a class="btn btn--light" href="custom-blends.html">Explore custom blends</a></div>
  </div></div>
</section>
'''
page("products.html", "Products — Single-Origin Red Chilli, Coriander & Turmeric | Ace7 Spices",
     "Ace7 Spices' range: single-origin red chilli (Guntur), coriander (Rajasthan) and turmeric (Sangli & Salem), whole and cold-pressed powder, in export-ready packaging. Request the spec & price list.",
     products, "Products")

# ===================== RED CHILLI =====================
# (variety, badge_class, badge_label, SHU, ASTA, note, image)
CW = "images/chilli-whole-red.jpg"; CB = "images/chilli-byadgi.jpg"
CC = "images/chilli-crushed.jpg"; CF = "images/chilli-flakes.jpg"
VARIETIES = [
 ("Teja (S17)","b-heat","High heat","50,000–100,000","32–42","One of India's hottest chillies. The benchmark for fiery heat and oleoresin extraction.",CW),
 ("334 / S4 Sannam","b-balanced","Balanced","25,000–40,000","32–38","The export workhorse of Guntur — a clean balance of heat and bright red colour.",CW),
 ("Syngenta Byadgi (5531)","b-color","Deep colour","8,000–15,000","60–130","Wrinkled, low-heat Byadgi prized for intense natural red colour and oleoresin.",CB),
 ("355 Byadgi","b-color","Deep colour","10,000–20,000","60–90","Colour-forward Byadgi type for paprika-style applications with gentle heat.",CB),
 ("2043 Byadgi","b-color","Colour + mild heat","15,000–25,000","50–80","Rich colour with a touch more bite than classic Byadgi.",CB),
 ("Spark 01","b-heat","Hot","30,000–55,000","35–45","Bright, glossy-skinned hybrid with strong heat and good colour.",CW),
 ("Armur","b-balanced","Balanced","25,000–40,000","30–38","Long, smooth pods — a versatile all-purpose Guntur chilli.",CW),
 ("Kubera","b-balanced","Balanced","25,000–45,000","35–45","Thick-skinned hybrid with dependable heat and colour for blends.",CW),
 ("414 Hybrid","b-heat","Hot","30,000–50,000","32–42","A popular all-rounder — solid heat, good colour, consistent supply.",CW),
 ("Romi 26","b-heat","Hot","30,000–50,000","35–45","Vibrant red pods with assertive heat for bold curries and sauces.",CW),
 ("341","b-balanced","Balanced","25,000–40,000","30–40","Smooth, uniform pods well suited to grinding and blends.",CW),
 ("DD (Dabbi)","b-color","Colour-rich","15,000–30,000","40–55","Wrinkled, colour-rich variety bridging Byadgi colour and Guntur heat.",CB),
 ("Endo 5","b-balanced","Balanced","25,000–45,000","32–42","A versatile hybrid for everyday culinary and processing use.",CW),
 ("Classic","b-balanced","Everyday","25,000–40,000","32–40","The dependable everyday curry chilli — clean colour, moderate heat.",CW),
 ("334 Crushed Seedless","b-balanced","Crushed","per 334","—","334 chilli crushed with seeds removed — even heat, less pungent dust.",CC),
 ("334 Chilli Flakes","b-balanced","Flakes","per 334","—","Coarse chilli flakes for finishing, toppings and table use.",CF),
]
vcards = ""
for name, bc, bl, shu, asta, note, im in VARIETIES:
    vcards += (
      '<div class="variety reveal"><div class="variety__media">' + img(im, name + " red chilli", "", "ph--sq") + '</div>'
      '<div class="variety__body"><span class="variety__cat">Guntur red chilli</span>'
      '<h4>' + name + '</h4>'
      '<span class="variety__badge ' + bc + '">' + bl + '</span>'
      '<div class="variety__specs"><div><span>SHU</span><b>' + shu + '</b></div>'
      '<div><span>ASTA</span><b>' + asta + '</b></div></div>'
      '<p style="font-size:.84rem;color:var(--ink-soft);margin-bottom:14px;line-height:1.45">' + note + '</p>'
      '<a class="txtlink" href="contact.html">Enquire ' + I["arrow"] + '</a></div></div>'
    )

redchilli = phero("Red chilli",
    "Guntur red chilli — heat and colour, measured.",
    "From the heartland of India's chilli trade. We don't just sell \"hot\" — we set pungency (SHU) and colour (ASTA) to your formulation, then prove it in the lab.",
    "images/red-chilli-hero.jpg", "Mounds of vivid red Guntur chillies",
    [("8k–100k","SHU range"),("32–160","ASTA colour"),("16","Varieties")]) + r'''

<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="split__body reveal">
        <span class="eyebrow">Origin · Guntur, Andhra Pradesh</span>
        <h2>Where the world's heat is graded.</h2>
        <p>Guntur is to chilli what Champagne is to sparkling wine. Its soil, sun and the vast Guntur Mirchi Yard — among the largest chilli markets on earth — make it the reference point global buyers measure heat and colour against.</p>
        <p>That depth of supply is what lets us be precise. Need fire? We reach for Teja. Need a clean culinary balance? Sannam. Need deep, natural red colour with gentle heat? The Byadgi family. Whatever your dish or label demands, there's a Guntur variety that hits it — and a lab number to confirm it.</p>
        <ul class="checklist">
          <li>''' + I["check"] + r'''<span><b>SHU to spec</b> — pungency matched to your recipe and market.</span></li>
          <li>''' + I["check"] + r'''<span><b>ASTA to spec</b> — colour value set for the look your buyers expect.</span></li>
          <li>''' + I["check"] + r'''<span><b>Whole, crushed, flakes &amp; powder</b> — cold-press milled for aroma.</span></li>
        </ul>
      </div>
      <div class="split__media reveal d1">''' + img("images/red-chilli-field.jpg", "Red chilli plants ripening in a Guntur field", "", "ph--tall") + r'''</div>
    </div>
  </div>
</section>

<section class="section roast" data-heatscale>
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow cream">Set the heat &amp; colour</span><h2>Pick a profile. See where it sits.</h2><p>SHU measures heat; ASTA measures colour. Most buyers want one high and the other balanced — here's how our main families compare. Tap a profile.</p></div>
    <div class="heatscale reveal">
      <div class="heatpicker">
        <button data-heat="byadgi">Byadgi — colour</button>
        <button data-heat="sannam">Sannam — balanced</button>
        <button data-heat="414">414 — hot</button>
        <button data-heat="teja">Teja — max heat</button>
      </div>
      <div class="heatscale__track">
        <div class="heatscale__mark"><b>Sannam</b><span>~40,000 SHU max</span></div>
      </div>
      <div class="heatscale__labels"><span>Mild · 5k</span><span>Medium · 30k</span><span>Hot · 60k</span><span>Very hot · 100k+</span></div>
      <div class="heatout">
        <div><span>Scoville (SHU)</span><b data-out="shu">25,000–40,000</b></div>
        <div><span>Colour (ASTA)</span><b data-out="asta">32–38</b></div>
        <div><span>Best for</span><b data-out="use" style="font-family:'IBM Plex Sans';font-size:.92rem;line-height:1.3">Balanced curry &amp; blends</b></div>
      </div>
      <p class="cal__hint" style="margin-top:18px">Indicative ranges — exact SHU &amp; ASTA are set per order and confirmed by lab report.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow">The catalogue</span><h2>16 Guntur &amp; Byadgi varieties.</h2><p>Whole pods, crushed, flakes and cold-pressed powder. Heat-forward, colour-forward or balanced — sorted into grades (Deluxe, Best, Stemless, Stem-cut, Fatki/Tall) on request.</p></div>
    <div class="varietygrid">''' + vcards + r'''</div>
    <p class="cal__hint" style="color:var(--ink-faint);margin-top:24px">SHU and ASTA figures are typical industry ranges and are tuned to your specification per order. Crushed &amp; flake heat follows the source variety.</p>
  </div>
</section>

<section class="section paper-2">
  <div class="wrap" data-tabs>
    <div class="section-head reveal"><span class="eyebrow">Forms &amp; grades</span><h2>Choose your form.</h2></div>
    <div class="tabs reveal" style="margin-bottom:30px">
      <button class="tab active" data-tab="whole">Whole pods</button>
      <button class="tab" data-tab="powder">Cold-pressed powder</button>
      <button class="tab" data-tab="cut">Crushed &amp; flakes</button>
    </div>
    <div class="tabpanel active" data-panel="whole">
      <div class="split">
        <div class="split__media reveal">''' + img("images/chilli-whole-red.jpg", "Whole dried red chilli pods", "", "ph--wide") + r'''</div>
        <div class="split__body reveal d1"><h3 style="font-size:1.6rem;margin-bottom:.5em">Whole dried chilli</h3><p>Sun-dried, cleaned and graded pods with stems on or off. Sorted into trade grades — Deluxe, Best, Medium Best, Stemless, Stem-cut and Fatki/Tall — to match your spec and budget.</p><ul class="checklist"><li>''' + I["check"] + r'''<span>Moisture held to export limits</span></li><li>''' + I["check"] + r'''<span>Colour- and defect-sorted</span></li><li>''' + I["check"] + r'''<span>Jute, gunny or PP packing</span></li></ul></div>
      </div>
    </div>
    <div class="tabpanel" data-panel="powder">
      <div class="split">
        <div class="split__media reveal">''' + img("images/chilli-powder.jpg", "Vivid red cold-pressed chilli powder", "", "ph--wide") + r'''</div>
        <div class="split__body reveal d1"><h3 style="font-size:1.6rem;margin-bottom:.5em">Cold-pressed chilli powder</h3><p>Milled at low RPM so the powder stays aromatic and deep red instead of dull and heat-stripped. Ground to your mesh, with SHU and ASTA confirmed by lab report on every lot.</p><ul class="checklist"><li>''' + I["check"] + r'''<span>Mesh ground to order</span></li><li>''' + I["check"] + r'''<span>No added colour or anti-caking chemicals</span></li><li>''' + I["check"] + r'''<span>SHU &amp; ASTA verified per lot</span></li></ul></div>
      </div>
    </div>
    <div class="tabpanel" data-panel="cut">
      <div class="split">
        <div class="split__media reveal">''' + img("images/chilli-flakes.jpg", "Coarse red chilli flakes", "", "ph--wide") + r'''</div>
        <div class="split__body reveal d1"><h3 style="font-size:1.6rem;margin-bottom:.5em">Crushed, seedless &amp; flakes</h3><p>334 crushed seedless for even heat with less pungent dust, and coarse chilli flakes for finishing, toppings and table use — cut from the same graded pods.</p><ul class="checklist"><li>''' + I["check"] + r'''<span>Seedless option for cleaner handling</span></li><li>''' + I["check"] + r'''<span>Flake size to specification</span></li><li>''' + I["check"] + r'''<span>Ideal for HORECA &amp; food service</span></li></ul></div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow">Where it goes</span><h2>What buyers use our chilli for.</h2></div>
    <div class="grid g-4">
      <div class="card reveal"><div class="card__ico">''' + I["chefhat"] + r'''</div><h4>HORECA kitchens</h4><p>Consistent heat and colour for curries, marinades and sauces, service after service.</p></div>
      <div class="card reveal d1"><div class="card__ico">''' + I["box"] + r'''</div><h4>Food manufacturing</h4><p>Spec-locked chilli for spice blends, snacks, pickles, sauces and ready meals.</p></div>
      <div class="card reveal d2"><div class="card__ico">''' + I["drop"] + r'''</div><h4>Colour &amp; oleoresin</h4><p>High-ASTA Byadgi and high-SHU Teja for natural colour and extraction.</p></div>
      <div class="card reveal d3"><div class="card__ico">''' + I["globe"] + r'''</div><h4>Retail &amp; private label</h4><p>Whole and powdered chilli packed under your own brand for shelf.</p></div>
    </div>
  </div>
</section>

<section class="section roast ctaband">
  <div class="wrap"><div class="ctaband__inner reveal">
    <h2>Tell us your SHU, ASTA and volume.</h2>
    <p>We'll match a Guntur variety, mill it to your mesh, and send documented samples with a lab report.</p>
    <div class="btn-row"><a class="btn btn--primary" href="contact.html">Request chilli samples ''' + I["arrow"] + r'''</a><a class="btn btn--light" href="harvest-calendar.html">When is chilli freshest?</a></div>
  </div></div>
</section>
'''
page("red-chilli.html", "Guntur Red Chilli Exporter — SHU & ASTA to Spec | Ace7 Spices",
     "Single-origin Guntur red chilli from Ace7 Spices: 16 varieties incl. Teja, Sannam (S4/334) and Byadgi. Whole, crushed, flakes & cold-pressed powder with SHU and ASTA set to your spec, lab-verified.",
     redchilli, "Products")
