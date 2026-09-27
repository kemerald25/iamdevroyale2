import os, base64, io
from PIL import Image

IMAGE_PATHS = {
    'id_card': r"C:\Users\HomePC\.gemini\antigravity-ide\brain\d8bd6319-5f24-44cd-9b10-efa481822620\unity_id_card_1790523334891.jpg",
    'sofa': r"C:\Users\HomePC\.gemini\antigravity-ide\brain\d8bd6319-5f24-44cd-9b10-efa481822620\unity_sofa_photo_1790523363194.jpg",
    'workspace': r"C:\Users\HomePC\.gemini\antigravity-ide\brain\d8bd6319-5f24-44cd-9b10-efa481822620\unity_workspace_photo_1790523383359.jpg",
    'working': r"C:\Users\HomePC\.gemini\antigravity-ide\brain\d8bd6319-5f24-44cd-9b10-efa481822620\unity_working_photo_1790523413408.jpg",
    'swift_liaison': r"C:\Users\HomePC\.gemini\antigravity-ide\brain\d8bd6319-5f24-44cd-9b10-efa481822620\swift_liaison_ui_1790523440538.jpg",
    'tal3nt': r"C:\Users\HomePC\.gemini\antigravity-ide\brain\d8bd6319-5f24-44cd-9b10-efa481822620\tal3nt_app_ui_1790523470059.jpg",
    'chessonchain': r"C:\Users\HomePC\.gemini\antigravity-ide\brain\d8bd6319-5f24-44cd-9b10-efa481822620\chessonchain_app_ui_1790523497448.jpg",
    'triviabase': r"C:\Users\HomePC\.gemini\antigravity-ide\brain\d8bd6319-5f24-44cd-9b10-efa481822620\triviabase_app_ui_1790523530509.jpg",
    'verda': r"C:\Users\HomePC\.gemini\antigravity-ide\brain\d8bd6319-5f24-44cd-9b10-efa481822620\verda_real_estate_ui_1790523563456.jpg",
    'nexboard': r"C:\Users\HomePC\.gemini\antigravity-ide\brain\d8bd6319-5f24-44cd-9b10-efa481822620\nexboard_dashboard_ui_1790523602230.jpg"
}

MAX_WIDTHS = {
    'id_card': 720,
    'sofa': 640,
    'workspace': 640,
    'working': 720,
    'swift_liaison': 900,
    'tal3nt': 900,
    'chessonchain': 900,
    'triviabase': 900,
    'verda': 900,
    'nexboard': 900
}

b64_dict = {}

for key, path in IMAGE_PATHS.items():
    if not os.path.exists(path):
        print(f"Error: {path} not found")
        continue
    img = Image.open(path)
    # Convert RGBA or RGB
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    max_w = MAX_WIDTHS.get(key, 800)
    if img.width > max_w:
        ratio = max_w / float(img.width)
        new_h = int(img.height * ratio)
        img = img.resize((max_w, new_h), Image.Resampling.LANCZOS)
    
    out_buf = io.BytesIO()
    img.save(out_buf, format='WEBP', quality=82, method=6)
    webp_bytes = out_buf.getvalue()
    b64_str = base64.b64encode(webp_bytes).decode('ascii')
    data_uri = f"data:image/webp;base64,{b64_str}"
    b64_dict[key] = data_uri
    print(f"Key: {key}, size: {len(webp_bytes):,} bytes, b64 len: {len(b64_str):,}")

import json
with open('b64_images.json', 'w') as f:
    json.dump(b64_dict, f)
print("Saved b64_images.json successfully")
