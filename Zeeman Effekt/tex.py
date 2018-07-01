def get_table(head_list,columns):  #Input: 1. Liste der Spalten-Bez.
                                        # 2. Liste von Listen mit Spalteneinträgen
    num_col = len(head_list)
    num_row = len(columns[0])
    
    header = '{}'
    rows = '{}'
    tab = '{|c|'
    for i in range(1,num_col):
        header += ' & {}'
        rows += ' & {}'
        tab += 'c|'
    header += ' \\\ \hline\hline'
    rows += ' \\\ \hline'
    tab += '}'
    
    
    print('\\begin{table}[H]\n\\centering')
    print('\\begin{}{}\n\\hline'.format('{tabular}',tab))
    print(header.format(*head_list))
    for i in range(num_row):
        row = []
        for j in range(num_col):
            row.append(columns[j][i]) 
        print(rows.format(*row))
    print('\\hline\n\\end{tabular}\n\\caption{}\n\\label{}\n\\end{table}')