# Dictionary containing events in Dortmund and their dates

events = {
    "DEW21 Museumsnacht": "19 September 2026",
    "Dortmunder U - Museumsnacht": "19 September 2026",
    "Museum Ostwall - Museumsnacht": "19 September 2026",
    "Kunsthalle Dortmund - Museumsnacht": "19 September 2026",
    "Museum für Kunst und Kulturgeschichte": "19 September 2026",
    "Museumsrallye durch den Adlerturm": "19 September 2026",
    "Dortmunder Kunstverein - Museumsnacht": "19 September 2026",
    "Polizeipräsidium Dortmund - Museumsnacht": "19 September 2026"
}

# Date of the Night of Museums
museumsnacht_date = "19 September 2026"

# List all events running during the Night of Museums
print("Events running during the Night of Museums in Dortmund:")
print()

for event, date in events.items():
    if date == museumsnacht_date:
        print(event, "->", date)
