{
  description = "A basic flake";

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
              ruff-check.enable = true;
              ruff-format.enable = true;
              shfmt.enable = true;
            };
          };

          devShells.default = pkgs.mkShell {
            # Sets up FLAKE_ROOT var.
            inputsFrom = [ config.flake-root.devShell ];
            packages = with pkgs; [
              nil
              ruff
              python3
              python3.pkgs.python-lsp-server
              python3.pkgs.pyls-isort
              python3.pkgs.pylsp-rope
              python3.pkgs.pylsp-mypy
              python3.pkgs.python-lsp-ruff
              python3.pkgs.python-lsp-jsonrpc
              python3.pkgs.pyflakes
              python3.pkgs.mccabe
              python3.pkgs.pycodestyle
              python3.pkgs.pydocstyle
              python3.pkgs.autopep8
              python3.pkgs.yapf
              python3.pkgs.pylint
              python3.pkgs.black
              python3.pkgs.pyls-memestra
              python3.pkgs.python-lsp-ruff
            ];
            env = {

            };

          };

          # Equivalent to  inputs'.nixpkgs.legacyPackages.hello;
          # packages.default = pkgs.hello;
        };
      flake = {
        # The usual flake attributes can be defined here, including system-
        # agnostic ones like nixosModule and system-enumerating ones, although
        # those are more easily expressed in perSystem.

      };
    };
}
