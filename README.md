# Web Crawler

<dl><dd><dl><dd><dl> 

### Patent

``` py
    CLASS Patent(pid, title, date, ipc, image_url, content)
```
<dd><dl><dd><dl><dd> 
    <blockquote>
    A class containing information of a patent.
    </blockquote>
    <dl>
        <dt> Attributes </dt>
        <dd><ul>
            <li><b>pid</b> (str) :&ensp; Publication number.
            <li><b>title</b> (str) :&ensp; Title.
            <li><b>date</b> (str) :&ensp; Publication date.
            <li><b>ipc</b> (str[ ]) :&ensp; IPC.
            <li><b>image_url</b> (str) :&ensp; Url of the main image.
            <li><b>content</b> (str) :&ensp; Abstract of the patent.
        </dd>
    </dl>
</dd></dl></dd></dl></dd>

---

``` py
    get_patents(date_from, date_to = today(), ipc = ..., limit = 50)
```
<dd><dl><dd><dl><dd> 
    <blockquote>
    Retrieve patents within a specified date range and categories. This returns an int and a generator of dictionary.
    </blockquote>
    <dl>
        <dt> Parameters </dt>
        <dd><ul>
            <li><b>date_from</b> (date) :&ensp; Starting date.
            <li><b>date_to</b> (date, opt) :&ensp; Ending date. Default is the current day.
            <li><b>ipc</b> (str[ ], opt) :&ensp; The IPC of the patents.
            <li><b>limit</b> (int, opt) :&ensp; Limit the maximum amount of data retrieved. Pass 0 if no limit is desired.
        </dd>
        <dt> Returns </dt>
        <dd><ul>
            <li><b>total_num</b> (int) :&ensp; The total number of data that matches the given conditions.
            <li><b>data</b> (<a href="#patent">Patent</a>[ ]) :&ensp; A generator of matching patents.
        </dd>
    </dl>
</dd></dl></dd></dl></dd>
</dl></dd></dl></dd></dl>


# Database

<dl><dd><dl><dd><dl> 

``` py
    get_patents(date_from, date_to = today(), ipc = ..., limit = 50)
```
<dd><dl><dd><dl><dd> 
    <blockquote>
    Retrieve patents within a specified date range. 
    </blockquote>
    <dl>
        <dt> Parameters </dt>
        <dd><ul>
            <li><b>date_from</b> (date) :&ensp; Starting date.
            <li><b>date_to</b> (date, opt) :&ensp; Ending date. Default is the current day.
            <li><b>ipc</b> (str[ ], opt) :&ensp; The IPC of the patents.
            <li><b>limit</b> (int, opt) :&ensp; Limit the maximum amount of data retrieved. Pass 0 if no limit is desired.
        </dd>
        <dt> Returns </dt>
        <dd><ul>
            <li><b>total_num</b> (int) :&ensp; The total number of data that matches the given date range.
            <li><b>data</b> (<a href="#patent">Patent</a>[ ]) :&ensp; A list of matching patents.
        </dd>
    </dl>
</dd></dl></dd></dl></dd>

---

``` py
    add_patents(patents)
```
<dd><dl><dd><dl><dd> 
    <blockquote>
    Insert patents into database. Overwrite existing data.
    </blockquote>
    <dl>
        <dt> Parameters </dt>
        <dd><ul>
            <li><b>patents</b> (<a href="#patent">Patent</a>[ ]) :&ensp; Patents to be added.
        </dd>
    </dl>
</dd></dl></dd></dl></dd>

---

``` py
    get_users()
```
<dd><dl><dd><dl><dd> 
    <blockquote>
    Get all users' info. This is a generator.
    </blockquote>
    <dl>
        <dt> Returns </dt>
        <dd><ul>
            <li><b>users</b> ([(str, str[ ])]) :&ensp; Each user contains "id" and "preferences".
        </dd>
    </dl>
</dd></dl></dd></dl></dd>

---

``` py
    add_users(users)
```
<dd><dl><dd><dl><dd> 
    <blockquote>
    Insert users into database. Overwrite existing data.
    </blockquote>
    <dl>
        <dt> Parameters </dt>
        <dd><ul>
            <li><b>users</b> ([(str, str[ ])]) :&ensp; Users to be added.
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

``` py
    Notify_all_users()
```
<dd><dl><dd><dl><dd> 
    <blockquote>
    Boardcast the newly announced patents to all users. Will prioritize displaying patents that are most relevant to each user's interests.
    </blockquote>
</dd></dl></dd></dl></dd>
</dl></dd></dl></dd></dl>