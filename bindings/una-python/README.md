# Python bindings for UNA

Requires Python >=3.7.

## Build

### Setup environment

```shell
$ cd bindings/una-python
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install -U pip maturin
```

### Build the package

```shell
$ maturin develop
```

### Test

You can try the build by running the test script (temporary, until automated tests). Replace the `config` values by your own node credentials (LND needs an admin macaroon).

```shell
$ python test.py
```

## Supported architectures

- macOS x86_64
- Windows x64
- Windows x86
- Linux x86_64
- Linux i686
- Linux aarch64
- Linux armv7
- Musllinux x86_64
- Musllinux aarch64
- Musllinux armv7

The following targets are currently not supported because of the `ring` Rust dependency not building:

- Linux s390x
- Linux ppc64le
- Linux ppc64

The following targets are currently not supported because of an `ssp` C library issue (to investigate):

- Linux i686
