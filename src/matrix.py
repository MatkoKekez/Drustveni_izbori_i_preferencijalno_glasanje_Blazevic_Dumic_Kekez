import os

def save_matrix_txt(d, candidates, outfile, name=None, cell_width=4):
    """
    Spremi tablicu poravnatu kao u tvom primjeru (za čitanje u radu).
    """
    os.makedirs(os.path.dirname(outfile), exist_ok=True)

    header = " " * (cell_width + 1) + "".join(f"{c:>{cell_width}}" for c in candidates)
    lines = []
    if name:
        lines.append(name)
    lines.append(header)

    for i in candidates:
        row_vals = []
        for j in candidates:
            val = 0 if i == j else d.get((i, j), 0)
            row_vals.append(f"{val:>{cell_width}}")
        lines.append(f"{i:<{cell_width}} " + "".join(row_vals))

    with open(outfile, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
