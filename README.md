# Youtube-queuer

Download lots of videos using `youtube-dl`, but allow queueing them up.

## Usage

```sh
$ ytl add -a "'https://www.youtube.com/watch?v=mxlpQMJt8XA&list=PL4o6UvJIdPNooxA4WQskzhF0_qe5GTMED' --playlist-start 41" -o /tmp
```

```sh
$ ytl add 'https://www.youtube.com/watch?v=atoqchvXkSU' -o /tmp
```

```sh
$ ytl list
1. Factorio: Entry Level to Megabase Ep 40: ROBOT FEEDING FRENZY - Tutorial Series Gameplay
```

```sh
$ ytl stop 1
Stopping download for "Factorio: Entry Level to Megabase Ep 40: ROBOT FEEDING FRENZY - Tutorial Series Gameplay"
```

## Implementation

* `ytl` binary with CLI
* `ytl-worker` binary which performs actual download
* `ytld` webserver handling communication
* `sqlite3` database handling state
* Communication over HTTP/JSON

### Request cycle

#### Workers

Workers request new data from `ytld` by accessing the url:
`GET /worker/next`. This returns the correct arguments for the next command.


#### CLI

The CLI inserts a new set of arguments with:

`POST /cli/new` and the body contains the required info
