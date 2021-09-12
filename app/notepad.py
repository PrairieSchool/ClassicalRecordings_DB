# This format without LEFT JOIN but FROM/WHERE statements isn't used anymore
#
#
# Composer / Work / title filter query
sql_composerWorkTitle_2 = '''
    SELECT "c"."composer", "e"."era", "cy"."country",
        "w"."work_name","w"."opus","wt"."work_type",
        "r"."title","l"."label","r"."cat_prefix","r"."cat_number","r"."disc_count","f"."format","r"."record_pk",
        "a"."artist","i"."instrument"
        FROM "record" AS "r", 
            "rec_work" AS "rw",
            "work" AS "w",
            "work_type" AS "wt",
            "composer" AS "c",
            "era" AS "e",
            "country" AS "cy",
            "artist" AS "a",
            "instrument" AS "i",
            "label" AS "l",
            "rec_work_artist" AS "rwm",
            "format" AS "f"

            WHERE "r"."record_pk" = "rw"."record_fk" AND
                "w"."work_pk" = "rw"."work_fk" AND
                "w"."work_type_fk" = "wt"."work_type_pk" AND
                "c"."composer_pk" = "w"."composer_fk" AND
                "c"."era_fk" = "e"."era_pk" AND
                "c"."country_fk" = "cy"."country_pk" AND
                "rw"."rec_work_pk" = "rwm"."rec_work_fk" AND
                "rwm"."artist_fk" = "a"."artist_pk" AND
                "r"."label_fk" = "l"."PrimaryKey" AND 
                "r"."format_fk" = "f"."format_pk" AND 
                "a"."instrument_fk" = "i"."instrument_pk" AND
                "c"."composer" ILIKE '{0}'
        ORDER BY "c"."composer_lname","wt"."file_order","w"."work_pk","r"."file_under","r"."record_pk","rwm"."rec_work_artist_pk"
        LIMIT '{1}';
    '''
# Composer / title / Work filter query
sql_composerTitleWork = '''
    SELECT "c"."composer", "e"."era", "cy"."country",
        "r"."title","l"."label","r"."cat_prefix","r"."cat_number","r"."disc_count","f"."format","r"."record_pk",
        "w"."work_name","w"."opus","wt"."work_type"
        FROM "record" AS "r", 
            "rec_work" AS "rw",
            "work" AS "w",
            "work_type" AS "wt",
            "composer" AS "c",
            "era" AS "e",   
            "country" AS "cy",
            "label" AS "l",
            "format" AS "f"
            WHERE "r"."record_pk" = "rw"."record_fk" AND
                "w"."work_pk" = "rw"."work_fk" AND
                "w"."work_type_fk" = "wt"."work_type_pk" AND
                "c"."composer_pk" = "w"."composer_fk" AND
                "c"."country_fk" = "cy"."country_pk" AND
                "c"."era_fk" = "e"."era_pk" AND
                "r"."label_fk" = "l"."PrimaryKey" AND 
                "r"."format_fk" = "f"."format_pk" AND 
                "c"."composer" ILIKE '{0}'
        ORDER BY "c"."composer_lname","r"."file_under","r"."record_pk","w"."work_pk"
        LIMIT {1};
    '''
