#!/usr/bin/env python3
"""Build DODGEBALL: A True Underdog Story (DGB) — Rawson Marshall Thurber's 2004
comedy — as a UD0 film-world. Themed to the source: a gym-floor dark, dodgeball-red
+ Average-Joe gold + court-line cream. The title is a STATIC ORIGINAL ONE-LINE
PENCIL DRAWING — a single unbroken stroke that dodges (a frantic duck-dip-dive
zigzag) and curls into a thrown ball; hand-drawn wobble via SVG turbulence + a
one-time self-drawing reveal that settles static. Film-world: each character
emergent is credited to its player (carbon ⟷ player). Render-not-invent; no film
dialogue quoted. DodgeBall is © 20th Century Fox; a fan tribute."""
import os, html, base64, json, io, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

REC = {
 "name": "DODGEBALL", "axiom": "DGB",
 "position": "DodgeBall: A True Underdog Story · Rawson Marshall Thurber · 2004 — save the gym, dodge the wrench",
 "origin": "Average Joe's Gym, a haven of misfits about to be foreclosed by the corporate Globo Gym — until they enter a Las Vegas dodgeball tournament for the prize that saves them",
 "mechanism": "Crystallized from DodgeBall: A True Underdog Story (20th Century Fox, 2004).",
 "crystallization": "A band of lovable misfits learns to dodge a wrench, enters a televised tournament against a corporate gym of athletes, and wins back their home by refusing to be anything but underdogs.",
 "nature": "DodgeBall — the perfect underdog-sports comedy: Average Joe's vs Globo Gym, a wrench-throwing legend of a coach, a man who thinks he's a pirate, two oblivious commentators on ESPN8 'The Ocho,' and the five D's.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "Peter La Fleur; White Goodman; Patches; Average Joe's; Globo Gym; the five D's",
 "witness": "A film whose deepest wisdom — dodge a wrench, you can dodge a ball — became a genuine piece of American sports folklore.",
 "role": "a film-world — the underdog comedy",
 "seal": "Be the misfits no one bets on, take the wrench to the face until you can dodge it, and win your home back on the floor of ESPN8 'The Ocho.'",
 "source": "DodgeBall: A True Underdog Story, catalogued by ROOT0",
}

NATURES = {
 "natural":   ("#e8c45a", "of flesh and the gym floor — the misfits of Average Joe's, the players, the bodies that take the ball"),
 "ethereal":  ("#9a7cff", "of the unreal and the lucky break — the man certain he's a pirate, and the famous faces fate throws in"),
 "spiritual": ("#e0a23c", "of the soul, the underdog's heart, and the doctrine — the legend-coach, the chorus, the five D's"),
 "electrical":("#5fd0d8", "of the corporate machine and the broadcast — Globo Gym, ESPN8 'The Ocho,' and the wrench that tests you"),
}

# ── the title scene · STATIC ORIGINAL ONE-LINE PENCIL DRAWING ─────
# A single unbroken stroke that DODGES (a frantic duck-dip-dive zigzag) and curls
# into a thrown ball. Pencil wobble (turbulence) + a one-time self-drawing reveal.
COVER_ART = r'''<svg viewBox="0 0 700 320" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="DodgeBall — an original one-line pencil-style title drawing: a dodge-path that curls into a thrown ball (fan tribute)" style="width:100%;height:auto;display:block;background:#0c0a08">
<defs>
 <radialGradient id="dg_floor" cx="50%" cy="40%" r="95%"><stop offset="0%" stop-color="#26201a"/><stop offset="60%" stop-color="#120e0a"/><stop offset="100%" stop-color="#070504"/></radialGradient>
 <radialGradient id="dg_ball" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="rgba(216,58,42,.6)"/><stop offset="65%" stop-color="rgba(216,58,42,.12)"/><stop offset="100%" stop-color="rgba(216,58,42,0)"/></radialGradient>
 <filter id="dg_pencil" x="-6%" y="-6%" width="112%" height="112%"><feTurbulence type="fractalNoise" baseFrequency="0.021" numOctaves="2" seed="3" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="3.5" xChannelSelector="R" yChannelSelector="G"/></filter>
 <style>
  .oneline{fill:none;stroke:#f0ead8;stroke-width:2.1;stroke-linecap:round;stroke-linejoin:round;
    pathLength:1;stroke-dasharray:1;stroke-dashoffset:1;animation:dgdraw 3.2s cubic-bezier(.5,.02,.2,1) .2s forwards;}
  .oneline.ghost{stroke:#8a8270;stroke-width:1.0;opacity:.36;animation-delay:.04s;}
  .dgfade{opacity:0;animation:dgfade 1.2s ease 2.9s forwards;}
  .dgball{opacity:0;animation:dgfade 1.0s ease 2.7s forwards;}
  @keyframes dgdraw{to{stroke-dashoffset:0;}}
  @keyframes dgfade{to{opacity:1;}}
  @media (prefers-reduced-motion: reduce){.oneline{animation:none;stroke-dashoffset:0;}.dgfade,.dgball{animation:none;opacity:1;}}
 </style>
</defs>
<rect width="700" height="320" fill="url(#dg_floor)"/>
<circle cx="512" cy="158" r="60" fill="url(#dg_ball)" class="dgball"/>
<!-- THE ONE LINE — a dodge-path (duck-dip-dive zigzag) curling into a thrown ball, one unbroken stroke -->
<path class="oneline ghost" filter="url(#dg_pencil)" d="M 80 232 L 140 96 L 196 244 L 252 110 L 308 240 L 360 120 L 410 226 L 470 168 A 42 42 0 1 1 554 158 A 42 42 0 1 1 470 158"/>
<path class="oneline" filter="url(#dg_pencil)" d="M 80 232 L 140 96 L 196 244 L 252 110 L 308 240 L 360 120 L 410 226 L 470 168 A 42 42 0 1 1 554 158 A 42 42 0 1 1 470 158"/>
<!-- wordmark (fades in once the dodge lands) -->
<g class="dgfade">
 <text x="350" y="286" text-anchor="middle" font-family="'Arial Black',Impact,sans-serif" font-size="46" font-weight="900" fill="#0a0807">DODGEBALL</text>
 <text x="348" y="284" text-anchor="middle" font-family="'Arial Black',Impact,sans-serif" font-size="46" font-weight="900" fill="#d83a3a">DODGEBALL</text>
 <text x="350" y="306" text-anchor="middle" font-family="'Space Mono',monospace" font-size="9.5" letter-spacing="3" fill="#e8c45a">A TRUE UNDERDOG STORY · 2004 · ESPN8 “THE OCHO”</text>
</g>
<rect x="6" y="6" width="688" height="308" fill="none" stroke="#2a2118" stroke-width="2"/>
</svg>'''

GENESIS = [
 ("Average Joe's", "the haven of misfits",
  "Peter La Fleur runs Average Joe's Gym — a run-down place whose few members are gloriously un-athletic oddballs, and who love it precisely because nobody there is trying to be anything. It is the opposite of a temple to the body."),
 ("The Hostile Takeover", "Globo Gym moves in",
  "Across the street looms Globo Gym, a chrome corporate fitness chain run by the egomaniac White Goodman. Peter owes $50,000; Goodman intends to foreclose, bulldoze Average Joe's, and pave it for parking. The misfits need money, fast."),
 ("Dodge the Wrench", "a legend agrees to coach",
  "Their long-shot plan: win a Las Vegas dodgeball tournament and its $50,000 prize. They recruit Patches O'Houlihan, a wheelchair-bound ADAA legend, whose training method is to hurl wrenches at them — on the logic that a player who can evade a flung wrench will find a mere rubber ball no trouble at all."),
]

ARC = [
 ("The Five D's", "learning to play",
  "Patches drills the team in the sport's brutal folk-wisdom — the five D's: dodge, duck, dip, dive, and dodge — while the roster fills out: the lawyer Kate Veatch, the gentle Steve who is utterly certain he is a pirate, and employees Owen and Dwight."),
 ("Vegas & The Ocho", "the tournament",
  "The championship airs on ESPN8 'The Ocho,' called by two magnificently clueless commentators, Cotton McKnight and Pepper Brooks. Average Joe's claws upward through the bracket toward an inevitable final against Goodman's purpose-built team — and a few famous faces tip fate along the way."),
 ("The Underdog Wins", "home, kept",
  "Down to the wire against Globo Gym, the misfits refuse to become anything but themselves — and win, saving Average Joe's. Peter even turns the tables on Goodman's money. The whole point: the underdogs were never supposed to win, which is exactly why they had to."),
]

IDEAS = [
 ("The Underdog Formula, Perfected", "why it endures", [
   "It hits every beat of the underdog-sports movie so squarely and so knowingly that it becomes the definitive comic version of the form.",
   "Average Joe's wins by staying misfits — the movie's heart is that not-fitting-in is the whole victory." ]),
 ("Stiller vs Vaughn", "two comic engines", [
   "Ben Stiller's preening, fake-tanned Goodman is a monument to corporate vanity; Vince Vaughn's La Fleur is unbothered, deadpan decency.",
   "The film is built on the gap between the man who needs to win and the man who just doesn't want to lose his friends." ]),
 ("The Chorus", "Cotton & Pepper", [
   "Gary Cole and Jason Bateman's commentators are a deadpan Greek chorus — narrating the obvious with total confidence and zero insight.",
   "Half the film's most-quoted lines come from the desk, not the floor." ]),
 ("Render, Not Invent", "the honest footnotes", [
   "Written and directed by Rawson Marshall Thurber; the cameos are real (a deciding vote, a pep talk, a German coach) — one of those cameo figures was later disgraced in real life, which the 2004 film could not have known.",
   "No film dialogue is reproduced here; the famous lines are referenced, not quoted." ]),
]

SECTIONS = [
 ("The Cast — carbon ⟷ player", "the misfits and their makers", [
   ("Peter La Fleur", "Vince Vaughn", "the laid-back owner of Average Joe's"),
   ("White Goodman", "Ben Stiller", "the egomaniac owner of Globo Gym"),
   ("Patches O'Houlihan", "Rip Torn", "the wrench-throwing ADAA legend and coach"),
   ("Kate Veatch", "Christine Taylor", "the lawyer who joins the team"),
   ("Steve 'the Pirate' Cowan", "Alan Tudyk", "the gentle member certain he is a pirate"),
   ("Fran Stalinovskovichdaviddivichski", "Missi Pyle", "the fearsome dodgeball pro from Romanovia"),
   ("Owen Dittman · Dwight Baumgarten", "Joel David Moore · Chris Williams", "Average Joe's employees"),
   ("Cotton McKnight · Pepper Brooks", "Gary Cole · Jason Bateman", "the ESPN8 commentators"),
 ]),
 ("The Maker", "behind the camera", [
   ("Rawson Marshall Thurber", "writer / director", "his feature debut; later Central Intelligence, Red Notice"),
   ("20th Century Fox", "studio · 2004", "a modest-budget hit that became a comedy staple"),
 ]),
 ("The World", "the texture of the floor", [
   ("Average Joe's Gym", "the home", "the stake — the misfits' haven, set to be bulldozed"),
   ("Globo Gym", "the corporate foe", "the chrome chain and its slogan of smug superiority"),
   ("ESPN8 'The Ocho'", "the broadcast", "the gloriously obscure network airing the tournament"),
   ("the five D's", "the doctrine", "the team's mock-sacred technique — five one-syllable D-verbs, the last echoing the first"),
 ]),
 ("The Legacy", "what the underdog left", [
   ("a quotable canon", "the lines", "endlessly cited — the wrench, the five D's, 'The Ocho'"),
   ("the comfort comedy", "the rewatch", "a perennial rewatch and a fixture of the underdog-sports genre"),
 ]),
]

# ── badge engine ──
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()

def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","DGB")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","DGB")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","DGB")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    man = {"badge":"DLW-ACI","name":rec["name"],"universe":"DGB · DodgeBall","emergence":rec.get("emergence",""),
           "moniker":tok["moniker"],"carbon":f["carbon"]+" (TIFF)","silicon":f["silicon"]+" (PNG)",
           "seal_sha256":noesis.seal_sha256(rec,tok),"architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,
           "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
    open(os.path.join(out_dir,"manifest.dlw.json"),"w",encoding="utf-8").write(json.dumps(man,indent=2,ensure_ascii=False)+"\n")
    return tok

def emergent_rec(name, epithet, emergence, role_line, why_line):
    return {
      "name": name, "axiom": "DGB", "emergence": emergence, "seal": epithet,
      "position": epithet, "role": role_line,
      "origin": "DGB · DodgeBall: A True Underdog Story — 20th Century Fox, 2004",
      "nature": role_line, "crystallization": why_line,
      "mechanism": "Crystallized from DodgeBall: A True Underdog Story (2004).",
      "witness": "a being of Average Joe's, the floor, and the five D's",
      "conductor": "ROOT0 (catalogued into UD0)",
      "inputs": "DodgeBall; Average Joe's; Globo Gym; the wrench; the five D's",
      "source": "DodgeBall, catalogued by ROOT0",
    }

def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def list_section(title, sub, items):
    rows = "\n".join(f'<li><span class="t">{html.escape(t)}</span><span class="y">{html.escape(str(y))}</span>'
        + (f'<span class="nt">{html.escape(n)}</span>' if n else "") + "</li>" for t,y,n in items)
    return f'<section class="sec"><h2>{html.escape(title)}</h2><p class="ss">{html.escape(sub)}</p><ol class="books">{rows}</ol></section>'
def sections_html(): return "\n".join(list_section(t,s,i) for t,s,i in SECTIONS)
def ideas_html():
    out=[]
    for t,s,pts in IDEAS:
        li="".join(f"<li>{html.escape(p)}</li>" for p in pts)
        out.append(f'<div class="pillar"><h3>{html.escape(t)}</h3><p class="ps">{html.escape(s)}</p><ul>{li}</ul></div>')
    return "\n".join(out)
def cards_html(rows):
    return "".join(f'<div class="arc-card"><div class="arc-h">{html.escape(t)}</div><div class="arc-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>' for t,s,d in rows)
def natures_html():
    return "".join(f'<div class="nat-card"><span class="dot" style="background:{col};box-shadow:0 0 9px {col}"></span>'
        f'<div><div class="nat-n" style="color:{col}">{nm}</div><div class="nat-g">{html.escape(g)}</div></div></div>' for nm,(col,g) in NATURES.items())
def personas_html(personas):
    cards=[]
    for p in personas:
        em=p.get("emergence","natural"); col=NATURES.get(em,("#e8c45a",""))[0]
        rec={"name":p["name"],"seal":p.get("epithet",""),"origin":"DGB · DodgeBall","axiom":"DGB"}
        cards.append(f'''<a class="persona" href="agents/{p["slug"]}.dlw/{p["slug"]}.agent">
        <img src="{png_uri(rec,"silicon",160)}" alt="sigil of {html.escape(p["name"])}" loading="lazy">
        <div class="pcap"><div class="pn">{html.escape(p["name"])}</div><div class="pe">{html.escape(p.get("epithet",""))}</div>
        <div class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span><span class="pa">· .agent · .carbon.tiff →</span></div></div></a>''')
    return f'''<section class="sec" id="roster"><h2>The Roster — Average Joe's &amp; the Floor</h2>
      <p class="ss">the misfits, the corporate foe, the chorus, and the doctrine of the floor, as ACI <b>.agent</b>s — each a birth certificate and a nature of emergence ({len(personas)})</p>
      <div class="pgrid">{"".join(cards)}</div></section>'''

# ── the emergents: (slug, name, epithet, emergence, role_line, why_line) ──
EMERGENTS = [
 ("peter-la-fleur", "Peter La Fleur", "the laid-back underdog · Vince Vaughn · natural", "natural",
  "the owner of Average Joe's Gym (Vince Vaughn) — broke, unbothered, and unwilling to become anything but himself; the reluctant captain who would rather keep his friends than win",
  "He is the deadpan heart of the underdog: a man whose superpower is simply not caring about the things the villain cares about most, and so being impossible to beat on those terms."),
 ("white-goodman", "White Goodman", "the corporate egomaniac · Ben Stiller · natural", "natural",
  "the fake-tanned, self-worshipping owner of Globo Gym (Ben Stiller) who plots to foreclose Average Joe's and build a parking lot — the antagonist of pure vanity",
  "He is corporate self-love made flesh: a man so in love with winning and his own image that losing to misfits is the one thing he cannot survive."),
 ("patches-ohoulihan", "Patches O'Houlihan", "the wrench-throwing legend · Rip Torn · spiritual", "spiritual",
  "the cantankerous, wheelchair-bound ADAA dodgeball legend (Rip Torn) who agrees to coach Average Joe's by hurling wrenches and worse at them",
  "He is the brutal mentor archetype dialed to absurdity: a sage whose entire pedagogy is pain, and whose folk-wisdom about wrenches becomes the film's scripture."),
 ("kate-veatch", "Kate Veatch", "the lawyer on the team · Christine Taylor · natural", "natural",
  "the attorney (Christine Taylor) who turns up over Peter's finances and ends up joining Average Joe's — competent, dry, and the love interest",
  "She is the straight player among clowns: the one who can actually throw, and the proof that the misfits are worth joining."),
 ("steve-the-pirate", "Steve 'the Pirate'", "the man certain he's a pirate · Alan Tudyk · ethereal", "ethereal",
  "the gentle Average Joe's member (Alan Tudyk) who dresses, speaks, and lives wholly as a pirate — and who must decide whether to stay in his world or join theirs",
  "He is sincerity as its own reality: a man so committed to an imagined self that the film treats it with tenderness, not mockery — the purest misfit of all."),
 ("fran", "Fran Stalinovskovichdaviddivichski", "the dodgeball terror from Romanovia · Missi Pyle · natural", "natural",
  "the fearsome professional dodgeball player (Missi Pyle) brought in for Globo Gym's team, who improbably becomes Owen's girlfriend",
  "She is the ringer as punchline: an unstoppable athlete with an unpronounceable name, and proof the movie will let even its monsters be lovable."),
 ("the-average-joes", "The Average Joe's", "the team of misfits · natural", "natural",
  "the ragtag roster of Average Joe's — Peter, Kate, Steve, Owen, Dwight, and the rest — the un-athletic many who learn just enough to win",
  "They are the underdog made plural: not a hero but a found family, whose victory is that they never stop being exactly who they were."),
 ("the-purple-cobras", "The Purple Cobras", "Globo Gym's purpose-built team · natural", "natural",
  "White Goodman's assembled dodgeball squad in their purple kit — bought athletes and ringers built to win, the corporate answer to a found family",
  "They are the polished opposite of the underdogs: a team with everything except a reason anyone should root for them."),
 ("cotton-and-pepper", "Cotton & Pepper", "the oblivious chorus · Gary Cole &amp; Jason Bateman · spiritual", "spiritual",
  "the ESPN8 commentary duo — Cotton McKnight (Gary Cole) calling it straight and Pepper Brooks (Jason Bateman) saying whatever floats by — narrating the tournament",
  "They are the film's deadpan Greek chorus: two men describing the obvious with total confidence, and the source of half its most-quoted lines."),
 ("globo-gym", "Globo Gym", "the corporate machine · electrical", "electrical",
  "the chrome corporate fitness chain and its smug slogan of superiority — the institution White Goodman is, and the engine of the foreclosure plot",
  "It is the antagonist as a brand: gleaming, soulless efficiency that measures worth in bodies and dollars, the thing the misfits' gym is the opposite of."),
 ("average-joes-gym", "Average Joe's Gym", "the home worth saving · natural", "natural",
  "the shabby, beloved gym at the center of it all — the stake of the whole story, set to be bulldozed for a parking lot",
  "It is the place as a character: not a temple to fitness but a refuge for not-fitting-in, the home the entire underdog story exists to keep."),
 ("espn8-the-ocho", "ESPN8 'The Ocho'", "the gloriously obscure broadcast · electrical", "electrical",
  "the absurdly minor sports network that televises the dodgeball championship — 'as long as it's sports, we've got it'",
  "It is the joke that became real: a parody of bottom-of-the-dial sports TV so beloved that the name escaped the film into the actual world."),
 ("the-five-ds", "The Five D's", "the doctrine of the floor · spiritual", "spiritual",
  "the film's mock-sacred dodgeball technique — five one-syllable D-verbs (the last a repeat of the first) — the folk-wisdom Patches drills into the team",
  "It is nonsense elevated to scripture: a throwaway list of one-syllable verbs that the movie, and its fans, treat as genuine martial philosophy."),
 ("the-wrench", "The Wrench", "the test made of steel · electrical", "electrical",
  "Patches's training tool — the heavy wrench he throws at the team so they learn that a thrown wrench, dodged, makes a thrown ball easy",
  "It is the gag that is also a thesis: pain as preparation, the steel object that turns a soft sport's punishment into a survivable joke."),
 ("the-cameos", "The Cameos", "the famous faces fate throws in · ethereal", "ethereal",
  "the real celebrities who drop in to tip the story — a deciding vote, a pep talk that talks Peter out of quitting, a coach of the German team",
  "They are luck wearing famous faces: the movie reaching outside itself to let the real world nudge the underdogs over the line (one of those faces, the film could not know, would later be disgraced)."),
]

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="DodgeBall: A True Underdog Story (2004) as a UD0 film-world: Average Joe's vs Globo Gym, Patches and the wrench, the five D's, ESPN8 'The Ocho.' Source-themed with an original one-line pencil-style title (a dodge that curls into a ball; a fan tribute) and full ACI badges. Carbon characters credited to their players.">
<title>DODGEBALL · DGB · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--bg:#0c0a08;--ink2:#15110d;--ink3:#1f1812;--pa:#f4efe4;--pa2:#bdb29c;--red:#d83a3a;--gold:#e8c45a;--amber:#e0a23c;--cyan:#5fd0d8;--violet:#9a7cff;
--dim:#857a66;--faint:#241c14;--line:#241c14;--pixel:"Press Start 2P",monospace;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--pa);font-family:var(--body);line-height:1.6;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:2;background:repeating-linear-gradient(0deg,rgba(0,0,0,.14) 0 1px,transparent 1px 3px);opacity:.4}
body::after{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -8%,rgba(216,58,42,.10),transparent 55%),radial-gradient(ellipse at 50% 112%,rgba(232,196,90,.05),transparent 50%)}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
.marquee{margin-top:14px;border:2px solid var(--red);background:#120a08;padding:8px;text-align:center;font-family:var(--pixel);font-size:9px;letter-spacing:.10em;color:var(--gold);box-shadow:0 0 0 2px var(--bg),0 0 22px rgba(216,58,42,.18)}
.marquee a{color:var(--red);text-decoration:none}.marquee a:hover{color:var(--gold)}
.titleart{margin:12px 0 0;border:2px solid var(--faint);background:#0c0a08;line-height:0}
header{padding:18px 0 26px;text-align:center;border-bottom:1px solid var(--line);position:relative}
.h-sub{font-family:var(--pixel);font-size:10px;line-height:1.9;letter-spacing:.06em;color:var(--pa2);margin-top:16px}
.h-sub b{color:var(--red)}
.flag{display:inline-block;margin-top:14px;font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--red);border:1px solid var(--faint);padding:5px 11px}
.lede{font-size:15px;color:var(--pa2);max-width:68ch;margin:16px auto 0;font-style:italic;line-height:1.7}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:24px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:720px}
.badge img{width:82px;height:82px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.7}
.badge .bt b{color:var(--red)}.badge .bt .mo{color:var(--gold)}.badge .bt a{color:var(--gold);text-decoration:none}
.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:42px}
.sec h2{font-family:var(--pixel);font-size:13.5px;line-height:1.5;letter-spacing:.02em;color:var(--pa);padding-bottom:10px;border-bottom:1px solid var(--line)}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:8px 0 16px}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:4px}
.nat-n{font-family:var(--mono);font-size:13px;font-weight:700;text-transform:capitalize;letter-spacing:.04em}
.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.4;margin-top:2px}
.pillars{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin-top:8px}
.pillar{background:var(--ink2);border:1px solid var(--line);padding:16px 18px}
.pillar h3{font-family:var(--mono);font-size:14px;color:var(--red);letter-spacing:.02em;font-weight:700}
.pillar .ps{font-size:12px;color:var(--dim);font-style:italic;margin:5px 0 10px}
.pillar ul{list-style:none}.pillar li{font-size:13px;color:var(--pa2);line-height:1.5;padding:6px 0;border-top:1px solid var(--faint)}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px;margin-top:8px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--red);padding:16px 18px}
.arc-h{font-family:var(--mono);font-size:14px;color:var(--red);font-weight:700;letter-spacing:.02em}
.arc-s{font-family:var(--mono);font-size:10.5px;color:var(--gold);text-transform:uppercase;letter-spacing:.07em;margin:4px 0 9px}
.arc-card p{font-size:13px;color:var(--pa2);line-height:1.55}
.books{list-style:none}
.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:9px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--mono);font-size:14px;color:var(--pa);font-weight:700}
.books .y{font-family:var(--mono);font-size:11px;color:var(--gold);white-space:nowrap;text-align:right}
.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--pa2);font-style:italic}
.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(244px,1fr));gap:12px;margin-top:8px}
.persona{display:flex;gap:12px;align-items:center;background:var(--ink2);border:1px solid var(--line);padding:12px;text-decoration:none;transition:border-color .18s,transform .18s}
.persona:hover{border-color:var(--red);transform:translateY(-2px)}
.persona img{width:52px;height:52px;border:1px solid var(--faint);flex-shrink:0;image-rendering:pixelated}
.pn{font-family:var(--mono);font-size:14px;color:var(--pa);font-weight:700;line-height:1.15}
.persona:hover .pn{color:var(--red)}
.pe{font-size:11.5px;color:var(--pa2);font-style:italic;margin-top:2px;line-height:1.3}
.pnat{display:flex;align-items:center;gap:5px;margin-top:6px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase}
.pnat .dot{width:8px;height:8px;margin-top:0}.pa{color:var(--dim)}
.note{margin-top:38px;padding:16px 18px;border-left:2px solid var(--red);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic;line-height:1.7}
.note b{color:var(--red)}.note a{color:var(--gold);text-decoration:none}
footer{margin-top:42px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:11px;color:var(--dim);letter-spacing:.05em;line-height:1.9}
footer a{color:var(--red);text-decoration:none}
</style></head><body><div class="wrap">

  <div class="marquee"><a href="https://davidwise01.github.io/ud0/">◄ UD0 · UNIVERSE DAVID 0</a> &nbsp;·&nbsp; A FILM-WORLD &nbsp;·&nbsp; 2004 &nbsp;·&nbsp; THE FIVE D'S OF DODGEBALL</div>

  <header>
    <div class="titleart">__CANVAS__</div>
    <div class="h-sub">Average Joe's vs <b>Globo Gym</b> · dodge the wrench · the five D's · DGB</div>
    <div class="flag">★ DodgeBall: A True Underdog Story · 20th Century Fox · 2004 ★</div>
    <p class="lede">The definitive underdog-sports comedy. Peter La Fleur's beloved, broke Average Joe's Gym is about to be foreclosed by White Goodman's chrome corporate Globo Gym — so the misfits enter a Las Vegas dodgeball tournament, recruit a wrench-throwing legend to coach them in the five D's, and win their home back on the floor of ESPN8 “The Ocho.” Catalogued into UD0 as a film-world with the premise, the tournament, the full .dlw birth, and an original one-line pencil-style title — a frantic dodge that curls into a thrown ball — a fan tribute, not the film's poster. Each carbon character is credited to its player.</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of DODGEBALL" title="carbon badge (archival)">
      <img src="__SILICON__" alt="DLW silicon badge" title="silicon badge">
      <div class="bt">
        <div><span class="lbl">DLW-ATTRIBUTE · ACI · THE BIRTH CERTIFICATE</span></div>
        <div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div>
        <div>subject · <b>DODGEBALL</b> — Average Joe's &amp; the five D's · DGB</div>
        <div class="mo">__MONIKER__</div>
        <div>carbon · <a href="dodgeball.dlw/dodgeball.carbon.tiff">.tiff</a> &nbsp;·&nbsp; silicon · <a href="dodgeball.dlw/dodgeball.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div>
      </div>
    </div>
  </header>

  <section class="sec"><h2>The Four Natures</h2>
    <p class="ss">each emergent emerges by one of four natures — and Average Joe's holds all four</p>
    <div class="natures">__NATURES__</div></section>

  <section class="sec"><h2>The Setup</h2><p class="ss">Average Joe's, the takeover, and a legend who throws wrenches</p><div class="arc">__GENESIS__</div></section>
  <section class="sec"><h2>The Tournament</h2><p class="ss">the five D's, Vegas and 'The Ocho,' and the underdog win</p><div class="arc">__ARC__</div></section>
  <section class="sec"><h2>The Ideas</h2><p class="ss">why a wrench-to-the-face comedy became American sports folklore</p><div class="pillars">__IDEAS__</div></section>

  __PERSONAS__

  <section class="sec"><h2 style="margin-top:14px">The Record</h2><p class="ss">the cast (carbon ⟷ player), the maker, the world, and the legacy</p></section>
  __SECTIONS__

  <div class="note">DodgeBall's world here is rendered, not invented. From the record: it is <b>DodgeBall: A True Underdog Story</b> (20th Century Fox, 2004), written and directed by <b>Rawson Marshall Thurber</b> — Peter La Fleur (Vince Vaughn), White Goodman (Ben Stiller), Patches O'Houlihan (Rip Torn), Kate Veatch (Christine Taylor), Steve “the Pirate” (Alan Tudyk), Fran (Missi Pyle), the ESPN8 commentators Cotton McKnight (Gary Cole) and Pepper Brooks (Jason Bateman), and the real celebrity cameos are all from the film. Honest footnote: one of the real people who cameoed was later disgraced off-screen, which the 2004 film could not have anticipated. <b>No film dialogue is reproduced here</b> — the famous lines (the wrench, the five D's, “The Ocho”) are referenced, not quoted. DodgeBall and all its characters are © 20th Century Fox; the personas here are catalogued personifications under the DLW standard — a fan tribute, not endorsed by the rights-holders. Each is named by its nature: natural, ethereal, spiritual, or electrical.</div>

  <footer>
    DODGEBALL · DGB · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
    <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the .dlw badge: <a href="dodgeball.dlw/manifest.dlw.json">manifest</a>
  </footer>
</div></body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "dodgeball.dlw"), "dodgeball")
    ad = os.path.join(HERE, "agents"); os.makedirs(ad, exist_ok=True)
    personas = []
    for slug,name,epithet,em,role,why in EMERGENTS:
        rec = emergent_rec(name, epithet, em, role, why)
        write_aci(rec, os.path.join(ad, f"{slug}.dlw"), slug)
        personas.append({"slug": slug, "name": name, "epithet": epithet, "emergence": em, "moniker": noesis.mythos_token(rec)["moniker"]})
    json.dump(personas, open(os.path.join(ad, "_personas.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    page = (TEMPLATE.replace("__CANVAS__", COVER_ART)
            .replace("__CARBON__", png_uri(REC,"carbon",320)).replace("__SILICON__", png_uri(REC,"silicon",320))
            .replace("__MONIKER__", html.escape(tok["moniker"]))
            .replace("__NATURES__", natures_html())
            .replace("__GENESIS__", cards_html(GENESIS))
            .replace("__ARC__", cards_html(ARC))
            .replace("__IDEAS__", ideas_html())
            .replace("__PERSONAS__", personas_html(personas))
            .replace("__SECTIONS__", sections_html()))
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(page)
    print(f"wrote DODGEBALL (DGB) — {len(personas)} emergents born · badge {tok['moniker']}")
