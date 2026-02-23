# Church History Character Profiles 

import csv
from PIL import Image, ImageDraw, ImageFont
import os

# --- 1. SETUP PATHS ---
TEMPLATE_PATH = "card_background.png" 
OUTPUT_FOLDER = "Character_Cards"
CSV_FILE = "Character_Cards_Data.csv"

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

# macOS Font Paths
font_path_bold = "/Library/Fonts/Arial Bold.ttf"
font_path_reg = "/Library/Fonts/Arial.ttf"
font_path_italic = "/Library/Fonts/Arial Italic.ttf"

try:
    font_name = ImageFont.truetype(font_path_bold, 65)
    font_date = ImageFont.truetype(font_path_italic, 38)
    font_header = ImageFont.truetype(font_path_bold, 30) 
    font_label = ImageFont.truetype(font_path_bold, 28) 
    font_body = ImageFont.truetype(font_path_reg, 28)
    font_italic = ImageFont.truetype(font_path_italic, 30)
except OSError:
    font_name = font_date = font_header = font_label = font_body = font_italic = ImageFont.load_default()

# --- 2. HELPER FUNCTIONS ---

def get_pixel_wrapped_lines(text, font, first_line_width, later_lines_width):
    if not text: return []
    words = str(text).split(' ')
    lines = []
    current_line = []
    
    word_idx = 0
    while word_idx < len(words):
        test_line = ' '.join(current_line + [words[word_idx]])
        w = ImageDraw.Draw(Image.new('RGB', (1, 1))).textlength(test_line, font=font)
        if w <= first_line_width:
            current_line.append(words[word_idx])
            word_idx += 1
        else:
            break
    lines.append(' '.join(current_line))
    
    current_line = []
    for word in words[word_idx:]:
        test_line = ' '.join(current_line + [word])
        w = ImageDraw.Draw(Image.new('RGB', (1, 1))).textlength(test_line, font=font)
        if w <= later_lines_width:
            current_line.append(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
    if current_line: 
        lines.append(' '.join(current_line))
    return lines

def draw_centered_text(draw, text, y, font, fill, image_width):
    w = draw.textlength(text, font=font)
    x = (image_width - w) / 2
    draw.text((x, y), text, font=font, fill=fill)

# --- 3. CARD GENERATOR ---

def make_card(row):
    card = Image.open(TEMPLATE_PATH)
    card_w, card_h = card.size
    draw = ImageDraw.Draw(card)
    
    # --- A. HEADER SECTION (DYNAMIC SPACING) ---
    y_cursor = 180 
    
    # 1. Name
    name_lines = get_pixel_wrapped_lines(row['Name'], font_name, card_w - 450, card_w - 450)
    for line in name_lines:
        draw_centered_text(draw, line, y_cursor, font_name, (40, 40, 40), card_w)
        y_cursor += 75 # Every line of name adds 75px

    # 2. Date - NO LONGER HARDCODED
    # We add a small buffer (15px) after the name ends, then draw the date
    y_cursor += 15 
    date_val = f"{row['Date']} AD"
    draw_centered_text(draw, date_val, y_cursor, font_date, (100, 100, 100), card_w)
    y_cursor += 55

    # 3. Era | Location
    subtitle_text = f"{row['Era']} | {row['Location']}"
    sub_lines = get_pixel_wrapped_lines(subtitle_text, font_header, card_w - 450, card_w - 450)
    for line in sub_lines:
        draw_centered_text(draw, line, y_cursor, font_header, (139, 0, 0), card_w)
        y_cursor += 45

    # --- B. BODY SECTION ---
    # We start the body relative to where the header ended or at a fixed floor
    y_content = max(y_cursor + 40, 420) 
    SIDE_MARGIN = 160 
    MAX_TOTAL_WIDTH = card_w - (SIDE_MARGIN * 2)

    def draw_section(column_key, y, use_bullets=False):
        content = row.get(column_key, "")
        if not content or content.strip() == "": return y
        
        label = f"{column_key}: "
        label_w = draw.textlength(label, font=font_label)

        if not use_bullets:
            lines = get_pixel_wrapped_lines(content, font_body, MAX_TOTAL_WIDTH - label_w, MAX_TOTAL_WIDTH)
            for i, line in enumerate(lines):
                if i == 0:
                    draw.text((SIDE_MARGIN, y), label, font=font_label, fill=(60, 60, 60))
                    draw.text((SIDE_MARGIN + label_w, y), line, font=font_body, fill="black")
                else:
                    draw.text((SIDE_MARGIN, y), line, font=font_body, fill="black")
                y += 35
            return y + 10
        else:
            draw.text((SIDE_MARGIN, y), label, font=font_label, fill=(60, 60, 60))
            y += 35 
            items = [i.strip() for i in content.split(';') if i.strip()]
            for item in items:
                bullet = "• "
                bullet_w = draw.textlength(bullet, font=font_body)
                item_lines = get_pixel_wrapped_lines(item, font_body, MAX_TOTAL_WIDTH - bullet_w, MAX_TOTAL_WIDTH - bullet_w)
                for i, line in enumerate(item_lines):
                    if i == 0:
                        draw.text((SIDE_MARGIN + 10, y), bullet, font=font_body, fill=(100, 0, 0))
                        draw.text((SIDE_MARGIN + 10 + bullet_w, y), line, font=font_body, fill="black")
                    else:
                        draw.text((SIDE_MARGIN + 10 + bullet_w, y), line, font=font_body, fill="black")
                    y += 35
                y += 5
            return y + 15

    # Processing columns
    y_content = draw_section("Nickname", y_content, False)
    y_content = draw_section("Writings", y_content, False)
    y_content = draw_section("Context/Controversies", y_content, False)
    y_content = draw_section("Opponents", y_content, True)
    y_content = draw_section("Most Well Known For", y_content, True)
    y_content = draw_section("Strengths/Weaknesses", y_content, True)

    # --- C. BOTTOM-ANCHORED QUOTE ---
    if row['Quote']:
        quote_text = f"{row['Quote']}"
        quote_lines = get_pixel_wrapped_lines(quote_text, font_italic, MAX_TOTAL_WIDTH - 100, MAX_TOTAL_WIDTH - 100)
        line_height = 38
        total_quote_height = len(quote_lines) * line_height
        y_quote_start = card_h - total_quote_height - 200 
        
        if y_content > y_quote_start:
             y_quote_start = y_content + 40
        
        for line in quote_lines:
            draw_centered_text(draw, line, y_quote_start, font_italic, (80, 80, 80), card_w)
            y_quote_start += line_height

    # --- 4. SAVE ---
    clean_name = row['Name'].replace("/", "-")
    card.save(f"{OUTPUT_FOLDER}/{clean_name}.png")
    print(f"Generated: {clean_name}")

# --- 5. RUN ---
with open(CSV_FILE, mode='r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row.get('Name'):
            make_card(row)

print("\nDone! Headers are now relative and will move together.")
