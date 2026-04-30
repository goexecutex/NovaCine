<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>NovaCine — AI Cinematic Video Studio</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#080810;--bg2:#0f0f1a;--bg3:#13131f;
  --accent:#7c5cfc;--accent2:#c45cfc;--accent3:#5cb8fc;
  --text:#f0eeff;--muted:#8a86aa;--border:rgba(124,92,252,0.18);
  --card:rgba(255,255,255,0.04);
}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--text);font-family:'Segoe UI',system-ui,sans-serif;overflow-x:hidden}

/* NAV */
nav{position:fixed;top:0;left:0;right:0;z-index:100;padding:0 5%;height:64px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid var(--border);backdrop-filter:blur(20px);background:rgba(8,8,16,0.7)}
.logo{font-size:1.3rem;font-weight:700;background:linear-gradient(90deg,var(--accent),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.nav-links{display:flex;gap:2rem;list-style:none}
.nav-links a{color:var(--muted);text-decoration:none;font-size:.9rem;transition:color .2s}
.nav-links a:hover{color:var(--text)}
.nav-cta{background:linear-gradient(135deg,var(--accent),var(--accent2));border:none;padding:.5rem 1.25rem;border-radius:8px;color:#fff;font-size:.9rem;font-weight:600;cursor:pointer;transition:opacity .2s}
.nav-cta:hover{opacity:.85}

/* HERO */
.hero{min-height:100vh;display:flex;align-items:center;justify-content:center;text-align:center;padding:100px 5% 60px;position:relative;overflow:hidden}
.hero-bg{position:absolute;inset:0;background:radial-gradient(ellipse 80% 60% at 50% 20%,rgba(124,92,252,.18) 0%,transparent 70%),radial-gradient(ellipse 50% 40% at 80% 80%,rgba(196,92,252,.1) 0%,transparent 60%);pointer-events:none}
.orb{position:absolute;border-radius:50%;filter:blur(80px);pointer-events:none}
.orb1{width:400px;height:400px;background:rgba(124,92,252,.12);top:-100px;left:-100px;animation:float 8s ease-in-out infinite}
.orb2{width:300px;height:300px;background:rgba(196,92,252,.1);bottom:0;right:-50px;animation:float 10s ease-in-out infinite reverse}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-30px)}}
.badge{display:inline-flex;align-items:center;gap:.5rem;background:rgba(124,92,252,.12);border:1px solid rgba(124,92,252,.3);border-radius:20px;padding:.35rem 1rem;font-size:.8rem;color:var(--accent);margin-bottom:1.5rem}
.badge-dot{width:6px;height:6px;border-radius:50%;background:var(--accent);animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.3}}
h1{font-size:clamp(2.4rem,6vw,4.5rem);font-weight:800;line-height:1.1;letter-spacing:-1px;margin-bottom:1.5rem}
h1 span{background:linear-gradient(90deg,var(--accent),var(--accent2),var(--accent3));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.hero p{font-size:1.15rem;color:var(--muted);max-width:600px;margin:0 auto 2.5rem;line-height:1.7}
.hero-btns{display:flex;gap:1rem;justify-content:center;flex-wrap:wrap}
.btn-primary{background:linear-gradient(135deg,var(--accent),var(--accent2));border:none;padding:.85rem 2.2rem;border-radius:10px;color:#fff;font-size:1rem;font-weight:600;cursor:pointer;transition:transform .2s,box-shadow .2s;box-shadow:0 0 30px rgba(124,92,252,.3)}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 0 50px rgba(124,92,252,.5)}
.btn-secondary{background:transparent;border:1px solid var(--border);padding:.85rem 2.2rem;border-radius:10px;color:var(--text);font-size:1rem;cursor:pointer;transition:border-color .2s,background .2s}
.btn-secondary:hover{border-color:var(--accent);background:rgba(124,92,252,.08)}
.hero-video{margin-top:4rem;border-radius:16px;border:1px solid var(--border);overflow:hidden;background:var(--bg3);position:relative;max-width:900px;margin-left:auto;margin-right:auto}
.video-mock{width:100%;aspect-ratio:16/9;background:linear-gradient(135deg,#0d0d1f,#1a1030,#0d0d1f);display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden}
.video-mock-bars{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:flex-end;gap:2px;padding:1rem}
.bar{height:4px;border-radius:4px;background:linear-gradient(90deg,var(--accent),var(--accent2));opacity:.3}
.play-btn{width:72px;height:72px;border-radius:50%;background:rgba(255,255,255,.1);backdrop-filter:blur(10px);border:2px solid rgba(255,255,255,.2);display:flex;align-items:center;justify-content:center;cursor:pointer;position:relative;z-index:1}
.play-btn::after{content:'';border-left:22px solid #fff;border-top:13px solid transparent;border-bottom:13px solid transparent;margin-left:5px}
.video-tag{position:absolute;top:1rem;left:1rem;background:rgba(124,92,252,.8);padding:.3rem .8rem;border-radius:6px;font-size:.75rem;font-weight:600}

/* STATS */
.stats{padding:3rem 5%;display:flex;justify-content:center;gap:4rem;flex-wrap:wrap;border-top:1px solid var(--border);border-bottom:1px solid var(--border);background:var(--bg2)}
.stat{text-align:center}
.stat-num{font-size:2rem;font-weight:800;background:linear-gradient(90deg,var(--accent),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.stat-label{font-size:.85rem;color:var(--muted);margin-top:.25rem}

/* SECTION COMMON */
section{padding:5rem 5%}
.section-tag{display:inline-block;background:rgba(124,92,252,.1);border:1px solid rgba(124,92,252,.25);color:var(--accent);font-size:.78rem;font-weight:600;padding:.3rem .9rem;border-radius:20px;margin-bottom:1rem;letter-spacing:.05em;text-transform:uppercase}
.section-title{font-size:clamp(1.8rem,4vw,2.8rem);font-weight:800;letter-spacing:-.5px;margin-bottom:1rem}
.section-sub{color:var(--muted);font-size:1rem;max-width:550px;line-height:1.7}

/* FEATURES */
.features{background:var(--bg2)}
.features-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:1.5rem;margin-top:3.5rem}
.feat-card{background:var(--card);border:1px solid var(--border);border-radius:16px;padding:2rem;transition:border-color .3s,transform .3s;cursor:default}
.feat-card:hover{border-color:rgba(124,92,252,.45);transform:translateY(-4px)}
.feat-icon{width:48px;height:48px;border-radius:12px;margin-bottom:1.25rem;display:flex;align-items:center;justify-content:center;font-size:1.4rem}
.feat-card h3{font-size:1.05rem;font-weight:700;margin-bottom:.65rem}
.feat-card p{font-size:.9rem;color:var(--muted);line-height:1.65}

/* MODELS */
.models-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:1rem;margin-top:3rem}
.model-pill{background:var(--bg3);border:1px solid var(--border);border-radius:12px;padding:1.25rem 1rem;text-align:center;transition:all .2s;cursor:default}
.model-pill:hover{background:rgba(124,92,252,.1);border-color:rgba(124,92,252,.4)}
.model-pill .name{font-size:.95rem;font-weight:600;margin-bottom:.3rem}
.model-pill .tag{font-size:.72rem;color:var(--muted);background:rgba(255,255,255,.05);padding:.2rem .6rem;border-radius:20px;display:inline-block}

/* TOOLS */
.tools{background:var(--bg2)}
.tools-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:1rem;margin-top:3rem}
.tool-item{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:1.25rem 1rem;text-align:center;font-size:.88rem;transition:all .2s;cursor:default}
.tool-item:hover{background:rgba(124,92,252,.08);border-color:rgba(124,92,252,.35);color:var(--accent)}
.tool-dot{width:8px;height:8px;border-radius:50%;margin:0 auto .75rem;background:linear-gradient(135deg,var(--accent),var(--accent2))}

/* STUDIOS */
.studios-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:2rem;margin-top:3.5rem}
.studio-card{border-radius:20px;padding:2.5rem;position:relative;overflow:hidden;border:1px solid var(--border)}
.studio-card.cinema{background:linear-gradient(135deg,rgba(124,92,252,.12),rgba(196,92,252,.08))}
.studio-card.marketing{background:linear-gradient(135deg,rgba(92,184,252,.1),rgba(124,92,252,.08))}
.studio-card h3{font-size:1.3rem;font-weight:700;margin-bottom:.75rem}
.studio-card p{font-size:.9rem;color:var(--muted);line-height:1.65;margin-bottom:1.5rem}
.studio-card ul{list-style:none;display:flex;flex-direction:column;gap:.5rem}
.studio-card ul li{font-size:.88rem;color:var(--muted);padding-left:1.25rem;position:relative}
.studio-card ul li::before{content:'✦';position:absolute;left:0;color:var(--accent);font-size:.6rem;top:3px}
.studio-badge{display:inline-block;background:rgba(124,92,252,.2);border:1px solid rgba(124,92,252,.3);padding:.3rem .8rem;border-radius:6px;font-size:.75rem;font-weight:600;color:var(--accent);margin-bottom:1rem}

/* PRICING */
.pricing{background:var(--bg2)}
.pricing-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1.5rem;margin-top:3.5rem;max-width:900px}
.price-card{background:var(--card);border:1px solid var(--border);border-radius:20px;padding:2rem}
.price-card.pro{border-color:rgba(124,92,252,.5);background:linear-gradient(160deg,rgba(124,92,252,.1),var(--card))}
.price-card .plan{font-size:.85rem;font-weight:600;color:var(--muted);margin-bottom:.75rem;text-transform:uppercase;letter-spacing:.08em}
.price-card .amount{font-size:2.5rem;font-weight:800;margin-bottom:.25rem}
.price-card .amount span{font-size:1rem;font-weight:400;color:var(--muted)}
.price-card .desc{font-size:.88rem;color:var(--muted);margin-bottom:1.5rem}
.price-card ul{list-style:none;margin-bottom:1.75rem;display:flex;flex-direction:column;gap:.6rem}
.price-card ul li{font-size:.88rem;display:flex;gap:.6rem;align-items:flex-start}
.price-card ul li::before{content:'✓';color:var(--accent);font-weight:700;flex-shrink:0}
.popular-tag{display:block;text-align:center;background:linear-gradient(90deg,var(--accent),var(--accent2));color:#fff;font-size:.75rem;font-weight:700;padding:.35rem;margin:-2rem -2rem 1.5rem;border-radius:18px 18px 0 0;letter-spacing:.05em}

/* CTA */
.cta-section{text-align:center;padding:6rem 5%;position:relative;overflow:hidden}
.cta-bg{position:absolute;inset:0;background:radial-gradient(ellipse 70% 60% at 50% 50%,rgba(124,92,252,.14) 0%,transparent 70%);pointer-events:none}
.cta-section h2{font-size:clamp(1.8rem,4vw,3rem);font-weight:800;margin-bottom:1.25rem}
.cta-section p{color:var(--muted);max-width:500px;margin:0 auto 2.5rem;line-height:1.7}

/* FOOTER */
footer{padding:3rem 5%;border-top:1px solid var(--border);display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1.5rem;background:var(--bg)}
.footer-links{display:flex;gap:1.5rem;flex-wrap:wrap}
.footer-links a{color:var(--muted);font-size:.85rem;text-decoration:none;transition:color .2s}
.footer-links a:hover{color:var(--text)}
.footer-copy{color:var(--muted);font-size:.82rem}

/* RESPONSIVE */
@media(max-width:640px){.nav-links{display:none}.stats{gap:2rem}.pricing-grid{max-width:100%}}
</style>
</head>
<body>

<nav>
  <div class="logo">NovaCine</div>
  <ul class="nav-links">
    <li><a href="#features">Features</a></li>
    <li><a href="#studios">Studios</a></li>
    <li><a href="#tools">Tools</a></li>
    <li><a href="#pricing">Pricing</a></li>
  </ul>
  <button class="nav-cta">Start Free</button>
</nav>

<!-- HERO -->
<section class="hero">
  <div class="hero-bg"></div>
  <div class="orb orb1"></div>
  <div class="orb orb2"></div>
  <div>
    <div class="badge"><span class="badge-dot"></span> Now with Seedance 2.0 · Kling 3.0 · Veo 3.1</div>
    <h1>Create <span>Cinematic AI Videos</span><br>Like a Hollywood Director</h1>
    <p>All the world's best AI video models in one creative workspace. Generate, direct, and publish stunning videos — from a single prompt.</p>
    <div class="hero-btns">
      <button class="btn-primary">Start Creating Free</button>
      <button class="btn-secondary">Watch Demo</button>
    </div>
    <div class="hero-video">
      <div class="video-mock">
        <div class="video-tag">Cinema Studio 3.5</div>
        <div class="play-btn"></div>
        <div class="video-mock-bars">
          <div class="bar" style="width:90%;opacity:.25"></div>
          <div class="bar" style="width:60%;opacity:.18"></div>
          <div class="bar" style="width:75%;opacity:.22"></div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- STATS -->
<div class="stats">
  <div class="stat"><div class="stat-num">20M+</div><div class="stat-label">Creators worldwide</div></div>
  <div class="stat"><div class="stat-num">50M+</div><div class="stat-label">Videos generated</div></div>
  <div class="stat"><div class="stat-num">5M</div><div class="stat-label">Videos per day</div></div>
  <div class="stat"><div class="stat-num">3B+</div><div class="stat-label">Social media reach</div></div>
</div>

<!-- FEATURES -->
<section class="features" id="features">
  <div class="section-tag">Features</div>
  <div class="section-title">Everything you need to<br>direct, generate &amp; publish</div>
  <div class="features-grid">
    <div class="feat-card">
      <div class="feat-icon" style="background:rgba(124,92,252,.15)">🎬</div>
      <h3>Multi-Model Workspace</h3>
      <p>Switch between Seedance, Kling, Veo, Sora, and Wan without leaving the platform. Compare outputs side by side.</p>
    </div>
    <div class="feat-card">
      <div class="feat-icon" style="background:rgba(196,92,252,.15)">🎥</div>
      <h3>Cinema Studio</h3>
      <p>1,296 virtual camera lenses, real optical physics, per-shot control, color grading, and multi-character consistency.</p>
    </div>
    <div class="feat-card">
      <div class="feat-icon" style="background:rgba(92,184,252,.15)">⚡</div>
      <h3>Click-to-Ad</h3>
      <p>Paste a product URL, get a social-first ad video in seconds. No brief, no photoshoot, no agency needed.</p>
    </div>
    <div class="feat-card">
      <div class="feat-icon" style="background:rgba(124,252,174,.15)">🧬</div>
      <h3>Soul ID — Character AI</h3>
      <p>Create a character from a reference image and keep it consistent across every shot, scene, and video you generate.</p>
    </div>
    <div class="feat-card">
      <div class="feat-icon" style="background:rgba(252,200,92,.15)">🖼️</div>
      <h3>Image-to-Video</h3>
      <p>Upload any static image and animate it with cinematic motion, depth of field, and professional camera moves.</p>
    </div>
    <div class="feat-card">
      <div class="feat-icon" style="background:rgba(252,92,92,.15)">📱</div>
      <h3>Social-First Export</h3>
      <p>Auto-format for TikTok, Reels, Shorts, and YouTube. Optimized aspect ratios, pacing, and hook timing built in.</p>
    </div>
  </div>
</section>

<!-- MODELS -->
<section style="padding:5rem 5%;background:var(--bg)">
  <div class="section-tag">AI Models</div>
  <div class="section-title">All top models.<br>One workspace.</div>
  <div class="section-sub">Pick the best engine for each project — speed, fidelity, dialogue, or multi-shot continuity.</div>
  <div class="models-grid">
    <div class="model-pill"><div class="name">Seedance 2.0</div><div class="tag">Best overall</div></div>
    <div class="model-pill"><div class="name">Kling 3.0</div><div class="tag">Lip-sync</div></div>
    <div class="model-pill"><div class="name">Veo 3.1</div><div class="tag">Realism</div></div>
    <div class="model-pill"><div class="name">Sora 2</div><div class="tag">Narrative</div></div>
    <div class="model-pill"><div class="name">Wan 2.7</div><div class="tag">Multi-shot</div></div>
    <div class="model-pill"><div class="name">MiniMax H02</div><div class="tag">Speed</div></div>
  </div>
</section>

<!-- STUDIOS -->
<section id="studios" style="padding:5rem 5%;background:var(--bg2)">
  <div class="section-tag">Studios</div>
  <div class="section-title">Two studios built for<br>every kind of creator</div>
  <div class="studios-grid">
    <div class="studio-card cinema">
      <div class="studio-badge">Cinema Studio 3.5</div>
      <h3>For Filmmakers &amp; Directors</h3>
      <p>Think in scenes and sequences. Real film terminology. Hollywood-grade output.</p>
      <ul>
        <li>AI Director with per-shot camera control</li>
        <li>1,296 virtual camera lenses &amp; focal lengths</li>
        <li>Character consistency across shots</li>
        <li>Collaborative editing timeline</li>
        <li>Color grading &amp; LUT presets</li>
      </ul>
    </div>
    <div class="studio-card marketing">
      <div class="studio-badge" style="background:rgba(92,184,252,.2);border-color:rgba(92,184,252,.3);color:var(--accent3)">Marketing Studio</div>
      <h3>For Brands &amp; Marketers</h3>
      <p>URL to ad in seconds. Scale campaigns without scaling your budget or team.</p>
      <ul>
        <li>Paste product URL → instant video ad</li>
        <li>Trend-matched visual presets</li>
        <li>Multi-format export (TikTok, Reels, YouTube)</li>
        <li>Batch generation for A/B testing</li>
        <li>Brand kit &amp; style locking</li>
      </ul>
    </div>
  </div>
</section>

<!-- TOOLS -->
<section class="tools" id="tools">
  <div class="section-tag">Creation Tools</div>
  <div class="section-title">50+ tools for every<br>creative use case</div>
  <div class="tools-grid">
    <div class="tool-item"><div class="tool-dot"></div>Text-to-Video</div>
    <div class="tool-item"><div class="tool-dot"></div>Image-to-Video</div>
    <div class="tool-item"><div class="tool-dot"></div>Motion Control</div>
    <div class="tool-item"><div class="tool-dot"></div>Face Swap</div>
    <div class="tool-item"><div class="tool-dot"></div>Outfit Swap</div>
    <div class="tool-item"><div class="tool-dot"></div>Background Remove</div>
    <div class="tool-item"><div class="tool-dot"></div>Video Upscale</div>
    <div class="tool-item"><div class="tool-dot"></div>Style Transfer</div>
    <div class="tool-item"><div class="tool-dot"></div>Lip Sync</div>
    <div class="tool-item"><div class="tool-dot"></div>Soul ID</div>
    <div class="tool-item"><div class="tool-dot"></div>AI Relight</div>
    <div class="tool-item"><div class="tool-dot"></div>Expand Image</div>
    <div class="tool-item"><div class="tool-dot"></div>Storyboards</div>
    <div class="tool-item"><div class="tool-dot"></div>Bullet Time</div>
    <div class="tool-item"><div class="tool-dot"></div>3D Render</div>
    <div class="tool-item"><div class="tool-dot"></div>Transitions</div>
  </div>
</section>

<!-- PRICING -->
<section class="pricing" id="pricing">
  <div class="section-tag">Pricing</div>
  <div class="section-title">Start free. Scale when ready.</div>
  <div class="pricing-grid">
    <div class="price-card">
      <div class="plan">Free</div>
      <div class="amount">$0 <span>/ month</span></div>
      <div class="desc">No credit card required. Create your first video in minutes.</div>
      <ul>
        <li>10 video generations / day</li>
        <li>720p HD export</li>
        <li>Access to 3 AI models</li>
        <li>Basic camera presets</li>
        <li>Commercial rights included</li>
      </ul>
      <button class="btn-secondary" style="width:100%;border-radius:10px;padding:.8rem">Get Started Free</button>
    </div>
    <div class="price-card pro">
      <span class="popular-tag">MOST POPULAR</span>
      <div class="plan">Pro</div>
      <div class="amount">$29 <span>/ month</span></div>
      <div class="desc">For creators who ship daily and need top quality at speed.</div>
      <ul>
        <li>Unlimited video generations</li>
        <li>4K Ultra HD export</li>
        <li>All 6 AI models unlocked</li>
        <li>Cinema Studio access</li>
        <li>Soul ID — character consistency</li>
        <li>Priority generation queue</li>
        <li>Marketing Studio + Click-to-Ad</li>
      </ul>
      <button class="btn-primary" style="width:100%;border-radius:10px">Start Pro Trial</button>
    </div>
    <div class="price-card">
      <div class="plan">Enterprise</div>
      <div class="amount">Custom</div>
      <div class="desc">For agencies, studios, and Fortune 500 teams.</div>
      <ul>
        <li>Everything in Pro</li>
        <li>Dedicated GPU capacity</li>
        <li>Custom model fine-tuning</li>
        <li>API access + webhooks</li>
        <li>SSO &amp; team management</li>
        <li>Dedicated account manager</li>
      </ul>
      <button class="btn-secondary" style="width:100%;border-radius:10px;padding:.8rem">Contact Sales</button>
    </div>
  </div>
</section>

<!-- CTA -->
<section class="cta-section">
  <div class="cta-bg"></div>
  <div class="section-tag">Get Started</div>
  <h2>Your first cinematic video<br>is one prompt away</h2>
  <p>Join 20 million creators already making Hollywood-grade content with NovaCine. Free forever. No credit card needed.</p>
  <button class="btn-primary" style="font-size:1.05rem;padding:1rem 2.8rem">Create Your First Video →</button>
</section>

<!-- FOOTER -->
<footer>
  <div class="logo">NovaCine</div>
  <div class="footer-links">
    <a href="#">Features</a>
    <a href="#">Pricing</a>
    <a href="#">Blog</a>
    <a href="#">Docs</a>
    <a href="#">Privacy</a>
    <a href="#">Terms</a>
  </div>
  <div class="footer-copy">© 2026 NovaCine Inc. All rights reserved.</div>
</footer>

</body>
</html>
