import pandas as pd

# Create a list of dictionaries containing product information
data = [
    {"Category": "Brides & Bridesmaids", "Target Audience": "Bridesmaid", "Style": "Playful & Practical", "Product Name": "Bridesmaid Survival Kits", "Suggested Price": "$25-$40", "Keywords": "bridesmaid gifts, bachelorette party favors, emergency kit, wedding essentials", "SKU (Example Format)": "BRIDESMAID-SURVIVAL-KIT-001", "Product ID (Example Format)": "123456"},
    {"Category": "Brides & Bridesmaids", "Target Audience": "Bridesmaid", "Style": "Luxurious & Relaxing", "Product Name": "Silk Robe Squad", "Suggested Price": "$50-$75", "Keywords": "bridesmaid robes, silk robes, wedding party gifts, spa day essentials", "SKU (Example Format)": "BRIDESMAID-SILK-ROBE-001", "Product ID (Example Format)": "123457"},
    {"Category": "Brides & Bridesmaids", "Target Audience": "Bride", "Style": "Romantic & Delicate", "Product Name": "Enchanted Evening Clutch", "Suggested Price": "$35-$50", "Keywords": "bridal clutch, wedding accessories, evening bag, elegant purse", "SKU (Example Format)": "BRIDE-CLUTCH-ENCHANTED-001", "Product ID (Example Format)": "123458"},
    {"Category": "Brides & Bridesmaids", "Target Audience": "Bride", "Style": "Modern & Minimalist", "Product Name": "The Vow Cuff", "Suggested Price": "$20-$30", "Keywords": "bride jewelry, minimalist bracelet, wedding vow, vow renewal gift", "SKU (Example Format)": "BRIDE-CUFF-VOW-001", "Product ID (Example Format)": "123459"},
    {"Category": "Bachelorette Parties", "Target Audience": "Bachelorette Party", "Style": "Themed (Spa)", "Product Name": "Pampered & Perfect Robes", "Suggested Price": "$40-$60", "Keywords": "bachelorette party gifts, spa party favors, relaxation gifts, personalized robes (if applicable)", "SKU (Example Format)": "BACHELORETTE-ROBE-SPA-001", "Product ID (Example Format)": "123460"},
    # ... Add more data as needed ...
    {"Category": "General Products", "Target Audience": "General", "Style": "Funny & Conversation Starters", "Product Name": "That's What She Said Tumblers", "Suggested Price": "$18-$25", "Keywords": "funny tumblers, conversation starter gifts, pop culture gifts, meme gifts", "SKU (Example Format)": "GENERAL-TUMBLER-FUNNY-001", "Product ID (Example Format)": "123468"},
]

# Create a Pandas DataFrame from the data
df = pd.DataFrame(data)

# Print the DataFrame to the console
print(df.to_string())
