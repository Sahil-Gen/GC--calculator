def gc_content(sequence):
    sequence = sequence.strip().upper()

    g = sequence.count("G")
    c = sequence.count("C")
    a = sequence.count("A")
    t = sequence.count("T")

    valid = g + c + a + t

    if valid == 0:
        return 0.0

    return round(((g + c) / valid) * 100, 2)


def read_fasta(filename):
    sequences = {}
    header = None
    seq = []

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            # Skip empty lines
            if not line:
                continue

            # Header line
            if line.startswith(">"):
                if header:
                    sequences[header] = "".join(seq)

                header = line[1:]   # Remove ">"
                seq = []

            else:
                seq.append(line)

        # Save last sequence
        if header:
            sequences[header] = "".join(seq)

    return sequences


if __name__ == "__main__":

    filename = input("Enter FASTA file name: ")

    try:
        fasta_sequences = read_fasta(filename)

        for header, sequence in fasta_sequences.items():
            gc = gc_content(sequence)
            print(f"{header}")
            print(f"GC Content: {gc}%\n")

    except FileNotFoundError:
        print("Error: File not found. Check file name and path.")
