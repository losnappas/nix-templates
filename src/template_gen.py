import jinja2
import os

dir = os.path.dirname(os.path.abspath(__file__))


def generate_flake(template_file, output_file, context):
    """
    Generates a Nix flake file from a Jinja2 template.

    Args:
        template_file (str): Path to the Jinja2 template file.
        output_file (str): Path to the output Nix flake file.
        context (dict): Dictionary containing the variables to be passed to the template.
    """
    with open(template_file, "r") as template_file:
        template_content = template_file.read()
    template = jinja2.Template(template_content)
    output_text = template.render(context)

    with open(output_file, "w") as f:
        f.write(output_text)


# actionlint.enable = true;
# alejandra.enable = true;
# asmfmt.enable = true;
# beautysh.enable = true;
# biome.enable = true;
# black.enable = true;
# buildifier.enable = true;
# cabal-fmt.enable = true;
# clang-format.enable = true;
# cljfmt.enable = true;
# cmake-format.enable = true;
# csharpier.enable = true;
# cue.enable = true;
# d2.enable = true;
# dart-format.enable = true;
# deadnix.enable = true;
# deno.enable = true;
# dhall.enable = true;
# dnscontrol.enable = true;
# dos2unix.enable = true;
# dprint.enable = true;
# elm-format.enable = true;
# erlfmt.enable = true;
# fantomas.enable = true;
# fish_indent.enable = true;
# fnlfmt.enable = true;
# formatjson5.enable = true;
# fourmolu.enable = true;
# fprettify.enable = true;
# gdformat.enable = true;
# genemichaels.enable = true;
# gleam.enable = true;
# gofmt.enable = true;
# gofumpt.enable = true;
# goimports.enable = true;
# golines.enable = true;
# google-java-format.enable = true;
# hclfmt.enable = true;
# hlint.enable = true;
# isort.enable = true;
# jsonfmt.enable = true;
# jsonnet-lint.enable = true;
# jsonnetfmt.enable = true;
# just.enable = true;
# keep-sorted.enable = true;
# ktfmt.enable = true;
# ktlint.enable = true;
# latexindent.enable = true;
# leptosfmt.enable = true;
# mdformat.enable = true;
# mdsh.enable = true;
# meson.enable = true;
# mix-format.enable = true;
# muon.enable = true;
# mypy.enable = true;
# nickel.enable = true;
# nimpretty.enable = true;
# nixfmt.enable = true;
# nixpkgs-fmt.enable = true;
# nufmt.enable = true;
# ocamlformat.enable = true;
# odinfmt.enable = true;
# opa.enable = true;
# ormolu.enable = true;
# packer.enable = true;
# perltidy.enable = true;
# php-cs-fixer.enable = true;
# pinact.enable = true;
# prettier.enable = true;
# protolint.enable = true;
# purs-tidy.enable = true;
# rubocop.enable = true;
# ruff-check.enable = true;
# ruff-format.enable = true;
# rufo.enable = true;
# rustfmt.enable = true;
# scalafmt.enable = true;
# shellcheck.enable = true;
# shfmt.enable = true;
# sqlfluff.enable = true;
# sqruff.enable = true;
# statix.enable = true;
# stylish-haskell.enable = true;
# stylua.enable = true;
# swift-format.enable = true;
# taplo.enable = true;
# templ.enable = true;
# terraform.enable = true;
# texfmt.enable = true;
# toml-sort.enable = true;
# typos.enable = true;
# typstfmt.enable = true;
# typstyle.enable = true;
# yamlfmt.enable = true;
# zig.enable = true;
# zprint.enable = true;

templates = [
    {
        "name": "default",
        "variables": {
            "treefmt": """
             """,
            "devshell": {
                "packages": """
                """,
                "extraConfig": """
                """,
                "env": """
                """,
            },
        },
    },
    {
        "name": "golang",
        "variables": {
            "treefmt": """
             gofmt.enable = true;
             gofumpt.enable = true;
             goimports.enable = true;
             golines.enable = true;
             """,
            "devshell": {
                "packages": """
                go
                gopls
                delve
                gomodifytags
                impl
                go-tools
                gotests
                """,
                "extraConfig": """
                """,
                "env": """
                """,
            },
        },
    },
    {
        "name": "python",
        "variables": {
            "treefmt": """
            black.enable = true;
            ruff-check.enable = true;
            ruff-format.enable = true;
            shfmt.enable = true;
            """,
            "devshell": {
                "packages": """
                python3
                python3.pkgs.poetry
                python3.pkgs.python-lsp-server
                python3.pkgs.pyls-isort
                python3.pkgs.pyls-rope
                python3.pkgs.pyls-mypy
                python3.pkgs.python-lsp-ruff
                python3.pkgs.python-lsp-jsonrpc
                python3.pkgs.pyflakes
                python3.pkgs.mccabe
                python3.pkgs.pycodestyle
                python3.pkgs.pydocstyle
                python3.pkgs.autopep8
                python3.pkgs.yapf
                python3.pkgs.pylint
                """,
                "extraConfig": "",
                "env": "",
            },
        },
    },
]


if __name__ == "__main__":
    template_file = dir + "/flake.nix.templ"

    for context in templates:
        output_file = f"{dir}/../templates/{context['name']}.nix"
        generate_flake(template_file, output_file, context["variables"])

    print(f"Generated flake file: {output_file}")
