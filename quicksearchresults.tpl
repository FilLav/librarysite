<!-- fits inside visitorhome. not called upon. maybe deleteme idk -->

<html>
    <head>
    <!-- actually I don't know if I want/need a title? -->
    </head>

    <body>
        <ol>
            % for result in search_results:
                <li>
                    <h3>{{result["title"]}}</h3>
                    <p>{{result["author"]}}</p>
                    <img height="100" width="100" src="{{result['imgsrc']}}" />
                </li>
            % end
        </ol>
    </body>
</html>