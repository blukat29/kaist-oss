# tinypoll

## Install

```
mkvirtualenv --python=`which python3` oss
workon oss
pip install -r requirements.txt
```

## Run

```
./manage.py run
```

## Database schema

### Persistent database (MySQL)

```
CREATE TABLE poll (
    id INT PRIMARY KEY,
    title VARCHAR(64),
    created_at DATETIME
);
CREATE TABLE option (
    id INT PRIMARY KEY,
    poll_id INT NOT NULL,
    text VARCHAR(100),
    votes INT,
    FOREIGN KEY poll_id REFERENCES poll (id)
);
```

### Cache (Arcus/Memcached)

```
poll:all -> ["1.aaaa", "2.bbbb", "3.cccc", ...] (list of poll ids and titles)
poll:1 -> "aaaaa" (title)
poll:1:options -> ["33.xyz", "34.www", "35.me", ...] (list of option ids and texts)
option:33 -> 88 (number of votes)
```
