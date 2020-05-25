{ pkgs ? import <nixpkgs> {} }:

with pkgs.python3.pkgs;

let
  # mypy does not find type annotations otherwise
  mypyEnv = (python.withPackages (ps: [
    ps.mypy
    ps.PyGithub
  ]));
in buildPythonPackage {
  name = "inactive-maintainers";
  src = ./.;
  propagatedBuildInputs = [
    PyGithub
  ];
  checkPhase = ''
    ${mypyEnv}/bin/mypy inactive_maintainers
  '';
}
