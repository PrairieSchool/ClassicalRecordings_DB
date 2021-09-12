from flask import render_template
from app import app, queries, loopString
import psycopg2
from config import config


@app.route('/index', methods = ['post', 'get'])
def index():
    user = {'username': 'JT'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'something, something, weather'
        },
        {
            'author':{'username':'Mike'},
            'body':'something, something, contradiction'
        }
    ]
    return render_template('index.htm', title='Home', user=user, posts=posts)

@app.route('/')
@app.route('/index_2', methods = ['POST', 'GET'])
def get_index_2():
    conn = None
    user = {'username': 'JT'}
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(queries.sql_label)
        rows = cur.fetchall()
        labelCt = cur.rowcount
 
        cur.execute(queries.sql_titles)
        rows = cur.fetchall()
        titleCt = cur.rowcount
 
        cur.execute(queries.sql_artist)
        rows = cur.fetchall()
        artistCt = cur.rowcount
 
        cur.execute(queries.sql_composer)
        rows = cur.fetchall()
        composerCt = cur.rowcount
 
        cur.execute(queries.sql_works)
        rows = cur.fetchall()
        workCt = cur.rowcount
 
        cur.execute(queries.sql_recWork)
        rows = cur.fetchall()
        recWorkCt = cur.rowcount
 
        cur.execute(queries.sql_recWorkArtist)
        rows = cur.fetchall()
        recWorkArtistCt = cur.rowcount
 
        cur.execute(queries.sql_totalDiscCt)
        rows = cur.fetchall()
        rowsData = []
        rowsData = rows[0]
        totalDiscCt = rowsData[0]
 


        return render_template(
            'index_2.htm',
            title="Index",
 
            labelCt=labelCt, 
            titleCt=titleCt,
            artistCt=artistCt,
            composerCt=composerCt,
            workCt=workCt,
            recWorkCt=recWorkCt,
            recWorkArtistCt=recWorkArtistCt,
            totalDiscCt=totalDiscCt        
            )

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
if __name__ == '__main__':
    get_index_2()

@app.route('/labels', methods = ['POST', 'GET'])
def get_label():
    conn = None
    user = {'username': 'JT'}
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(queries.sql_label)
        rows = cur.fetchall()
        print("The number of labels: ", cur.rowcount)

        return render_template('labelTable.htm', title="Labels",user=user, rows=rows)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
if __name__ == '__main__':
    get_label()

@app.route('/titles', methods = ['POST', 'GET'])
def get_titles():
    conn = None
    user = {'username': 'JT'}
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(queries.sql_titles)
        rows = cur.fetchall()
        print("The number of Titles: ", cur.rowcount)
        # for row in rows:
        #     print(row)
        return render_template('titlesTable.htm', title="Records",user=user, rows=rows)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
if __name__ == '__main__':
    get_titles()

@app.route('/artists', methods = ['POST', 'GET'])
def get_artists_Q():
    conn = None
    user = {'username': 'JT'}
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(queries.sql_artistInstrument)
        rows = cur.fetchall()
        print("The number of Artists: ", cur.rowcount)
        # for row in rows:
        #     print(row)
        return render_template('artistTable.htm', title="Artists",user=user, rows=rows)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
if __name__ == '__main__':
    get_artists_Q()

@app.route('/composers', methods = ['POST', 'GET'])
def get_composers():
    conn = None
    user = {'username': 'JT'}
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(queries.sql_composer)
        rows = cur.fetchall()
        print("The number of Composers: ", cur.rowcount)
        # for row in rows:
        #     print(row)
        return render_template('composerTable.htm', title="Composers",user=user, rows=rows)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
if __name__ == '__main__':
    get_composers()

# Displays Works table
@app.route('/works', methods = ['POST', 'GET'])
def get_works():
    conn = None
    user = {'username': 'JT'}
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(queries.sql_works)
        rows = cur.fetchall()
        print("The number of works: ", cur.rowcount)
        # for row in rows:
        #     print(row)
        return render_template('worksTable.htm', title="works",user=user, rows=rows)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
if __name__ == '__main__':
    get_works()

@app.route('/manyToMany', methods = ['POST', 'GET'])
def get_manyToMany():
    conn = None
    user = {'username': 'JT'}
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(queries.sql_manyToMany)
        rows = cur.fetchall()
        print("The number of rows: ", cur.rowcount)
        return render_template('manyToManyTable.htm', title="manyToMany",user=user, rows=rows)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
if __name__ == '__main__':
    get_manyToMany()

# Displays Titles by Label query
@app.route('/labelTitle', methods = ['POST', 'GET'])
def get_LabelTitle():
    conn = None
    user = {'username': 'JT'}
    label="%%"
    limit = 100
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(queries.sql_labelTitles.format(label,limit))
        rows = cur.fetchall()
        rowcount = cur.rowcount

        loopString.loopString_label(rows,rowcount)

        return render_template('labelTitle.htm', title="labelTitle",user=user, html_string=loopString.loopString_label.html_string,rowcount=rowcount)

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    get_LabelTitle()

# Displays Titles w/ Works and Artitsts query
@app.route('/titleWorkArt', methods = ['POST', 'GET'])
def get_TitleWorkArt():
    conn = None
    user = {'username': 'JT'}
    limit=10000
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(queries.sql_titleWorkArtist.format(limit))
        rows = cur.fetchall()

        loopString.loopString_titleWorkArtist(rows)

        return render_template('concatString.htm', title="titleWorkArtist",user=user, html_string=loopString.loopString_titleWorkArtist.html_string)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
if __name__ == '__main__':
    get_TitleWorkArt()

#  Displays Artists by Works 
@app.route('/artistWorkTitle', methods = ['POST', 'GET'])
def get_ArtistWorkTitle():
    conn = None
    user = {'username': 'JT'}
    artist='%%'
    limit=100
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(queries.sql_artistWorkTitle.format(artist,limit))
        rows = cur.fetchall()

        loopString.loopString_artistWorkTitle(rows)

        return render_template('concatString.htm', title="artistWorkTitle",user=user, html_string=loopString.loopString_artistWorkTitle.html_string)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    get_ArtistWorkTitle()

# Displays Artists by Titles
@app.route('/artistTitleWork', methods = ['POST', 'GET'])
def get_ArtistTitleWork():
    conn = None
    user = {'username': 'JT'}
    artist='%%'
    limit=100
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(queries.sql_artistTitleWork.format(artist,limit))
        rows = cur.fetchall()
        
        loopString.loopString_artistTitleWork(rows)

        return render_template('concatString.htm', title="artistTitleWork",user=user, html_string=loopString.loopString_artistTitleWork.html_string)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    get_ArtistTitleWork()

# Displays Composers by Works
@app.route('/composerWorkTitle', methods = ['POST', 'GET'])
def get_ComposerWorkTitle():
    conn = None
    user = {'username': 'JT'}
    comp='%%'
    limit=100
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(queries.sql_composerWorkTitle.format(comp,limit))
        rows = cur.fetchall()

        loopString.loopString_composerWorkTitle(rows)
                
        return render_template('concatString.htm', title="composerWorkTitle",user=user, html_string=loopString.loopString_composerWorkTitle.html_string)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    get_ComposerWorkTitle()

# Displays Composers by Titles
@app.route('/composerTitleWork', methods = ['POST', 'GET'])
def get_ComposerTitle():
    conn = None
    user = {'username': 'JT'}
    comp='%%'
    limit=100
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(queries.sql_composerTitleWork.format(comp,limit))
        rows = cur.fetchall()

        loopString.loopString_composerTitleWork(rows)

        return render_template('concatString.htm', title="ComposerTitleWork",user=user, html_string=loopString.loopString_composerTitleWork.html_string)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    get_ComposerTitle()

#Displays Labels for filter (titles by label)
@app.route('/label_filter', methods = ['POST', 'GET'])
def get_label_filter():
    conn = None
    user = {'username': 'JT'}
    labelList=[]
    labelDict={"labelList":labelList}
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(queries.sql_label)
        rows = cur.fetchall()
        print("The number of labels: ", cur.rowcount)
        for i in range(0,len(rows)):
            labelList.append(rows[i][1])
        return render_template('labelFilter.htm', title="Labels",user=user, rows=rows,dict=labelDict)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
if __name__ == '__main__':
    get_label_filter()

#Displays Artists for filter (artist/work/title)
@app.route('/artist_filter', methods = ['POST', 'GET'])
def get_artists():
    conn = None
    user = {'username': 'JT'}
    artistList=[]
    artistDict={"artistList":artistList}
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(queries.sql_artist)
        rows = cur.fetchall()
        for i in range(0,len(rows)):
            artistList.append(rows[i][0])
        # print(artistDict)
        print("The number of Artists: ", cur.rowcount)
        return render_template('artistFilter_AWT.htm', title='artist', dict=artistDict)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
if __name__ == '__main__':
    get_artists()

#Displays Artists for filter (artist/title/work)
@app.route('/artist_filter_2', methods = ['POST', 'GET'])
def get_artist_2():
    conn = None
    user = {'username': 'JT'}
    artistList=[]
    artistDict={"artistList":artistList}
    print("test")
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(queries.sql_artist)
        rows = cur.fetchall()
        for i in range(0,len(rows)):
            artistList.append(rows[i][0])
        # print(artistDict)
        print("The number of artists: ", cur.rowcount)
        return render_template('artistFilter_ATW.htm', title='artists', dict=artistDict)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
if __name__ == '__main__':
    get_artist_2()

#Displays Composers for filter (composer/work/title)
@app.route('/composer_filter', methods = ['POST', 'GET'])
def get_Composers():
    conn = None
    user = {'username': 'JT'}
    compList=[]
    compDict={"compList":compList}
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(queries.sql_composer)
        rows = cur.fetchall()
        for i in range(0,len(rows)):
            compList.append(rows[i][1])
        # print(compDict)
        print("The number of Composers: ", cur.rowcount)
        return render_template('composerFilter_CWT.htm', title='composer', dict=compDict)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
if __name__ == '__main__':
    get_Composers()

#Displays Composers for filter (composer/title/work)
@app.route('/composer_filter_2', methods = ['POST', 'GET'])
def get_Composers_2():
    conn = None
    user = {'username': 'JT'}
    compList=[]
    compDict={"compList":compList}
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(queries.sql_composer)
        rows = cur.fetchall()
        for i in range(0,len(rows)):
            compList.append(rows[i][1])
        print("The number of Composers: ", cur.rowcount)
        return render_template('composerFilter_CTW.htm', title='composer', dict=compDict)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
if __name__ == '__main__':
    get_Composers_2()

# Records by Label, filtered
@app.route('/recordsBy/<label>', methods = ['POST', 'GET'])
def get_LabelTitle_filter(**kwargs):
    label = kwargs['label']
    print("label = ",label)
    conn = None
    user = {'username': 'JT'}
    if label=="ALL":
        label=label.replace(label,"%%")
    limit=500
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(queries.sql_labelTitles.format(label,limit))
        rows = cur.fetchall()
        print("The number of Titles: ", cur.rowcount)
        rowcount = cur.rowcount

        loopString.loopString_label(rows,rowcount)

        return render_template('labelTitle.htm', title="labelTitle",user=user, html_string=loopString.loopString_label.html_string,rowcount=rowcount)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    get_LabelTitle_filter()

# Displays Artist by Works, Titles, filtered
@app.route('/workBy/<artist>', methods = ['POST', 'GET'])
def get_ArtistWorkTitle_filter(**kwargs):
    artist = kwargs['artist']
    limit=99999
    if artist=="ALL":
        artist=artist.replace(artist,"%%")
        limit=500
    print(f"Artist = {artist}")
    conn = None
    user = {'username': 'JT'}
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(queries.sql_artistWorkTitle.format(artist,limit))
        rows = cur.fetchall()

        loopString.loopString_artistWorkTitle(rows)

        return render_template('concatString.htm', title="artistWorkTitle",user=user, rows=rows, html_string=loopString.loopString_artistWorkTitle.html_string)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    get_ArtistWorkTitle_filter()

# Displays Artist by Titles, Works, filtered
@app.route('/titleBy/<artist>', methods = ['POST', 'GET'])
def get_ArtistTitleWork_filter(**kwargs):
    artist = kwargs['artist']
    limit=99999
    if artist=="ALL":
        artist=artist.replace(artist,"%%")
        limit=250
    print(f"Artist = {artist}")
    conn = None
    user = {'username': 'JT'}

    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(queries.sql_artistTitleWork.format(artist,limit))
        rows = cur.fetchall()

        loopString.loopString_artistTitleWork(rows)

        return render_template('concatString.htm', title="artistTitleWork",user=user, rows=rows, html_string=loopString.loopString_artistTitleWork.html_string)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    get_ArtistTitleWork_filter()

# Displays Composer(s) by Works, Titles, filtered
@app.route('/worksBy/<comp>', methods = ['post', 'get'])
def get_composerWorks_filter(**kwargs):
    comp = kwargs['comp']
    limit=99999
    if comp=="ALL":
        comp=comp.replace(comp,"%%")
        limit = 500
    print(f"Composer = {comp}")
    user = {'username': 'JT'}

    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(queries.sql_composerWorkTitle.format(comp,limit))
        rows = cur.fetchall()

        loopString.loopString_composerWorkTitle(rows)

        return render_template('concatString.htm', title="composerWorkTitle",user=user, html_string=loopString.loopString_composerWorkTitle.html_string)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    get_composerWorks_filter()

# Displays Composer(s) by Titles, Works, filtered
@app.route('/titlesBy/<comp>', methods = ['post', 'get'])
def get_ComposerTitle_Filter(**kwargs):
    comp = kwargs['comp']
    limit=99999
    if comp=="ALL":
        comp=comp.replace(comp,"%%")
        limit = 500
    print(f"Composer = {comp}")
    conn = None
    user = {'username': 'JT'}

    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(queries.sql_composerTitleWork.format(comp,limit))
        rows = cur.fetchall()

        loopString.loopString_composerTitleWork(rows)
        
        return render_template('concatString.htm', title="ComposerTitleWork",user=user, html_string=loopString.loopString_composerTitleWork.html_string)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    get_ComposerTitle_Filter()

