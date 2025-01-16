{ pkgs ? import <nixpkgs> {} }:

-- Aucun rapport avec le projet

pkgs.mkShell {
  buildInputs = [
    pkgs.python312Full
    pkgs.git
  ];
}

