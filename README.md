# UNA - Universal Node API

![npm (scoped)](https://img.shields.io/npm/v/blc-org/una)
![Crates.io](https://img.shields.io/crates/v/una-core)
![PyPI](https://img.shields.io/pypi/v/una)

Una is a Lightning network node wrapper for all the existing Lightning backends: LND, c-lightning, Eclair, LndHub, LNBits, and more.

Una allows you to build a backend-agnostic Lightning application: starting from now, you no longer need to implement support for each Lightning node, it is supported right away!

Una is a Rust library, offering bindings to Python and NodeJS. It is thus available as a [crate](https://crates.io/crates/una), a [PyPi package](https://pypi.org/) and an [NPM package](https://npmjs.com/). Learn more how it works [here](bindings/README.md).

🚧 Una is still in development: methods and backends are missing. An HTTP and gRPC API is also in development.

## Supported actions

- [x] Create invoice
- [x] Get invoice
- [x] Pay invoice
- More to come

## Supported backends

- [x] LND (REST)
- [x] Core Lightning (gRPC) (>=0.11.2)
- [x] Eclair (REST) (>= v0.6.2)
- [ ] LndHub
- [ ] LNBits
- [ ] Sensei
- Any missing implementation? [Open an issue](https://github.com/blc-org/una/issues/new)
