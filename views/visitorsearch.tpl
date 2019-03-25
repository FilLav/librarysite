<html>
    <head>
        <title>Library - Search for books</title>

        <link rel="stylesheet" type="text/css" href="/static/visitorsearchstyle.css">
        <link rel="stylesheet" type="text/css" href="/static/navbarstyle.css">
        <link rel="stylesheet" type="text/css" href="/static/homebuttonstyle.css">
    </head>

    <body>

        <!-- standard templates -->
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
                    <option value="">Any</option>
                    <option value="fantasy">Fantasy</option>
                    <option value="mystery">Mystery</option>
                    <option value="cooking">Cooking</option>
                </select>
                <!-- keywords/blurbs aren't yet represented in the db so this shouldn't exist for nowww
                <input id="refinedsearchkeyword" name="refinedsearchkeyword" type="text" placeholder="Keywords" />
                -->
                <input id="refinedsearchsubmit" name="quicksearchsubmit" type="submit">
            </form>
        </div>

        <!-- box where search results are displayed, or, if no search has been made, says so -->
        <div class="resultslist">
            % if defined('search_results'):
                % include('refinedsearchresults.tpl')
            % else:
                <h2 class="searchtitle">Enter your search terms</h2>
            % end
        </div>

    </body>
</html>