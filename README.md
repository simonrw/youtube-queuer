# Youtube-queuer

Download lots of videos using `youtube-dl`, but allow queueing them up.

## Usage

```sh
$ ytq add 'https://www.youtube.com/watch?v=mxlpQMJt8XA' -o /tmp
```

```sh
$ ytq add 'https://www.youtube.com/watch?v=atoqchvXkSU' -o /tmp
```

```sh
$ ytq list
1. Factorio: Entry Level to Megabase Ep 40: ROBOT FEEDING FRENZY - Tutorial Series Gameplay
```

```sh
$ ytq delete 1
Stopping download for "Factorio: Entry Level to Megabase Ep 40: ROBOT FEEDING FRENZY - Tutorial Series Gameplay"
```

## Implementation

* `ytq` binary with CLI
* `ytq-worker` binary which performs actual download
* `ytqd` webserver handling communication
* `sqlite3` database handling state
* Communication over HTTP/JSON

### Request cycle

#### Workers

Workers request new data from `ytqd` by accessing the url:
`GET /worker/next`. This returns the correct arguments for the next command.

#### CLI

The CLI inserts a new set of arguments with:

`POST /cli/new` and the body contains the required info
