# to loop through "rows" of label query from the database server and concatenating into html string
def loopString_label(rows,rowcount):

    rows_clean=[]
    for i in range(0,len(rows)):
        rows_list = list(rows[i])
        if rows_list[1]==None:
            rows_list[1]=''
        rows_tuple = tuple(rows_list)
        rows_clean.append(rows_tuple)

    loopString_label.html_string = """ """
    rows_clean.append(("","","","",))

    for i in range(0,len(rows_clean)-1):
        if rows_clean[i][0]==rows_clean[i-1][0]:
            loopString_label.html_string += str \
            (f"<tr id='title_5' style='background-color: None;'> \
            <td style='text-align:right'>{rows_clean[i][1]} {rows_clean[i][2]}</td> \
            <td style='text-align:left'> &#x229A; \
            </td><td>{rows_clean[i][3]}</td></tr>")
        else:
            loopString_label.html_string += str \
            (f"<tr><th id='labelHeader' colspan='3'>{rows_clean[i][0]}<td style='text-align:right'></th><tr> \
            <tr id='title_5' style='background-color: None'> \
            <td style='text-align:right'>{rows_clean[i][1]} {rows_clean[i][2]}</td> \
            <td style='text-align:left'> &#x229A; </td> \
            <td>{rows_clean[i][3]}</td></tr>")
            
    return loopString_label.html_string

# to loop through "rows" of titleWorkArtist query from the database server and concatenating into html string
def loopString_titleWorkArtist(rows):

    rows_clean=[]
    for i in range(0,len(rows)):
        rows_list = list(rows[i])
        if rows_list[2]==None:
            rows_list[2]=''
        if rows_list[10]==None:
            rows_list[10]='&#x2205'
        rows_tuple = tuple(rows_list)
        rows_clean.append(rows_tuple)

    loopString_titleWorkArtist.html_string=""" """
    rows_clean.append(("","","","","","","","","","",""))
    rows_clean.append(("","","","","","","","","","",""))
    rows_clean.append(("","","","","","","","","","",""))


    for i in range(0,len(rows)-1):
        if rows_clean[i][0]==rows_clean[i-1][0]:

            if rows_clean[i][7]==rows_clean[i-1][7]:
                loopString_titleWorkArtist.html_string += str(f"<p id='artist_4'>&#9659; { rows_clean[i][9] } \
                <span style='float:right'>{ rows_clean[i][10] }</span></p>")
            else: 
                loopString_titleWorkArtist.html_string += str(f"<p id='work_4'>&#x21D2; { rows_clean[i][6] } / \
                { rows_clean[i][7] } &nbsp &nbsp \
                <span style='float:right'>{ rows_clean[i][8] }</span></p> \
                \
                <p id='artist_4'>&#9659; { rows_clean[i][9] } &nbsp &nbsp \
                <span style='float:right'>{ rows_clean[i][10] }</span></p>")

        else:

            if rows_clean[i][11]:
                featureFilterTuple = rows_clean[i]
                featureFilter(featureFilterTuple)

                loopString_titleWorkArtist.html_string += str(f"<br><p id='title_4'><b>&#x229A; { rows_clean[i][0] }</b> &nbsp &nbsp \
                <span style='float:right'>{rows_clean[i][1] } \
                {rows_clean[i][2] } \
                {rows_clean[i][3] }, \
                {rows_clean[i][4] } \
                {rows_clean[i][5] }(s)</span></p> \
                <p id='notes' >Notes &#x21F0 <span style='float:right'>{featureFilter.string}</span></p> \
                \
                <p id='work_4'>&#x21D2; { rows_clean[i][6] } / \
                { rows_clean[i][7] } &nbsp &nbsp \
                <span style='float:right'>{ rows_clean[i][8] }</span></p> \
                \
                <p id='artist_4'>&#9659; { rows_clean[i][9] } &nbsp &nbsp \
                <span style='float:right'>{ rows_clean[i][10] }</span></p>")

            else:

                loopString_titleWorkArtist.html_string += str(f"<br><p id='title_4'><b>&#x229A; { rows_clean[i][0] }</b> &nbsp &nbsp \
                <span style='float:right'>{rows_clean[i][1] } \
                {rows_clean[i][2] } \
                {rows_clean[i][3] }, \
                {rows_clean[i][4] } \
                {rows_clean[i][5] }(s)</span></p> \
                \
                <p id='work_4'>&#x21D2; { rows_clean[i][6] } / \
                { rows_clean[i][7] } &nbsp &nbsp \
                <span style='float:right'>{ rows_clean[i][8] }</span></p> \
                \
                <p id='artist_4'>&#9659; { rows_clean[i][9] } &nbsp &nbsp \
                <span style='float:right'>{ rows_clean[i][10] }</span></p>")

    return loopString_titleWorkArtist.html_string

# to loop through "rows" of artistWorkTitle query from the database server and concatenating into html string
def loopString_artistWorkTitle(rows):

    rows_clean=[]
    for i in range(0,len(rows)):
        rows_list = list(rows[i])
        if rows_list[1]==None:
            rows_list[1]='&#x2205'
        if rows_list[8]==None:
            rows_list[8]=''
        rows_tuple = tuple(rows_list)
        rows_clean.append(rows_tuple)

    loopString_artistWorkTitle.html_string = """ """
    rows_clean.append(("","","","","","","","","","","",""))

    for i in range(0,len(rows_clean)-1):
        if rows_clean[i][0]==rows_clean[i-1][0]:

            if rows_clean[i][3]==rows_clean[i-1][3]:
                loopString_artistWorkTitle.html_string += str(f"<p id='title'>&#x229A; { rows_clean[i][6] } &nbsp &nbsp \
                <span style='float:right'>{ rows_clean[i][7] } \
                { rows_clean[i][8] } \
                { rows_clean[i][9] }, \
                { rows_clean[i][10] } \
                { rows_clean[i][11] }(s)</span></p>")
                
            else:
                loopString_artistWorkTitle.html_string += str(f"<p id='work'>&#x21D2; { rows_clean[i][2] } / \
                { rows_clean[i][3] } &nbsp &nbsp \
                <span style='float:right'>{ rows_clean[i][5] }</span></p> \
                \
                <p id='title'>&#x229A; { rows_clean[i][6] } &nbsp &nbsp \
                <span style='float:right'>{ rows_clean[i][7] } \
                { rows_clean[i][8] } \
                { rows_clean[i][9] }, \
                { rows_clean[i][10] } \
                { rows_clean[i][11] }(s)</span></p>")
                
        else:
            loopString_artistWorkTitle.html_string += str(f"<br><p id='artist_3'><b>{ rows_clean[i][0] }</b> &nbsp &nbsp \
            <span style='float:right'>{rows_clean[i][1] }</span><p><hr> \
            \
            <p id='work'>&#x21D2; { rows_clean[i][2] } / \
            { rows_clean[i][3] } &nbsp &nbsp \
            <span style='float:right'>{ rows_clean[i][5] }</span></p> \
            \
            <p id='title'>&#x229A; { rows_clean[i][6] } &nbsp &nbsp \
            <span style='float:right'>{ rows_clean[i][7] } \
            { rows_clean[i][8] } \
            { rows_clean[i][9] }, \
            { rows_clean[i][10] } \
            { rows_clean[i][11] }(s)</span></p>")

    return loopString_artistWorkTitle.html_string

# to loop through "rows" of artistTitleWork query from the database server and concatenating into html string
def loopString_artistTitleWork(rows):
    id="artistTitleWork"
    rows_clean=[]
    for i in range(0,len(rows)):
        rows_list = list(rows[i])
        if rows_list[1]==None:
            rows_list[1]='&#x2205'
        if rows_list[4]==None:
            rows_list[4]=''
        rows_tuple = tuple(rows_list)
        rows_clean.append(rows_tuple)

    loopString_artistTitleWork.html_string=""" """
    rows_clean.append(("","","","","","","","","","","",""))

    for i in range(0,len(rows_clean)-1):

        if rows_clean[i][0]==rows_clean[i-1][0]:

            if rows_clean[i][2]==rows_clean[i-1][2]:
                loopString_artistTitleWork.html_string += str(f"<p id='work_3'>&#x21D2; { rows_clean[i][8] }  / \
                { rows_clean[i][9] } &nbsp &nbsp \
                <span style='float:right'>{ rows_clean[i][11] }</span></p>")

            else: 
                loopString_artistTitleWork.html_string += str(f"<p id='title_3'>&#x229A; { rows_clean[i][2] } &nbsp &nbsp\
                <span style='float:right'> { rows_clean[i][3] } \
                { rows_clean[i][4] } \
                { rows_clean[i][5] }, \
                { rows_clean[i][6] } \
                { rows_clean[i][7] }(s)</span></p> \
                \
                <p id='work_3'>&#x21D2; { rows_clean[i][8] }  / \
                { rows_clean[i][9] } &nbsp &nbsp \
                <span style='float:right'>{ rows_clean[i][11] }</span></p>")

        else:
            loopString_artistTitleWork.html_string += str(f"<br><p id='artist_3'><b>{ rows_clean[i][0] }</b> \
            <span style='float:right'>{rows_clean[i][1] }</span><p><hr>")

            loopString_artistTitleWork.html_string += str(f"<p id='title_3'>&#x229A; { rows_clean[i][2] } &nbsp &nbsp  \
            <span style='float:right'> { rows_clean[i][3] } \
            { rows_clean[i][4] } \
            { rows_clean[i][5] }, \
            { rows_clean[i][6] } \
            { rows_clean[i][7] }(s)</span></p> \
            \
            <p id='work_3'>&#x21D2; { rows_clean[i][8] }  / \
            { rows_clean[i][9] } &nbsp &nbsp \
            <span style='float:right'>{ rows_clean[i][11] }</span></p>")

    return loopString_artistTitleWork.html_string

# to loop through "rows" of composerWorkTitle query from the database server and concatenating into html string
def loopString_composerWorkTitle(rows):
    rows_clean=[]
    for i in range(0,len(rows)):
        rows_list = list(rows[i])
        if rows_list[1]==None:
            rows_list[1]='&#x2205'
        if rows_list[2]==None:
            rows_list[2]='&#x2205'
        if rows_list[8]==None:
            rows_list[8]=''
        if rows_list[14]==None:
            rows_list[14]='&#x2205'
        rows_tuple = tuple(rows_list)
        rows_clean.append(rows_tuple)

    loopString_composerWorkTitle.html_string=""" """
    rows_clean.append(("","","","","","","","","","","","","","",""))

    for i in range(0,len(rows_clean)-1):

        if rows_clean[i][0]==rows_clean[i-1][0]:

            if rows_clean[i][3]==rows_clean[i-1][3]:

                if rows_clean[i][12]==rows_clean[i-1][12]:
                    loopString_composerWorkTitle.html_string += str(f"<p id='artist'>&#9659; { rows_clean[i][13] } &nbsp &nbsp \
                    <span style='float:right'> { rows_clean[i][14] }</span></p>")

                else:
                    loopString_composerWorkTitle.html_string += str(f"<p id='title'>&#x229A; { rows_clean[i][6] }</b> &nbsp &nbsp \
                    <span style='float:right'> { rows_clean[i][7] } \
                    { rows_clean[i][8] } \
                    { rows_clean[i][9] }, \
                    { rows_clean[i][10] } \
                    { rows_clean[i][11] }(s)</span>")

                    loopString_composerWorkTitle.html_string += str(f"<p id='artist'>&#9659; { rows_clean[i][13] } &nbsp &nbsp \
                    <span style='float:right'> { rows_clean[i][14] }</span></p>")

            else: 
                loopString_composerWorkTitle.html_string += str(f"<p id='work'>&#x21D2; { rows_clean[i][3] } &nbsp &nbsp \
                <span style='float:right'> { rows_clean[i][5] }</span></p> \
                \
                <p id='title'>&#x229A; { rows_clean[i][6] }</b> &nbsp &nbsp \
                <span style='float:right'> { rows_clean[i][7] } \
                { rows_clean[i][8] } \
                { rows_clean[i][9] }, \
                { rows_clean[i][10] } \
                { rows_clean[i][11] }(s)</span>")

                loopString_composerWorkTitle.html_string += str(f"<p id='artist'>&#9659; { rows_clean[i][13] } &nbsp &nbsp \
                <span style='float:right'> { rows_clean[i][14] }</span></p>")

        else:
            loopString_composerWorkTitle.html_string += str(f"<p style='padding-top:12px;'><b>{ rows_clean[i][0] } </b> &nbsp &nbsp \
            <span  style='float:right;'>{rows_clean[i][1] }, \
            { rows_clean[i][2] }</span></p><hr> \
            \
            <p id='work'>&#x21D2; { rows_clean[i][3] } &nbsp &nbsp \
            <span style='float:right'> { rows_clean[i][5] }</span></p> \
            \
            <p id='title'>&#x229A; { rows_clean[i][6] }</b> &nbsp &nbsp \
            <span style='float:right'> { rows_clean[i][7] } \
            { rows_clean[i][8] } \
            { rows_clean[i][9] }, \
            { rows_clean[i][10] } \
            { rows_clean[i][11] }(s)</span> \
            \
            <p id='artist'>&#9659; { rows_clean[i][13] } &nbsp &nbsp \
            <span style='float:right'> { rows_clean[i][14] }</span></p>")

    return loopString_composerWorkTitle.html_string

# to loop through "rows" of composerTitleWork query from the database server and concatenating into html string
def loopString_composerTitleWork(rows):

    rows_clean=[]
    for i in range(0,len(rows)):
        rows_list = list(rows[i])
        if rows_list[1]==None:
            rows_list[1]='&#x2205'
        if rows_list[2]==None:
            rows_list[2]='&#x2205'
        if rows_list[5]==None:
            rows_list[5]=''
        rows_tuple = tuple(rows_list)
        rows_clean.append(rows_tuple)

    loopString_composerTitleWork.html_string=""" """
    rows_clean.append(("","","","","","","","","","","","",""))

    for i in range(0,len(rows_clean)-1):

        if rows_clean[i][0]==rows_clean[i-1][0]:

            if rows_clean[i][9]==rows_clean[i-1][9]:
                loopString_composerTitleWork.html_string += str(f"<p id='work_2'>&#x21D2; { rows_clean[i][10] } &nbsp &nbsp \
                <span style='float:right'>{ rows_clean[i][12] }</span><p>")

            else: 
                loopString_composerTitleWork.html_string += str(f"<p id='title_2'>&#x229A; { rows_clean[i][3] } &nbsp &nbsp \
                <span style='float:right'>{ rows_clean[i][4] } \
                { rows_clean[i][5] } \
                { rows_clean[i][6] } , \
                { rows_clean[i][7] } \
                { rows_clean[i][8] }(s)</span></p> \
                \
                <p id='work_2'>&#x21D2; { rows_clean[i][10] } &nbsp &nbsp \
                <span style='float:right'>{ rows_clean[i][12] }</span><p>")

        else:
            loopString_composerTitleWork.html_string += str(f"<p style='padding-top:12px;'><b>{ rows_clean[i][0] }</b> &nbsp &nbsp \
            <span style='float:right'>{rows_clean[i][1] }, \
            {rows_clean[i][2] }</span><p><hr> \
            \
            <p id='title_2'>&#x229A; { rows_clean[i][3] } &nbsp &nbsp \
            <span style='float:right'>{ rows_clean[i][4] } \
            { rows_clean[i][5] } \
            { rows_clean[i][6] } , \
            { rows_clean[i][7] } \
            { rows_clean[i][8] }(s)</span></p> \
            \
            <p id='work_2'>&#x21D2; { rows_clean[i][10] } &nbsp &nbsp \
            <span style='float:right'>{ rows_clean[i][12] }</span><p>")

    return loopString_composerTitleWork.html_string

# breakout function to parse Features/Notes where applicable
def featureFilter(featureFilterTuple):
    featureFilter.list = []

    if featureFilterTuple[12] == True:
        featureFilter.list.append("gatefold")
    if featureFilterTuple[13] == True:
        featureFilter.list.append("pis")
    if featureFilterTuple[14] == True:
        featureFilter.list.append("insert")
    if featureFilterTuple[15] == True:
        featureFilter.list.append("digipak")
    if featureFilterTuple[16] == True:
        featureFilter.list.append("booklet")
    if featureFilterTuple[17] == True:
        featureFilter.list.append("label insert")
    if featureFilterTuple[18] == True:
        featureFilter.list.append("box")
    if featureFilterTuple[19] == True:
        featureFilter.list.append("sticker")
    if featureFilterTuple[20] == True:
        featureFilter.list.append("cutout")
    if featureFilterTuple[21] == True:
        featureFilter.list.append("stamp")
    if featureFilterTuple[22] == True:
        featureFilter.list.append("mono")
    if featureFilterTuple[23] == True:
        featureFilter.list.append("fake stereo")
    if featureFilterTuple[24] == True:
        featureFilter.list.append("quad")
    if featureFilterTuple[25] == True:
        featureFilter.list.append("cd slipcover")
    if featureFilterTuple[26]:
        featureFilter.list.append(featureFilterTuple[26])
        
    featureFilter.string = ''
    for j in range(0,len(featureFilter.list)):
        featureFilter.string +=f"&#x229B {featureFilter.list[j]} "
    return(featureFilter.string)


