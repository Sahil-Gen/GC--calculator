def gc_content(sequence):
    sequence = sequence.strip().upper()      # <-- important fix

    g = sequence.count("G")
    c = sequence.count("C")
    a = sequence.count("A")
    t = sequence.count("T")

    valid = g + c + a + t
    if valid == 0:
        return 0.0

    return round(((g + c) / valid) * 100, 2)

if __name__ == "__main__":
    seq = input("Enter DNA sequence: ").strip()
    print("GC Content:", gc_content(seq), "%")
