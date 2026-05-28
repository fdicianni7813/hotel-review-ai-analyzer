import pandas as pd
import random

random.seed(69)

def vary_length(text):
    sentences = text.split('.')
    
    if random.random() < 0.3 and len(sentences) > 2:
        return '. '.join(sentences[:2]) + '.'
    
    if random.random() < 0.6:
        return text + ". " + random.choice([
            "Prezzo nella media",
            "Struttura ben tenuta",
            "Servizio migliorabile"
        ])
    
    return text


def add_contrast(sentiment, pos_list, neg_list):
    # ridotto e più realistico
    if random.random() < 0.15:
        if sentiment == "positivo":
            return random.choice(neg_list)
        else:
            return random.choice(pos_list)
    return None


user_styles = {
    "formale": lambda t: f"{t}.", 
    "breve": lambda t: ' '.join(t.split()[:8]),
    "lamentoso": lambda t: t,
    "neutro": lambda t: t
}

synonyms = {
    "pulita": ["pulita", "in ordine", "ben sistemata", "curata"],
    "sporco": ["sporco", "poco pulito", "trascurato"],
    "gentile": ["gentile", "cordiale", "disponibile"],
    "lento": ["lento", "un po' lungo", "troppo lento"],
    "ottimo": ["ottimo", "molto buono", "eccellente"],
    "scarso": ["scarso", "deludente", "insufficiente"]
}

def replace_synonyms(text):
    for key, values in synonyms.items():
        if key in text:
            text = text.replace(key, random.choice(values))
    return text

housekeeping_pos = [
    "La camera era molto pulita",
    "Stanza ordinata e ben sistemata",
    "Pulizia impeccabile",
    "Il bagno era perfettamente pulito",
    "Lenzuola fresche e cambiate ogni giorno",
    "La stanza veniva pulita puntualmente",
    "Ambiente curato e profumato",
    "Tutto era in ordine all'arrivo",
    "Asciugamani puliti e cambiati regolarmente",
    "La pulizia della stanza era eccellente"
]

housekeeping_neg = [
    "La stanza era sporca",
    "Pulizia insufficiente",
    "Ho trovato capelli nel bagno",
    "Il pavimento non era stato lavato",
    "Stanza non pulita al momento del check-in",
    "Polvere ovunque nella stanza, improponibile",
    "Il bagno aveva aloni e macchie",
    "Le lenzuola non erano state cambiate, che schifo",
    "Cattivo odore nella stanza",
    "La pulizia lasciava molto a desiderare...",
    "Camera davvero trascurata",
    "Pulizia pessima e stanza disordinata",
    "Bagno sporco e poco igienico"
]

housekeeping_short_pos = [
    "bagno pulito",
    "tutto ok",
    "stanza perfetta"
]

housekeeping_short_neg = [
    "camera sporca",
    "odore terribile",
    "lenzuola sporche"
]

reception_pos = [
    "Check-in veloce e personale gentile",
    "Reception molto disponibile",
    "Servizio accoglienza eccellente",
    "Il personale ci ha accolti calorosamente",
    "Check-out rapido e senza problemi, receptionist molto simpatico",
    "Staff sempre pronto ad aiutare",
    "Personale cordiale e professionale",
    "Risposta rapida a ogni richiesta",
    "Il receptionist ci ha dato ottime indicazioni",
    "Nessun problema con prenotazione e pagamento"
]

reception_neg = [
    "Attesa lunga al check-in",
    "Personale scortese alla reception",
    "Problemi con il pagamento",
    "Nessuno alla reception all'arrivo",
    "Check-in caotico e disorganizzato",
    "Il personale era poco disponibile",
    "Errore nella prenotazione non risolto",
    "Tempi di attesa eccessivi",
    "Staff poco professionale",
    "Risposta lenta alle richieste",
    "Personale maleducato e arrogante",
    "Receptionist molto indisponente",
    "Staff poco educato",
    "Comportamento davvero scortese"
]

reception_short_pos = [
    "staff gentile",
    "tutto rapido",
    "pagamento ok"
]

reception_short_neg = [
    "checkin lentissimo",
    "attesa infinita",
    "reception pessima",
    "personale scostumato"
]

fb_pos = [
    "Colazione abbondante e varia, fantasici i pancakes",
    "Cibo ottimo e ben servito",
    "Ristorante di alta qualità",
    "Buffet ricco e sempre rifornito",
    "Pietanze fresche e ben preparate",
    "Il menu era vario e gustoso",
    "Ottima scelta di dolci a colazione",
    "Il ristorante aveva un'ottima atmosfera",
    "Porzioni abbondanti e prezzi onesti",
    "Personale del ristorante attento e veloce"
]

fb_neg = [
    "Colazione scarsa",
    "Cibo freddo e di bassa qualità",
    "Servizio lento al ristorante",
    "Poca scelta al buffet",
    "Cibo scadente e mal presentato",
    "Il ristorante era sempre sovraffollato",
    "Tempi di attesa troppo lunghi per ordinare",
    "Pietanze fredde e poco fresche",
    "Menu limitato e ripetitivo",
    "Il personale del ristorante era disattento",
    "Cibo davvero mediocre",
    "Esperienza deludente al ristorante",
    "Piatti arrivati freddi e in ritardo"
]

fb_short_pos = [
    "colazione top",
    "buffet ottimo"
]

fb_short_neg = [
    "cibo pessimo",
    "ristorante pienissimo",
    "servizio lento",
    "mai più"
]

dept_titles_pos = {
    "Housekeeping": ["Camera impeccabile", "Pulizia ottima", "Stanza curata"],
    "Reception": ["Accoglienza eccellente", "Staff fantastico", "Check-in perfetto"],
    "F&B": ["Colazione ottima", "Ristorante consigliato", "Cibo eccellente"]
}

dept_titles_neg = {
    "Housekeeping": ["Pulizia insufficiente", "Stanza trascurata", "Camera deludente"],
    "Reception": ["Accoglienza pessima", "Staff scortese", "Check-in caotico"],
    "F&B": ["Colazione deludente", "Cibo scadente", "Ristorante da evitare"]
}

neg_to_department = {
    phrase: "Housekeeping" for phrase in housekeeping_neg
}
neg_to_department.update({
    phrase: "Reception" for phrase in reception_neg
})
neg_to_department.update({
    phrase: "F&B" for phrase in fb_neg
})

pos_to_department = {
    phrase: "Housekeeping" for phrase in housekeeping_pos
}
pos_to_department.update({
    phrase: "Reception" for phrase in reception_pos
})
pos_to_department.update({
    phrase: "F&B" for phrase in fb_pos
})

intro_pos = [
    "Nel complesso il soggiorno è stato molto piacevole",
    "Ho trascorso un ottimo soggiorno",
    "Esperienza generalmente positiva"
]

intro_neg = [
    "Purtroppo l'esperienza non è stata all'altezza",
    "Soggiorno deludente",
    "Mi aspettavo molto di più"
]

closing = [
    "Tornerei volentieri",
    "Non credo tornerò",
    "Consigliato",
    "Da migliorare",
    ""
]

extra_details = [
    "per una notte",
    "per lavoro",
    "nel weekend",
    "in alta stagione",
    "con la mia famiglia",
    "durante un viaggio veloce",
    ""
]

def add_detail(text):
    if random.random() < 0.4:
        detail = random.choice(extra_details)
        if detail:
            return f"{text} ({detail})"
    return text

data = []
id_counter = 1

def lower_safe(text):
    return text[0].lower() + text[1:] if len(text) > 1 else text

def build_review(base_sentence, sentiment, pos_list, neg_list):

    intro = random.choice(intro_pos if sentiment == "positivo" else intro_neg)

    main = base_sentence
    if main.endswith(("che", "di", "con", "per")):
        main += " ..."

    contrast = None
    if random.random() < 0.15:
        all_pos = housekeeping_pos + reception_pos + fb_pos
        all_neg = housekeeping_neg + reception_neg + fb_neg
        other_pos = [p for p in all_pos if p not in pos_list]
        other_neg = [n for n in all_neg if n not in neg_list]
        if sentiment == "positivo" and other_neg:
            contrast = random.choice(other_neg)
        elif sentiment == "negativo" and other_pos:
            contrast = random.choice(other_pos)
        # COSTRUZIONE FRASE
    parts = []

    if random.random() < 0.7:
        parts.append(intro)

    parts.append(main)

    if contrast:
        connector = random.choice(["Tuttavia", "Però", "Nonostante ciò"])
        parts.append(f"{connector}, {lower_safe(contrast)}")

    if random.random() < 0.5:
        if sentiment == "positivo":
            closing_choice = random.choice(["Tornerei volentieri", "Consigliato"])
        else:
            closing_choice = random.choice(["Non credo tornerò", "Da migliorare"])
        parts.append(closing_choice)

    body = ". ".join(parts)

    body = body.strip()

    if not body.endswith((".", "!", "...")):
        body += "."

    body = add_detail(body)
    body = vary_length(body)
    body = replace_synonyms(body)

    return normalize_text(body)

def normalize_text(text):
    text = text.replace("  ", " ")
    text = text.strip()
    return text

def fix_truncated(text):
    endings = ["che", "di", "con", "per", "in particolare", "devo dire che"]
    
    for e in endings:
        if text.lower().endswith(e):
            return text + " ..."
    
    return text
    

def build_title(base_sentence, sentiment, department=""): 
    titles_generic_pos = [
        "Ottimo soggiorno",
        "Tutto perfetto",
        "Molto soddisfatto",
        "Esperienza positiva"
    ]

    titles_generic_neg = [
        "Deludente",
        "Non ci siamo",
        "Esperienza negativa",
        "Sconsigliato"
    ]

    titles_specific = [
        random.choice(dept_titles_pos.get(department, ["Esperienza positiva"]) if sentiment == "positivo" else dept_titles_neg.get(department, ["Esperienza negativa"])),
        "Problemi con il servizio" if sentiment == "negativo" else "Servizio eccellente",
        "Esperienza con il servizio",
        f"{'Buona' if sentiment == 'positivo' else random.choice(['Pessima', 'Così così'])} esperienza",
        f"{' '.join(base_sentence.split()[:3])} da rivedere" if sentiment == "negativo" else random.choice(dept_titles_pos.get(department, ["Esperienza positiva"]))
    ]   

    if random.random() < 0.2:
        if sentiment == "positivo":
            return random.choice(["Non male", "Esperienza ok", "Top!"])
        else:
            return random.choice(["Meh", "Ci aspettavamo di più", "Esperienza ok"])

    # scegli tipo di titolo
    choice = random.choice(["generic", "specific"])

    if choice == "generic":
        if sentiment == "positivo":
            return random.choice(titles_generic_pos)
        else:
            return random.choice(titles_generic_neg)
    else:
        return random.choice(titles_specific)

def generate_reviews(sentences, department, sentiment, pos_list, neg_list):
    global id_counter
    for sentence in sentences:
        data.append({
            "id": id_counter,
            "title": build_title(sentence, sentiment, department),
            "body": build_review(sentence, sentiment, pos_list, neg_list),
            "department": department,
            "sentiment": sentiment
        })
        id_counter += 1

def generate_random_reviews(sentences, department, sentiment, n=20):
    global id_counter
    for _ in range(n):
        sentence = random.choice(sentences)

        body = build_review(sentence, sentiment, housekeeping_pos if department == "Housekeeping" else reception_pos if department == "Reception" else fb_pos, housekeeping_neg if department == "Housekeeping" else reception_neg if department == "Reception" else fb_neg)
        title = build_title(sentence, sentiment, department)

        data.append({
            "id": id_counter,
            "title": title,
            "body": body,
            "department": department,
            "sentiment": sentiment
        })
        id_counter += 1        

def generate_mixed_reviews(n=30):
    global id_counter

    departments = {
        "Housekeeping": (housekeeping_pos, housekeeping_neg),
        "Reception": (reception_pos, reception_neg),
        "F&B": (fb_pos, fb_neg)
    }

    for _ in range(n):

        pos_department = random.choice(list(departments.keys()))

        neg_department = random.choice(
            [d for d in departments.keys() if d != pos_department]
        )

        pos = random.choice(departments[pos_department][0])

        neg = random.choice(departments[neg_department][1])

        text = f"{pos}, però {lower_safe(neg)}"

        body = build_review(
            text,
            "negativo",
            housekeeping_pos + reception_pos + fb_pos,
            housekeeping_neg + reception_neg + fb_neg
        )

        data.append({
            "id": id_counter,
            "title": build_title(text, "negativo"),
            "body": body,
            "department": neg_department,
            "sentiment": "negativo"
        })

        id_counter += 1

def generate_mixed_positive_reviews(n=20):
    global id_counter

    departments = {
        "Housekeeping": (housekeeping_pos, housekeeping_neg),
        "Reception": (reception_pos, reception_neg),
        "F&B": (fb_pos, fb_neg)
    }

    for _ in range(n):

        pos_department = random.choice(list(departments.keys()))

        neg_department = random.choice(
            [d for d in departments.keys() if d != pos_department]
        )

        pos = random.choice(departments[pos_department][0])

        neg = random.choice(departments[neg_department][1])

        text = f"{pos}, anche se {lower_safe(neg)}"

        body = build_review(
            text,
            "positivo",
            housekeeping_pos + reception_pos + fb_pos,
            housekeeping_neg + reception_neg + fb_neg
        )

        data.append({
            "id": id_counter,
            "title": build_title(text, "positivo", pos_department),
            "body": body,
            "department": pos_department,
            "sentiment": "positivo"
        })

        id_counter += 1

if __name__ == "__main__":
    generate_reviews(housekeeping_pos, "Housekeeping", "positivo", housekeeping_pos, housekeeping_neg)
    generate_reviews(housekeeping_neg, "Housekeeping", "negativo", housekeeping_pos, housekeeping_neg)

    generate_reviews(reception_pos, "Reception", "positivo", reception_pos, reception_neg)
    generate_reviews(reception_neg, "Reception", "negativo", reception_pos, reception_neg)

    generate_reviews(fb_pos, "F&B", "positivo", fb_pos, fb_neg)
    generate_reviews(fb_neg, "F&B", "negativo", fb_pos, fb_neg)

    generate_random_reviews(housekeeping_pos, "Housekeeping", "positivo", 30)
    generate_random_reviews(housekeeping_neg, "Housekeeping", "negativo", 30)

    generate_random_reviews(reception_pos, "Reception", "positivo", 30)
    generate_random_reviews(reception_neg, "Reception", "negativo", 30)

    generate_random_reviews(fb_pos, "F&B", "positivo", 30)
    generate_random_reviews(fb_neg, "F&B", "negativo", 30)

    generate_random_reviews(housekeeping_short_pos, "Housekeeping", "positivo", 10)
    generate_random_reviews(housekeeping_short_neg, "Housekeeping", "negativo", 10)

    generate_random_reviews(reception_short_pos, "Reception", "positivo", 10)
    generate_random_reviews(reception_short_neg, "Reception", "negativo", 10)

    generate_random_reviews(fb_short_pos, "F&B", "positivo", 10)
    generate_random_reviews(fb_short_neg, "F&B", "negativo", 10)
    
    generate_mixed_reviews(20)
    generate_mixed_positive_reviews(20)

    df = pd.DataFrame(data)

    import os

    os.makedirs("data/raw", exist_ok=True)
    df.to_csv("data/raw/reviews.csv", index=False)

    print(f"Dataset creato con {len(df)} recensioni")
    
    print("\nDistribuzione reparti:")
    print(df["department"].value_counts())

    print("\nDistribuzione sentiment:")
    print(df["sentiment"].value_counts())