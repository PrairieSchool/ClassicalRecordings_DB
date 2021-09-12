# label query
sql_label = '''
    SELECT *
        FROM "label"
        ORDER BY "label"
        '''
# titles query
sql_titles = '''
    SELECT "r"."file_under","r"."title","f"."format","l"."label","r"."cat_prefix","r"."cat_number","r"."disc_count"
        FROM "record" AS "r"
            LEFT JOIN "format" AS "f" ON "r"."format_fk" = "f"."format_pk"
            LEFT JOIN "label" AS "l" ON "r"."label_fk" = "l"."PrimaryKey"
        ORDER BY "file_under","format"
        LIMIT 999999;
        '''
# Musician/Ensemble query 
sql_artist = f'''
    SELECT "a"."artist" 
        FROM "artist" AS "a"
        ORDER BY "artist_lname"
        --LIMIT 25
        '''
# Musician/Ensemble by instrument/range query
sql_artistInstrument = '''
    SELECT "a".*,"i"."instrument","cy"."country"
        FROM "artist" AS "a"
                LEFT JOIN "instrument" AS "i" ON "a"."instrument_fk" = "i"."instrument_pk"
                LEFT JOIN "country" AS "cy" ON "a"."country_fk" = "cy"."country_pk"
        WHERE "i"."instrument" ILIKE '%%'
        ORDER BY "artist_lname"
        LIMIT 999999
    ; '''
# Composer query, ordered
sql_composer = f''' 
    SELECT "c".*, "e"."era", "cy"."country" 
        FROM "composer" AS "c"
            LEFT JOIN "country" AS "cy" ON "c"."country_fk" = "cy"."country_pk"
            LEFT JOIN "era" AS "e" ON "c"."era_fk" = "e"."era_pk"
        ORDER BY "composer_lname"
        --LIMIT 10
    ; '''
# Works query
sql_works = '''
    SELECT "w"."work_pk","c"."composer","w"."work_name","wt"."work_type","w"."opus","w"."work_notes" 
        FROM "composer" AS "c"
            LEFT JOIN "work" AS "w" ON "c"."composer_pk" = "w"."composer_fk"
            LEFT JOIN "work_type" AS "wt" ON "w"."work_type_fk" = "wt"."work_type_pk"
        ORDER BY "work_pk"
        LIMIT 999999
    ; '''
# titles / Works / Artists query
sql_titleWorkArtist = '''
    SELECT "r"."title","l"."label","r"."cat_prefix","r"."cat_number","r"."disc_count","f"."format",
            "c"."composer","w"."work_name","wt"."work_type",
            "a"."artist","i"."instrument",
            "n".*
        FROM "record" AS "r" LEFT JOIN "rec_work" AS "rw" ON "r"."record_pk" = "rw"."record_fk"
            LEFT JOIN "work" AS "w" ON "w"."work_pk" = "rw"."work_fk"
            LEFT JOIN "composer" AS "c" ON "c"."composer_pk" = "w"."composer_fk"
            LEFT JOIN "rec_work_artist" AS "rwm" ON "rw"."rec_work_pk" = "rwm"."rec_work_fk"
            LEFT JOIN "artist" AS "a" ON "rwm"."artist_fk" = "a"."artist_pk"
            LEFT JOIN "instrument" AS "i" ON "a"."instrument_fk" = "i"."instrument_pk"
            LEFT JOIN "label" AS "l" ON "r"."label_fk" = "l"."PrimaryKey"
            LEFT JOIN "format" AS "f" ON "r"."format_fk" = "f"."format_pk"
            LEFT JOIN "work_type" AS "wt" ON "w"."work_type_fk" = "wt"."work_type_pk"
            LEFT JOIN "notes" AS "n" ON "r"."record_pk" = "n"."ID"
        --WHERE "l"."label" ILIKE '%CRI%'
        WHERE "a"."artist" ILIKE '%alban berg%'
        ORDER BY "r"."file_under","l"."label","r"."cat_number", "r"."format_fk","rw"."rec_work_pk","rwm"."rec_work_artist_pk"
        LIMIT {0}
    ; '''
# label / title filter query
sql_labelTitles = '''
    SELECT "l"."label","r"."cat_prefix","r"."cat_number","r"."title"
        FROM "record" as "r"
            LEFT JOIN "label" as "l" ON "l"."PrimaryKey" = "r"."label_fk"
        WHERE "l"."label" ILIKE '{0}'
        ORDER BY "l"."label","r"."cat_prefix","r"."cat_number"
        LIMIT {1}
    ; '''
# Artist / Work / title filter query
sql_artistWorkTitle = '''
    SELECT "a"."artist","i"."instrument",
            "c"."composer","w"."work_name","w"."opus","wt"."work_type",
            "r"."title","l"."label","r"."cat_prefix","r"."cat_number","r"."disc_count","f"."format"
        FROM "record" AS "r" 
            LEFT JOIN "rec_work" AS "rw" ON "r"."record_pk" = "rw"."record_fk"
            LEFT JOIN "work" AS "w" ON "w"."work_pk" = "rw"."work_fk"
            LEFT JOIN "work_type" AS "wt" ON "w"."work_type_fk" = "wt"."work_type_pk"
            LEFT JOIN "composer" AS "c" ON "c"."composer_pk" = "w"."composer_fk"
            LEFT JOIN "rec_work_artist" AS "rwm" ON "rw"."rec_work_pk" = "rwm"."rec_work_fk"
            LEFT JOIN "artist" AS "a" ON "rwm"."artist_fk" = "a"."artist_pk"
            LEFT JOIN "instrument" as "i" ON "a"."instrument_fk" = "i"."instrument_pk"
            LEFT JOIN "label" AS "l" ON "r"."label_fk" = "l"."PrimaryKey"
            LEFT JOIN "format" AS "f" ON "r"."format_fk" = "f"."format_pk"
        WHERE "a"."artist" ILIKE '{0}'
        ORDER BY "a"."artist_lname", "wt"."work_type", "w"."work_pk","r"."file_under","r"."record_pk"
        LIMIT {1}
    ; '''
# Artist / title / Work filter query
sql_artistTitleWork = '''
    SELECT "a"."artist","i"."instrument",
            "r"."title","l"."label","r"."cat_prefix","r"."cat_number","r"."disc_count","f"."format",
            "c"."composer","w"."work_name","w"."opus","wt"."work_type"
        FROM "record" AS "r" 
            LEFT JOIN "rec_work" AS "rw" ON "r"."record_pk" = "rw"."record_fk"
            LEFT JOIN "work" AS "w" ON "w"."work_pk" = "rw"."work_fk"
            LEFT JOIN "work_type" AS "wt" ON "w"."work_type_fk" = "wt"."work_type_pk"
            LEFT JOIN "composer" AS "c" ON "c"."composer_pk" = "w"."composer_fk"
            LEFT JOIN "rec_work_artist" AS "rwm" ON "rw"."rec_work_pk" = "rwm"."rec_work_fk"
            LEFT JOIN "artist" AS "a" ON "rwm"."artist_fk" = "a"."artist_pk"
            LEFT JOIN "instrument" AS "i" ON "a"."instrument_fk" = "i"."instrument_pk"
            LEFT JOIN "label" AS "l" ON "r"."label_fk" = "l"."PrimaryKey"
            LEFT JOIN "format" AS "f" ON "r"."format_fk" = "f"."format_pk"
        WHERE "a"."artist" ILIKE '{0}'
        ORDER BY "a"."artist_lname", "r"."file_under","r"."record_pk","w"."work_pk"
        LIMIT {1};
    '''
# Composer / Work / title filter query
sql_composerWorkTitle = '''
    SELECT "c"."composer", "e"."era", "cy"."country",
        "w"."work_name","w"."opus","wt"."work_type",
        "r"."title","l"."label","r"."cat_prefix","r"."cat_number","r"."disc_count","f"."format","r"."record_pk",
        "a"."artist","i"."instrument"

        FROM "record" AS "r" 

            LEFT JOIN "rec_work" AS "rw" ON "r"."record_pk" = "rw"."record_fk"
            LEFT JOIN "work" AS "w" ON "w"."work_pk" = "rw"."work_fk"
            LEFT JOIN "work_type" AS "wt" ON "w"."work_type_fk" = "wt"."work_type_pk"
            LEFT JOIN "composer" AS "c" ON "c"."composer_pk" = "w"."composer_fk"
            LEFT JOIN "era" AS "e" ON "c"."era_fk" = "e"."era_pk"
            LEFT JOIN "country" AS "cy" ON "c"."country_fk" = "cy"."country_pk"
            LEFT JOIN "rec_work_artist" AS "rwm" ON "rw"."rec_work_pk" = "rwm"."rec_work_fk"
            LEFT JOIN "artist" AS "a" ON "rwm"."artist_fk" = "a"."artist_pk"
            LEFT JOIN "instrument" as "i" ON "a"."instrument_fk" = "i"."instrument_pk"
            LEFT JOIN "label" AS "l" ON "r"."label_fk" = "l"."PrimaryKey"
            LEFT JOIN "format" AS "f" ON "r"."format_fk" = "f"."format_pk"

        WHERE "c"."composer" ILIKE '{0}'
        ORDER BY "c"."composer_lname","wt"."file_order","w"."work_pk","r"."file_under","r"."record_pk","rwm"."rec_work_artist_pk"
        LIMIT '{1}';
    '''
# Composer / title / Work filter query
sql_composerTitleWork = '''
    SELECT "c"."composer", "e"."era", "cy"."country",
        "r"."title","l"."label","r"."cat_prefix","r"."cat_number","r"."disc_count","f"."format","r"."record_pk",
        "w"."work_name","w"."opus","wt"."work_type"

        FROM "record" AS "r"
            LEFT JOIN "rec_work" AS "rw" ON "r"."record_pk" = "rw"."record_fk"
            LEFT JOIN "work" AS "w" ON "w"."work_pk" = "rw"."work_fk"
            LEFT JOIN "work_type" AS "wt" ON "w"."work_type_fk" = "wt"."work_type_pk"
            LEFT JOIN "composer" AS "c" ON "c"."composer_pk" = "w"."composer_fk"
            LEFT JOIN "era" AS "e" ON "c"."era_fk" = "e"."era_pk"
            LEFT JOIN "country" AS "cy" ON "c"."country_fk" = "cy"."country_pk"
            LEFT JOIN "label" AS "l" ON "r"."label_fk" = "l"."PrimaryKey"
            LEFT JOIN "format" AS "f" ON "r"."format_fk" = "f"."format_pk"
        WHERE "c"."composer" ILIKE '{0}'
        ORDER BY "c"."composer_lname","r"."file_under","r"."record_pk","w"."work_pk"
        LIMIT {1};
    '''
#  Many-to-many query of Record / Work / Artist
sql_manyToMany = '''
    SELECT "rw".*, "rwm".*, "a"."artist"
        FROM "rec_work" AS "rw"
            LEFT JOIN "rec_work_artist" AS "rwm" ON "rw"."rec_work_pk" = "rwm"."rec_work_fk"
            LEFT JOIN "artist" AS "a" ON "a"."artist_pk" = "rwm"."artist_fk"
        ORDER BY "rw"."record_fk","rw"."rec_work_pk","rwm"."rec_work_artist_pk";
    '''

# Query of the Rec_Work table for counting purposes
sql_recWork = '''
    SELECT "rw"."rec_work_pk"
        FROM "rec_work" AS "rw"
    '''
# Query of the Rec_Work_Artist table for counting purposes
sql_recWorkArtist = '''
    SELECT "rwa"."rec_work_artist_pk"
        FROM "rec_work_artist" AS "rwa"
    '''
# Query to SUM the total disc count of all the records in the collection
sql_totalDiscCt = '''
SELECT SUM ("disc_count") AS "totalDiscCt"
FROM "record" AS "r";
'''
