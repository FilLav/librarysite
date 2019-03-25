<!-- template to insert into visitorhome -->

<ol>
    % for result in search_results:
        <li>
            <h3>{{result["title"]}}</h3>
            <p>{{result["author"]}}</p>
            <img height="100" width="100" src="{{result['imgsrc']}}" />
            % if result["is_available"]==1:
                <p class="available">AVAILABLE</p>
                <form name="quickborrowform" action="/borrow/{{result['id']}}" method="post">
                    <input id="quickborrowbutton" name="quickborrowbutton" value="Borrow!" type="submit">
                </form>
            % else:
                <p class="unavailable">UNAVAILABLE</p>
            % end
        </li>
    % end
</ol>