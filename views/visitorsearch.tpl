<html>
    <head>
        <title>Library - Search for books</title>

        <link rel="stylesheet" type="text/css" href="/static/visitorsearchstyle.css">
        <link rel="stylesheet" type="text/css" href="/static/navbarstyle.css">
        <link rel="stylesheet" type="text/css" href="/static/homebuttonstyle.css">
    </head>

    <body>

        % include('navbar.tpl')

        % include('homebutton.tpl')

        <!-- wanna take this out for now...
            <div class="searchboxclass">
                <form name="quicksearchform" action="" method="post">
                    <input id="searchboxid" name="searchbox" type="text" placeholder="Search..." />
                </form>
            </div> -->

        <div class="refinedform"> <!-- this should appear from the left side of the screen -->
            <form name="refinedsearchform" action="/frontend/visitorsearch/search" method="post">
                <input id="refinedsearchtitle" name="refinedsearchtitle" type="text" placeholder="Title" />
                <input id="refinedsearchauthors" name="refinedsearchauthors" type="text" placeholder="Author(s)" />
                <input id="refinedsearchisbn" name="refinedsearchisbn" type="text" placeholder="ISBN" />
                <select title="genre" id="refinedsearchgenre" name="refinedsearchgenre">
                    <option value="fantasy">Fantasy</option>
                    <option value="mystery">Mystery</option>
                    <option value="cooking">Cooking</option>
                </select>
                <!-- keywords/blurbs aren't yet represented in the db so this shouldn't exist for nowww
                <input id="refinedsearchkeyword" name="refinedsearchkeyword" type="text" placeholder="Keywords" />
                -->
            </form>
        </div>

        <div class="resultslist">
            <h2>Results:</h2>
            <ol>
                <li>
                    <h3 class="bookname">Book Name</h3>
                    <p>Book Author</p>
                    <p class="bookavailable">AVAILABLE</p>
                    <img height="100" width="100" src="/static/images/bookish.png" />
                    <!-- the rest of this shouldn't be visible by default -->
                    <p>ISBN: 9781444913989</p>
                    <p>Genres: A, B</p>
                    <p>Short description of the book, maybe the blurb or an excerpt from it.</p>
                    
                </li>
            </ol>
        </div>

    </body>
</html>