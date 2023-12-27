# **MAD 2 boilerplate**

This is just a boilerplate code for people to get started with Flask, SQLAlchemy and SQLite3 database (with a user table). Make sure you have the `sqlite3` cli tool installed

## **Install SQLite3**
**On Debian or Debian-based distros like Ubuntu, Pop!\_OS, Linux Mint, etc**
```sh
sudo apt install -y sqlite3
```
**On Fedora**
```sh
sudo dnf install sqlite
```
**On Arch or Arch-based distros**
> You guys know it already XD
```sh
yay -S sqlite
```

## **Run the flask app**
1. Clone this repo
2. `cd MAD2`
3. Create a virtual environment
    - `python3 -m venv .venv`
    - `. .venv/bin/activate`
4. Install the dependencies `pip install -r requirement.txt`
5. Run it `python app.py`

## **Run the vue app**
1. Clone this repo (if haven't already)
2. `cd MAD2/client`
3. Install the dependencies `npm install`
4. `npm run dev`

## **Open the SQLite db from cli**
```sh
sqlite3 database/site.db
```
- When inside the sqlite3 cli, run this command first `.mode column` (thank me later)
- To view all the tables
```sql
.tables
```
- To query all
```sql
select * from user;
```

## **To deploy the flask backend using docker**
1. Make sure you have [docker](https://docs.docker.com/engine/install/) installed
2. `./deploy.sh`
