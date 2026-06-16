# -*- coding: utf-8 -*-
"""Shared building blocks for every Ace7 Spices page."""

PHONE = "+917415032994"
PHONE_DISP = "+91 74150 32994"
EMAIL = "support@ace7spices.com"

ICONS = {
 "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 "chevron": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9l6 6 6-6"/></svg>',
 "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg>',
 "leaf": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/><path d="M2 21c0-3 1.85-5.36 5.08-6"/></svg>',
 "flask": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M9 3h6M10 3v6.5L4.5 18A2 2 0 0 0 6.2 21h11.6a2 2 0 0 0 1.7-3l-5.5-8.5V3"/><path d="M7.5 14h9"/></svg>',
 "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z"/><path d="m9 12 2 2 4-4"/></svg>',
 "grind": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3.2"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2.1 2.1M16.9 16.9 19 19M19 5l-2.1 2.1M7.1 16.9 5 19"/></svg>',
 "tag": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M20.6 13.4 13.4 20.6a2 2 0 0 1-2.8 0l-7.2-7.2A2 2 0 0 1 2.8 12V4.8A2 2 0 0 1 4.8 2.8H12a2 2 0 0 1 1.4.6l7.2 7.2a2 2 0 0 1 0 2.8Z"/><circle cx="7.5" cy="7.5" r="1.2"/></svg>',
 "sprout": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M7 20h10M12 20V9"/><path d="M12 9C12 6 10 4 6 4c0 4 2 6 6 6Z"/><path d="M12 12c0-2.5 2-4.5 6-4.5 0 3.5-2 5.5-6 5.5Z"/></svg>',
 "globe": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20 15 15 0 0 1 0-20Z"/></svg>',
 "box": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="m21 8-9-5-9 5v8l9 5 9-5V8Z"/><path d="m3 8 9 5 9-5M12 13v8"/></svg>',
 "qr": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><path d="M14 14h3v3M21 14v7M17 21h-3"/></svg>',
 "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2 4.2 2 2 0 0 1 4 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.2a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.8 2Z"/></svg>',
 "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m2 6 10 7L22 6"/></svg>',
 "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>',
 "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
 "fire": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2s4 4 4 8a4 4 0 0 1-8 0c0-1 .5-2 .5-2S6 9 6 13a6 6 0 0 0 12 0c0-5-6-11-6-11Z"/></svg>',
 "drop": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2.5S5 10 5 14.5a7 7 0 0 0 14 0C19 10 12 2.5 12 2.5Z"/></svg>',
 "chefhat": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M6 13.9V19a1 1 0 0 0 1 1h10a1 1 0 0 0 1-1v-5.1a4.5 4.5 0 1 0-3-8.4 4 4 0 0 0-7 0 4.5 4.5 0 1 0-2 8.4Z"/><path d="M6 17h12"/></svg>',
 "doc": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8Z"/><path d="M14 2v6h6M9 13h6M9 17h6"/></svg>',
 "scale": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v18M7 7h10M5 21h14"/><path d="M7 7 4 14h6L7 7ZM17 7l-3 7h6l-3-7Z"/></svg>',
 "handshake": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="m11 17 2 2a1 1 0 0 0 1.4 0l5-5"/><path d="M3 9 8 4l4 4-2.5 2.5a1.8 1.8 0 0 0 2.5 2.6L15 10l6 6"/><path d="M21 14V9l-5-5"/></svg>',
 "fb": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M14 9h3V6h-3c-2.2 0-4 1.8-4 4v2H7v3h3v7h3v-7h3l.5-3H13v-2c0-.6.4-1 1-1Z"/></svg>',
 "ig": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg>',
 "li": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M6.5 8.5v10h-3v-10h3Zm-1.5-5a1.8 1.8 0 1 1 0 3.6 1.8 1.8 0 0 1 0-3.6ZM20.5 18.5h-3v-5.3c0-1.3-.5-2.1-1.6-2.1-1.2 0-1.7.8-1.7 2.1v5.3h-3v-10h3v1.3c.5-.8 1.4-1.6 3-1.6 2.2 0 3.3 1.4 3.3 4.2v6.1Z"/></svg>',
 "wa": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15l-1.3 4.7 4.8-1.3A10 10 0 1 0 12 2Zm5.3 13.9c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7-2.8-1.1-4.5-3.9-4.7-4.1-.1-.2-1-1.4-1-2.6 0-1.3.6-1.9.9-2.1.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 2c.1.1.1.3 0 .5l-.4.5c-.2.2-.3.3-.1.6.2.3.8 1.3 1.7 2 1.2.9 1.5 1 1.8.7.2-.3.4-.5.6-.7l.5-.2 1.9.9c.2.1.4.2.5.3.1.4.1 1-.1 1.6Z"/></svg>',
}

GOOGLE_FONTS = (
 '<link rel="preconnect" href="https://fonts.googleapis.com">'
 '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
 '<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400..700;1,9..144,400..600&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">'
)


def head(title, desc, rel=""):
    return (
        '<!DOCTYPE html><html lang="en"><head>'
        '<meta charset="UTF-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        '<title>' + title + '</title>'
        '<meta name="description" content="' + desc + '">'
        '<meta property="og:title" content="' + title + '">'
        '<meta property="og:description" content="' + desc + '">'
        '<meta property="og:type" content="website">'
        '<meta name="theme-color" content="#1E150F">'
        + GOOGLE_FONTS +
        '<link rel="stylesheet" href="' + rel + 'assets/styles.css">'
        '</head><body>'
        '<a href="#main" class="skip">Skip to content</a>'
    )


NAV = [
    ("Home", "index.html", None),
    ("About", None, [
        ("Our story", "about.html", "Origin, the Ace7 Standard & parent company"),
        ("Our process", "process.html", "Source → sort → cold-press → ship"),
        ("Sustainability", "sustainability.html", "Farmer partnerships & single-origin sourcing"),
    ]),
    ("Products", None, [
        ("All products", "products.html", "Whole & powdered range overview"),
        ("Red chilli — Guntur", "red-chilli.html", "16 varieties · SHU & ASTA to spec"),
        ("Coriander — Rajasthan", "coriander.html", "Bold seed · high volatile oil"),
        ("Turmeric — Sangli & Salem", "turmeric.html", "Graded by curcumin %"),
        ("Custom blends & private label", "custom-blends.html", "Built to your formulation"),
    ]),
    ("Quality", None, [
        ("Quality & traceability", "quality.html", "Batch lab-testing & lot tracing"),
        ("Harvest calendar", "harvest-calendar.html", "Crop cycles & freshness windows"),
    ]),
    ("Markets", "industries.html", None),
    ("Contact", "contact.html", None),
]


def header(active, rel=""):
    items = ""
    for label, href, drop in NAV:
        is_active = (active == label)
        cls = " active" if is_active else ""
        if drop:
            sub = ""
            for dlabel, dhref, ddesc in drop:
                sub += ('<a href="' + rel + dhref + '"><b>' + dlabel + '</b><span>' + ddesc + '</span></a>')
            items += (
                '<li class="nav__item"><span class="nav__link' + cls + '">' + label + ICONS["chevron"] + '</span>'
                '<div class="dropdown">' + sub + '</div></li>'
            )
        else:
            items += '<li class="nav__item"><a class="nav__link' + cls + '" href="' + rel + href + '">' + label + '</a></li>'

    return (
        '<header class="header"><div class="header__inner">'
        '<a class="brand" href="' + rel + 'index.html" aria-label="Ace7 Spices home">'
        '<span class="brand__mark">7</span>'
        '<span><span class="brand__name">ACE<b>7</b> SPICES</span>'
        '<span class="brand__tag">The real flavours of India</span></span></a>'
        '<nav class="nav" aria-label="Primary"><ul style="display:flex;align-items:center;gap:4px">' + items + '</ul></nav>'
        '<div class="header__cta">'
        '<a class="header__phone" href="tel:' + PHONE + '">' + PHONE_DISP + '</a>'
        '<a class="btn btn--primary" href="' + rel + 'contact.html">Request a quote ' + ICONS["arrow"] + '</a>'
        '</div>'
        '<button class="burger" aria-label="Menu" aria-expanded="false" aria-controls="drawer">'
        '<span></span><span></span><span></span></button>'
        '</div></header>' + drawer(rel)
    )


def drawer(rel=""):
    out = '<nav class="drawer" id="drawer" aria-label="Mobile">'
    out += '<a href="' + rel + 'index.html">Home</a>'
    out += '<div class="grp-label">About</div>'
    out += '<a class="sub" href="' + rel + 'about.html">Our story</a>'
    out += '<a class="sub" href="' + rel + 'process.html">Our process</a>'
    out += '<a class="sub" href="' + rel + 'sustainability.html">Sustainability</a>'
    out += '<div class="grp-label">Products</div>'
    out += '<a class="sub" href="' + rel + 'products.html">All products</a>'
    out += '<a class="sub" href="' + rel + 'red-chilli.html">Red chilli — Guntur</a>'
    out += '<a class="sub" href="' + rel + 'coriander.html">Coriander — Rajasthan</a>'
    out += '<a class="sub" href="' + rel + 'turmeric.html">Turmeric — Sangli &amp; Salem</a>'
    out += '<a class="sub" href="' + rel + 'custom-blends.html">Custom blends &amp; private label</a>'
    out += '<div class="grp-label">Quality</div>'
    out += '<a class="sub" href="' + rel + 'quality.html">Quality &amp; traceability</a>'
    out += '<a class="sub" href="' + rel + 'harvest-calendar.html">Harvest calendar</a>'
    out += '<div class="grp-label">More</div>'
    out += '<a class="sub" href="' + rel + 'industries.html">Markets &amp; industries</a>'
    out += '<a class="sub" href="' + rel + 'contact.html">Contact</a>'
    out += '<a class="btn btn--primary" href="' + rel + 'contact.html">Request a quote</a>'
    out += '</nav>'
    return out


def lotstrip_track():
    """Marquee track for the home hero — duplicated for seamless scroll."""
    chips = [
        ('LOT', 'AC7-RC-2406'), ('ORIGIN', 'GUNTUR, AP'), ('SHU', '35,000'),
        ('ASTA', '160'), ('MOISTURE', '9.2%'), ('STATUS', 'LAB-VERIFIED ✓'),
        ('LOT', 'AC7-TM-2402'), ('ORIGIN', 'SALEM, TN'), ('CURCUMIN', '3.4%'),
        ('Pb-CHROMATE', 'NOT DETECTED'), ('LOT', 'AC7-CN-2403'),
        ('ORIGIN', 'RAMGANJ, RJ'), ('VOLATILE OIL', '0.42%'), ('PURITY', '99.7%'),
    ]
    one = ""
    for k, v in chips:
        one += '<span class="lotstrip"><i class="dot"></i>' + k + ' <b>' + v + '</b></span>'
    return one + one


def footer(rel=""):
    y = '<span data-year>2025</span>'
    return (
        '<footer class="footer"><div class="wrap">'
        '<div class="footer__top">'
        '<div class="footer__brand">'
        '<a class="brand" href="' + rel + 'index.html">'
        '<span class="brand__mark">7</span>'
        '<span><span class="brand__name">ACE<b>7</b> SPICES</span>'
        '<span class="brand__tag">Pure · Authentic · Fresh</span></span></a>'
        '<p class="footer__about">Single-origin Indian red chilli, coriander and turmeric — cold-press milled, batch lab-tested and fully traceable, for serious buyers across HORECA, the GCC, Europe and India.</p>'
        '<div class="footer__lot">SAMPLE LOT · <b>AC7-RC-2406</b> · LAB-VERIFIED</div>'
        '<div class="footer__social">'
        '<a href="#" aria-label="LinkedIn">' + ICONS["li"] + '</a>'
        '<a href="#" aria-label="Instagram">' + ICONS["ig"] + '</a>'
        '<a href="#" aria-label="Facebook">' + ICONS["fb"] + '</a>'
        '<a href="https://wa.me/917415032994" aria-label="WhatsApp">' + ICONS["wa"] + '</a>'
        '</div></div>'
        '<div><h5>Products</h5><div class="footer__links">'
        '<a href="' + rel + 'red-chilli.html">Red chilli</a>'
        '<a href="' + rel + 'coriander.html">Coriander</a>'
        '<a href="' + rel + 'turmeric.html">Turmeric</a>'
        '<a href="' + rel + 'custom-blends.html">Custom blends</a>'
        '<a href="' + rel + 'products.html">Full range</a>'
        '</div></div>'
        '<div><h5>Company</h5><div class="footer__links">'
        '<a href="' + rel + 'about.html">Our story</a>'
        '<a href="' + rel + 'process.html">Our process</a>'
        '<a href="' + rel + 'quality.html">Quality &amp; traceability</a>'
        '<a href="' + rel + 'sustainability.html">Sustainability</a>'
        '<a href="' + rel + 'harvest-calendar.html">Harvest calendar</a>'
        '</div></div>'
        '<div><h5>Trade</h5><div class="footer__links">'
        '<a href="' + rel + 'industries.html">Markets &amp; industries</a>'
        '<a href="' + rel + 'contact.html">Request a quote</a>'
        '<a href="tel:' + PHONE + '">' + PHONE_DISP + '</a>'
        '<a href="mailto:' + EMAIL + '">' + EMAIL + '</a>'
        '</div></div>'
        '</div>'
        '<div class="footer__bottom">'
        '<span class="footer__parent">© ' + y + ' Ace7 Spices™ — a brand of <b>Ace Adam International LLP</b></span>'
        '<div class="footer__legal">'
        '<a href="' + rel + 'privacy-policy.html">Privacy policy</a>'
        '<a href="' + rel + 'terms.html">Terms &amp; conditions</a>'
        '<a href="' + rel + 'contact.html">Enquiries</a>'
        '</div></div>'
        '</div></footer>'
        '<script src="' + rel + 'assets/script.js"></script>'
        '</body></html>'
    )
