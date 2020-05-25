# Implementation of RFC 55 

This is a script to find inactive nixpkgs maintainers as part of [RFC-55 - Retire inactive nixpkgs committers](https://github.com/NixOS/rfcs/blob/master/rfcs/0055-retired-committers.md).

## USAGE

nixpkgs-inactive-committers expects an API token passed in the environment as GITHUB_TOKEN .
Such a token can be created at https://github.com/settings/tokens
Make sure to enable the read:org scope

```
$ export GITHUB_TOKEN=<insert-token-here>
$ nix-build
$ ./result
```


