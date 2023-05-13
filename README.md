# Web Crawler

<dl><dd><dl><dd><dl> 

### Patent
``` py
    CLASS get_patents(*, date_from, date_to = today(), IPC = ..., limit = 50)
```
<dd><dl><dd><dl><dd> 
    <blockquote>
    A class containing information of a patent.
    </blockquote>
    <dl>
        <dt> Attributes </dt>
        <dd><ul>
            <li><b>id</b> (str) :&ensp; Publication number.
            <li><b>title</b> (str) :&ensp; Title.
            <li><b>date</b> (str) :&ensp; Publication date.
            <li><b>IPC</b> (str[ ]) :&ensp; IPC.
            <li><b>image_url</b> (str) :&ensp; Url of the main image.
            <li><b>content</b> (str) :&ensp; Abstract of the patent.
        </dd>
    </dl>
</dd></dl></dd></dl></dd>

---

``` py
    get_patents(*, date_from, date_to = today(), IPC = ..., limit = 50)
```
<dd><dl><dd><dl><dd> 
    <blockquote>
    Retrieve patents within a specified date range. This returns an int and a generator of dictionary.
    </blockquote>
    <dl>
        <dt> Parameters </dt>
        <dd><ul>
            <li><b>date_from</b> (date) :&ensp; Starting date.
            <li><b>date_to</b> (date, opt) :&ensp; Ending date. Default is the current day.
            <li><b>IPC</b> (str[ ], opt) :&ensp; The IPC of the patents.
            <li><b>limit</b> (int, opt) :&ensp; Limit the maximum amount of data retrieved. Pass 0 if no limit is desired.
        </dd>
        <dt> Returns </dt>
        <dd><ul>
            <li><b>total_num</b> (int) :&ensp; The total number of data that matches the given date range.
            <li><b>data</b> (dict[ ]):&ensp; A generator. Each data consists of "id", "title", "date", "url", "image_url", and "content".
        </dd>
    </dl>
</dd></dl></dd></dl></dd>
</dl></dd></dl></dd></dl>


# Database

<dl><dd><dl><dd><dl> 

``` py
    get_patents(date_from, date_to = today(), limit = 50)
```
<dd><dl><dd><dl><dd> 
    <blockquote>
    Retrieve patents within a specified date range.
    </blockquote>
    <dl>
        <dt> Parameters </dt>
        <dd><ul>
            <li> date_from (date) :&ensp; Starting date
            <li> date_to (date, opt) :&ensp; End date
        </dd>
        <dt> Returns </dt>
        <dd>
            <ul><li> abc
        </dd>
    </dl>
</dd></dl></dd></dl></dd>
</dl></dd></dl></dd></dl>

# NLP

<dl><dd><dl><dd><dl> 

``` py
    get_features(articles)
```
<dd><dl><dd><dl><dd> 
    <blockquote>
    Calculate and represent the likelihood of articles belonging to each category in vectors.
    </blockquote>
    <dl>
        <dt> Parameters </dt>
        <dd>
            <ul><li> articles (str[ ]) :&ensp; strings composed of the name and content of patents.
        </dd>
        <dt> Returns </dt>
        <dd>
            <ul><li> features (float[ ][ ])
        </dd>
    </dl>
</dd></dl></dd></dl></dd>
</dl></dd></dl></dd></dl>

# Line Bot

<dl><dd><dl><dd><dl> 

    get_patents(from, to)
<dd><dl><dd><dl><dd> 
    取得指定日期範圍內的專利
    <dl>
        <dt> Parameters </dt>
        <dd>
            <ul><li> abc
        </dd>
        <dt> Returns </dt>
        <dd>
            <ul><li> abc
        </dd>
    </dl>
</dd></dl></dd></dl></dd>
</dl></dd></dl></dd></dl>