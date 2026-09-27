import json

with open('b64_images.json', 'r') as f:
    b64 = json.load(f)

html_content = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Unity Ekeoba — Full Stack Developer, Blockchain Engineer &amp; Founder</title>
<meta name="description" content="Personal portfolio of Unity Ekeoba — Nigeria-based Full Stack Developer, Blockchain Engineer and Founder of ReplyIQ &amp; CabVibe. Turning ideas into scalable products.">

<!-- Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Mrs+Saint+Delafield&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Unbounded:wght@700;800&display=swap" rel="stylesheet">

<style>
/* ==========================================================================
   DESIGN TOKENS & RESET (STRICT: NO GRADIENTS ANYWHERE, ONLY PURPLE & PINK)
   ========================================================================== */
:root {{
  --purple: #1c0b2e;
  --pink: #ffd3e6;
  --white: #ffffff;
  --status-dot: #7cc576;
  --whatsapp: #25d366;
  
  --font-display: "Unbounded", system-ui, sans-serif;
  --font-body: "Plus Jakarta Sans", system-ui, sans-serif;
  --font-sig: "Mrs Saint Delafield", cursive;
  
  --ease-main: cubic-bezier(0.2, 0.8, 0.2, 1);
  --ease-flip: cubic-bezier(0.65, 0, 0.25, 1);
  
  --gutter: clamp(24px, 6vw, 96px);
  --section-pad: clamp(96px, 11vw, 170px);
}}

*, *::before, *::after {{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}}

html {{
  scroll-behavior: smooth;
  background-color: var(--purple);
  color: var(--pink);
  font-family: var(--font-body);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  overflow-x: hidden;
}}

body {{
  background-color: var(--purple);
  color: var(--pink);
  font-family: var(--font-body);
  overflow-x: hidden;
  position: relative;
  width: 100%;
}}

img {{
  max-width: 100%;
  display: block;
}}

a {{
  color: inherit;
  text-decoration: none;
}}

button {{
  font-family: inherit;
  cursor: pointer;
  border: none;
  background: none;
}}

:focus-visible {{
  outline: 2px solid var(--pink);
  outline-offset: 4px;
}}

/* ==========================================================================
   GLOBAL HEADER (FLOATING PILL NAV)
   ========================================================================== */
.header-wrap {{
  position: fixed;
  top: 24px;
  left: 0;
  right: 0;
  display: flex;
  justify-content: center;
  z-index: 100;
  pointer-events: none;
  transition: transform 0.6s var(--ease-main), opacity 0.6s var(--ease-main);
}}

.header-wrap.hidden {{
  transform: translateY(-100px);
  opacity: 0;
}}

.nav-pill {{
  pointer-events: auto;
  display: flex;
  align-items: center;
  gap: clamp(14px, 3vw, 28px);
  padding: 8px 10px 8px 20px;
  background-color: rgba(28, 11, 46, 0.38);
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
  border: 1px solid rgba(255, 255, 255, 0.28);
  border-radius: 999px;
  color: var(--white);
  box-shadow: 0 16px 32px rgba(0, 0, 0, 0.3);
}}

.nav-logo {{
  font-family: var(--font-display);
  font-weight: 800;
  font-size: 15px;
  letter-spacing: -0.03em;
  color: var(--white);
  display: inline-flex;
  align-items: center;
  gap: 4px;
}}

.nav-logo svg {{
  width: 13px;
  height: 13px;
  fill: var(--pink);
}}

.nav-links {{
  display: flex;
  align-items: center;
  gap: 20px;
  font-size: 14px;
  font-weight: 500;
}}

.nav-link {{
  color: rgba(255, 255, 255, 0.8);
  transition: color 0.2s ease;
}}

.nav-link:hover {{
  color: var(--white);
}}

.nav-cta {{
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background-color: var(--white);
  color: var(--purple);
  padding: 8px 16px;
  border-radius: 999px;
  font-size: 13px;
  font-weight: 600;
  transition: transform 0.2s var(--ease-main), background-color 0.2s ease;
}}

.nav-cta:hover {{
  transform: scale(1.04);
  background-color: var(--pink);
}}

.status-dot {{
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background-color: var(--status-dot);
  box-shadow: 0 0 0 3px rgba(124, 197, 118, 0.35);
}}

@media (max-width: 600px) {{
  .nav-links {{
    display: none;
  }}
  .nav-pill {{
    padding: 6px 8px 6px 16px;
    gap: 14px;
  }}
}}

/* ==========================================================================
   FLOATING WHATSAPP BUTTON
   ========================================================================== */
.whatsapp-btn {{
  position: fixed;
  right: clamp(20px, 4vw, 36px);
  bottom: clamp(20px, 4vw, 36px);
  width: 58px;
  height: 58px;
  border-radius: 50%;
  background-color: var(--whatsapp);
  color: var(--white);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 10px 24px rgba(37, 211, 102, 0.4);
  z-index: 99;
  transition: transform 0.5s cubic-bezier(0.34, 1.56, 0.64, 1), opacity 0.4s ease;
}}

.whatsapp-btn.hidden {{
  transform: scale(0) rotate(-45deg);
  opacity: 0;
  pointer-events: none;
}}

.whatsapp-btn:hover {{
  transform: scale(1.1) rotate(6deg);
}}

.whatsapp-btn svg {{
  width: 30px;
  height: 30px;
  fill: currentColor;
}}

/* ==========================================================================
   SECTION BASE STYLES & ALTERNATING THEME
   ========================================================================== */
section {{
  position: relative;
  width: 100%;
}}

.theme-purple {{
  background-color: var(--purple);
  color: var(--pink);
}}

.theme-pink {{
  background-color: var(--pink);
  color: var(--purple);
}}

.container {{
  max-width: 1320px;
  margin: 0 auto;
  padding-left: var(--gutter);
  padding-right: var(--gutter);
}}

/* Split text word mask reveal */
.split-word {{
  display: inline-block;
  overflow: hidden;
  vertical-align: top;
}}

.split-word i {{
  display: inline-block;
  font-style: normal;
  transform: translateY(115%);
  transition: transform 0.85s var(--ease-main);
}}

.revealed .split-word i,
.split-word.active i {{
  transform: translateY(0);
}}

/* Animation reveal system */
[data-anim] {{
  opacity: 0;
  transition: opacity 0.85s var(--ease-main), transform 0.85s var(--ease-main);
}}

[data-anim="up"] {{
  transform: translateY(50px);
}}

[data-anim="left"] {{
  transform: translateX(-80px) rotate(-3deg);
}}

[data-anim="right"] {{
  transform: translateX(80px) rotate(3deg);
}}

[data-anim="scale"] {{
  transform: scale(0.8) rotate(-4deg);
}}

[data-anim].revealed {{
  opacity: 1;
  transform: translate(0, 0) rotate(0deg) scale(1);
}}

/* ==========================================================================
   1. INTRO (ID CARD HERO) — PURPLE
   ========================================================================== */
.section-intro {{
  height: 100svh;
  min-height: 640px;
  position: relative;
  overflow: hidden;
  background-color: var(--purple);
  --cw: min(66vw, 360px);
  --ch: calc(var(--cw) * 1.41);
}}

.intro-words {{
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 0 clamp(16px, 4vw, 48px);
  font-family: var(--font-display);
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: -0.03em;
  white-space: nowrap;
  line-height: 0.88;
  font-size: min(12.5vw, 13svh, 175px);
  color: var(--pink);
  z-index: 1;
  user-select: none;
  pointer-events: none;
  --gap: calc(var(--ch) * 0.98);
}}

.intro-words span {{
  display: block;
  overflow: hidden;
}}

.intro-words span i {{
  display: block;
  font-style: normal;
  transform: translateY(105%);
  transition: transform 0.9s var(--ease-main);
}}

.intro-words span:nth-child(even) {{
  text-align: right;
}}

.intro-words span:nth-child(3) {{
  margin-top: var(--gap);
}}

@media (min-width: 768px) {{
  .intro-words {{
    font-size: min(11vw, 13svh, 170px);
    --gap: calc(var(--ch) * 0.65);
  }}
}}

/* Rig & ID Card Hanging System */
.id-rig {{
  position: absolute;
  top: 0;
  left: 50%;
  width: var(--cw);
  margin-left: calc(var(--cw) / -2);
  z-index: 2;
  transform: translateY(-120vh);
  transform-origin: 50% 0;
}}

.id-rig.dropped {{
  animation: dropSway 2.4s var(--ease-main) forwards;
}}

@keyframes dropSway {{
  0% {{
    transform: translateY(-120vh) rotate(0deg);
  }}
  48% {{
    transform: translateY(8px) rotate(3.5deg);
  }}
  64% {{
    transform: translateY(-5px) rotate(-2deg);
  }}
  80% {{
    transform: translateY(2px) rotate(1deg);
  }}
  100% {{
    transform: translateY(0) rotate(0deg);
  }}
}}

.id-strap {{
  width: 32px;
  margin: 0 auto;
  height: calc((100svh - var(--ch)) / 2 + 8px);
  min-height: 48px;
  background-color: var(--pink);
  border-left: 2px dashed rgba(28, 11, 46, 0.25);
  border-right: 2px dashed rgba(28, 11, 46, 0.25);
  position: relative;
}}

.id-clip {{
  display: block;
  width: 48px;
  height: 44px;
  margin: -6px auto -24px;
  position: relative;
  z-index: 3;
}}

.card-stage {{
  perspective: 1400px;
}}

.id-card {{
  position: relative;
  width: var(--cw);
  height: var(--ch);
  transform-style: preserve-3d;
  cursor: pointer;
  transition: transform 0.95s var(--ease-flip);
}}

/* Badge holder (transparent plastic cover with top slot) */
.card-face {{
  position: absolute;
  inset: 0;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  border-radius: calc(var(--cw) * 0.07);
  background-color: rgba(255, 255, 255, 0.25);
  border: 1.5px solid rgba(255, 255, 255, 0.9);
  box-shadow: 0 32px 64px -16px rgba(0, 0, 0, 0.5);
  padding: calc(var(--cw) * 0.13) calc(var(--cw) * 0.035) calc(var(--cw) * 0.035);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
}}

/* Top oval slot in the clear plastic badge holder */
.card-face::before {{
  content: "";
  position: absolute;
  top: calc(var(--cw) * 0.04);
  left: 50%;
  width: 32%;
  height: calc(var(--cw) * 0.05);
  transform: translateX(-50%);
  border-radius: 999px;
  border: 1.5px solid rgba(255, 255, 255, 0.95);
  background-color: rgba(0, 0, 0, 0.08);
}}

.card-face.back {{
  transform: rotateY(180deg);
}}

/* Inside printed card */
.card-inner {{
  height: 100%;
  border-radius: calc(var(--cw) * 0.05);
  overflow: hidden;
  position: relative;
  color: var(--purple);
}}

/* FRONT OF CARD */
.front-inner {{
  background-color: var(--pink);
  display: flex;
  flex-direction: column;
  padding: calc(var(--cw) * 0.03);
}}

.card-photo-box {{
  height: 56%;
  width: 100%;
  border-radius: calc(var(--cw) * 0.035);
  overflow: hidden;
  position: relative;
  background-color: var(--purple);
}}

.card-photo-box img {{
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center 15%;
}}

.card-photo-overlay {{
  position: absolute;
  inset: 0;
  padding: calc(var(--cw) * 0.03);
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  pointer-events: none;
}}

.card-tag-pill {{
  background-color: var(--purple);
  color: var(--pink);
  font-size: calc(var(--cw) * 0.026);
  font-weight: 700;
  letter-spacing: 0.04em;
  padding: 3px 6px;
  border-radius: 4px;
}}

.card-globe-pill {{
  background-color: rgba(28, 11, 46, 0.85);
  color: var(--white);
  font-size: calc(var(--cw) * 0.024);
  font-weight: 600;
  padding: 3px 6px;
  border-radius: 4px;
  display: flex;
  align-items: center;
  gap: 3px;
}}

.card-info {{
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding-top: calc(var(--cw) * 0.03);
}}

.card-name-title {{
  display: flex;
  flex-direction: column;
  gap: 2px;
}}

.card-name {{
  font-family: var(--font-display);
  font-weight: 800;
  font-size: calc(var(--cw) * 0.088);
  letter-spacing: -0.03em;
  line-height: 1;
  color: var(--purple);
}}

.card-role {{
  font-size: calc(var(--cw) * 0.033);
  font-weight: 600;
  color: rgba(28, 11, 46, 0.78);
  margin-top: 2px;
}}

.card-pill-row {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: calc(var(--cw) * 0.015);
}}

.freelance-pill {{
  display: inline-flex;
  align-items: center;
  gap: 5px;
  background-color: var(--purple);
  color: var(--white);
  padding: 3px 8px;
  border-radius: 999px;
  font-size: calc(var(--cw) * 0.026);
  font-weight: 600;
}}

.freelance-pill .dot {{
  width: 5px;
  height: 5px;
  background-color: var(--status-dot);
  border-radius: 50%;
}}

.card-sig-box {{
  display: flex;
  align-items: center;
  gap: 2px;
}}

.card-sig {{
  font-family: var(--font-sig);
  font-size: calc(var(--cw) * 0.095);
  line-height: 0.8;
  color: var(--purple);
}}

.card-bottom-row {{
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  margin-top: calc(var(--cw) * 0.02);
  border-top: 1px solid rgba(28, 11, 46, 0.15);
  padding-top: calc(var(--cw) * 0.015);
}}

.card-barcode {{
  height: calc(var(--cw) * 0.065);
  opacity: 0.85;
}}

.card-id-num {{
  font-family: var(--font-display);
  font-size: calc(var(--cw) * 0.028);
  font-weight: 700;
  color: rgba(28, 11, 46, 0.6);
}}

/* BACK OF CARD */
.back-inner {{
  background-color: #f7ecf2;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: calc(var(--cw) * 0.06);
}}

.back-head {{
  font-family: var(--font-display);
  font-weight: 800;
  font-size: calc(var(--cw) * 0.065);
  letter-spacing: -0.02em;
  color: var(--purple);
  border-bottom: 2px solid var(--purple);
  padding-bottom: calc(var(--cw) * 0.02);
}}

.back-rows {{
  display: flex;
  flex-direction: column;
  gap: calc(var(--cw) * 0.035);
  margin-top: calc(var(--cw) * 0.02);
}}

.back-row-title {{
  font-family: var(--font-display);
  font-weight: 700;
  font-size: calc(var(--cw) * 0.038);
  color: var(--purple);
}}

.back-row-desc {{
  font-size: calc(var(--cw) * 0.031);
  color: rgba(28, 11, 46, 0.75);
  line-height: 1.3;
}}

.back-quote {{
  font-family: var(--font-sig);
  font-size: calc(var(--cw) * 0.062);
  line-height: 1.2;
  color: var(--purple);
  margin-top: calc(var(--cw) * 0.02);
  text-align: center;
}}

.back-foot {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-top: 1px solid rgba(28, 11, 46, 0.15);
  padding-top: calc(var(--cw) * 0.02);
}}

.back-handle {{
  font-family: var(--font-display);
  font-weight: 800;
  font-size: calc(var(--cw) * 0.032);
  color: var(--purple);
}}

/* Intro Footer Line */
.intro-foot {{
  position: absolute;
  left: 0;
  right: 0;
  bottom: clamp(16px, 3vh, 32px);
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  padding: 0 var(--gutter);
  font-size: 14px;
  color: var(--pink);
  z-index: 3;
  pointer-events: none;
}}

.typing-lead {{
  font-weight: 500;
  letter-spacing: -0.01em;
  display: flex;
  align-items: center;
  gap: 8px;
}}

.typing-lead .caret {{
  width: 2px;
  height: 16px;
  background-color: var(--pink);
  animation: blink 0.8s infinite;
}}

@keyframes blink {{
  0%, 100% {{ opacity: 1; }}
  50% {{ opacity: 0; }}
}}

.scroll-cue {{
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 13px;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  font-weight: 600;
}}

.scroll-line {{
  width: 1.5px;
  height: 28px;
  background-color: var(--pink);
  transform-origin: top;
  animation: scrollPulse 1.8s ease-in-out infinite;
}}

@keyframes scrollPulse {{
  0% {{ transform: scaleY(0); transform-origin: top; }}
  50% {{ transform: scaleY(1); transform-origin: top; }}
  50.1% {{ transform-origin: bottom; }}
  100% {{ transform: scaleY(0); transform-origin: bottom; }}
}}

/* ==========================================================================
   2. ABOUT (PHOTO COLLAGE) — PINK
   ========================================================================== */
.section-about {{
  padding-top: var(--section-pad);
  padding-bottom: var(--section-pad);
  background-color: var(--pink);
  color: var(--purple);
}}

.about-grid {{
  display: grid;
  grid-template-columns: 1fr;
  gap: clamp(48px, 8vw, 84px);
  align-items: center;
}}

@media (min-width: 900px) {{
  .about-grid {{
    grid-template-columns: 1.05fr 1.15fr;
  }}
}}

.collage-wrap {{
  position: relative;
  width: 100%;
  max-width: 480px;
  margin: 0 auto;
}}

.collage-main {{
  width: 82%;
  border-radius: 18px;
  border: 6px solid var(--purple);
  box-shadow: 12px 12px 0px var(--purple);
  transform: rotate(-2deg);
  overflow: hidden;
  background-color: var(--purple);
}}

.collage-main img {{
  width: 100%;
  height: auto;
  display: block;
}}

.collage-secondary {{
  position: absolute;
  right: 0;
  bottom: -24px;
  width: 58%;
  border-radius: 14px;
  border: 6px solid var(--purple);
  box-shadow: 10px 10px 0px var(--purple);
  transform: rotate(4deg);
  overflow: hidden;
  background-color: var(--purple);
  z-index: 2;
}}

.collage-secondary img {{
  width: 100%;
  height: auto;
  display: block;
}}

.collage-note {{
  position: absolute;
  left: -12px;
  bottom: 24px;
  background-color: var(--purple);
  color: var(--pink);
  padding: 8px 18px;
  border-radius: 999px;
  font-family: var(--font-sig);
  font-size: 32px;
  line-height: 0.9;
  z-index: 3;
  transform: rotate(-7deg);
  box-shadow: 4px 4px 0px rgba(0, 0, 0, 0.2);
}}

.about-content {{
  display: flex;
  flex-direction: column;
  gap: 24px;
}}

.about-heading {{
  font-family: var(--font-display);
  font-weight: 800;
  font-size: clamp(32px, 4.5vw, 54px);
  letter-spacing: -0.03em;
  line-height: 1.1;
  color: var(--purple);
  min-height: 2.2em;
}}

.about-heading .typed-text {{
  color: var(--purple);
}}

.about-heading .type-caret {{
  display: inline-block;
  width: 3px;
  height: 0.85em;
  background-color: var(--purple);
  margin-left: 4px;
  animation: blink 0.8s infinite;
  vertical-align: baseline;
}}

.about-copy {{
  font-size: clamp(16px, 1.8vw, 19px);
  line-height: 1.65;
  color: rgba(28, 11, 46, 0.88);
  font-weight: 500;
  max-width: 560px;
}}

/* ==========================================================================
   3. SERVICES (WHAT I DO) — PURPLE
   ========================================================================== */
.section-services {{
  padding-top: var(--section-pad);
  padding-bottom: var(--section-pad);
  background-color: var(--purple);
  color: var(--pink);
}}

.services-list {{
  display: flex;
  flex-direction: column;
  margin-top: 48px;
}}

.service-row {{
  display: grid;
  grid-template-columns: auto 1fr;
  align-items: center;
  gap: clamp(16px, 4vw, 36px);
  padding: clamp(28px, 4vw, 44px) 0;
  border-top: 1px solid rgba(255, 211, 230, 0.18);
  transition: transform 0.3s var(--ease-main), padding-left 0.3s var(--ease-main);
}}

.service-row:last-child {{
  border-bottom: 1px solid rgba(255, 211, 230, 0.18);
}}

.service-icon {{
  width: clamp(52px, 6vw, 68px);
  height: clamp(52px, 6vw, 68px);
  border-radius: 18px;
  background-color: var(--pink);
  color: var(--purple);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform 0.4s var(--ease-main);
}}

.service-icon svg {{
  width: 50%;
  height: 50%;
  fill: currentColor;
}}

.service-body {{
  display: flex;
  flex-direction: column;
  gap: 6px;
}}

@media (min-width: 768px) {{
  .service-body {{
    flex-direction: row;
    align-items: baseline;
    justify-content: space-between;
  }}
}}

.service-title {{
  font-family: var(--font-display);
  font-weight: 800;
  font-size: clamp(28px, 4vw, 44px);
  letter-spacing: -0.03em;
  color: var(--pink);
  transition: transform 0.3s var(--ease-main);
}}

.service-desc {{
  font-size: clamp(15px, 1.6vw, 18px);
  color: rgba(255, 255, 255, 0.85);
  font-weight: 500;
}}

.service-row:hover .service-icon {{
  transform: scale(1.12) rotate(-12deg);
}}

.service-row:hover .service-title {{
  transform: translateX(12px);
}}

/* ==========================================================================
   4. STATS (NUMBERS) — PINK
   ========================================================================== */
.section-stats {{
  padding-top: var(--section-pad);
  padding-bottom: var(--section-pad);
  background-color: var(--pink);
  color: var(--purple);
}}

.stats-grid {{
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: clamp(32px, 5vw, 64px);
}}

@media (min-width: 900px) {{
  .stats-grid {{
    grid-template-columns: repeat(4, 1fr);
  }}
}}

.stat-item {{
  display: flex;
  flex-direction: column;
  gap: 8px;
}}

.stat-number {{
  font-family: var(--font-display);
  font-weight: 800;
  font-size: clamp(48px, 6vw, 76px);
  letter-spacing: -0.03em;
  line-height: 1;
  color: var(--purple);
  display: flex;
  align-items: baseline;
}}

.stat-suffix {{
  color: var(--purple);
}}

.stat-label {{
  font-size: 15px;
  font-weight: 600;
  color: rgba(28, 11, 46, 0.78);
  line-height: 1.4;
}}

/* ==========================================================================
   5. TOOL STRIP MARQUEE — PURPLE
   ========================================================================== */
.section-marquee {{
  background-color: var(--purple);
  padding: clamp(20px, 3vh, 32px) 0;
  overflow: hidden;
  border-top: 1px solid rgba(255, 211, 230, 0.12);
  border-bottom: 1px solid rgba(255, 211, 230, 0.12);
}}

.marquee-track {{
  display: flex;
  width: fit-content;
  white-space: nowrap;
  animation: scrollMarquee 30s linear infinite;
}}

.marquee-content {{
  display: flex;
  align-items: center;
  font-size: clamp(16px, 2vw, 22px);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: var(--pink);
}}

.marquee-item {{
  display: inline-flex;
  align-items: center;
}}

.marquee-star {{
  color: var(--pink);
  margin: 0 clamp(16px, 3vw, 28px);
  font-size: 0.85em;
}}

@keyframes scrollMarquee {{
  0% {{
    transform: translateX(0);
  }}
  100% {{
    transform: translateX(-50%);
  }}
}}

/* ==========================================================================
   6. SELECTED WORK — PINK
   ========================================================================== */
.section-work-container {{
  position: relative;
  background-color: var(--pink);
  color: var(--purple);
  height: 400vh; /* scroll distance to drive horizontal carousel */
}}

.work-sticky {{
  position: sticky;
  top: 0;
  height: 100svh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  overflow: hidden;
  padding: 32px 0 24px;
}}

.work-header {{
  text-align: center;
  margin-bottom: clamp(32px, 5vh, 48px);
  padding: 0 var(--gutter);
}}

.work-title {{
  font-family: var(--font-display);
  font-weight: 800;
  font-size: clamp(34px, 5vw, 60px);
  letter-spacing: -0.03em;
  color: var(--purple);
  line-height: 1.1;
}}

.work-subtitle {{
  margin-top: 10px;
  font-size: clamp(15px, 1.7vw, 18px);
  font-weight: 500;
  color: rgba(28, 11, 46, 0.75);
}}

.work-carousel-wrap {{
  position: relative;
  width: 100%;
  overflow: hidden;
}}

.work-track {{
  display: flex;
  gap: clamp(24px, 4vw, 44px);
  padding-left: clamp(24px, 12vw, 160px);
  padding-right: clamp(24px, 12vw, 160px);
  width: max-content;
  will-change: transform;
}}

.project-card {{
  width: clamp(280px, 42vw, 560px);
  flex-shrink: 0;
  background-color: var(--white);
  border-radius: 22px;
  overflow: hidden;
  box-shadow: 0 24px 48px -12px rgba(28, 11, 46, 0.18);
  transition: transform 0.25s ease-out;
  transform-origin: center center;
}}

.project-img-box {{
  width: 100%;
  height: min(44svh, 420px);
  overflow: hidden;
  background-color: #ede2e8;
  position: relative;
}}

.project-img-box img {{
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: top center;
  display: block;
}}

.project-caption {{
  padding: 16px 22px 20px;
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 12px;
  background-color: var(--white);
}}

.project-name {{
  font-size: 16px;
  font-weight: 600;
  color: var(--purple);
}}

.project-category {{
  font-size: 13px;
  font-weight: 500;
  color: rgba(28, 11, 46, 0.6);
}}

.work-progress-bar-wrap {{
  max-width: 480px;
  width: calc(100% - (var(--gutter) * 2));
  height: 4px;
  background-color: rgba(28, 11, 46, 0.15);
  border-radius: 999px;
  margin: clamp(24px, 4vh, 36px) auto 0;
  overflow: hidden;
}}

.work-progress-fill {{
  height: 100%;
  width: 0%;
  background-color: var(--purple);
  border-radius: 999px;
  transition: width 0.1s linear;
}}

/* ==========================================================================
   7. ABOUT ME — PURPLE
   ========================================================================== */
.section-aboutme {{
  padding-top: var(--section-pad);
  padding-bottom: var(--section-pad);
  background-color: var(--purple);
  color: var(--pink);
}}

.aboutme-grid {{
  display: grid;
  grid-template-columns: 1fr;
  gap: clamp(40px, 7vw, 80px);
  align-items: center;
}}

@media (min-width: 900px) {{
  .aboutme-grid {{
    grid-template-columns: 1fr 1.25fr;
  }}
}}

.aboutme-pic-frame {{
  border-radius: 24px;
  overflow: hidden;
  background-color: var(--purple);
  border: 1px solid rgba(255, 211, 230, 0.2);
  box-shadow: 0 28px 56px -16px rgba(0, 0, 0, 0.6);
  position: relative;
}}

.aboutme-pic-frame .pic-inner {{
  overflow: hidden;
  clip-path: inset(12%);
  transition: clip-path 1.2s var(--ease-main);
}}

.aboutme-pic-frame .pic-inner img {{
  width: 100%;
  height: auto;
  transform: scale(1.15);
  transition: transform 1.2s var(--ease-main);
}}

.aboutme-pic-frame.revealed .pic-inner {{
  clip-path: inset(0%);
}}

.aboutme-pic-frame.revealed .pic-inner img {{
  transform: scale(1);
}}

.aboutme-details {{
  display: flex;
  flex-direction: column;
  gap: 20px;
}}

.badge-pill {{
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background-color: var(--pink);
  color: var(--purple);
  padding: 6px 16px;
  border-radius: 999px;
  font-size: 13px;
  font-weight: 700;
  width: fit-content;
}}

.aboutme-heading {{
  font-family: var(--font-display);
  font-weight: 800;
  font-size: clamp(34px, 4.5vw, 54px);
  letter-spacing: -0.03em;
  color: var(--pink);
  line-height: 1.1;
}}

.aboutme-bio {{
  font-size: clamp(16px, 1.7vw, 18px);
  line-height: 1.65;
  color: rgba(255, 255, 255, 0.88);
  font-weight: 500;
}}

.loves-list {{
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-top: 8px;
}}

.love-item {{
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: clamp(14px, 1.5vw, 16px);
  font-weight: 600;
  color: var(--pink);
}}

.love-item svg {{
  width: 18px;
  height: 18px;
  fill: var(--pink);
  flex-shrink: 0;
}}

.social-pills {{
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 12px;
}}

.social-pill {{
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 18px;
  border-radius: 999px;
  border: 1px solid rgba(255, 211, 230, 0.35);
  color: var(--pink);
  font-size: 14px;
  font-weight: 600;
  transition: background-color 0.2s ease, color 0.2s ease, transform 0.2s var(--ease-main);
}}

.social-pill:hover {{
  background-color: var(--pink);
  color: var(--purple);
  transform: translateY(-2px);
}}

.social-pill svg {{
  width: 15px;
  height: 15px;
  fill: currentColor;
}}

/* ==========================================================================
   8. FINAL CTA & FOOTER — PINK
   ========================================================================== */
.section-contact {{
  padding-top: var(--section-pad);
  padding-bottom: clamp(48px, 6vw, 80px);
  background-color: var(--pink);
  color: var(--purple);
}}

.contact-wrap {{
  display: flex;
  flex-direction: column;
  gap: clamp(48px, 7vw, 84px);
}}

.contact-top {{
  max-width: 900px;
}}

.contact-heading {{
  font-family: var(--font-display);
  font-weight: 800;
  font-size: clamp(40px, 7vw, 88px);
  letter-spacing: -0.03em;
  line-height: 1;
  color: var(--purple);
}}

.contact-buttons {{
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  margin-top: clamp(28px, 4vw, 44px);
}}

.btn-primary {{
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background-color: var(--purple);
  color: var(--pink);
  padding: 16px 32px;
  border-radius: 999px;
  font-size: 16px;
  font-weight: 700;
  transition: transform 0.2s var(--ease-main), box-shadow 0.2s ease;
  position: relative;
}}

.btn-primary .arrow {{
  display: inline-block;
  transition: transform 0.25s var(--ease-main);
}}

.btn-primary:hover .arrow {{
  transform: translate(3px, -3px);
}}

.btn-secondary {{
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background-color: transparent;
  color: var(--purple);
  border: 2px solid var(--purple);
  padding: 14px 30px;
  border-radius: 999px;
  font-size: 16px;
  font-weight: 700;
  transition: transform 0.2s var(--ease-main), background-color 0.2s ease, color 0.2s ease;
}}

.btn-secondary .arrow {{
  display: inline-block;
  transition: transform 0.25s var(--ease-main);
}}

.btn-secondary:hover {{
  background-color: var(--purple);
  color: var(--pink);
}}

.btn-secondary:hover .arrow {{
  transform: translate(3px, -3px);
}}

.contact-cols {{
  display: grid;
  grid-template-columns: 1fr;
  gap: 32px;
  border-top: 2px solid var(--purple);
  padding-top: clamp(32px, 5vw, 56px);
}}

@media (min-width: 768px) {{
  .contact-cols {{
    grid-template-columns: repeat(3, 1fr);
  }}
}}

.contact-col-item {{
  display: flex;
  flex-direction: column;
  gap: 6px;
}}

.contact-col-label {{
  font-size: 13px;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-weight: 700;
  color: rgba(28, 11, 46, 0.6);
}}

.contact-col-val {{
  font-size: clamp(18px, 2.2vw, 24px);
  font-weight: 700;
  color: var(--purple);
  transition: opacity 0.2s ease;
}}

.contact-col-val:hover {{
  opacity: 0.7;
}}

.footer-bottom {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-top: 1px solid rgba(28, 11, 46, 0.2);
  padding-top: 32px;
  font-size: 14px;
  font-weight: 600;
  color: rgba(28, 11, 46, 0.8);
}}

.back-to-top {{
  cursor: pointer;
  transition: transform 0.2s var(--ease-main);
}}

.back-to-top:hover {{
  transform: translateY(-2px);
  color: var(--purple);
}}

/* ==========================================================================
   ACCESSIBILITY: PREFERS REDUCED MOTION
   ========================================================================== */
@media (prefers-reduced-motion: reduce) {{
  *, *::before, *::after {{
    animation-duration: 0.001ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.001ms !important;
    scroll-behavior: auto !important;
  }}
  .intro-words span i,
  .split-word i,
  [data-anim] {{
    transform: none !important;
    opacity: 1 !important;
  }}
  .id-rig {{
    transform: none !important;
    animation: none !important;
  }}
  .aboutme-pic-frame .pic-inner,
  .aboutme-pic-frame .pic-inner img {{
    clip-path: none !important;
    transform: none !important;
  }}
  .marquee-track {{
    animation: none !important;
  }}
}}
</style>
</head>

<body>

<!-- ==========================================================================
     GLOBAL FLOATING PILL NAV
     ========================================================================== -->
<header class="header-wrap hidden" id="headerNav" aria-label="Main Navigation">
  <nav class="nav-pill">
    <a href="#intro" class="nav-logo" aria-label="Unity Ekeoba Home">
      <span>unity</span>
      <svg viewBox="0 0 24 24" aria-hidden="true">
        <path d="M5 16L3 5l5.5 5L12 4l3.5 6L21 5l-2 11H5zm14 3c0 .6-.4 1-1 1H6c-.6 0-1-.4-1-1v-1h14v1z"/>
      </svg>
    </a>
    <div class="nav-links">
      <a href="#work" class="nav-link">Work</a>
      <a href="#about" class="nav-link">About</a>
    </div>
    <a href="mailto:unity@replyiq.cv?subject=Project%20enquiry" class="nav-cta">
      <span class="status-dot" aria-hidden="true"></span>
      <span>Contact me</span>
    </a>
  </nav>
</header>

<!-- ==========================================================================
     FLOATING WHATSAPP BUTTON
     ========================================================================== -->
<a href="https://wa.me/2349076948648?text=Hi%20Unity%2C%20I'd%20like%20to%20talk%20about%20a%20project." 
   target="_blank" 
   rel="noopener noreferrer" 
   class="whatsapp-btn hidden" 
   id="whatsappBtn" 
   aria-label="Chat with Unity on WhatsApp">
  <svg viewBox="0 0 24 24" aria-hidden="true">
    <path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.82 9.82 0 0012.04 2zm.01 18.15c-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.13 8.13 0 01-1.25-4.38c0-4.5 3.66-8.16 8.17-8.16 2.18 0 4.23.85 5.78 2.39a8.12 8.12 0 012.39 5.77c0 4.51-3.66 8.16-8.17 8.16zm4.47-6.11c-.25-.12-1.46-.72-1.69-.8-.23-.08-.39-.12-.56.12-.17.25-.64.8-.79.97-.15.17-.3.19-.55.07-.25-.12-1.05-.39-2-1.23-.74-.66-1.23-1.47-1.38-1.72-.15-.25-.02-.38.11-.5.11-.11.25-.29.37-.43.12-.15.17-.25.25-.42.08-.17.04-.31-.02-.43s-.56-1.34-.76-1.84c-.2-.48-.41-.42-.56-.43h-.48c-.17 0-.43.06-.66.31-.22.25-.86.84-.86 2.05 0 1.21.88 2.38 1 2.55.13.17 1.74 2.66 4.21 3.73.59.25 1.05.41 1.41.52.59.19 1.13.16 1.56.1.47-.07 1.46-.6 1.67-1.18.21-.58.21-1.07.15-1.18-.07-.12-.23-.19-.48-.31z"/>
  </svg>
</a>

<!-- ==========================================================================
     SECTION 1: INTRO (ID CARD HERO) — PURPLE
     ========================================================================== -->
<section class="section-intro theme-purple" id="intro" aria-label="Introduction">
  <div class="intro-words" id="introWords" aria-hidden="true">
    <span><i>DEVELOPER</i></span>
    <span><i>ENGINEER</i></span>
    <span><i>FOUNDER</i></span>
    <span><i>BUILDER</i></span>
  </div>

  <div class="id-rig" id="idRig">
    <div class="id-strap"></div>
    <!-- Metal Clip -->
    <svg class="id-clip" viewBox="0 0 48 44" aria-hidden="true">
      <rect x="8" y="2" width="32" height="15" rx="6" fill="#ffffff" stroke="#1c0b2e" stroke-width="2"/>
      <rect x="14" y="14" width="20" height="26" rx="4" fill="#ffffff" stroke="#1c0b2e" stroke-width="2"/>
      <circle cx="24" cy="24" r="3.5" fill="#1c0b2e"/>
    </svg>

    <div class="card-stage">
      <div class="id-card" id="idCard" role="button" tabindex="0" aria-label="Unity Ekeoba ID Card (Click to flip)">
        <!-- FRONT OF CARD -->
        <div class="card-face front">
          <div class="card-inner front-inner">
            <div class="card-photo-box">
              <img src="{b64['id_card']}" alt="Unity Ekeoba portrait photo">
              <div class="card-photo-overlay">
                <span class="card-tag-pill">FULL STACK DEVELOPER</span>
                <span class="card-globe-pill">
                  <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 014 10 15.3 15.3 0 01-4 10 15.3 15.3 0 01-4-10 15.3 15.3 0 014-10z"/>
                  </svg>
                  AVAILABLE
                </span>
              </div>
            </div>

            <div class="card-info">
              <div class="card-name-title">
                <h1 class="card-name">UNITY</h1>
                <p class="card-role">Full Stack Developer + Blockchain Engineer</p>
              </div>

              <div class="card-pill-row">
                <div class="freelance-pill">
                  <span class="dot"></span>
                  <span>AVAILABLE FOR FREELANCE</span>
                </div>
                <div class="card-sig-box">
                  <span class="card-sig">Unity</span>
                  <svg width="10" height="10" viewBox="0 0 24 24" fill="#1c0b2e" style="margin-top:-8px;">
                    <path d="M5 16L3 5l5.5 5L12 4l3.5 6L21 5l-2 11H5zm14 3c0 .6-.4 1-1 1H6c-.6 0-1-.4-1-1v-1h14v1z"/>
                  </svg>
                </div>
              </div>

              <div class="card-bottom-row">
                <!-- Barcode SVG -->
                <svg class="card-barcode" viewBox="0 0 120 22" aria-hidden="true">
                  <rect x="0" y="0" width="3" height="22" fill="#1c0b2e"/>
                  <rect x="5" y="0" width="2" height="22" fill="#1c0b2e"/>
                  <rect x="10" y="0" width="4" height="22" fill="#1c0b2e"/>
                  <rect x="16" y="0" width="1.5" height="22" fill="#1c0b2e"/>
                  <rect x="20" y="0" width="3" height="22" fill="#1c0b2e"/>
                  <rect x="26" y="0" width="5" height="22" fill="#1c0b2e"/>
                  <rect x="34" y="0" width="2" height="22" fill="#1c0b2e"/>
                  <rect x="38" y="0" width="3" height="22" fill="#1c0b2e"/>
                  <rect x="44" y="0" width="1" height="22" fill="#1c0b2e"/>
                  <rect x="48" y="0" width="4" height="22" fill="#1c0b2e"/>
                  <rect x="55" y="0" width="2" height="22" fill="#1c0b2e"/>
                  <rect x="60" y="0" width="4" height="22" fill="#1c0b2e"/>
                  <rect x="66" y="0" width="1.5" height="22" fill="#1c0b2e"/>
                  <rect x="70" y="0" width="3" height="22" fill="#1c0b2e"/>
                  <rect x="76" y="0" width="2" height="22" fill="#1c0b2e"/>
                  <rect x="81" y="0" width="4" height="22" fill="#1c0b2e"/>
                  <rect x="88" y="0" width="2" height="22" fill="#1c0b2e"/>
                  <rect x="92" y="0" width="3.5" height="22" fill="#1c0b2e"/>
                  <rect x="98" y="0" width="1.5" height="22" fill="#1c0b2e"/>
                  <rect x="102" y="0" width="4" height="22" fill="#1c0b2e"/>
                  <rect x="109" y="0" width="2" height="22" fill="#1c0b2e"/>
                  <rect x="114" y="0" width="3" height="22" fill="#1c0b2e"/>
                </svg>
                <span class="card-id-num">ID 0001</span>
              </div>
            </div>
          </div>
        </div>

        <!-- BACK OF CARD -->
        <div class="card-face back">
          <div class="card-inner back-inner">
            <h2 class="back-head">What I do</h2>
            <div class="back-rows">
              <div class="back-row">
                <div class="back-row-title">Developer</div>
                <div class="back-row-desc">Next.js, React, TypeScript, Node.js</div>
              </div>
              <div class="back-row">
                <div class="back-row-title">Engineer</div>
                <div class="back-row-desc">Solidity, smart contracts, Web3</div>
              </div>
              <div class="back-row">
                <div class="back-row-title">Founder</div>
                <div class="back-row-desc">ReplyIQ, AI SaaS, product strategy</div>
              </div>
            </div>

            <div class="back-quote">
              &ldquo;Turning ideas into products people actually use.&rdquo;
            </div>

            <div class="back-foot">
              <span class="back-handle">@KEMERALD25</span>
              <svg class="card-barcode" viewBox="0 0 100 22" style="width:75px;" aria-hidden="true">
                <rect x="0" y="0" width="3" height="22" fill="#1c0b2e"/>
                <rect x="5" y="0" width="2" height="22" fill="#1c0b2e"/>
                <rect x="10" y="0" width="4" height="22" fill="#1c0b2e"/>
                <rect x="17" y="0" width="2" height="22" fill="#1c0b2e"/>
                <rect x="22" y="0" width="3" height="22" fill="#1c0b2e"/>
                <rect x="28" y="0" width="5" height="22" fill="#1c0b2e"/>
                <rect x="36" y="0" width="2" height="22" fill="#1c0b2e"/>
                <rect x="41" y="0" width="3" height="22" fill="#1c0b2e"/>
                <rect x="47" y="0" width="1" height="22" fill="#1c0b2e"/>
                <rect x="52" y="0" width="4" height="22" fill="#1c0b2e"/>
                <rect x="59" y="0" width="2" height="22" fill="#1c0b2e"/>
                <rect x="64" y="0" width="4" height="22" fill="#1c0b2e"/>
                <rect x="71" y="0" width="2" height="22" fill="#1c0b2e"/>
                <rect x="76" y="0" width="3" height="22" fill="#1c0b2e"/>
                <rect x="82" y="0" width="5" height="22" fill="#1c0b2e"/>
                <rect x="90" y="0" width="2" height="22" fill="#1c0b2e"/>
                <rect x="95" y="0" width="3" height="22" fill="#1c0b2e"/>
              </svg>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="intro-foot">
    <div class="typing-lead">
      <span id="introTyping">Building AI-powered SaaS products</span>
      <span class="caret" aria-hidden="true"></span>
    </div>
    <div class="scroll-cue">
      <span>Scroll</span>
      <div class="scroll-line" aria-hidden="true"></div>
    </div>
  </div>
</section>

<!-- ==========================================================================
     SECTION 2: ABOUT (PHOTO COLLAGE) — PINK
     ========================================================================== -->
<section class="section-about theme-pink" id="about" aria-label="About Unity Ekeoba">
  <div class="container">
    <div class="about-grid">
      <!-- Left: Overlapping collage -->
      <div class="collage-wrap">
        <div class="collage-main" data-anim="left">
          <img src="{b64['sofa']}" alt="Unity Ekeoba sitting relaxed on a contemporary cream sofa, white t-shirt and jeans">
        </div>
        <div class="collage-secondary" data-anim="right" style="transition-delay: 0.15s;">
          <img src="{b64['workspace']}" alt="Unity's developer workstation setup with code editor and dual monitor">
        </div>
        <div class="collage-note" data-anim="scale" style="transition-delay: 0.35s;">
          hi, I'm Unity
        </div>
      </div>

      <!-- Right: Heading + copy -->
      <div class="about-content">
        <h2 class="about-heading" id="aboutTypeHeading">
          <span class="typed-text"></span><span class="type-caret" aria-hidden="true"></span>
        </h2>
        <p class="about-copy" data-anim="up" style="transition-delay: 0.15s;">
          Full-stack developer, blockchain engineer and founder. My work spans AI, SaaS, web development and blockchain — turning ideas into scalable products used by businesses and communities across fintech, real estate, gaming and Web3.
        </p>
      </div>
    </div>
  </div>
</section>

<!-- ==========================================================================
     SECTION 3: SERVICES (WHAT I DO) — PURPLE
     ========================================================================== -->
<section class="section-services theme-purple" id="services" aria-label="Services and capabilities">
  <div class="container">
    <h2 class="split-heading" style="font-family: var(--font-display); font-weight:800; font-size:clamp(32px, 4.5vw, 54px); letter-spacing:-0.03em; color:var(--pink);">
      What I do
    </h2>
    <div class="services-list">
      <!-- Row 1: Developer -->
      <div class="service-row" data-anim="left">
        <div class="service-icon" aria-hidden="true">
          <svg viewBox="0 0 24 24">
            <path d="M9.4 16.6L4.8 12l4.6-4.6L8 6l-6 6 6 6 1.4-1.4zm5.2 0l4.6-4.6-4.6-4.6L16 6l6 6-6 6-1.4-1.4z"/>
          </svg>
        </div>
        <div class="service-body">
          <h3 class="service-title">Developer</h3>
          <p class="service-desc">Next.js, React, TypeScript, Node.js web apps</p>
        </div>
      </div>

      <!-- Row 2: Engineer -->
      <div class="service-row" data-anim="right" style="transition-delay: 0.1s;">
        <div class="service-icon" aria-hidden="true">
          <svg viewBox="0 0 24 24">
            <path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm0 10.99h7c-.53 4.12-3.28 7.79-7 8.94V12H5V6.3l7-3.11v8.8z"/>
          </svg>
        </div>
        <div class="service-body">
          <h3 class="service-title">Engineer</h3>
          <p class="service-desc">Solidity and smart contracts across EVM chains</p>
        </div>
      </div>

      <!-- Row 3: Founder -->
      <div class="service-row" data-anim="left" style="transition-delay: 0.15s;">
        <div class="service-icon" aria-hidden="true">
          <svg viewBox="0 0 24 24">
            <path d="M12 2.5a2.5 2.5 0 0 1 2 4.02A4 4 0 0 1 18 10v1.5a1.5 1.5 0 0 1-1.5 1.5h-9A1.5 1.5 0 0 1 6 11.5V10a4 4 0 0 1 4-3.48A2.5 2.5 0 0 1 12 2.5zM7 16h10v2a2 2 0 0 1-2 2H9a2 2 0 0 1-2-2v-2zm-3 5h16v1H4v-1z"/>
          </svg>
        </div>
        <div class="service-body">
          <h3 class="service-title">Founder</h3>
          <p class="service-desc">Building and scaling ReplyIQ and CabVibe</p>
        </div>
      </div>

      <!-- Row 4: Builder -->
      <div class="service-row" data-anim="right" style="transition-delay: 0.2s;">
        <div class="service-icon" aria-hidden="true">
          <svg viewBox="0 0 24 24">
            <path d="M22 9V7h-2V5c0-1.1-.9-2-2-2H4c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2v-2h2v-2h-2v-2h2v-2h-2V9h2zm-4 10H4V5h14v14zM6 13h5v5H6v-5zm7-6h3v3h-3V7zm-7 0h5v5H6V7z"/>
          </svg>
        </div>
        <div class="service-body">
          <h3 class="service-title">Builder</h3>
          <p class="service-desc">AI, SaaS and Web3 products end to end</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ==========================================================================
     SECTION 4: STATS (NUMBERS) — PINK
     ========================================================================== -->
<section class="section-stats theme-pink" id="stats" aria-label="Key statistics and metrics">
  <div class="container">
    <div class="stats-grid">
      <div class="stat-item" data-anim="up">
        <div class="stat-number">
          <span class="stat-counter" data-target="6">0</span><span class="stat-suffix">+</span>
        </div>
        <div class="stat-label">Blockchains shipped to</div>
      </div>

      <div class="stat-item" data-anim="up" style="transition-delay: 0.1s;">
        <div class="stat-number">
          <span class="stat-counter" data-target="150">0</span><span class="stat-suffix">+</span>
        </div>
        <div class="stat-label">Freelancers served on TAL3NT</div>
      </div>

      <div class="stat-item" data-anim="up" style="transition-delay: 0.2s;">
        <div class="stat-number">
          <span class="stat-counter" data-target="300">0</span><span class="stat-suffix">+</span>
        </div>
        <div class="stat-label">On-chain transactions enabled</div>
      </div>

      <div class="stat-item" data-anim="up" style="transition-delay: 0.3s;">
        <div class="stat-number">
          <span class="stat-counter" data-target="5">0</span><span class="stat-suffix">+</span>
        </div>
        <div class="stat-label">Years building software</div>
      </div>
    </div>
  </div>
</section>

<!-- ==========================================================================
     SECTION 5: MARQUEE TOOL STRIP — PURPLE
     ========================================================================== -->
<section class="section-marquee theme-purple" aria-label="Technologies and tools">
  <div class="marquee-track" aria-hidden="true">
    <div class="marquee-content">
      <span class="marquee-item">Next.js</span><span class="marquee-star">✦</span>
      <span class="marquee-item">React</span><span class="marquee-star">✦</span>
      <span class="marquee-item">TypeScript</span><span class="marquee-star">✦</span>
      <span class="marquee-item">Node.js</span><span class="marquee-star">✦</span>
      <span class="marquee-item">Solidity</span><span class="marquee-star">✦</span>
      <span class="marquee-item">Tailwind CSS</span><span class="marquee-star">✦</span>
      <span class="marquee-item">MongoDB</span><span class="marquee-star">✦</span>
      <span class="marquee-item">Web3.js</span><span class="marquee-star">✦</span>
    </div>
    <!-- Duplicate for infinite seamless scroll -->
    <div class="marquee-content">
      <span class="marquee-item">Next.js</span><span class="marquee-star">✦</span>
      <span class="marquee-item">React</span><span class="marquee-star">✦</span>
      <span class="marquee-item">TypeScript</span><span class="marquee-star">✦</span>
      <span class="marquee-item">Node.js</span><span class="marquee-star">✦</span>
      <span class="marquee-item">Solidity</span><span class="marquee-star">✦</span>
      <span class="marquee-item">Tailwind CSS</span><span class="marquee-star">✦</span>
      <span class="marquee-item">MongoDB</span><span class="marquee-star">✦</span>
      <span class="marquee-item">Web3.js</span><span class="marquee-star">✦</span>
    </div>
  </div>
</section>

<!-- ==========================================================================
     SECTION 6: SELECTED WORK — PINK
     ========================================================================== -->
<div class="section-work-container" id="work">
  <div class="work-sticky">
    <div class="work-header">
      <h2 class="work-title split-heading">Selected work</h2>
      <p class="work-subtitle" data-anim="up">Web, Web3 and AI. Real estate, blockchain gaming, and SaaS.</p>
    </div>

    <div class="work-carousel-wrap">
      <div class="work-track" id="workTrack">
        <!-- 1. Swift Liaison -->
        <figure class="project-card">
          <div class="project-img-box">
            <img src="{b64['swift_liaison']}" alt="Swift Liaison modern real estate platform website">
          </div>
          <figcaption class="project-caption">
            <span class="project-name">Swift Liaison</span>
            <span class="project-category">Real estate platform</span>
          </figcaption>
        </figure>

        <!-- 2. TAL3NT -->
        <figure class="project-card">
          <div class="project-img-box">
            <img src="{b64['tal3nt']}" alt="TAL3NT Web3 talent and job marketplace application">
          </div>
          <figcaption class="project-caption">
            <span class="project-name">TAL3NT</span>
            <span class="project-category">Web3 job marketplace</span>
          </figcaption>
        </figure>

        <!-- 3. ChessOnChain -->
        <figure class="project-card">
          <div class="project-img-box">
            <img src="{b64['chessonchain']}" alt="ChessOnChain multi-chain decentralized chess game app">
          </div>
          <figcaption class="project-caption">
            <span class="project-name">ChessOnChain</span>
            <span class="project-category">Multi-chain chess</span>
          </figcaption>
        </figure>

        <!-- 4. TriviaBase -->
        <figure class="project-card">
          <div class="project-img-box">
            <img src="{b64['triviabase']}" alt="TriviaBase interactive blockchain trivia game app">
          </div>
          <figcaption class="project-caption">
            <span class="project-name">TriviaBase</span>
            <span class="project-category">Blockchain trivia</span>
          </figcaption>
        </figure>

        <!-- 5. Verda -->
        <figure class="project-card">
          <div class="project-img-box">
            <img src="{b64['verda']}" alt="Verda tokenized real estate investment platform website">
          </div>
          <figcaption class="project-caption">
            <span class="project-name">Verda</span>
            <span class="project-category">Tokenized real estate</span>
          </figcaption>
        </figure>

        <!-- 6. Nexboard -->
        <figure class="project-card">
          <div class="project-img-box">
            <img src="{b64['nexboard']}" alt="Nexboard modern SaaS analytics dashboard website">
          </div>
          <figcaption class="project-caption">
            <span class="project-name">Nexboard</span>
            <span class="project-category">SaaS analytics dashboard</span>
          </figcaption>
        </figure>
      </div>
    </div>

    <!-- Scroll Progress Bar -->
    <div class="work-progress-bar-wrap" aria-hidden="true">
      <div class="work-progress-fill" id="workProgressFill"></div>
    </div>
  </div>
</div>

<!-- ==========================================================================
     SECTION 7: ABOUT ME — PURPLE
     ========================================================================== -->
<section class="section-aboutme theme-purple" id="about_me" aria-label="About Unity Ekeoba founder journey">
  <div class="container">
    <div class="aboutme-grid">
      <!-- Left: Photo of Unity working with inset clip reveal -->
      <div class="aboutme-pic-frame" id="aboutPicFrame">
        <div class="pic-inner">
          <img src="{b64['working']}" alt="Unity Ekeoba working on his laptop at a modern workspace">
        </div>
      </div>

      <!-- Right: Details -->
      <div class="aboutme-details">
        <span class="badge-pill" data-anim="up">✦ Founder of ReplyIQ</span>
        <h2 class="aboutme-heading split-heading">About me</h2>
        <p class="aboutme-bio" data-anim="up" style="transition-delay: 0.1s;">
          I'm Unity Ekeoba, founder of ReplyIQ and a full-stack developer passionate about building technology that solves real business problems — spanning AI, SaaS, web development and blockchain, with a track record of turning ideas into scalable products.
        </p>

        <div class="loves-list" data-anim="up" style="transition-delay: 0.18s;">
          <div class="love-item">
            <svg viewBox="0 0 24 24" aria-hidden="true">
              <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
            </svg>
            <span>Building AI and SaaS products for real businesses</span>
          </div>
          <div class="love-item">
            <svg viewBox="0 0 24 24" aria-hidden="true">
              <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
            </svg>
            <span>Shipping smart contracts across EVM chains</span>
          </div>
          <div class="love-item">
            <svg viewBox="0 0 24 24" aria-hidden="true">
              <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
            </svg>
            <span>Growing ReplyIQ and CabVibe from the ground up</span>
          </div>
        </div>

        <div class="social-pills" data-anim="up" style="transition-delay: 0.25s;">
          <a href="https://github.com/kemerald25" target="_blank" rel="noopener noreferrer" class="social-pill" aria-label="GitHub profile">
            <svg viewBox="0 0 24 24" aria-hidden="true">
              <path d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.53 1.032 1.53 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z"/>
            </svg>
            <span>kemerald25</span>
          </a>
          <a href="https://linkedin.com/in/unityekeoba" target="_blank" rel="noopener noreferrer" class="social-pill" aria-label="LinkedIn profile">
            <svg viewBox="0 0 24 24" aria-hidden="true">
              <path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.46 8.76a1.64 1.64 0 1 0-.01-3.27 1.64 1.64 0 0 0 .01 3.27m1.4 9.74V9.97H5.06v8.53h2.8z"/>
            </svg>
            <span>unityekeoba</span>
          </a>
          <a href="https://x.com/iamdevroyale" target="_blank" rel="noopener noreferrer" class="social-pill" aria-label="X (Twitter) profile">
            <svg viewBox="0 0 24 24" aria-hidden="true">
              <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
            </svg>
            <span>@iamdevroyale</span>
          </a>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ==========================================================================
     SECTION 8: FINAL CTA & FOOTER — PINK
     ========================================================================== -->
<section class="section-contact theme-pink" id="contact" aria-label="Contact Unity Ekeoba">
  <div class="container">
    <div class="contact-wrap">
      <div class="contact-top">
        <h2 class="contact-heading split-heading">
          Got an idea?<br>Let's build it.
        </h2>
        <div class="contact-buttons">
          <a href="mailto:unity@replyiq.cv?subject=Project%20enquiry" class="btn-primary magnetic-btn">
            <span>Contact me</span>
            <span class="arrow" aria-hidden="true">↗</span>
          </a>
          <a href="https://wa.me/2349076948648?text=Hi%20Unity%2C%20I'd%20like%20to%20talk%20about%20a%20project." 
             target="_blank" 
             rel="noopener noreferrer" 
             class="btn-secondary magnetic-btn">
            <span>Get a quote</span>
            <span class="arrow" aria-hidden="true">↗</span>
          </a>
        </div>
      </div>

      <!-- 3 Contact Columns -->
      <div class="contact-cols" data-anim="up">
        <div class="contact-col-item">
          <span class="contact-col-label">Email</span>
          <a href="mailto:unity@replyiq.cv?subject=Project%20enquiry" class="contact-col-val">
            unity@replyiq.cv
          </a>
        </div>
        <div class="contact-col-item">
          <span class="contact-col-label">WhatsApp</span>
          <a href="https://wa.me/2349076948648?text=Hi%20Unity%2C%20I'd%20like%20to%20talk%20about%20a%20project." 
             target="_blank" 
             rel="noopener noreferrer" 
             class="contact-col-val">
            +234 907 694 8648
          </a>
        </div>
        <div class="contact-col-item">
          <span class="contact-col-label">Social</span>
          <a href="https://linkedin.com/in/unityekeoba" 
             target="_blank" 
             rel="noopener noreferrer" 
             class="contact-col-val">
            unityekeoba
          </a>
        </div>
      </div>

      <!-- Footer Bottom -->
      <div class="footer-bottom">
        <div>&copy; 2026 Unity Ekeoba</div>
        <a href="#intro" class="back-to-top" id="backToTop">Back to top &uarr;</a>
      </div>
    </div>
  </div>
</section>

<!-- ==========================================================================
     VANILLA JAVASCRIPT: ANIMATION SYSTEM, CAROUSEL, ID CARD & CONTROLS
     ========================================================================== -->
<script>
(function () {{
  'use strict';
  
  const isReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  
  /* --------------------------------------------------------------------------
     1. SPLIT HEADINGS INTO WORD SPANS (OVERFLOW MASK)
     -------------------------------------------------------------------------- */
  const splitHeadings = document.querySelectorAll('.split-heading');
  splitHeadings.forEach(h => {{
    const lines = h.innerHTML.split(/<br\s*\\/?>/i);
    const transformed = lines.map(line => {{
      const text = line.trim();
      const words = text.split(/\\s+/);
      return words.map((w, idx) => {{
        return `<span class="split-word"><i style="transition-delay:${{idx * 70}}ms">${{w}}</i></span>`;
      }}).join(' ');
    }}).join('<br>');
    h.innerHTML = transformed;
  }});

  /* --------------------------------------------------------------------------
     2. INTERSECTION OBSERVER FOR SCROLL REVEALS
     -------------------------------------------------------------------------- */
  const animElements = document.querySelectorAll('[data-anim], .split-heading, .aboutme-pic-frame');
  
  if (isReducedMotion) {{
    animElements.forEach(el => {{
      el.classList.add('revealed');
      el.querySelectorAll('.split-word i').forEach(i => i.style.transform = 'none');
    }});
  }} else {{
    const observer = new IntersectionObserver((entries) => {{
      entries.forEach(entry => {{
        if (entry.isIntersecting) {{
          entry.target.classList.add('revealed');
          if (entry.target.classList.contains('split-heading')) {{
            entry.target.querySelectorAll('.split-word i').forEach(i => {{
              i.style.transform = 'translateY(0)';
            }});
          }}
          observer.unobserve(entry.target);
        }}
      }});
    }}, {{
      threshold: 0.18,
      rootMargin: '0px 0px -40px 0px'
    }});

    animElements.forEach(el => observer.observe(el));
  }}

  /* --------------------------------------------------------------------------
     3. INTRO: WORDS RISE, RIG DROP & ID CARD AUTO-FLIP
     -------------------------------------------------------------------------- */
  const idRig = document.getElementById('idRig');
  const idCard = document.getElementById('idCard');
  const introWords = document.querySelectorAll('#introWords span i');
  
  // 1) Words rise line by line (0.9s, 110ms stagger)
  if (!isReducedMotion) {{
    introWords.forEach((word, idx) => {{
      setTimeout(() => {{
        word.style.transform = 'translateY(0)';
      }}, 150 + idx * 110);
    }});
  }} else {{
    introWords.forEach(w => w.style.transform = 'none');
  }}

  // 2) Drop lanyard + card
  if (!isReducedMotion) {{
    setTimeout(() => {{
      idRig.classList.add('dropped');
    }}, 200);
  }} else {{
    idRig.style.transform = 'translateY(0)';
  }}

  // 3) Card Flipping logic
  let cardAngle = 0;
  let autoFlipTimer = null;
  
  function flipCard() {{
    cardAngle += 180;
    idCard.style.transform = `rotateY(${{cardAngle}}deg)`;
  }}

  function resetAutoFlip() {{
    if (autoFlipTimer) clearInterval(autoFlipTimer);
    if (!isReducedMotion) {{
      autoFlipTimer = setInterval(flipCard, 3600);
    }}
  }}

  // First flip at 3.1s after load, then every 3.6s
  if (!isReducedMotion) {{
    setTimeout(() => {{
      flipCard();
      autoFlipTimer = setInterval(flipCard, 3600);
    }}, 3100);
  }}

  // Tapping or clicking flips instantly and resets timer
  idCard.addEventListener('click', () => {{
    flipCard();
    resetAutoFlip();
  }});

  idCard.addEventListener('keydown', (e) => {{
    if (e.key === 'Enter' || e.key === ' ') {{
      e.preventDefault();
      flipCard();
      resetAutoFlip();
    }}
  }});

  /* --------------------------------------------------------------------------
     4. INTRO FOOTER TYPING TEXT CYCLING
     -------------------------------------------------------------------------- */
  const typingElement = document.getElementById('introTyping');
  const phrases = [
    'Building AI-powered SaaS products',
    'Shipping smart contracts across chains',
    'Founding ReplyIQ and CabVibe',
    'Studying Estate Management at UNIBEN',
    'Based in Nigeria, working worldwide'
  ];
  let phraseIdx = 0;
  let charIdx = phrases[0].length;
  let isDeleting = false;
  let typingSpeed = 60;

  function typeCycle() {{
    const currentPhrase = phrases[phraseIdx];
    
    if (isDeleting) {{
      typingElement.textContent = currentPhrase.substring(0, charIdx - 1);
      charIdx--;
      typingSpeed = 30;
    }} else {{
      typingElement.textContent = currentPhrase.substring(0, charIdx + 1);
      charIdx++;
      typingSpeed = 65;
    }}

    if (!isDeleting && charIdx === currentPhrase.length) {{
      typingSpeed = 2400; // pause on full phrase
      isDeleting = true;
    }} else if (isDeleting && charIdx === 0) {{
      isDeleting = false;
      phraseIdx = (phraseIdx + 1) % phrases.length;
      typingSpeed = 400;
    }}

    setTimeout(typeCycle, typingSpeed);
  }}

  if (!isReducedMotion) {{
    setTimeout(typeCycle, 2000);
  }}

  /* --------------------------------------------------------------------------
     5. ABOUT SECTION: TYPING OUT HEADING LETTER BY LETTER
     -------------------------------------------------------------------------- */
  const aboutTypeHeading = document.getElementById('aboutTypeHeading');
  const aboutTypedText = aboutTypeHeading.querySelector('.typed-text');
  const fullAboutHeading = 'I build things businesses actually use.';
  let aboutTyped = false;

  const aboutObserver = new IntersectionObserver((entries) => {{
    entries.forEach(entry => {{
      if (entry.isIntersecting && !aboutTyped) {{
        aboutTyped = true;
        let idx = 0;
        if (isReducedMotion) {{
          aboutTypedText.textContent = fullAboutHeading;
        }} else {{
          function typeLetter() {{
            if (idx < fullAboutHeading.length) {{
              aboutTypedText.textContent += fullAboutHeading.charAt(idx);
              idx++;
              setTimeout(typeLetter, 45);
            }}
          }}
          typeLetter();
        }}
        aboutObserver.unobserve(entry.target);
      }}
    }});
  }}, {{ threshold: 0.25 }});

  aboutObserver.observe(aboutTypeHeading);

  /* --------------------------------------------------------------------------
     6. STATS NUMBER COUNTER (COUNT UP WITH EASE-OUT CURVE 1.8s)
     -------------------------------------------------------------------------- */
  const statCounters = document.querySelectorAll('.stat-counter');
  let statsDone = false;

  const statsObserver = new IntersectionObserver((entries) => {{
    entries.forEach(entry => {{
      if (entry.isIntersecting && !statsDone) {{
        statsDone = true;
        statCounters.forEach(counter => {{
          const target = parseInt(counter.dataset.target, 10);
          if (isReducedMotion) {{
            counter.textContent = target;
            return;
          }}
          const duration = 1800;
          const startTime = performance.now();
          function updateCounter(now) {{
            const elapsed = now - startTime;
            const progress = Math.min(elapsed / duration, 1);
            // Ease out cubic
            const easeProgress = 1 - Math.pow(1 - progress, 3);
            const current = Math.floor(easeProgress * target);
            counter.textContent = current;
            if (progress < 1) {{
              requestAnimationFrame(updateCounter);
            }} else {{
              counter.textContent = target;
            }}
          }}
          requestAnimationFrame(updateCounter);
        }});
        statsObserver.unobserve(entry.target);
      }}
    }});
  }}, {{ threshold: 0.6 }});

  const statsSection = document.getElementById('stats');
  if (statsSection) statsObserver.observe(statsSection);

  /* --------------------------------------------------------------------------
     7. PINNED WORK SECTION: VERTICAL SCROLL DRIVES HORIZONTAL CAROUSEL
        + 3D TILT & SCALE ACCORDING TO CENTER DISTANCE
     -------------------------------------------------------------------------- */
  const workContainer = document.getElementById('work');
  const workTrack = document.getElementById('workTrack');
  const workProgressFill = document.getElementById('workProgressFill');
  const projectCards = document.querySelectorAll('.project-card');

  function updateWorkScroll() {{
    if (!workContainer || !workTrack) return;
    const rect = workContainer.getBoundingClientRect();
    const totalDist = workContainer.offsetHeight - window.innerHeight;
    if (totalDist <= 0) return;
    
    const scrolled = -rect.top;
    const progress = Math.max(0, Math.min(scrolled / totalDist, 1));

    // Progress bar fill
    if (workProgressFill) {{
      workProgressFill.style.width = `${{progress * 100}}%`;
    }}

    // Horizontal translation
    const maxTrackScroll = workTrack.scrollWidth - window.innerWidth;
    if (maxTrackScroll > 0) {{
      const xOffset = progress * maxTrackScroll;
      workTrack.style.transform = `translateX(-${{xOffset}}px)`;
    }}

    // Card 3D scale and tilt effect (center card is biggest)
    if (!isReducedMotion) {{
      const screenCenter = window.innerWidth / 2;
      projectCards.forEach(card => {{
        const cardRect = card.getBoundingClientRect();
        const cardCenter = cardRect.left + cardRect.width / 2;
        const distFromCenter = (cardCenter - screenCenter) / (window.innerWidth / 2);
        const clampedDist = Math.max(-1.5, Math.min(distFromCenter, 1.5));
        
        // Scale down slightly further from center (1.0 down to 0.91)
        const scale = 1 - Math.min(Math.abs(clampedDist) * 0.08, 0.09);
        // Tilt slightly (tilt up to 4 degrees)
        const tilt = clampedDist * 3.5;
        
        card.style.transform = `scale(${{scale}}) rotate(${{tilt}}deg)`;
      }});
    }}
  }}

  window.addEventListener('scroll', updateWorkScroll, {{ passive: true }});
  window.addEventListener('resize', updateWorkScroll);
  updateWorkScroll();

  /* --------------------------------------------------------------------------
     8. GLOBAL HEADER & WHATSAPP BUTTON VISIBILITY
        (Hidden on intro, slide/pop in at ~70% scroll past intro)
     -------------------------------------------------------------------------- */
  const headerNav = document.getElementById('headerNav');
  const whatsappBtn = document.getElementById('whatsappBtn');
  const introSection = document.getElementById('intro');

  function updateGlobalVisibility() {{
    const introH = introSection ? introSection.offsetHeight : 600;
    const pastIntro = window.scrollY > introH * 0.7;
    
    if (headerNav) {{
      headerNav.classList.toggle('hidden', !pastIntro);
    }}
    if (whatsappBtn) {{
      whatsappBtn.classList.toggle('hidden', !pastIntro);
    }}

    // Parallax on intro big words
    if (introSection && !isReducedMotion && window.scrollY < introH) {{
      const wordsBox = document.getElementById('introWords');
      if (wordsBox) {{
        wordsBox.style.transform = `translateY(${{window.scrollY * 0.22}}px)`;
        wordsBox.style.opacity = `${{1 - (window.scrollY / introH) * 1.1}}`;
      }}
    }}
  }}

  window.addEventListener('scroll', updateGlobalVisibility, {{ passive: true }});
  updateGlobalVisibility();

  /* --------------------------------------------------------------------------
     9. MAGNETIC BUTTONS (DESKTOP)
     -------------------------------------------------------------------------- */
  if (window.matchMedia('(hover: hover) and (pointer: fine)').matches && !isReducedMotion) {{
    const magneticBtns = document.querySelectorAll('.magnetic-btn');
    magneticBtns.forEach(btn => {{
      btn.addEventListener('mousemove', (e) => {{
        const rect = btn.getBoundingClientRect();
        const x = e.clientX - (rect.left + rect.width / 2);
        const y = e.clientY - (rect.top + rect.height / 2);
        btn.style.transform = `translate(${{x * 0.22}}px, ${{y * 0.22}}px)`;
      }});
      btn.addEventListener('mouseleave', () => {{
        btn.style.transform = 'translate(0px, 0px)';
      }});
    }});
  }}

  /* --------------------------------------------------------------------------
     10. BACK TO TOP BUTTON
     -------------------------------------------------------------------------- */
  const backToTop = document.getElementById('backToTop');
  if (backToTop) {{
    backToTop.addEventListener('click', (e) => {{
      e.preventDefault();
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }});
  }}

}})();
</script>

</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Successfully generated index.html (size: {len(html_content):,} bytes)")
