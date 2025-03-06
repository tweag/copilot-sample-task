{
  pkgs ? import (builtins.fetchTarball {
    # Branch: nixos-23.05
    url = "https://github.com/NixOS/nixpkgs/archive/9790f3242da2152d5aa1976e3e4b8b414f4dd206.tar.gz";
    sha256 = "1y6zipys4803ckvnamfljb8raglgkbz1fz1fg03cxp4jqiiva5s1";
  }) { }
}:
pkgs.mkShell {
  name = "copilot-draft";
  buildInputs = with pkgs; [
    python311
    poetry
  ];
  shellHook = ''
    export LD_LIBRARY_PATH="${pkgs.stdenv.cc.cc.lib}/lib:${pkgs.zlib}/lib";
    poetry env use "${pkgs.python311}/bin/python"
    poetry install --sync --with=dev
    source "$(poetry env info --path)/bin/activate"
  '';
}
