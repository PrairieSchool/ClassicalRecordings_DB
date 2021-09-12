# My Personal Project: a database of classical music recordings

This is a web-based app I wrote in **Python** and **SQL** using **Flask** and **Psycopg** with **Postgresql** as a backend server and, of course, **HTML** on the front. There is some **Javascript** in the templates and I wrote all the *.css* style sheets with no downloaded framework like **Bootstrap**. The app is a user interface for my database of classical music recordings.  
On the home page I show an *Entity Relationship Diagaram* of the fourteen tables and a descriptive paragraph that includes live counts of rows in the database.

![index.png](screenshots/index.png)

# Filter tab

Under the **Filter** tab, i can show records in the database in six ways. 
Here is a screenshot of the *titleWorkArtist* ordering of the data. The top line prints the title of the record on the left and the label, catalogue number, and the number and type of discs on the right. Below the title is a list of the different pieces on the record, showing the composer and name of the piece on the left and the type of work on the right. Below that is a list of the musicians who play on the piece on the left and the artist's role, instrument or type on the right. 


![titleWorkArtist.png](screenshots/titleWorkArtist.png)

This *titleWorkArtist* view `SELECTS` data from ten of the fourteen tables which have to  be joined based on their key constraints using a `SQL` statement.  This statement is among all the other `SQL` statements in a **Python** `.py` file and pulled into the main `routes.py` file as a subroutine.

![titleWorkArtist_sql.png](screenshots/titleWorkArtist_sql.png)

Because **Psycopg** retrieves data from the database in table form, I had to devise a way to display it in the above, easier to read format. In order to do this I wrote functions to loop through and seperate common data points like the record title first and musical work second then compiling a string with `html tags` which is then passed on to the template for the web page. All of these functions are saved on a separate **python** `.py `file and pulled into the main `routes.py` file as a subroutine. Here is a section of one of these functions. 

![titleWorkArtist_loopString.png](screenshots/titleWorkArtist_loopString.png)


Back to the **Filter** tab, if i select *artistTitleWork*, i will get a list of names of all the artists in the database. The names as displayed are hyperlinks that will lead to the *artistTitleWork* view for that particular artist. The search box will narrow down the choices by entering any part of the artist's name in upper or lower case.

![artistTitleWork_main.png](screenshots/artistTitleWork_main.png)

![artistWorkTitle_select_1.png](screenshots/artistWorkTitle_select_1.png)

![artistWorkTitle_select_2.png](screenshots/artistWorkTitle_select_2.png)

When I click on the link Anne-Sophie Mutter, I am showed a scrollable page with all the different works she plays ordered by type and alphabetically by composer.  On the beginning of her page, the violinist's chamber works are showed starting with those by Bartok. Under each work is printed the title information of whichever records i have in my collection.  You can see that I have three different records featuring Mutter playing Brahms's first violin sonata.

![artistWorkTitle_view.png](screenshots/artistWorkTitle_view.png)

Back at the **Filter** tab, when I select *artistTitleWork* I will see the list of artists. When i click on one of the links, I see the arist's name and instrument again, but now i see a list of the records i have with them on it then a list of only the works that artist is featured on.  The Anne-Sophie Mutter page starts with an alphabetical list of all the titles she's featured on.

![artistTitleWork_view.png](screenshots/artistTitleWork_view.png)

When I select *composerWorkArtist* from the **Filter** tab, I am taken to a list of composers which i can narrow down in the search box. Here is the beginning of JS Bach's page which shows a list of his works and the records I have featuring those pieces. This list is ordered by the type -- first, seen below, is piano pieces -- and then by opus number, starting in this case by BWV 543. 

![composerWorkTitle.png](screenshots/composerWorkTitle.png)

If I scroll down, i see two recordings of one of the concertos Anne-Sophie Mutter plays on along with three other recordings I have of those pieces, two by Adolph Busch and one by David Oistrakh as soloist.

![composerWorkArtist_Bach1042.png](screenshots/composerWorkArtist_Bach1042.png)

I also have available under the **Filters** tab a view called *composerTitleWork*. This shows a list of composers to choose, then record titles and the works featured on them. This list is sorted by the records place on my shelves and features only the works by the composer selected. For example the first record to feature JS Bach on my list is called *Albinoni: Adagio / Mendelssohn, Mozart, Bach, Pachelbel, Beethoven / Marriner*. It features pieces by six composers but this view only shows the two by Bach.

![composerTitleWork_view.png](screenshots/composerTitleWork_view.png)

Scrolling down, here is a view of some of the violin concertos we saw above.

![composerTitleWork_section.png](screenshots/composerTitleWork_section.png)

The last important view I have written is that of titles by record label.  This view is useful to display all the titles i have of one label, ordered by catalog number. Again, I can select from a list and use a text box.

![labelTitle_list.png](screenshots/labelTitle_list.png)

Here is the beginning of the CRI list.

![labelTitle_CRI.png](screenshots/labelTitle_CRI.png)

The app also has two other tabs, **Queries** and **Tables**. I used these as stages in developement for reference while writing the more flexible **Filters** code. I am currently developing `ALTER TABLE` forms for data entry so I can continue to add records as I acquire them.  After that, I plan on writing a new app for my pop record collection. That will be simpler because there are fewer tables as there is no need to JOIN composers to works and works to records and artists to the recordings of these works.  


