<!-- template to insert into visitorsearch. CURRENTLY PLACEHOLDER-Y -->

<h2 class="searchtitle">Results:</h2>
<ol>
    % for result in search_results:
        <li>
            <h3 class="bookname">{{result["title"]}}</h3>
            <p class="bookauthor">{{result["author"]}}</p>
            % if result["is_available"]==1:
                <p class="available">AVAILABLE</p>
                <form name="quickborrowform" action="/borrow/{{result['id']}}" method="post">
                    <input id="quickborrowbutton" name="quickborrowbutton" value="Borrow!" type="submit">
                </form>
            % else:
                <p class="unavailable">UNAVAILABLE</p>
            % end
            <img height="100" width="100" src="{{result['imgsrc']}}" />
            <!-- the rest of this shouldn't be visible by default -->
            <p>ISBN: {{result["isbn"]}}</p>
            <p>Genres: {{result["genre"]}}</p>
            <p>Short description of the book, maybe the blurb or an excerpt from it.</p>
        </li>
    % end
</ol>