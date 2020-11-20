# TwitterNumberPoll

## Get Replies
Before running code, we need to get latest replies. Obviously this need
`Twitter Developer Account` . If you don't have one, skip this part cause
there is an example `replies.jsonl` in directory.

#### 1. install `twarc`
```
pip install twarc
```

or (**mac only**)
```
brew install twarc
```

#### 2. Configure
First you're going to need to tell twarc about your application API keys and
grant access to one or more Twitter accounts:
```
twarc configure
```
This will store your credentials in a file called `.twarc` in your home
directory so you don't have to keep entering them in. If you would rather supply
them directly you can set them in the environment (`CONSUMER_KEY`,
`CONSUMER_SECRET`, `ACCESS_TOKEN`, `ACCESS_TOKEN_SECRET`) or using command line
options (`--consumer_key`, `--consumer_secret`, `--access_token`,
`--access_token_secret`).

#### 3. Export Replies
If you want to get the replies to a given tweet you can:
```
twarc replies 824077910927691778 > replies.jsonl
```

#### 4. Placement
Make sure to place `replies.jsonl` in root directory of this project. Don't rename.

## Usage

#### 1. Run code
```
python3 main.py
```