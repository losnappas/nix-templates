{
  description = "Description for the project";

  inputs = {
    flake-parts.url = "github:hercules-ci/flake-parts";
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    systems.url = "github:nix-systems/default";
    flake-root.url = "github:srid/flake-root";
    treefmt-nix = {
      url = "github:numtide/treefmt-nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs =
    inputs@{ flake-parts, ... }:
    flake-parts.lib.mkFlake { inherit inputs; } {
      imports = [
        inputs.flake-root.flakeModule
        inputs.treefmt-nix.flakeModule
      ];
      systems = import inputs.systems;
      perSystem =
        {
          config,
          self',
          inputs',
          pkgs,
          system,
          lib,
          ...
        }:
        {

          # Per-system attributes can be defined here. The self' and inputs'
          # module parameters provide easy access to attributes of the same
          # system.

          treefmt = {
            inherit (config.flake-root) projectRootFile;
            programs = {
              nixfmt.enable = true;
            };
          };

          devShells.default = pkgs.mkShell {
            # Sets up FLAKE_ROOT var.
            inputsFrom = [ config.flake-root.devShell ];
            packages = [
              pkgs.nil
            ];
            env = {
              PROJECT_FORMATTER = lib.getExe self'.formatter;
              # LD_LIBRARY_PATH=pkgs.lib.makeLibraryPath [
              #   pkgs.stdenv.cc.cc.lib
              # ];
            };
            # shellHook = ''
            #   # e.g.
            #   # export STACK_ROOT="$FLAKE_ROOT/.stack"
            # '';
          };

          # Equivalent to  inputs'.nixpkgs.legacyPackages.hello;
          # packages.default = pkgs.hello;
        };
      flake =
        { lib, ... }:
        {
          # The usual flake attributes can be defined here, including system-
          # agnostic ones like nixosModule and system-enumerating ones, although
          # those are more easily expressed in perSystem.
          templates =
            let
              templatesDir = ./templates;
              entries = builtins.readDir templatesDir;
              dirs = lib.filterAttrs (_: p: p == "directory") entries;
            in
            (lib.mapAttrs (name: _: {
              path = "${templatesDir}/${name}";
              description = "${name} flake template";
            }) dirs);
        };
    };
}
