# Leer una cantidad de notas y clasificarlas por nivel de aprendizaje.


def classify_note(note):
   if note < 60:
      return "Aprendizaje inicial"
   if note < 70:
      return "Aprendizaje fundamental"
   if note < 90:
      return "Aprendizaje satisfactorio"
   return "Aprendizaje avanzado"


def classify_notes(notes):
   return [(note, classify_note(note)) for note in notes]
