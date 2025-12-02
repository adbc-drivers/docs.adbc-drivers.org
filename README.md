# ADBC Driver Foundry Driver Documentation

Source code for the [ADBC Driver Foundry](https://adbc-drivers.org) Driver Documentation [website](https://docs.adbc-drivers.org).
This project uses [Sphinx](https://sphinx-doc.org) and can be built with [Pixi](https://pixi.sh).

## Building

## Prerequisites

- [Pixi](https://pixi.sh) (see [Pixi Installation](https://pixi.sh/latest/installation/))

## Build and Preview

Build the site with:

```console
$ pixi run build
```

To preview the site you built, run:

```console
$ pixi run serve
```

Then open your web browser to <http://localhost:8000>.

For development, you can instead use the development server which will automatically rebuild the site when changes are made:

```console
$ pixi run watch
```

Then visit <http://localhost:8000>.

Note that the theme used does not always work well with incremental builds.
You may need to remove `_build` and start again, especially when changing theme options.

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for information on how to contribute.
