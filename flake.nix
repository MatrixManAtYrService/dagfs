{
  description = "A dependency-aware 'filesystem' for use with Apache Airflow";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs";
  };

  outputs = { self, nixpkgs, flake-utils }: (flake-utils.lib.eachSystem [
    "x86_64-linux"
    "x86_64-darwin"
    "aarch64-linux"
    "aarch64-darwin"
  ] (system:
    let
      pkgs = nixpkgs.legacyPackages.${system};
    in
    rec {
      packages.dagfs = pkgs.poetry2nix.mkPoetryApplication {
        projectDir = ./.;
      };

      defaultPackage= packages.dagfs;

      devShell = pkgs.mkShell {

        buildInputs = [
          pkgs.python37
          pkgs.poetry
          pkgs.pre-commit
          pkgs.docker-compose
        ];

      shellHook = ''
        export PATH=$PATH:$PWD/scripts
        '';

      };
    }));
}
