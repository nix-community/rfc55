{ pkgs ? import <nixpkgs> {} }:

with pkgs;

mkShell {
  nativeBuildInputs = [
    (python3.withPackages (ps: [
      ps.mypy
      ps.PyGithub
    ]))
  ];
}
