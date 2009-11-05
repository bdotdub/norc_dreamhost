# Norc on Dreamhost

Norc is a Task Management System that replaces Unix cron developed by [Darrell Silver](http://darrellsilver.com/) for use at [Perpetually.com](http://www.perpetually.com/). Norc on Dreamhost gives you a basic template to get Norc up and running on Dreamhost.

To read more about Norc: [http://github.com/darrellsilver/norc](http://github.com/darrellsilver/norc)

## Installation

The installation process involves a few steps. Before we get started, make sure you have *shell* access for your user. To check this, go to `Users > Manage Users` in your Dreamhost Web Panel.

### Create a domain/subdomain on Dreamhost

First, you need to create a domain/subdomain for your installation to live.

* In your browser, go to `https://panel.dreamhost.com` and login
* Go to *Domains > Manage Domains* in the left navigation
* Click on *Add New Domain / Sub-Domain*
* Fill in the fields in the form:
   * Enter the domain you want your Norc installation to be in
   * Choose the username you want it to be under
   * Under *Web Directory*, it will have what you put in the *Domain to Host* field. However, you must add `public` after that. For example, if you wanted to host your Norc installation on `norc.example.com`, you need to put `norc.example.com/public` in the *Web Directory* field.
   * Then, click the checkbox next to *Passeger (Ruby/Python apps only)*
* Click on *Fully host this domain*

### Clone repo and install

Login into Dreamhost and clone the repo.

    $ ssh user@example.com
    $ cd norc.example.com
    $ git clone clone git://github.com/bdotdub/norc_dreamhost.git

Since Dreamhost's default Python version is Python 2.3, we have to convert all the executables to use Python 2.4 (newest Python available on Dreamhost). Because of this, I have created a helper script to convert the Python executable path in the files in `bin`.

Also, since the Norc codebase is a submodule of this repo, the helper script also does a `init` and `update` to load the Norc code.

    ./dh_install.sh

### Setup Norc installation

Now that you have everything Dreamhost related setup, follow the instructions in `norc/INSTALL.md`.

    $ less norc/INSTALL.md

You can skip the *Start up Django development enviroment* steps because it is handled i `passenger_wsgi.py` and Passenger itself.

## Running Norc

Since Norc is running under Passenger, it should be up and running if you go to `http://norc.example.com`. However, whenever you make a change in `passenger_wsgi.py` or the Norc codebase, you'll have to restart it by running the following:

    $ mkdir -p tmp
    $ touch tmp/restart.txt

### Running a Norc daemon

I believe Dreamhost may kill daemons at any time, so to have a daemon run, you may want to start a `screen` session and start it there

    $ tmsd --region MY_REGION

## Resources

* [Norc](http://github.com/darrellsilver/norc)
* [Norc Install](http://github.com/darrellsilver/norc/blob/master/INSTALL.md)
* [GNU Screen Manual](http://www.gnu.org/software/screen/manual/screen.html)

#### Dreamhost

* [Python on Dreamhost](http://wiki.dreamhost.com/Python)
* [Passenger WSGI](http://wiki.dreamhost.com/Passenger_WSGI)
* [MySQL](http://wiki.dreamhost.com/MySQL)

