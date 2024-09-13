{
  pkgs ? import <nixpkgs> {}
  #pkgs ? import ./. {}
}:

let
  # HTTP 404
  # expected https://files.pythonhosted.org/packages/f8/64/ae51d6c88406ab8a685b0c83af9fc6ef4275982f391258d9167ddde88cf1/pyppeteer_stealth-2.7.4.tar.gz
  # actual https://pypi.org/packages/source/p/pyppeteer-stealth/pyppeteer-stealth-2.7.4.tar.gz
  extraPythonPackages = rec {
    aiohttp-chromium = pkgs.python3.pkgs.callPackage ./nix/aiohttp-chromium.nix {
      # FIXME scope
      selenium-driverless = pkgs.python3.pkgs.callPackage ./nix/selenium-driverless.nix {
        cdp-socket = pkgs.python3.pkgs.callPackage ./nix/cdp-socket.nix {};
        selenium = pkgs.python3.pkgs.callPackage ./nix/selenium.nix { };
      };
    };
    cdp-socket = pkgs.python3.pkgs.callPackage ./nix/cdp-socket.nix {};
    # error: Package ‘python3.10-selenium-driverless-1.6.3.3’ has an unfree license (‘cc-by-nc-sa-40’), refusing to evaluate.
    selenium-driverless = pkgs.python3.pkgs.callPackage ./nix/selenium-driverless.nix {
      cdp-socket = pkgs.python3.pkgs.callPackage ./nix/cdp-socket.nix {};
      selenium = pkgs.python3.pkgs.callPackage ./nix/selenium.nix { };
    };
    # fix: ModuleNotFoundError: No module named 'selenium.webdriver.common.devtools'
    # https://github.com/milahu/nixpkgs/issues/20
    selenium = pkgs.python3.pkgs.callPackage ./nix/selenium.nix { };
    torf = pkgs.python3.pkgs.callPackage ./nix/torf.nix {
      flatbencode = pkgs.python3.pkgs.callPackage ./nix/flatbencode.nix {};
    };
  };

  buster-client = pkgs.callPackage ./nix/buster-client.nix {};
  buster-client-setup = pkgs.callPackage ./nix/buster-client-setup.nix {
    buster-client = pkgs.callPackage ./nix/buster-client.nix {};
  };
  buster-client-setup-cli = pkgs.callPackage ./nix/buster-client-setup-cli.nix {
    buster-client = pkgs.callPackage ./nix/buster-client.nix {};
  };

  python = pkgs.python3.withPackages (pythonPackages:
  (with pythonPackages; [
    requests
    magic # libmagic
    chardet
    charset-normalizer
    guessit # parse video filenames
    langcodes
    #playwright
    setuptools # pkg_resources for playwright-stealth
    #pyppeteer pyppeteer-stealth # puppeteer # old
    #kaitaistruct
    #sqlglot
    # distributed processing
    # ray is too complex, has only binary package in nixpkgs https://github.com/NixOS/nixpkgs/pull/194357
    #ray
    # https://github.com/tomerfiliba-org/rpyc
    #rpyc
    aiohttp
    aiohttp-socks # https://stackoverflow.com/a/76656557/10440128
    aiohttp-retry
    aiodns # make aiohttp faster
    brotli # make aiohttp faster
    natsort
    #pycdlib
    psutil
    pyparsing
    cryptography
    nest-asyncio
    # FIXME passlib.exc.InternalBackendError: crypt.crypt() failed for unknown reason; passlib recommends running `pip install bcrypt` for general bcrypt support.(config=<hash <class 'str'> value omitted>, secret=<hash <class 'bytes'> value omitted>)
    #bcrypt
    # no. use patched version in lib/thirdparty/pysubs2
    #pysubs2
    lxml # xhtml parser
    beautifulsoup4 # html parser
    fritzconnection # fritzbox client
    #selenium
    praw # python reddit api wrapper
  ])
  ++
  (with extraPythonPackages; [
    #aiohttp-chromium
    selenium-driverless
    cdp-socket
    selenium
    torf # torrent file
  ])
  );

  chromium = pkgs.ungoogled-chromium;

in

pkgs.mkShell rec {

  buildInputs = (with pkgs; [
    chromium # for selenium
    #torrenttools
    #lighttpd
  ]) ++ [
    python
  ]
  ++
  (with extraPythonPackages; [
    selenium-driverless
    cdp-socket
    selenium
    torf # torrent file
  ]);

}
