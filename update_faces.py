import os, base64, io, json
from PIL import Image

NEW_IMAGES = {
    'id_card': (r"C:\Users\HomePC\.gemini\antigravity-ide\brain\d8bd6319-5f24-44cd-9b10-efa481822620\devroyale_id_card_1790531385506.jpg", 720),
    'sofa': (r"C:\Users\HomePC\.gemini\antigravity-ide\brain\d8bd6319-5f24-44cd-9b10-efa481822620\devroyale_sofa_1790531421761.jpg", 640),
    'working': (r"C:\Users\HomePC\.gemini\antigravity-ide\brain\d8bd6319-5f24-44cd-9b10-efa481822620\devroyale_working_1790531649553.jpg", 720),
}

with open('b64_images.json', 'r', encoding='utf-8') as f:
    b64_dict = json.load(f)

with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

for key, (path, max_w) in NEW_IMAGES.items():
    if not os.path.exists(path):
        raise FileNotFoundError(f"Missing file: {path}")
    
    img = Image.open(path)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    if img.width > max_w:
        ratio = max_w / float(img.width)
        new_h = int(img.height * ratio)
        img = img.resize((max_w, new_h), Image.Resampling.LANCZOS)
    
    out_buf = io.BytesIO()
    img.save(out_buf, format='WEBP', quality=82, method=6)
    webp_bytes = out_buf.getvalue()
    b64_str = base64.b64encode(webp_bytes).decode('ascii')
    new_uri = f"data:image/webp;base64,{b64_str}"
    
    old_uri = b64_dict.get(key)
    if not old_uri:
        raise ValueError(f"Key {key} not found in b64_images.json")
    
    count = html_content.count(old_uri)
    print(f"Key '{key}': found {count} instances of old URI in index.html (size: {len(webp_bytes):,} bytes)")
    if count == 0:
        # maybe prefix matches? let's check
        old_prefix = old_uri[:40]
        pos = html_content.find(old_prefix)
        print(f"Old prefix check for '{key}': pos={pos}")
    else:
        html_content = html_content.replace(old_uri, new_uri)
    
    b64_dict[key] = new_uri

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

with open('b64_images.json', 'w', encoding='utf-8') as f:
    json.dump(b64_dict, f)

print("Updated index.html and b64_images.json successfully!")
