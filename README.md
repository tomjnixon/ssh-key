## STATUS: pre-release

# SSH-KEY

Makes it easy to use a separate SSH key for each system you want to log in to.

- Each key has access only to a single host, and may have different passwords,
  so becomes less valuable.
- Each host sees a different public key, so your public key no longer identifies
  you across hosts. For example, this trick no longer works:
  [ssh whoami.filippo.io](https://blog.filippo.io/ssh-whoami-filippo-io/).

## HOWTO

When you want to generate a key for a hostname that you have SSH access to:

    ./ssh-key new $NEW_HOSTNAME

This will:

- generate a new key called `id_${NEW_HOSTNAME}_22` in `~/.ssh/`
- copy it to the authorized_heys file on `$NEW_HOSTNAME`
- add lines to your SSH config that cause only the generated identity to be
  used for this host

## CONFIGURATION

Unfortunately, there appears to be no easy way to tell SSH where to get its
configuration from, or to #include other files. Thus, the following approach is
used:

- ssh-key generates ~/.ssh/config.keys, with an entry like the following for each host:

        Match host $HOSTNAME exec "test %p = $PORTNUM"
            IdentitiesOnly yes
            IdentityFile /home/tom/.ssh/id_$HOSTNAME_$PORTNUM

- `~/.ssh/config` is produced from the concatenation of `~/.ssh/config.head`,
  `./.ssh/config.keys` and `~/.ssh/config.tail`.

This happen whenever you run a `ssh-key new` command. Run `ssh-key config` to
just re-run these steps (for example when you've edited `~/.ssh/config.head`).

## KNOWN HOSTS

Sometimes, there may be multiple ways to reach a given host that SSH does not
know about, perhaps because there are multiple DNS entries for a given host,
you have an entry in your `/etc/hosts`, or you sometimes access it by its IP
address. This is resolved using information in your `~/.ssh/known_hosts` file,
which stores a list of known hostnames/IPs, and the public key of the
associated SSH server.

This means that if you try to SSH into a host using a new hostname, the correct
key will not be used (and SSH will ask you for a password). Even without
completing the log-in, SSH will have updated the authorized_keys file, so
re-running `ssh-key configure` and trying again will cause the correct key to
be used.
