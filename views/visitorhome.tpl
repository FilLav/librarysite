<html>
    <head>
        <title>Library - Home</title>

        <link rel="stylesheet" type="text/css" href="/static/visitorhomestyle.css">
        <link rel="stylesheet" type="text/css" href="/static/navbarstyle.css">
    </head>

    <body>

        <!-- standard navbar template -->
        % include('navbar.tpl')

        <div class="container">

            <div class="quickborrow boxes">
                <h2>Quick Borrow</h2>
                <form name="quicksearchform" action="/frontend/visitorhome/quicksearch" method="post">
                    <p>Type in the name of the book you're looking for...</p>
                    <input id="quicksearchbox" name="quicksearchbox" type="text" placeholder="Search..." />
                    <input id="quicksearchsubmit" name="quicksearchsubmit" type="submit">
                </form>

                <!-- after making a search, quicksearchresults template is called upon: -->
                % if defined('search_results'):
                    % include('quicksearchresults.tpl')
                % end
            </div><!-- comment in order to remove weird whitespace...

         --><a href="/frontend/useraccount.html" class="accountbox boxes">
            <div>
                <div id="accountboxid">
                    <h2>Account</h2>
                    <p>– view books</p>
                    <p>– renew</p>
                    <p>– outstanding charges</p>
                    <p>– history</p>
                    <p>– change details</p>
                </div>
            </div>
            </a><!--

         --><div class="browsebooks boxes">
                <h2>Browse</h2>
                <p><a href="" class="browselink">– by genre</a></p>
                <p><a href="" class="browselink">– recent additions</a></p>
                <p><a href="" class="browselink">– recommendations</a></p>
                <br>
                <p><a href="/frontend/visitorsearch" class="browselink"><h3>refined search</h3></a></p>
            </div>

        </div>

    </body>
</html>