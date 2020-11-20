CHART_START = r'''\begin{table}[htp]
\centering
\begin{tabular}{|l|l|l|l|l|l|l|l|}
\hline
& \textbf{I} & \textbf{ii} & \textbf{iii} & \textbf{IV} & \textbf{V} & \textbf{vi} & \textbf{vii\textsuperscript{\circ}} \\ \hline'''
CHART_END = r'''\end{tabular}
\end{table}'''

# (note name, is sharped)
CHROMATIC_SCALE_NOTES = (('C'),
                         (r'C\textsuperscript{\sharp{}}'),
                         ('D'),
                         (r'D\textsuperscript{\sharp{}}'),
                         ('E'),
                         ('F'),
                         (r'F\textsuperscript{\sharp{}}'),
                         ('G'),
                         (r'G\textsuperscript{\sharp{}}'),
                         ('A'),
                         (r'A\textsuperscript{\sharp{}}'),
                         ('B'))
MAJOR_SCALE_STEPS = (0, 2, 4, 5, 7, 9, 11)
MAJOR_SCALE_MINORS = (False, True, True, False, False, True, False)


def major_scale_from_index(i):
    indexes = tuple((i + step) % 12 for step in MAJOR_SCALE_STEPS)
    without_minors = (CHROMATIC_SCALE_NOTES[index] for index in indexes)
    with_minors = tuple(x + ('m' if is_minor else '') for x, is_minor in zip(without_minors, MAJOR_SCALE_MINORS))
    return with_minors[:-1] + (with_minors[-1] + r'\textsuperscript{\circ}', )


def row_header_cell_text(note_text):
    return r'\textbf{' + note_text + '}'


def chord_cell_text(note_text):
    return '& {} '.format(note_text)


def row_text(chromatic_scale_index):
    root_note_text = CHROMATIC_SCALE_NOTES[chromatic_scale_index]
    return '{} {} \\\\ \\hline'.format(
            row_header_cell_text(root_note_text),
            ''.join(chord_cell_text(note_text) for note_text in major_scale_from_index(chromatic_scale_index))
        )


def print_rows():
    for i in range(len(CHROMATIC_SCALE_NOTES)):
        print(row_text(i))


def print_chart():
    print(CHART_START)
    print_rows()
    print(CHART_END)


def main():
    print_chart()


if __name__ == '__main__':
    main()
